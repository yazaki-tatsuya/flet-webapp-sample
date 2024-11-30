# app01_views/page104_view.py
import flet as ft
from app02_ui_components.navbar import navbar
from .build_ui import build_ui 

def page104_view(page: ft.Page):

    # 改行ありのテキスト
    text = ft.Text(
        """
        ビジョン:
            HSPの人々が自分の理想の「心地よい世界」をデザインし、それを仮想空間で体験できる。
            現実世界の困難に対する耐性を高めるためのリハーサル環境を提供。
        
        具体案:
            理想の空間設計ツール: 自分が安心できる空間や状況をVR内でデザインし、現実にもその一部を反映。
            自信構築シナリオ: VR内で他者との対話や挑戦的な状況をシミュレートし、自信を高めるトレーニング。
        
        期待される効果:
            安全な環境で挑戦を重ねることで、現実の困難に立ち向かう力を育む。
            自分が望む人生の「模擬体験」が可能になる。
        """
    )    

    return ft.View(
        "/page104",
        controls=[
            navbar(page),
            text
        ]
    )