# app01_views/page103_view.py
import flet as ft
from app02_ui_components.navbar import navbar
from .build_ui import build_ui 

def page103_view(page: ft.Page):

    # 改行ありのテキスト
    text = ft.Text(
        """
        ここにテキストが入ります
        """
    )    

    return ft.View(
        "/page104",
        controls=[
            navbar(page),
            text
        ]
    )