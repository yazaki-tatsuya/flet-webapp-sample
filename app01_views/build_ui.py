# app01_views/build_ui.py
import flet as ft
from app03_services.db_access import get_data_from_db
from app03_services.file_access import download_blob_from_azure
from app03_services.generate_sas_url import generate_sas_url
from app05_utils.ocr_processing import perform_ocr
import os
import env_production

def build_ui(page: ft.Page) -> ft.Control:
    """
    画像とOCR結果を表示するUIを構築し、UIコンポーネントを返します。

    Args:
        page (ft.Page): Fletのページオブジェクト。

    Returns:
        ft.Control: 構築されたUIコンポーネント。
    """
    # スクロール可能なColumnコンポーネント
    scrollable_content = ft.Column(
        spacing=10,
        height=500,  # 表示領域の高さを指定
        scroll=ft.ScrollMode.ALWAYS,  # 常時スクロール可能に設定
    )

    # 環境変数の取得
    connection_string = env_production.get_env_variable("AZURE_CONNECTION_STRING")
    container_name = env_production.get_env_variable("AZURE_SHARE_NAME")
    blob_name = env_production.get_env_variable("AZURE_FILE_NAME")
    download_path = f"./downloads/{blob_name}"

    # ダウンロードパスのディレクトリを作成
    os.makedirs(os.path.dirname(download_path), exist_ok=True)

    try:
        # ファイルのダウンロード (Azure Blob Storage)
        downloaded_file = download_blob_from_azure(
            container_name=container_name,
            blob_name=blob_name,
            connection_string=connection_string,
            download_path=download_path
        )
        print(f"Image data length: {len(downloaded_file)}")  # デバッグ用
        print(f"Image data preview: {downloaded_file[:100]}...")  # 画像データの一部を表示
    except Exception as e:
        scrollable_content.controls.append(ft.Text(f"Error downloading file: {e}"))
        return ft.Container(
            content=scrollable_content,
            padding=ft.Padding(10, 10, 10, 10),
        )

    # OCRの実行
    try:
        ocr_result = perform_ocr(downloaded_file)
    except Exception as e:
        scrollable_content.controls.append(ft.Text(f"Error performing OCR: {e}"))
        return ft.Container(
            content=scrollable_content,
            padding=ft.Padding(10, 10, 10, 10),
        )

    # SAS URL の生成
    try:
        blob_url = generate_sas_url(connection_string, container_name, blob_name)
    except Exception as e:
        scrollable_content.controls.append(ft.Text(f"Error generating SAS URL: {e}"))
        return ft.Container(
            content=scrollable_content,
            padding=ft.Padding(10, 10, 10, 10),
        )

    # UIの構築
    scrollable_content.controls.extend([
        # レシート画像のタイトル
        ft.Container(
            content=ft.Text("レシート画像", size=20, weight="bold"),
            margin=ft.Margin(top=20, left=0, right=0, bottom=10)
        ),
        # レシート画像の表示
        ft.Image(src=blob_url, width=400, height=300, fit=ft.ImageFit.CONTAIN),
        # OCR結果のタイトル
        ft.Container(
            content=ft.Text("OCR結果", size=20, weight="bold"),
            margin=ft.Margin(top=20, left=0, right=0, bottom=10)
        ),
        # OCR結果の表示
        ft.Container(
            content=ft.Text(ocr_result, selectable=True, size=14),
            margin=ft.Margin(top=0, left=0, right=0, bottom=20)
        ),
        # 再読み込みボタン
        ft.Container(
            content=ft.ElevatedButton(
                "再読み込み",
                on_click=lambda e: page.go("/page99")  # ページを再読み込み
            ),
            margin=ft.Margin(top=0, left=0, right=0, bottom=20)
        )
    ])

    # データベースからのデータ取得
    try:
        data = get_data_from_db()
        scrollable_content.controls.append(ft.Text(f"Database data: {data}"))
    # エラーの場合はエラーメッセージを表示
    except Exception as e:
        scrollable_content.controls.append(ft.Text(f"Error getting data from database: {e}"))

    # 最終的なコンテナを返す
    return ft.Container(
        content=scrollable_content,
        padding=ft.Padding(10, 10, 10, 10),
    )
