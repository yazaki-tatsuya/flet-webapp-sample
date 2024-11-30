# app01_views/page99_view.py
import flet as ft
from app02_ui_components.navbar import navbar
from .build_ui import build_ui 

def page99_view(page: ft.Page):

    # build_ui関数からUIコンポーネントを取得
    content = build_ui(page)

    # ナビゲーションバーとコンテンツを含むビューを返す
    return ft.View(
        "/page99",
        controls=[
            navbar(page),
            content,
            ft.Text("これはページ99です。")
        ]
    )