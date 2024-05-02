import reflex as rx
from mago_oscuro91_web_rx.util import _meta, title_colacao, description_colacao
from mago_oscuro91_web_rx.views.footer import footer
from mago_oscuro91_web_rx.views.navbar import navbar
from mago_oscuro91_web_rx.views.navbar2 import navbar2
from mago_oscuro91_web_rx.views.dark_mode import dark_mode
from mago_oscuro91_web_rx.views.banner import banner
from mago_oscuro91_web_rx.views.author import author
from mago_oscuro91_web_rx.views.colacao_view import colacao_view
from mago_oscuro91_web_rx.styles.colors import Colors


@rx.page(
        route="/colacao",
        title=title_colacao,
        description=description_colacao,
        # image="",
        meta=_meta
)
def herramienta() -> rx.Component:
    return rx.box(
        dark_mode(),
        banner(),
        navbar(),
        rx.center( 
            rx.vstack(
                colacao_view(),
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
