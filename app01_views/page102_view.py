# app01_views/page102_view.py
import flet as ft
from app02_ui_components.navbar import navbar
from .build_ui import build_ui 

def page102_view(page: ft.Page):

    # 改行ありのテキスト
    text = ft.Text(
        """
        ビジョン:
            AIを「共感型の友人」や「伴走者」として活用し、HSPの人々の孤独感を軽減。
            自分の感情や悩みに対して常に共感し、対話を通じて新たな気づきを提供。
        
        具体案:
            AIカウンセラー: ユーザーが深く考えすぎた時に「自分が信じている価値観」や「心の軸」をリマインド。
            共感モード搭載AI: 普段の生活の中で感じたストレスや喜びを記録し、共感する形で応答。
        
        期待される効果:
            「誰かに受け入れられている」という感覚を常に持てる。
            孤独を感じず、自分のペースで前向きに生きられる。
        """
    )    

    return ft.View(
        "/page102",
        controls=[
            navbar(page),
            text
        ]
    )