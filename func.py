# https://www.figma.com/community/file/1012561224815784091

import flet as ft

def start():
    ft.app(main, assets_dir='assets', view=ft.AppView.WEB_BROWSER)

def main(page: ft.Page):
    page.theme = ft.Theme(font_family='fonts/OpenSans-Regular.ttf')
    page.theme = ft.ThemeMode.LIGHT

    # header
    brandname = ft.Text (
        'Brandname',
        size=24
    )

    home_button = ft.CupertinoButton(
        content=ft.Text('Home'),
        opacity_on_click=0.3
    )
    product_button = ft.CupertinoButton(
        content=ft.Text('Product'),
        opacity_on_click=0.3
    )
    pricing_button = ft.CupertinoButton(
        content=ft.Text('Pricing'),
        opacity_on_click=0.3
    )
    contact_button = ft.CupertinoButton(
        content=ft.Text('Contact'),
        opacity_on_click=0.3
    )


    header = ft.Row([brandname, home_button, product_button, pricing_button, contact_button])

    page.add(
        header
    )