import flet as ft
from app03_services.db_access import get_data_from_db
from app01_views.ui import build_ui
from app03_services.file_access import download_file_from_azure, download_blob_from_azure
from app05_utils.ocr_processing import perform_ocr
from app03_services.generate_sas_url import generate_sas_url
import os
import env_production



def main(page: ft.Page):
    """
    Fletアプリケーションのメイン関数。
    """
    # 画面の初期化
    page.title = "レシート読み取りアプリ"

    # 環境変数の取得
    connection_string = env_production.get_env_variable("AZURE_CONNECTION_STRING")
    container_name = env_production.get_env_variable("AZURE_SHARE_NAME")
    directory_name = env_production.get_env_variable("AZURE_DIRECTORY_NAME")
    blob_name = env_production.get_env_variable("AZURE_FILE_NAME")
    download_path = f"./downloads/{blob_name}"

    # ダウンロードパスのディレクトリを作成
    os.makedirs(os.path.dirname(download_path), exist_ok=True)

    try:
        # # ファイルのダウンロード (Azure File Storage)
        # downloaded_file = download_file_from_azure(
        #     share_name=share_name,
        #     directory_name=directory_name,
        #     file_name=file_name,
        #     connection_string=connection_string,
        #     download_path=download_path
        # )
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
        page.add(ft.Text(f"Error downloading file: {e}"))
        page.update()
        return

    # OCRの実行
    try:
        ocr_result = perform_ocr(downloaded_file)
    except Exception as e:
        page.add(ft.Text(f"Error performing OCR: {e}"))
        page.update()
        return

    # SAS URL の生成
    try:
        blob_url = generate_sas_url(connection_string, container_name, blob_name)
    except Exception as e:
        page.add(ft.Text(f"Error generating SAS URL: {e}"))
        page.update()
        return
    
    build_ui(page, image_url=blob_url, ocr_text=ocr_result)

    # データベースからのデータ取得
    data = get_data_from_db()
    page.controls.append(ft.Text(f"Database data: {data}"))

    # 更新
    page.update()

if __name__ == "__main__":
    # 直接実行された場合はFletアプリを起動
    ft.app(target=main, view=ft.AppView.FLET_APP, port=8550, web_renderer="auto")
else:
    # モジュールとしてインポートされた場合は、ASGIアプリとしてエクスポート
    app = ft.app(target=main, export_asgi_app=True)


# import flet as ft
# from app03_services.db_access import get_data_from_db
# from app01_views.ui import build_ui

# def main(page: ft.Page):
#     # 画面の初期化
#     page.title = "My Flet App"
    
#     # UIの構築
#     build_ui(page)

#     # データベースからのデータ取得
#     data = get_data_from_db()
#     page.controls.append(ft.Text(f"Database data: {data}"))
    
#     # 更新
#     page.update()

# # app = ft.app(main)
# # ASGIアプリとしてエクスポート
# app = ft.app(main, export_asgi_app=True)