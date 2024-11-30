# app01_views/page100_view.py
import flet as ft
from app02_ui_components.navbar import navbar
from .build_ui import build_ui 

def page100_view(page: ft.Page):

    # 改行ありのテキスト
    text = ft.Text(
        """
        ビジョン:
            HSPが感じやすい不安や否定的な感情を、「脳内での言語変換」によってポジティブな感情に変換するAIツール。
            AIが一緒に「感情の再フレーミング」を行い、思考の癖を変える。

        具体案:
            会話型AIコーチ: ユーザーが不安や悲しみを感じた際、その内容をAIに伝えると、具体的で励まされる解釈や視点を提示。
            セルフケア日記ツール: 日々の出来事や感情を記録すると、AIが分析し、長期的にポジティブなパターンを形成。

        期待される効果:
            自分の感情を否定せず、価値あるものとして再認識。
            日々の生活における「小さな幸せ」や喜びを増幅させる。
        """
    )    

    return ft.View(
        "/page100",
        controls=[
            navbar(page),
            text
        ]
    )