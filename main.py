import flet as ft
from database_access.db_access import get_data_from_db
from user_interface.ui import build_ui

def main(page: ft.Page):
    # 画面の初期化
    page.title = "My Flet App"
    
    # UIの構築
    build_ui(page)

    # データベースからのデータ取得
    data = get_data_from_db()
    page.controls.append(ft.Text(f"Database data: {data}"))
    page.update()

app = ft.app(main, export_asgi_app=True)



# import flet as ft

# def main(page: ft.Page):
#     # タイトルを設定
#     page.title = "Simple Registration Form"

#     # ユーザー名の入力フィールド
#     username = ft.TextField(label="Username", autofocus=True)
#     page.add(username)

#     # パスワードの入力フィールド
#     password = ft.TextField(label="Password", password=True)
#     page.add(password)

#     # 登録ボタン押下時の処理
#     def register_click(e):
#         # ここで登録処理を行う（今は単に入力されたユーザー名を表示するだけ）
#         page.add(ft.Text(value=f"Registered user: {username.value}"))

#     # 登録ボタン
#     register_btn = ft.ElevatedButton(text="Register", on_click=register_click)
#     page.add(register_btn)


# app = ft.app(main, export_asgi_app=True)