# main.py
import flet as ft
from routes import route_change

def main(page: ft.Page):

    page.title = "レシート読み取りアプリ"
    # ルートの変更時に呼び出す関数を設定
    page.on_route_change = route_change
    # 初期ページの設定
    page.go(page.route)

if __name__ == "__main__":
    # 直接実行された場合はFletアプリを起動
    ft.app(target=main, view=ft.AppView.FLET_APP, port=8550, web_renderer="auto")
else:
    # モジュールとしてインポートされた場合は、ASGIアプリとしてエクスポート
    app = ft.app(target=main, export_asgi_app=True)
