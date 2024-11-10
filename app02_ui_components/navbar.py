# components/navbar.py
import flet as ft

def navbar(page: ft.Page):
    return ft.AppBar(
        title=ft.Text("アプリケーション名"),
        leading=ft.IconButton(ft.icons.HOME, on_click=lambda e: page.go("/")),
        actions=[
            ft.IconButton(ft.icons.SETTINGS, on_click=lambda e: page.go("/settings")),
        ]
    )
