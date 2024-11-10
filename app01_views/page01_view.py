# views/page1_view.py
import flet as ft
from app02_ui_components.navbar import navbar

def page01_view(page: ft.Page):
    return ft.View(
        "/page01",
        controls=[
            navbar(page),
            ft.Text("これはページ01です。")
        ]
    )