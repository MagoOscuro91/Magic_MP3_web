import reflex as rx


def banner() -> rx.Component:
    return rx.hstack(
        rx.spacer(),
        rx.heading(
            "MAGICMP3",
            font_size="300%",
            font_family="miltown_",
            color="#00CC00"
        ),
        rx.spacer(),
        align="center",
        background_image="url('/matrix_verde.jpg')",
        background_size="cover",
        background_position="center",
        width="100%",
        height="10em"
    )
