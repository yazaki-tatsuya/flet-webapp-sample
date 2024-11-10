# views/home_view.py
import flet as ft
from app02_ui_components.navbar import navbar

def home_view(page: ft.Page):
    return ft.View(
        "/",
        controls=[
            navbar(page),
            ft.Column([
                ft.Text("これはホームページです。"),
                ft.ElevatedButton("ページ01へ", on_click=lambda e: page.go("/page01")),
                ft.ElevatedButton("ページ02へ", on_click=lambda e: page.go("/page02")),
                ft.ElevatedButton("ページ99へ", on_click=lambda e: page.go("/page99")),
            ])
        ]
    )
