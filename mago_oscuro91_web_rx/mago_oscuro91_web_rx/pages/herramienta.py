import reflex as rx
from mago_oscuro91_web_rx.util import _meta, title_herramienta, description_herramienta
from mago_oscuro91_web_rx.views.footer import footer
from mago_oscuro91_web_rx.views.navbar import navbar
from mago_oscuro91_web_rx.views.navbar2 import navbar2
from mago_oscuro91_web_rx.views.dark_mode import dark_mode
from mago_oscuro91_web_rx.views.herramienta_view import herramienta_view
from mago_oscuro91_web_rx.views.banner import banner
from mago_oscuro91_web_rx.views.author import author
from mago_oscuro91_web_rx.styles.colors import Colors


@rx.page(
        route="/herramienta",
        title=title_herramienta,
        description=description_herramienta,
        # image="",
        meta=_meta
)
def herramienta() -> rx.Component:
    return rx.box(
        dark_mode(),
        banner(),
        navbar("Hola neo..."),
        rx.center( 
            rx.vstack(
                herramienta_view(),
                author(),
                width="100%",
                spacing="4",
                align_items="center"
            )
        ),
        rx.center(
            footer(),
            bg=Colors.NEGRO_NAVBAR
        ),
        navbar2()
    )
