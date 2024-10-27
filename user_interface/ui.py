# ui.py
import flet as ft

def build_ui(page: ft.Page):
    page.add(
        ft.Text("Welcome to My App"),
        ft.ElevatedButton("Click Me", on_click=lambda e: page.dialog(ft.AlertDialog("Button clicked!")))
    )
