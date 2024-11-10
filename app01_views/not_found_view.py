# views/not_found_view.py
import flet as ft
from app02_ui_components.navbar import navbar

def not_found_view(page: ft.Page):
    return ft.View(
        "/404",
        controls=[
            navbar(page),
            ft.Column(
                [
                    ft.Text("404 - ページが見つかりません", style="headlineMedium"),
                    ft.Text("お探しのページは存在しないか、移動した可能性があります。"),
                    ft.ElevatedButton(
                        text="ホームに戻る",
                        on_click=lambda e: page.go("/")
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ]
    )
