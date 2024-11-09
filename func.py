# https://www.figma.com/community/file/1012561224815784091

import flet as ft

from files.header.first_part import *
from files.second_part import *
from files.third_part import *
from files.fourth_part import *
from files.fifth_part import *
from files.sixth_part import *
from files.footer import *

def start():
    ft.app(main, assets_dir='assets', view=ft.AppView.WEB_BROWSER)

def main(page: ft.Page):
    page.title = 'School site'

    page.theme = ft.Theme(font_family='fonts/OpenSans-Regular.ttf')
    page.theme_mode = ft.ThemeMode.LIGHT

    page.scroll = ft.ScrollMode.AUTO

    page.add(
        first_part,
        second_part,
        third_part,
        fourth_part,
        fifth_part,
        sixth_part,
        footer
    )