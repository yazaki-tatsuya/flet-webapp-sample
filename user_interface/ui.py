# # ui.py
# import flet as ft

# def build_ui(page: ft.Page):
#     page.add(
#         ft.Text("Welcome to My App"),
#         ft.ElevatedButton("Click Me", on_click=lambda e: page.dialog(ft.AlertDialog("Button clicked!")))
#     )

# ui.py
import flet as ft
import base64
import os

def build_ui(page: ft.Page, image_path: str, ocr_text: str):
    """
    画像とOCR結果を表示するUIを構築します。
    """
    # 画像をBase64にエンコード
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()

    # 画像の拡張子に応じてMIMEタイプを設定
    _, ext = os.path.splitext(image_path)
    ext = ext.lower()
    if ext == ".png":
        mime = "image/png"
    elif ext in [".jpg", ".jpeg"]:
        mime = "image/jpeg"
    else:
        mime = "application/octet-stream"

    image_data = f"data:{mime};base64,{encoded_string}"

    # UIコンポーネントの追加
    page.add(
        ft.Column(
            [
                # レシート画像のタイトル
                ft.Container(
                    content=ft.Text("レシート画像", size=20, weight="bold"),
                    margin=ft.Margin(top=20, left=0, right=0, bottom=10)
                ),
                # レシート画像の表示
                ft.Image(src=image_data, width=400, height=300, fit=ft.ImageFit.CONTAIN),
                
                # OCR結果のタイトル
                ft.Container(
                    content=ft.Text("OCR結果", size=20, weight="bold"),
                    margin=ft.Margin(top=20, left=0, right=0, bottom=10)
                ),
                # OCR結果の表示
                ft.Container(
                    content=ft.Text(ocr_text, selectable=True, size=14),
                    margin=ft.Margin(top=0, left=0, right=0, bottom=20)
                ),
                # 再読み込みボタン
                ft.Container(
                    content=ft.ElevatedButton(
                        "再読み込み",
                        on_click=lambda e: page.reload()
                    ),
                    margin=ft.Margin(top=0, left=0, right=0, bottom=20)
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            tight=True,
            spacing=0  # 各Containerでマージンを設定しているため、Columnのspacingは不要
        )
    )

