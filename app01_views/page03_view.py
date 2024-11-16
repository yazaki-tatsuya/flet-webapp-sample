# views/page2_view.py
import flet as ft
from app02_ui_components.navbar import navbar
from app03_services.speech_service import get_audio_text
from .build_ui_v2 import build_ui_v2

def page03_view(page: ft.Page):

    page.title = "レシート読み取りアプリ - Page 99"

    # 音声データの文字起こし
    audio_text = get_audio_text()

    # build_ui関数からUIコンポーネントを取得
    content = build_ui_v2(page)


    # # 音声認識結果を表示するコンポーネントを追加
    # audio_text_control = ft.Container(
    #     content=ft.Text(audio_text, selectable=True, size=14),
    #     margin=ft.Margin(top=20, left=0, right=0, bottom=20)
    # )

    # # コンテンツに音声認識結果を追加
    # content.content.controls.append(
    #     ft.Container(
    #         content=ft.Text("音声認識結果", size=20, weight="bold"),
    #         margin=ft.Margin(top=20, left=0, right=0, bottom=10)
    #     )
    # )
    # content.content.controls.append(audio_text_control)

    # ナビゲーションバーとコンテンツを含むビューを返す
    return ft.View(
        "/page03",
        controls=[
            navbar(page),
            content,
            ft.Text("これはページ03です。")
        ]
    )