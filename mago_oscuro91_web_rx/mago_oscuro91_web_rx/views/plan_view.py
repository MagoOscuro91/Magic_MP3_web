import reflex as rx
import mago_oscuro91_web_rx.constants as costants
from mago_oscuro91_web_rx.styles import styles
from mago_oscuro91_web_rx.components import ant_components


def index_plan_head() -> rx.Component:
    return rx.vstack(
        rx.spacer(weidth="100%"),
        rx.heading(
            "PLAN DE ESTUDIO",
            font_size="300%",
            size="8",
            margin_y="35px"
        ),
        rx.heading(
            "AUTOR",
            size="8"
        ),
        rx.text(
            "MagoOscuro91"
        ),
        rx.heading(
            "OBJETIVO",
            margin_top="25px",
            size="8"
        ),
        rx.text(
            "Aprender a programar"
        ),
        rx.text(
            "en un lenguaje de programación"
        ),
        rx.text(
            "de manera autodidacta y gratis."
        ),
        rx.spacer(weidth="100%"),
        style=styles.max_width_style_center
    )


def plan_view() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.heading(
                "MI PLAN DE ESTUDIO",
                margin_top="15px",
                size="8"
            ),
            rx.text(
                "Este es el plan de estudio que a mí me ha ayudado a de no saber ni inglés prácticamente ni de programación \
                a diseñar esta web con un Framework nuevo como Reflex en 6 meses, espero que a ti también te ayude. Este plan me ha servido a mi \
                pero a ti puede que no. En internet existe información mejor seguro, esto es una opinión personal, nada más.",
                margin_top="10px"
            ),
            rx.text(
                "1 Elige un lenguaje amigable de programación tranquilamente, investiga basándote en lo que quieres acabar creando a corto plazo \
                por qué a programar se aprende programando y peleándote con tu código, cuanto mejor base tengas más fácil te será luego aprender\
                o programar algo nuevo por lo que siempre recomiendo estudiar un grado medio o superior de desarrollo de aplicaciones multiplataforma o similar.\
                Pero si es cierto que cada vez más las empresas buscan gente que demuestre sus habilidades con proyectos, trabajos, etc... no solo un título universitario.\
                En internet hoy en día tenemos a personas maravillosas que regalan su tiempo y conocimiento como mouredev, midudev, hola mundo (Nicolás), etc.\
                Tenemos la inteligencia artificial que bien utilizada puedes aprender mucho más fácil y rápido sobre la marcha, mi manera de usarla es para ver ejemplos de algoritmos, estructuras,\
                librerías, etc y si no entiendo una línea le pido que me la explique, pero que no me dé la solución. Mi lenguaje fue Python por gusto personal y por recomendaciones generales\
                lo amigable que parecía comparado con c. También recomiendo el curso CS50X de Harvard gratis para ir cogiendo base poco a poco.",
                margin_top="15px"
            ),
            rx.text(
                "2 Tenemos el lenguaje después de haberlo pensado bien en mi caso Python, ahora es el momento de buscar contenido gratuito para tu lenguaje.",
                margin_top="15px"
            ),
            rx.text(
                "Estos son los cursos en orden que yo realicé:"
            ),
            rx.text(
                "* Ultímate Python de @HolaMundoDev (Nicolás) las 5 h gratuitas de su canal, con este aprendí de 0 rápidos y poco a poco, pero no está completo.",
                margin_top="10px"
            ),
            rx.video(
                url="https://www.youtube.com/watch?v=tQZy0U8s9LY&t=23s&ab_channel=HolaMundo",
                width="100%",
                height="auto",
                margin_bottom="25px"
            ),
            rx.text(
                "* Python para principiantes desde 0 de @mouredev (MoureDev by Brais Moure) de su canal, con este repase y asenté muchos conceptos.",
                margin_top="10px"
            ),
            rx.video(
                url="https://www.youtube.com/watch?v=Kp4Mvapo5kc&t=21443s&ab_channel=MoureDevbyBraisMoure",
                width="100%",
                height="auto",
                margin_bottom="25px"
            ),
            rx.text(
                "* Python intermedio desde 0 de @mouredev (MoureDev by Brais Moure) de su canal, con este ya me empecé a soltar y hacía mis pruebas para ideas de apps que seme ocurrían.",
                margin_top="10px"
            ),
            rx.video(
                url="https://www.youtube.com/watch?v=TbcEqkabAWU&t=2s&ab_channel=MoureDevbyBraisMoure",
                width="100%",
                height="auto",
                margin_bottom="25px"
            ),
            rx.text(
                "* Python para back-end desde 0 de @mouredev (MoureDev by Brais Moure) de su canal, en este punto me confíe pare un tiempo por Navidad dejando el curso a medias cuando retome\
                 me di cuenta de que lo tenía que repasar y aún no lo he acabado.",
                 margin_top="10px"
            ),
            rx.video(
                url="https://www.youtube.com/watch?v=_y9qQZXE24A&ab_channel=MoureDevbyBraisMoure",
                width="100%",
                height="auto",
                margin_bottom="25px"
            ),
            rx.text(
                "* Python web 1 h de @mouredev (MoureDev by Brais Moure) de su canal, cuando retome el curso anterior me cruce con este video que llamo mi atención y me gusto mucho",
                margin_top="10px"
            ),
            rx.video(
                url="https://www.youtube.com/watch?v=2u7JlBEavx0&t=2773s&ab_channel=MoureDevbyBraisMoure",
                width="100%",
                height="auto",
                margin_bottom="25px"
            ),
            rx.text(
                "* Python web 3 h de @mouredev (MoureDev by Brais Moure) de su canal, aDEViento_web me toco pelearme con la versión del Framework y me acostumbré a entrar documentación a buscar lo que \
                necesitaba.Me puse a copiar una web de una empresa de mi pueblo como trabajo final del curso cuando me crucé con la hackaton y este concurso de Reflex\
                 al que me presento con esta web y mucha ilusión no de ganar (que también) sino de compartir algo desarrollado por mí que ayude a alguien.",
                 margin_top="10px"
            ),
            rx.video(
                url="https://www.youtube.com/watch?v=h8Tn0ITRoQs&t=1s&ab_channel=MoureDevTV",
                width="100%",
                height="auto",
                margin_bottom="25px"
            ),
            rx.text(
                "3 Necesitas un horario y ser disciplinado con él, al principio al estar motivados vamos a estar bien, pero la motivación no dura eternamente la disciplina sí.\
                Como estoy acostumbrado a trabajar 8 h 5 días a la semana, decidí usar ese tiempo para ocuparme de las tareas del hogar, estudiar, entrenar y programar con la idea de\
                acavar programando esas 8 h en mi teletrabajo durmiendo 8 h y en las 8 h restantes ocuparme de tareas del hogar, ejercicio y ocio.\
                El día tiene 24 h, 8 h para el grupo anterior, 8 h son sagradas para dormir, necesitas descansar para tener mejor rendimiento al día siguiente, 8 h de tiempo libre es superimportante\
                desconectar el cerebro, es un músculo que también se cansa y tenemos que cuidar su salud.\
                El día que no te apetezca que va a pasar te pones a repasar videos de cursos o material ya echo, tranquilamente y sin agobios, el caso es ser disciplinado con tu horario.",
                margin_top="10px"
            ),
            rx.text(
                "4 Cuidar nuestro cuerpo, al pasar tantas horas sentado nuestro cuerpo se deteriora.\
                Mantener un orden en casa y zona de trabajo limpia.\
                Administra bien tu tiempo para cambiarlo por sabiduría, salud o dinero lo que más necesites ahora.\
                Come bien, duerme 8, haz 1 h de ejercicio, 5 días a la semana, 3 h o 5 h de ocio diarias y 2 h o 4 h tareas en general.\
                Cuidar nuestro estado emocional y mental también es superimportante, a veces sentirás frustración o simplemente tendrás\
                un mal día. No pasa nada todos tenemos días mejores días peores tómate un colacao ponte tu canción favorita y motívate.\
                Aquí te dejo una lista de Spotify para programar que ami me anima en estos momentos, espero que te guste. En tener tiempo\
                añadiré todas las canciones.",
                margin_top="10px"
            ),
            rx.link(
                "Lista Spotify By: jona_THAI para programar Metal_python  ",
                ant_components.spotify_icon(),
                is_external=True,
                href=costants.METAL_PYTHON
            ),
            rx.text(
                "5 Próximamente...",
                margin_top="10px"
            )
        ),
        padding_top="15px",
        style=styles.max_width_style
    )
