import reflex as rx
import mago_oscuro91_web_rx.constants as costants
from mago_oscuro91_web_rx.styles import styles
from mago_oscuro91_web_rx.components import ant_components


def herramienta_view() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.heading(
                "HERRAMIENTA",
                font_size="300%",
                size="8"
            ),
            rx.image(
                src="/herramienta_magicmp3_foto.png",
                alt="La imagen de la herramienta magic mp3",
                border_radius="15px 50px",
                border="5px solid #555"
            ),
            rx.text(
                "Una herramienta desarrollada por mi gratis y de código abierto.",
                padding_top="5px"
            ),
            rx.heading(
                "DESCARGAR",
                size="8"
            ),
            rx.text(
                'Si quieres el ejecutable listo para Windows entra en la carpeta "EXE" \
                dentro de la carpeta "dist" se encuentra "app.exe" listo para ejecutar.'
            ),
            rx.link(
                'Descarga desde GitHub aquí  ',
                ant_components.download_icon(),
                href=costants.GITHUB_DESCARGAR
            ),
            rx.text(
                'Si quieres ejecutar la app desde vscode la carpeta assets contiene los recursos y la\
                carpeta magic_mp3_app los ficheros.py, entra al directorio principal desde VScode y ejecuta "app.py".'
            ),
            rx.link(
                'Código en GitHub aquí  ',
                ant_components.codeicon(),
                href=costants.GITHUB_MAGICMP3
            ),
            rx.heading(
                "DESCRIPCIÓN",
                size="8"
            ),
            rx.text(
                "Una app de escritorio para Windows con la que podrás descargar mediante una URL de YouTube \
                un video en formato mp4/mp3 o un clip mp4/mp3 de un punto a otro a tu escritorio fácil y sin meterte a ninguna página con anuncios, etc...\
                Para más de un archivo de la misma URL, crea una carpeta y arrastra cada archivo dándole un nombre distinto."
            ),
            rx.heading(
                "INSTRUCCIONES",
                size="8"
            ),
            rx.text(
                "1 Abrimos la app en modo administrador."
            ),
            rx.text(
                "2 Pegamos la URL de YouTube en el campo indicado."
            ),
            rx.text(
                "3 En la parte inferior a la izquierda tenemos dos botones mp3 o mp4 para descargar."
            ),
            rx.text(
                '4 Para clip es necesario indicar en segundos "totales" el principio del mismo y el final en los campos indicados,\
                en la parte inferior a la derecha tenemos dos botones clip mp3 o clip mp4 para descargar.'
            ),
            rx.text(
                "5 Tu archivo deseado se descargara en tu escritorio, cuanto más largo sea el video más tarda."
            ),
            rx.text(
                "6 Cada nuevo archivo de la misma URL sobreescribe el anterior, crea una carpeta y arrastra cada archivo con nombre distinto."
            ),
            rx.heading(
                "TUTORIAL",
                size="8"
            ),
            rx.video(
                url=costants.TUTORIAL_MAGICMP3,
                width="100%",
                height="auto"
            )
        ),
        padding_top="15px",
        style=styles.max_width_style
    )
