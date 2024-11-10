import flet as ft

# UIの構築
def build_ui(page: ft.Page, image_url: str, ocr_text: str):
    """
    画像とOCR結果を表示するUIを構築します。
    
    Args:
        page (ft.Page): Fletのページオブジェクト。
        image_url (str): 表示する画像のURL（SAS URL）。
        ocr_text (str): OCRの結果テキスト。
    """

    # スクロール可能なColumnコンポーネント
    scrollable_content = ft.Column(
        spacing=10,
        height=500,  # 表示領域の高さを指定
        scroll=ft.ScrollMode.ALWAYS,  # 常時スクロール可能に設定
    )

    # UI要素をスクロール可能な領域に追加
    scrollable_content.controls.extend([
        # レシート画像のタイトル
        ft.Container(
            content=ft.Text("レシート画像", size=20, weight="bold"),
            margin=ft.Margin(top=20, left=0, right=0, bottom=10)
        ),
        # レシート画像の表示
        ft.Image(src=image_url, width=400, height=300, fit=ft.ImageFit.CONTAIN),
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