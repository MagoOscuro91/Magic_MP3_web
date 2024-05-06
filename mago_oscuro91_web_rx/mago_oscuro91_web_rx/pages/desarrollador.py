import reflex as rx
from mago_oscuro91_web_rx.util import _meta, title_desarrollador, description_desarrollador
from mago_oscuro91_web_rx.views.footer import footer
from mago_oscuro91_web_rx.views.navbar import navbar
from mago_oscuro91_web_rx.views.navbar2 import navbar2
from mago_oscuro91_web_rx.views.dark_mode import dark_mode
from mago_oscuro91_web_rx.views.author import author
from mago_oscuro91_web_rx.views.desarrollador_view import desarrollador_view1, desarrollador_view2, desarrollador_view3
from mago_oscuro91_web_rx.views.banner import banner
from mago_oscuro91_web_rx.styles.colors import Colors


@rx.page(
        route="/desarrollador",
        title=title_desarrollador,
        description=description_desarrollador,
        # image="",
        meta=_meta
)
def herramienta() -> rx.Component:
    return rx.box(
        dark_mode(),
        banner(),
        navbar("Hola Neo..."),
        rx.center( 
            rx.vstack(
                desarrollador_view1(),
                author(),
                desarrollador_view2(),
                desarrollador_view3(),
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
