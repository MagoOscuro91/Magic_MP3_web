import reflex as rx
from mago_oscuro91_web_rx.styles.colors import Colors
from mago_oscuro91_web_rx.components import ant_components


def navbar2() -> rx.Component:
    return rx.flex(
        rx.spacer(),
        rx.link(
            ant_components.codeicon(padding_left="27.5px"),
            rx.text("Herramienta", size="1", margin_left="3px"),
            margin="0.3em",
            href="/herramienta",
            bg=Colors.NEGRO_NAVBAR.value
        ),
        rx.spacer(),
        rx.link(
            ant_components.codeicon(padding_left="31px"),
            rx.text("Plan de estudio", size="1"),
            margin="0.3em",
            href="/plan",
            bg=Colors.NEGRO_NAVBAR.value
        ),
        rx.spacer(),
        rx.link(
            ant_components.codeicon(padding_left="27.5px"),
            rx.text("Desarollador", size="1", margin_left="3px"),
            margin="0.3em",
            href="/desarrollador",
            bg=Colors.NEGRO_NAVBAR.value
        ),
        rx.spacer(),
        rx.link(
            ant_components.coffee_icon(padding_left="16px"),
            rx.text("Colacao", size="1", margin_left="3px"),
            margin="0.3em",
            href="/colacao",
            bg=Colors.NEGRO_NAVBAR.value
        ),
        rx.spacer(),
        bg=Colors.NEGRO_NAVBAR.value,
        border_top="1px solid #333333",
        flex_direction=["row", "row", "row", "row", "row"],
        position="sticky",
        z_index="999",
        bottom="0"
    )
