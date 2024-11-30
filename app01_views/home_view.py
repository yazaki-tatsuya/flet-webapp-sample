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
                ft.ElevatedButton("ページ03へ", on_click=lambda e: page.go("/page03")),
                ft.ElevatedButton("ページ99へ", on_click=lambda e: page.go("/page99")),
                ft.ElevatedButton("ページ：(仮)「感情の「再定義」を助けるAIコーチング」へ", on_click=lambda e: page.go("/page100")),
                ft.ElevatedButton("ページ：(仮)「新しい「感性の活用」モデルを提案するプラットフォーム」へ", on_click=lambda e: page.go("/page101")),
                ft.ElevatedButton("ページ：(仮)「人間とAIの「共感パートナーシップ」へ", on_click=lambda e: page.go("/page102")),
                ft.ElevatedButton("ページ：(仮)「自分の世界を「再構築」する体験型VR/AR」へ", on_click=lambda e: page.go("/page103")),
                ft.ElevatedButton("ページ104へ", on_click=lambda e: page.go("/page104")),
                
            ])
        ]
    )
