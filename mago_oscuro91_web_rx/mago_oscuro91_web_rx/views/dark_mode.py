import reflex as rx


def dark_mode() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            width="100%",
            bg="#fff"
        ),
        rx.hstack(
            rx.spacer(),
            rx.hstack(
                rx.text("Light/Dark"),
                rx.color_mode.switch(padding_top="4px"),
                padding_y="0.50em"
            ),
            align_items="start",
            padding_x="1em",
            width="100%"
            # bg="#34393D"
        ),
        widt="100%"
        # bg="#fff"
    )
