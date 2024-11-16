# app01_views/build_ui.py
# 役割：
#   各ページで共通して使用される基本的なUIコンポーネントやレイアウトを構築するための関数として設計されています。
# 　この関数は、ページ全体の共通レイアウトやスタイルを定義し、個々のページではこの関数を呼び出した後に、
# 　特定の機能やコンテンツを追加することを想定しています。
import flet as ft
from app02_ui_components.navbar import navbar

def build_ui_v2(page: ft.Page) -> ft.Container:

    """
    一覧画面のUIコンポーネントを構築します。

    Args:
        page (ft.Page): Fletのページオブジェクト。

    Returns:
        ft.Container: 一覧画面のコンテナ。
    """
    # # サンプルの一覧データ
    # items = [
    #     "アイテム1",
    #     "アイテム2",
    #     "アイテム3",
    #     "アイテム4",
    #     "アイテム5",
    # ]

    # # 一覧を作成
    # list_view = ft.ListView(
    #     expand=True,
    #     spacing=10,
    #     padding=10,
    #     controls=[
    #         ft.ListTile(
    #             title=ft.Text(item),
    #             leading=ft.Icon(ft.icons.LIST),
    #             on_click=lambda e, item=item: print(f"{item} がクリックされました。")  # サンプルのクリックイベント
    #         )
    #         for item in items
    #     ],
    # )

    # return ft.Container(
    #     content=list_view,
    # )

    """
    一覧画面のテーブル形式のUIコンポーネントを構築します。

    Args:
        page (ft.Page): Fletのページオブジェクト。

    Returns:
        ft.Container: テーブルを含むコンテナ。
    """
    """
    一覧画面のテーブル形式のUIコンポーネントを構築します。
    
    Args:
        page (ft.Page): Fletのページオブジェクト。
    
    Returns:
        ft.Container: テーブルを含むコンテナ。
    """
    # サンプルデータ
    data = [
        {"ID": 1, "名前": "アイテム1", "説明": "説明1"},
        {"ID": 2, "名前": "アイテム2", "説明": "説明2"},
        {"ID": 3, "名前": "アイテム3", "説明": "説明3"},
        {"ID": 4, "名前": "アイテム4", "説明": "説明4"},
        {"ID": 5, "名前": "アイテム5", "説明": "説明5"},
    ]

    # テーブルのカラム定義
    columns = [
        ft.DataColumn(ft.Text("ID")),
        ft.DataColumn(ft.Text("名前")),
        ft.DataColumn(ft.Text("説明")),
    ]

    # テーブルの行定義
    rows = [
        ft.DataRow(cells=[
            ft.DataCell(ft.Text(str(item["ID"]))),
            ft.DataCell(ft.Text(item["名前"])),
            ft.DataCell(ft.Text(item["説明"])),
        ]) for item in data
    ]

    # DataTableの作成
    data_table = ft.DataTable(
        columns=columns,
        rows=rows,
        # 境界線の設定（各辺を個別に指定）
        border=ft.Border(
            top=ft.BorderSide(width=1, color=ft.colors.BLACK),
            bottom=ft.BorderSide(width=1, color=ft.colors.BLACK),
            left=ft.BorderSide(width=1, color=ft.colors.BLACK),
            right=ft.BorderSide(width=1, color=ft.colors.BLACK),
        ),
        # 角の丸みを設定（各角を個別に指定）
        border_radius=ft.BorderRadius(
            top_left=5,
            top_right=5,
            bottom_left=5,
            bottom_right=5
        ),
        # 水平線と垂直線を非表示にするために透明色と幅0を設定
        horizontal_lines=ft.Border(
            top=ft.BorderSide(width=1, color=ft.colors.BLACK),
            bottom=ft.BorderSide(width=1, color=ft.colors.BLACK),
            left=ft.BorderSide(width=0, color=ft.colors.TRANSPARENT),
            right=ft.BorderSide(width=0, color=ft.colors.TRANSPARENT),
        ),
        vertical_lines=ft.Border(
            top=ft.BorderSide(width=0, color=ft.colors.TRANSPARENT),
            bottom=ft.BorderSide(width=0, color=ft.colors.TRANSPARENT),
            left=ft.BorderSide(width=1, color=ft.colors.BLACK),
            right=ft.BorderSide(width=1, color=ft.colors.BLACK),
        ),
    )

    # レスポンシブなレイアウト
    responsive_row = ft.ResponsiveRow(
        controls=[
            ft.Container(
                content=data_table,
                expand=True,  # 横幅を拡張
            )
        ],
        alignment=ft.MainAxisAlignment.START,
        # horizontal_alignment=ft.CrossAxisAlignment.START,
    )

    return ft.Container(
        content=responsive_row,
        padding=ft.Padding(20, 20, 20, 20),
        expand=True,  # 縦横の拡張
    )
