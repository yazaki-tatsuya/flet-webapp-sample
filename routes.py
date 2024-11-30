# routes.py
import flet as ft
from app01_views.home_view import home_view
from app01_views.page01_view import page01_view
from app01_views.page02_view import page02_view
from app01_views.page03_view import page03_view
from app01_views.page99_view import page99_view
from app01_views.page100_view import page100_view
from app01_views.page101_view import page101_view
from app01_views.page102_view import page102_view
from app01_views.page103_view import page103_view
from app01_views.page104_view import page104_view
from app01_views.not_found_view import not_found_view

def route_change(e):
    # RouteChangeEventオブジェクトからPageオブジェクトを取得
    page = e.page
    page.views.clear()
    if page.route == "/":
        page.views.append(home_view(page))
    elif page.route == "/page01":
        page.views.append(page01_view(page))
    elif page.route == "/page02":
        page.views.append(page02_view(page))
    elif page.route == "/page03":
        page.views.append(page03_view(page))
    elif page.route == "/page99":
        page.views.append(page99_view(page))
    elif page.route == "/page100":
        page.views.append(page100_view(page))
    elif page.route == "/page101":
        page.views.append(page101_view(page))
    elif page.route == "/page102":
        page.views.append(page102_view(page))
    elif page.route == "/page103":
        page.views.append(page103_view(page))
    elif page.route == "/page104":
        page.views.append(page104_view(page))
    else:
        page.views.append(not_found_view(page))
    page.update()