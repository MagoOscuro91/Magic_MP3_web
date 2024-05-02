import reflex as rx
import mago_oscuro91_web_rx.constants as costants
from mago_oscuro91_web_rx.styles import styles
from mago_oscuro91_web_rx.components import ant_components


def plan_view() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.heading(
                "PLAN DE ESTUDIO",
                font_size="300%",
                size="8",
                margin_y="25px"
            ),
            rx.heading(
                "AUTOR",
                size="8"
            ),
            rx.text(
                "MagoOscuro91",
                padding_top="5px"
            ),
            rx.heading(
                "OBJETIVO",
                size="8"
            ),
            rx.text(
                "Aprender a programar en un lenguaje de programacion de manera autodidacta y gratis."
            ),
            rx.heading(
                "MI PLAN DE ESTUDIO",
                size="8"
            ),
            rx.text(
                "Este es el plan de estudio que a mi me a ayudado a de no saber ni ingles practicamente ni de programacion \
                a diseñar esta web con un framework nuevo como reflex en 6 meses, espero que ati tambien te ayude. Este plan me a servido a mi \
                pero a ti puede que no. En internet existe informacion mejor seguro, esto es una opinion personal nada mas."
            ),
            rx.text(
                "1 Elige un lenguaje amigable de programacion tranquilamente, investiga en base a lo que quieres acavar creando a corto plazo \
                por que a programar se aprende programando y peleandote con tu codigo, cuanto mejor base tengas mas facil te sera luego aprender\
                o programar algo nuevo por lo que siempre recomiendo estudiar un grado medio o superior de desarollo de aplicaciones multiplataforma o similiar.\
                Pero si es cierto que cada vez mas las empresas buscan gente que demuestre sus habilidades con proyectos, trabajos etc no solo un titulo universitario.\
                En internet hoy en dia tenemos a personas maravillosas que regalan su tiempo y conocimiento como mouredev, midudev, holamundo (nicolas), etc.\
                Tenemos la inteligencia artificial que bien utilizada puedes aprender mucho mas facil y rapido sobre la marcha, mi manera de usarla es para ver ejemplos de algoritmos, estructuras,\
                librerias, etc y si no entiendo una linea le pido que me la explique pero que no me de la solucion.Mi lenguaje fue python por gusto personal y por recomendaciones generales\
                lo amigable que parecia comparado con c.Tambien recomiendo el curso cs50x de harvad gratis para ir cogiendo base poco a poco."
            ),
            rx.text(
                "2 Tenemos el lenguaje despues de haberlo pensado bien en mi caso python, ahora es el momento de buscar contenido gratuito para tu lenguaje."
            ),
            rx.text(
                "Estos son los cursos en orden que yo ize:"
            ),
            rx.text(
                "* Ultimate python de holamundo (Nicolas) las 5h gratuitas de su canal, con este aprendi de 0 rapido y poco a poco pero no esta completo.",
                margin_top="20px"
            ),
            rx.video(
                url="https://www.youtube.com/watch?v=tQZy0U8s9LY&t=23s&ab_channel=HolaMundo",
                width="100%",
                height="auto",
                margin_bottom="25px"
            ),
            rx.text(
                "* Python para principiantes desde 0 mouredev, con este repase y asente muchos conceptos."
            ),
            rx.video(
                url="https://www.youtube.com/watch?v=Kp4Mvapo5kc&t=21443s&ab_channel=MoureDevbyBraisMoure",
                width="100%",
                height="auto",
                margin_bottom="25px"
            ),
            rx.text(
                "* Python intermedio desde 0 mouredev, con este ya me empeze a soltar ya hacia mis pruebas para ideas de apps que seme ocurrian."
            ),
            rx.video(
                url="https://www.youtube.com/watch?v=TbcEqkabAWU&t=2s&ab_channel=MoureDevbyBraisMoure",
                width="100%",
                height="auto",
                margin_bottom="25px"
            ),
            rx.text(
                "* Python para backend desde 0 mouredev, en este punto me comfie pare un tiempo por navidad dejando el curso a medias cuando retome\
                 me di cuenta que lo tenia que repasar y aun no lo e acavado."
            ),
            rx.video(
                url="https://www.youtube.com/watch?v=_y9qQZXE24A&ab_channel=MoureDevbyBraisMoure",
                width="100%",
                height="auto",
                margin_bottom="25px"
            ),
            rx.text(
                "* Python web mouredev 1h, cuando retome el curso anterior me cruze con este video que llamo mi atencion y me gusto mucho"
            ),
            rx.video(
                url="https://www.youtube.com/watch?v=2u7JlBEavx0&t=2773s&ab_channel=MoureDevbyBraisMoure",
                width="100%",
                height="auto",
                margin_bottom="25px"
            ),
            rx.text(
                "* Python web mouredev 3h, aDEViento_web me toco pelearme con la version del framework y me acostumbre a entrar documentacion a buscar lo que \
                necesitaba.Me puse a copiar una web de una empresa de mi pueblo como trabajo final del curso cuando me cruze con la hackaton y este concurso de reflex\
                 al que me presento con esta web y mucha ilusion no de ganar (que tambien) si no de compartir algo desarrollado por mi que ayude a alguien."
            ),
            rx.video(
                url="https://www.youtube.com/watch?v=h8Tn0ITRoQs&t=1s&ab_channel=MoureDevTV",
                width="100%",
                height="auto",
                margin_bottom="25px"
            ),
            rx.text(
                "3 Necesitas un horario y ser disciplinado con el, al principio al estar motivados vamos a estar bien pero la motivacion no dura eternamente la disciplina si.\
                Como estoy acostumbrado a trabajar 8h 5 dias a la semana, decidi usar ese tiempo para ocuparme de las tareas del hogar, estudiar, entrenar y programar con la idea de\
                acavar programando esas 8h en mi teletrabajo durmiendo 8h y en las 8h restantes ocuparme de tareas del hogar ejercicio y ocio.\
                El dia tiene 24h, 8h para el grupo anterior, 8h son sagradas para dormir necesitas descansar para tener mejor rendimiento al dia siguiente, 8h de tiempo libre es super importante\
                desconectar el cerebro, es un musculo que tambien se cansa y tenemos que cuidar su salud.\
                El dia que no te apetezca que va a pasar te pones a repasar videos de cursos o material ya echo tranquilamente y sin agobios, el caso es ser disciplinado con tu horario."
            ),
            rx.text(
                "4 Cuidar nuestro cuerpo, al pasar tantas horas sentado nuestro cuerpo se deteriora.\
                Mantener un orden en casa y zona de trabajo limpia.\
                Administra bien tu tiempo para cambiarlo por sabiduria salud o dinero lo que mas necesites ahora.\
                Come bien, duerme 8h az 1h de ejercicio 5 dias a la semana\
                3h o 5h de ocio diarias y 2h o 4h tareas en general.\
                Cuidar nuestro estado emocional y mental tambien es super importante, aveces sentiras frustracion o sinplemente tendras\
                un mal dia.No pasa nada todos tenemos dias mejores dias peores tomate un colacao ponte tu cancion favorita y motivate.\
                Aqui te dejo una lista de Spotify para programar que ami me anima en estos momentos espero que te guste.En tener tiempo\
                añadire todas las canciones."
            ),
            rx.link(
                "Lista Spotify By: jona_THAI para programar Metal_python  ",
                ant_components.spotify_icon(),
                href="https://open.spotify.com/playlist/0IuAVLwz2i6TzxiU3W9jK4?si=bcbe6c399cea4fb4"
            ),
            rx.text(
                "5 Proximamente..."
            )
            # rx.image(
            #     src="/herramienta_magicmp3_foto.png",
            #     alt="La imagen de la herramienta magicmp3 ",
            #     border_radius="15px 50px",
            #     border="5px solid #555"
            # ),
            # rx.link(
            #     'Descarga desde github aqui  ',
            #     ant_components.download_icon(),
            #     href=costants.GITHUB_DESCARGAR
            # ),
            # rx.link(
            #     'Codigo en github aqui  ',
            #     ant_components.codeicon(),
            #     href=costants.GITHUB_MAGICMP3
            # ),
            # rx.text(
            #     "Un dia creando una app de escritorio quise personalizar la parte frontend, buscando sonidos para mis botones\
            #     seme ocurrio la idea de desarrollar algo como ejercicio que me ayudara en este campo para mi comodidad."
            # ),
        ),
        padding_top="15px",
        style=styles.max_width_style
    )
