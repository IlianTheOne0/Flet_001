import flet as ft

from .container_fluid import container_fluid
from .navbar import navbar

first_part = ft.Column(
    controls=[
        navbar,
        container_fluid
    ]
)