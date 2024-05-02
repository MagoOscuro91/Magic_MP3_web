import reflex as rx
from mago_oscuro91_web_rx.util import _meta, title_index, description_index
from mago_oscuro91_web_rx.styles.colors import Colors
from mago_oscuro91_web_rx.views.footer import footer
from mago_oscuro91_web_rx.views.navbar import navbar
from mago_oscuro91_web_rx.views.navbar2 import navbar2
from mago_oscuro91_web_rx.views.dark_mode import dark_mode
from mago_oscuro91_web_rx.views.banner import banner
from mago_oscuro91_web_rx.views.author import author
from mago_oscuro91_web_rx.views.index_view import index_view, index_view_image


@rx.page(
        title=title_index,
        description=description_index,
        meta=_meta
)
def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        dark_mode(),
        banner(),
        navbar(),
        rx.center( 
            rx.vstack(
                index_view_image(),
                index_view(),
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
