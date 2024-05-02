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
                alt="La imagen de la herramienta magicmp3 ",
                border_radius="15px 50px",
                border="5px solid #555"
            ),
            rx.text(
                "Una herramienta desarrollada por mi gratis y de codigo abierto.",
                padding_top="5px"
            ),
            rx.heading(
                "DESCARGAR",
                size="8"
            ),
            rx.text(
                'Si quieres el ejecutable listo para windows entra en la carpeta "EXE" \
                dentro de la carpeta "dist" se encuentra "app.exe" listo para ejecutar.'
            ),
            rx.link(
                'Descarga desde github aqui  ',
                ant_components.download_icon(),
                href=costants.GITHUB_DESCARGAR
            ),
            rx.text(
                'Si quieres ejecutar la app desde vscode la carpeta assets contiene los recursos y la\
                carpeta magic_mp3_app los ficheros.py, entra al directorio principal desde vscode y ejecuta "app.py".'
            ),
            rx.link(
                'Codigo en github aqui  ',
                ant_components.codeicon(),
                href=costants.GITHUB_MAGICMP3
            ),
            rx.heading(
                "DESCRIPCION",
                size="8"
            ),
            rx.text(
                "Una app de escritorio para windows con la que podras descargar mediante una url de youtube \
                un video en formato mp4/mp3 o un clip mp4/mp3 de un punto a otro a tu escritorio facil y sin meterte a ninguna pagina con anuncios etc..\
                Para mas de un archivo de la misma url crea una carpeta y arrastra cada archivo dandole un nombre distinto."
            ),
            rx.heading(
                "INSTRUCCIONES",
                size="8"
            ),
            rx.text(
                "1 Abrimos la app en modo administrador."
            ),
            rx.text(
                "2 Pegamos la url de youtube en el campo indicado."
            ),
            rx.text(
                "3 En la parte inferior a la izquierda tenemos dos botones mp3 o mp4 para descargar."
            ),
            rx.text(
                '4 Para clip es necesario indicar en segundos "totales" el principio del mismo y el final en los campos indicados,\
                en la parte inferior a la derecha tenemos dos botones clip mp3 o clip mp4 para descargar.'
            ),
            rx.text(
                "5 Tu archivo deseado se descargara en tu escritorio, cuanto mas largo sea el video mas tarda."
            ),
            rx.text(
                "6 Cada nuevo archivo de la misma url sobreescribe el anterior, crea una carpeta y arrastra cada archivo con nombre distinto."
            ),
            rx.heading(
                "TRAILER",
                size="8"
            ),
            rx.video(
                url=costants.TRAILER_MAGIC_YOUTUBE,
                width="100%",
                height="auto"
            )
        ),
        padding_top="15px",
        style=styles.max_width_style
    )
