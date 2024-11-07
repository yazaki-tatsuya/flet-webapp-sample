# # # ui.py
# # import flet as ft

# # def build_ui(page: ft.Page):
# #     page.add(
# #         ft.Text("Welcome to My App"),
# #         ft.ElevatedButton("Click Me", on_click=lambda e: page.dialog(ft.AlertDialog("Button clicked!")))
# #     )

# # ui.py
# import flet as ft
# import base64
# import os

# def build_ui(page: ft.Page, image_path: str, ocr_text: str):
#     """
#     画像とOCR結果を表示するUIを構築します。
#     """
#     # テキストのスクロールイベントをハンドリングする関数
#     def on_column_scroll(e: ft.OnScrollEvent):
#         print(
#             f"Type: {e.event_type}, pixels: {e.pixels}, min_scroll_extent: {e.min_scroll_extent}, max_scroll_extent: {e.max_scroll_extent}"
#         )

#     # スクロール可能なColumnコンポーネントをコンテナ部品内部に作成
#     cl = ft.Column(
#         spacing=10,
#         height=200,
#         width=200,
#         scroll=ft.ScrollMode.ALWAYS,
#         on_scroll=on_column_scroll,
#     )

#     for i in range(0, 50):
#         cl.controls.append(ft.Text(f"Text line {i}", key=str(i)))

#     page.add(
#         ft.Container(cl, border=ft.border.all(1)),
#     )

#     # 画像をBase64にエンコード
#     with open(image_path, "rb") as img_file:
#         encoded_string = base64.b64encode(img_file.read()).decode()

#     # 画像の拡張子に応じてMIMEタイプを設定
#     _, ext = os.path.splitext(image_path)
#     ext = ext.lower()
#     if ext == ".png":
#         mime = "image/png"
#     elif ext in [".jpg", ".jpeg"]:
#         mime = "image/jpeg"
#     else:
#         mime = "application/octet-stream"

#     image_data = f"data:{mime};base64,{encoded_string}"

#     # UIコンポーネントの追加
#     page.add(
#         ft.Column(
#             [
#                 # レシート画像のタイトル
#                 ft.Container(
#                     content=ft.Text("レシート画像", size=20, weight="bold"),
#                     margin=ft.Margin(top=20, left=0, right=0, bottom=10)
#                 ),
#                 # レシート画像の表示
#                 ft.Image(src=image_data, width=400, height=300, fit=ft.ImageFit.CONTAIN),
                
#                 # OCR結果のタイトル
#                 ft.Container(
#                     content=ft.Text("OCR結果", size=20, weight="bold"),
#                     margin=ft.Margin(top=20, left=0, right=0, bottom=10)
#                 ),
#                 # OCR結果の表示
#                 ft.Container(
#                     content=ft.Text(ocr_text, selectable=True, size=14),
#                     margin=ft.Margin(top=0, left=0, right=0, bottom=20)
#                 ),
#                 # 再読み込みボタン
#                 ft.Container(
#                     content=ft.ElevatedButton(
#                         "再読み込み",
#                         on_click=lambda e: page.reload()
#                     ),
#                     margin=ft.Margin(top=0, left=0, right=0, bottom=20)
#                 )
#             ],
#             alignment=ft.MainAxisAlignment.START,
#             horizontal_alignment=ft.CrossAxisAlignment.START,
#             tight=True,
#             spacing=0  # 各Containerでマージンを設定しているため、Columnのspacingは不要
#         )
#     )


import flet as ft
import base64
import os

def build_ui(page: ft.Page, image_path: str, ocr_text: str):
    """
    画像とOCR結果を表示するUIを構築します。
    """
    # スクロール可能なColumnコンポーネント
    scrollable_content = ft.Column(
        spacing=10,
        height=500,  # 表示領域の高さを指定
        scroll=ft.ScrollMode.ALWAYS,  # 常時スクロール可能に設定
    )

    # レシート画像セクション
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()

    _, ext = os.path.splitext(image_path)
    ext = ext.lower()
    mime = "image/png" if ext == ".png" else "image/jpeg" if ext in [".jpg", ".jpeg"] else "application/octet-stream"
    image_data = f"data:{mime};base64,{encoded_string}"

    # UI要素をスクロール可能な領域に追加
    scrollable_content.controls.extend([
        ft.Container(
            content=ft.Text("レシート画像", size=20, weight="bold"),
            margin=ft.Margin(top=20, left=0, right=0, bottom=10)
        ),
        ft.Image(src=image_data, width=400, height=300, fit=ft.ImageFit.CONTAIN),
        ft.Container(
            content=ft.Text("OCR結果", size=20, weight="bold"),
            margin=ft.Margin(top=20, left=0, right=0, bottom=10)
        ),
        ft.Container(
            content=ft.Text(ocr_text, selectable=True, size=14),
            margin=ft.Margin(top=0, left=0, right=0, bottom=20)
        ),
        ft.Container(
            content=ft.ElevatedButton(
                "再読み込み",
                on_click=lambda e: page.reload()
            ),
            margin=ft.Margin(top=0, left=0, right=0, bottom=20)
        )
    ])

    # ページにスクロール可能なコンテンツを追加
    page.add(
        ft.Container(
            content=scrollable_content,
            # スクロール可能な領域に枠線とパディングを追加
            # border=ft.border.all(1),
            padding=ft.Padding(10,10,10,10),
        )
    )
