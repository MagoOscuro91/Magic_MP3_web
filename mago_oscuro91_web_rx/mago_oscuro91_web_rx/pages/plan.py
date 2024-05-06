import reflex as rx
from mago_oscuro91_web_rx.util import _meta, title_plan, description_plan
from mago_oscuro91_web_rx.views.footer import footer
from mago_oscuro91_web_rx.views.navbar import navbar
from mago_oscuro91_web_rx.views.navbar2 import navbar2
from mago_oscuro91_web_rx.views.dark_mode import dark_mode
from mago_oscuro91_web_rx.views.plan_view import plan_view, index_plan_head
from mago_oscuro91_web_rx.views.banner import banner
from mago_oscuro91_web_rx.views.author import author
from mago_oscuro91_web_rx.styles.colors import Colors


@rx.page(
        route="/plan",
        title=title_plan,
        description=description_plan,
        # image="",
        meta=_meta
)
def herramienta() -> rx.Component:
    return rx.box(
        dark_mode(),
        banner(),
        navbar("Wake up, Neo..."),
        rx.center( 
            rx.vstack(
                index_plan_head(),
                plan_view(),
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
