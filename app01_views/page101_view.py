# app01_views/page101_view.py
import flet as ft
from app02_ui_components.navbar import navbar
from .build_ui import build_ui 

def page101_view(page: ft.Page):

    # 改行ありのテキスト
    text = ft.Text(
        """
        ビジョン:
            HSP特有の繊細さや洞察力を活かし、社会での自己実現を可能にする環境を作る。
            単に「生きやすくする」だけでなく、「活躍できる場」を提供。
        
        具体案:
            AIによる強み発見プログラム: HSPならではのスキルや感性を評価し、それを活かせる仕事やプロジェクトを提案。
            HSP専用クリエイティブコミュニティ: アートや執筆、デザインなど、感性を最大限活かせる分野での活動を支援するプラットフォーム。
        
        期待される効果:
            HSPの人々が「自分だからこそできること」を見つけ、自己肯定感を高める。
            自分の特性が社会の中で求められていると実感できる。
        """
    )    

    return ft.View(
        "/page101",
        controls=[
            navbar(page),
            text
        ]
    )