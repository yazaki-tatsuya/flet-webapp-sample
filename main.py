import flet as ft
from common_data_access.db_access import get_data_from_db
from user_interface.ui import build_ui
from common_data_access.file_access import download_file_from_azure
from common_tools.ocr_processing import perform_ocr
import os
import env_production


def main(page: ft.Page):
    # 画面の初期化
    page.title = "レシート読み取りアプリ"

    # Azure File Storageからファイルをダウンロード
    connection_string = env_production.get_env_variable('AZURE_CONNECTION_STRING')
    share_name = env_production.get_env_variable("AZURE_SHARE_NAME")
    directory_name = env_production.get_env_variable("AZURE_DIRECTORY_NAME")
    file_name = env_production.get_env_variable("AZURE_FILE_NAME")
    download_path = f"./downloads/{file_name}"

    # ダウンロードパスのディレクトリを作成
    os.makedirs(os.path.dirname(download_path), exist_ok=True)

    try:
        downloaded_file = download_file_from_azure(
            share_name=share_name,
            directory_name=directory_name,
            file_name=file_name,
            connection_string=connection_string,
            download_path=download_path
        )
    except Exception as e:
        page.add(ft.Text(f"Error downloading file: {e}"))
        page.update()
        return

    # OCRを実行
    try:
        ocr_result = "perform_ocr(downloaded_file)"
    except Exception as e:
        page.add(ft.Text(f"Error performing OCR: {e}"))
        page.update()
        return

    # UIの構築
    build_ui(page, image_path=downloaded_file, ocr_text=ocr_result)

    # データベースからのデータ取得
    data = get_data_from_db()
    page.controls.append(ft.Text(f"Database data: {data}"))

    # 更新
    page.update()

app = ft.app(main, export_asgi_app=True)


# import flet as ft
# from common_data_access.db_access import get_data_from_db
# from user_interface.ui import build_ui

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