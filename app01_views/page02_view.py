# views/page2_view.py
import flet as ft
from app02_ui_components.navbar import navbar

def page02_view(page: ft.Page):
    return ft.View(
        "/page02",
        controls=[
            navbar(page),
            ft.Text("これはページ02です。")
        ]
    )