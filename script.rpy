# TENT ARCANA

init python:
    def _set_speaker_zorder(speaker=None):
        if not getattr(renpy.store, "speaker_zorder_enabled", False):
            return

        layer = getattr(renpy.store, "speaker_zorder_layer", "master")
        group = getattr(renpy.store, "speaker_zorder_group", {})
        active_zorder = getattr(renpy.store, "speaker_zorder_active", 10)

        for tag, base_zorder in group.items():
            zorder = active_zorder if tag == speaker else base_zorder
            renpy.change_zorder(layer, tag, zorder)

        renpy.store.current_group_speaker = speaker

    def speaker_zorder_callback(event, speaker=None, **kwargs):
        if event != "begin":
            return

        _set_speaker_zorder(speaker)

# Personajes:
define narrator = Character(None, callback=speaker_zorder_callback, cb_speaker=None)
define player = Character("[player_name]", callback=speaker_zorder_callback, cb_speaker=None)

define unknown = Character("????", color = "#d6b41d")
define unknown_2 = Character("????", color = "#62c7e8")
define unknown_3 = Character("????", color = "#c58af9")

define thesun = Character("Solei", color = "#C94B45")
define thequeen = Character("Regina", color = "#D5AA3F", callback=speaker_zorder_callback, cb_speaker="regina")
define thewheel = Character("Routa", color = "#D65A32", callback=speaker_zorder_callback, cb_speaker="routa")
define wlover = Character("Alicia", color = "#72B84F", callback=speaker_zorder_callback, cb_speaker="alicia")
define mlover = Character("Homero", color = "#6197B5")
define thechariot = Character("Chariot", color = "#78B8D0")

define gold2 = Character("Chuu", color = "#eccc12")
define gold5_1 = Character("Fill", color = "#eccc12", callback=speaker_zorder_callback, cb_speaker="fill")
define gold5_2 = Character("Vell", color = "#eccc12", callback=speaker_zorder_callback, cb_speaker="vell")
define gold6 = Character("Sixs", color = "#eccc12")
define gold7 = Character("Week", color = "#eccc12")
define goldhelper = Character("Ayudante 1", color = "#eccc12")
image sixs = "characters/Sixs.png"

default speaker_zorder_enabled = False
default speaker_zorder_layer = "master"
default speaker_zorder_group = {}
default speaker_zorder_active = 10

default current_group_speaker = None
default homero_work_question_asked = False
default homero_services_question_asked = False
default homero_circus_question_asked = False

default circus_crafts_visited = False
default circus_food_visited = False
default circus_animals_visited = False

default homero_presentation_seen = False
default solei_show_seen = False
default routa_show_seen = False
default alicia_show_seen = False
default chariot_show_seen = False
default homero_show_seen = False

image gold_ticket = "objects/gold ticket.png"
image apple = "objects/apple.png"
image bread = "objects/bread.png"
image goldens_bag = "objects/goldens_bag.png"
image water = "objects/water.png"
image golden = "objects/golden.png"
image mc_memories = Transform(
    renpy.display.anim.TransitionAnimation(
        "memories/mc_hands/frame_01.webp", 1.5, Dissolve(0.35),
        "memories/mc_hands/frame_02.webp", 1.5, Dissolve(0.35),
        "memories/mc_hands/frame_01.webp", 1.5, Dissolve(0.35),
        "memories/mc_hands/frame_03.webp", 1.5, Dissolve(0.35),
        "memories/mc_hands/frame_01.webp", 1.5, Dissolve(0.35),
        "memories/mc_hands/frame_04.webp", 1.5, Dissolve(0.35),
        "memories/mc_hands/frame_01.webp", 1.5, Dissolve(0.35),
        "memories/mc_hands/frame_05.webp", 1.5, Dissolve(0.35),
        "memories/mc_hands/frame_01.webp", 1.5, Dissolve(0.35),
        "memories/mc_hands/frame_06.webp", 1.5, Dissolve(0.35),
    ),
    xysize=(1920, 1080),
)

image mc_hands_six_goldens = Composite(
    (1920, 1080),
    (0, 0), Transform("memories/mc_hands/frame_01.webp", xysize=(1920, 1080)),
    (390, 350), Transform("objects/golden.png", xysize=(150, 150), rotate=-12, matrixcolor=BrightnessMatrix(-0.17)),
    (515, 405), Transform("objects/golden.png", xysize=(150, 150), rotate=8, matrixcolor=BrightnessMatrix(-0.17)),
    (420, 500), Transform("objects/golden.png", xysize=(150, 150), rotate=-4, matrixcolor=BrightnessMatrix(-0.17)),
    (1245, 350), Transform("objects/golden.png", xysize=(150, 150), rotate=10, matrixcolor=BrightnessMatrix(-0.17)),
    (1370, 405), Transform("objects/golden.png", xysize=(150, 150), rotate=-8, matrixcolor=BrightnessMatrix(-0.17)),
    (1280, 500), Transform("objects/golden.png", xysize=(150, 150), rotate=5, matrixcolor=BrightnessMatrix(-0.17)),
)

image bg limfool_three = Transform(
    "backgrounds/bg Limfool_three.png",
    xysize=(1920, 1080),
)

image bg sunflower_rush = Transform(
    "backgrounds/bg Sunflower_Rush.png",
    xysize=(1920, 1080),
)

image bg_golden_circus_tent = Transform(
    "backgrounds/bg_golden_circus_tent.jpg",
    xysize=(1920, 1080),
    fit="cover",
    xalign=0.5,
    yalign=0.5,
)
image closed_eyes = Solid("#000")
image anxiety_haze = Solid("#101522")

transform horse_gallop_1:
    zoom 1.02
    yoffset 0
    ease 0.18 yoffset -8
    ease 0.20 yoffset 6
    ease 0.18 yoffset 0
    repeat

transform stop_horse_gallop_1:
    ease 0.3 yoffset 0 zoom 1.0

transform horse_trot:
    zoom 1.02
    yoffset 0
    ease 0.18 yoffset -4
    ease 0.20 yoffset 3
    ease 0.18 yoffset 0
    repeat

transform stop_horse_trot:
    ease 0.3 yoffset 0 zoom 1.0

transform vell_position:
    xalign 0.5
    yalign 1.0
    zoom 0.8

transform memory_flicker:
    alpha 1.0
    pause 0.35
    ease 0.25 alpha 0.0
    pause 0.60
    ease 0.25 alpha 1.0
    pause 0.35
    repeat

transform bread_position:
    xcenter 600
    ycenter 500
    zoom 0.6

transform anxiety_haze_in:
    alpha 0.0
    ease 1.20 alpha 0.38

transform anxiety_vibration:
    zoom 1.01
    xoffset 0
    yoffset 0
    ease 0.25 xoffset -2 yoffset 1
    ease 0.30 xoffset 2 yoffset -1
    ease 0.25 xoffset 0 yoffset 0
    repeat

transform stop_anxiety_vibration:
    ease 0.40 xoffset 0 yoffset 0 zoom 1.0

transform recent_memory:
    blur 4.0
    matrixcolor SaturationMatrix(0.8)

transform circus_approach:
    subpixel True
    xalign 0.52
    yalign 0.31
    zoom 1.0
    ease 12.0 zoom 1.5

transform solei_group_side:
    xalign 0.0
    yalign 1.0
    zoom 0.74

transform arcana_group_left:
    xalign 0.50
    yalign 1.0
    zoom 0.70

transform arcana_group_center:
    xalign 0.75
    yalign 1.0
    zoom 0.70

transform arcana_group_right:
    xalign 1.0
    yalign 1.0
    zoom 0.70

transform solei_exit_left:
    subpixel True
    xalign 0.0
    yalign 1.0
    zoom 0.74
    ease 1.1 xalign -0.65

transform arcana_focus_left:
    subpixel True
    xalign 0.50
    yalign 1.0
    zoom 0.70
    ease 0.8 xalign 0.18 zoom 0.82

transform arcana_focus_center:
    subpixel True
    xalign 0.75
    yalign 1.0
    zoom 0.70
    ease 0.8 xalign 0.50 zoom 0.82

transform arcana_focus_right:
    subpixel True
    xalign 1.0
    yalign 1.0
    zoom 0.70
    ease 0.8 xalign 0.82 zoom 0.82

transform arcana_focused_routa:
    xalign 0.18
    yalign 1.0
    zoom 0.82

transform arcana_focused_regina:
    xalign 0.50
    yalign 1.0
    zoom 0.82

transform arcana_focused_alicia:
    xalign 0.82
    yalign 1.0
    zoom 0.82

transform chariot_first_encounter:
    xalign 0.5
    yalign 1.0
    zoom 0.85

transform solei_scare:
    xalign 0.5
    yalign 0.2
    zoom 1.99

transform homero_show_button:
    xalign 0.5
    yalign 0.9
    zoom 0.6

transform solei_show_button:
    xalign 0.13
    yalign 0.168
    zoom 0.7

transform routa_show_button:
    xalign 0.2
    yalign 0.85
    zoom 0.6

transform chariot_show_button:
    xalign 0.7
    yalign 0.87
    zoom 0.6

transform alicia_show_button:
    xalign 0.93
    zoom 0.6

# El juego comienza aquí.

label start:

    # Prólogo.

    #Acá entra un narrador desconocido

    play music "audio/ms_intro.mp3" fadein 2.0

    scene bg intro
    with fade

    "El vasto firmamento."

    "El Sol y la Luna giran en una danza alrededor de la Tierra, mientras las estrellas observan en silencio aquel eterno ballet cósmico."

    "La luz de los astros desciende sobre la Tierra y se refleja en cada rincón de su infinita belleza."

    "Terra respira."

    "Los árboles se mecen con la brisa, sus ríos guardan memorias antiguas, y bajo su cielo, todo pertenece a un orden sagrado."

    "Pero toda luz provoca un reflejo."

    "Al otro lado de ese espejo, existe otro mundo tan verdadero como el mundano, tan vivo como aquello que puedes tocar."

    "En tiempos remotos, sus habitantes no eran más que polvo estelar suspendido en el vacío, fragmentos perdidos en una oscuridad donde nada tenía nombre, forma ni destino."

    "Fuimos nosotros quienes les dimos poder, y son ustedes quienes deciden qué hacer con él: aceptarlo, ignorarlo, temerlo... o hacerlo suyo."

    "El poder de vivir, sentir y amar."

    "Elige tu propio camino."

    "Sé tu propio arcano."

    stop music fadeout 2.0

    scene bg black
    with fade

    menu:
        "¿Cuáles son tus pronombres?"

        "Él":
            $ player_pronouns = "él"

        "Ella":
            $ player_pronouns = "ella"

        "Elle":
            $ player_pronouns = "elle"

    call choose_player_name

    # Fin del prólogo.

label act_i_intro:
    scene bg title act i day i
    "{cps=14}ACTO I: EL LOCO"

    "{cps=14}Día 1"

    scene bg limfool_three
    with fade

    "Tus ojos se abren lentamente bajo el árbol donde te venció el sueño. Entre las hojas, logras divisar un amplio cielo azul que se extiende sobre ti."
    play music "audio/ms_ambience_nature.mp3" fadein 2.0 volume 0.6
    player "((¿Dónde estoy?))"

    "Te frotas los ojos y parpadeas un par de veces hasta que la vista se aclara. Entonces distingues mejor el paisaje y sientes el viento correr entre tu cabello."

    player "((Qué extraño... Debería volver a mi... ¿casa? ¡Agh! Tengo la mente en blanco. No sé qué hacer.))"

    "Te levantas y das unos pasos fuera de la sombra del gran árbol mientras buscas alguna señal que te indique dónde estás."

    "Sigues caminando durante un buen rato, aunque sientes que avanzas sin rumbo. El sudor que baja lentamente por tus mejillas te hace notar el calor que irradia el Sol."

    player "((Qué calor... ¿Hace cuánto estoy caminando? Si sigo aquí, me voy a cocinar...))"

    "A lo lejos, sobre una colina, distingues un hermoso girasol inclinado hacia la luz. La cima no parece difícil de alcanzar, y la curiosidad te impulsa a acercarte."

    "De cerca, sus pétalos parecen capturar los rayos del Sol. El resplandor que descansa sobre ellos le da un aspecto casi etéreo."

    "Al fijarte detrás de la flor, descubres un campo de girasoles que se extiende hacia el horizonte."

    scene bg sunflowers
    with fade

    player "((Se ve muy lindo desde aquí.))"

    "Una ráfaga fresca te eriza la piel."

    "Al bajar la colina, logras vislumbrar un sendero y decides seguirlo, adentrándote en el campo de flores."

    call sunflower_maze_sequence

    scene bg sunflowers
    with fade
    play sound "sfx_horse-galloping.mp3"

    "De pronto, un sonido rompe la monotonía. A diferencia de tus pasos, es más intenso, más violento, y se acerca con una prisa feroz."

    "Tu cuerpo reacciona más rápido que tu mente agotada. Sientes el impulso de darte la vuelta, como si tu instinto más primitivo hubiese decidido tomar las riendas."

    "Cuando por fin logras identificarlo, comprendes que aquello no son simples pasos: es el galope veloz de un caballo."

    #Solei
    unknown "¡Rápido! ¡Rápido! ¡Rápido!"

    "El galope se aproxima antes de que puedas reaccionar. El animal{nw}"

    play audio "sfx_horse_neigh_recorded.mp3" volume 0.45

    extend " relincha y clava las pezuñas en la tierra, luchando por detenerse antes de arrollarte."

    #Solei
    unknown "¡CUIDADO!"

    "Cierras los ojos con fuerza y esperas el impacto."

    stop sound

    "El caballo logra detenerse...{w=0.8}{cps=*2} pero no lo suficientemente pronto.{/cps}"

    window hide
    play sound "sfx_dry_impact.wav"
    with hpunch
    with Fade(0.05, 0.55, 0.15, color="#000")
    window auto

    "Su costado te golpea con fuerza suficiente para derribarte. Alcanzas a extender las manos antes de que tu cuerpo choque contra el suelo."

    #Solei
    unknown "Shh, shh, preciosa, calma..."

    "La misma voz de antes intenta tranquilizar a la criatura. A medida que la conmoción inicial se disipa, te atreves por fin a levantar la mirada."

    "Frente a ti, una yegua blanca brilla bajo la luz dorada del cielo, ahora más serena gracias a la voz de su jinete."

    show solei casual ashamed

    unknown "¡PERDÓN, PERDÓN, PERDÓN!"

    "Un joven de cabellos dorados como los girasoles que los rodean clava su preocupada mirada en ti mientras baja del caballo, un poco más rápido de lo debido."

    "Por un momento, la punta de su bota se engancha en el estribo antes de que consiga tocar tierra."

    unknown "¡Oh, por mis cartas! ¡¿Estás bien?! No te rompiste nada, ¡¿verdad?!"

    "Su enorme melena dorada cubre tu vista del cielo en cuanto se acerca a ti. Solo te queda fijarte en su mirada azulada; sus ojos transmiten preocupación y calidez al observarte."

    "Por un segundo, sientes que podrías perderte en su mirada, pero una punzada de dolor recorre tu cuerpo trayéndote de vuelta a la realidad."

    show solei casual neutral

    unknown "Uf... Menos mal, sigues con vida..."

    "Él sonríe mirándote con una inocencia demasiado ofensiva para alguien que estuvo a punto de pasarte su yegua por encima."

    "Hay algo torpe en su expresión. Sus ojos siguen recorriéndote buscando señales de que sigues [player_form('entero', 'entera', 'entere')]."

    "Luego, baja un poco la mirada a tus manos apoyadas en la tierra, hacia el polvo en tu ropa, y nota ese gesto de dolor que intentas ocultar. Su sonrisa vacila apenas, volviéndose más suave."

    "Extiende una mano hacia ti, cuidadoso, como si temiera asustarte con cualquier movimiento brusco."

    unknown "Por favor, déjame ayudarte."

    "Su mano permanece allí, abierta, esperando a que decidas tomarla."

    #1-OPCIONES / primer encuentro con Solei
    menu:
        "Aceptar.":

            show solei casual happy

            "Te levantas lentamente del suelo con ayuda de su mano, que te sostiene con una firmeza inesperada."

            "Su agarre es mucho más decidido de lo que su expresión torpe te haría suponer."

            "Intentas fijar la mirada en su rostro, distinguirlo con mayor claridad, pero los pocos rayos de sol que se filtran entre sus mechones de cabello te obligan a entrecerrar los ojos."

            "Por un instante, su figura queda envuelta en luz, borrosa, casi irreal."

            "Una vez de pie, te frotas los ojos con el dorso de tu mano para aclarar la vista y verlo mejor."

            player "Ugh... Me duele todo."

            unknown "Gracias a las estrellas, me sentiría muy mal si te hubieras lastimado."

            "Te limpias la tierra de la ropa con un par de palmadas rápidas, intentando recuperar algo de dignidad después de la caída."

            "Cerca de ti, el hocico de la yegua resopla con suavidad, y el aire cálido de su respiración te provoca un respingo involuntario."

            "El desconocido sigue observándote con atención, demasiado pendiente del estado en que te encuentras tras el incidente."

            unknown "Está bien, tranquila."

            "El muchacho se aproxima con cuidado y posa una mano sobre el cuello de su yegua, guiando su atención hacia ti, como si quisiera hacerle entender que no te ha hecho daño."

            "La yegua resopla cerca de tu hombro, ahora mucho más dócil, casi como si estuviera avergonzada."

        "Denegar.":

            player "¡¿\"SIGUES CON VIDA\"?! ¡Casi me atropellas, animal!"

            show solei casual awkward

            "Su sonrisa se congela por un instante, como si no hubiese terminado de asimilar lo que acabas de decir."

            show solei casual pout blushing

            "Puedes notar cómo las comisuras de sus labios van bajando poco a poco hasta formar un puchero. Por apenas un instante, te sientes un poco culpable por hablarle de esa forma."

            unknown "¡No fue mi intención! Por favor, déjame ayudarte."

            "Pese a tu mal humor, el desconocido parece dispuesto a ayudarte. Su mirada conserva la misma calidez de antes, aunque ahora es más cautelosa."

            "Como si tratara de decidir de qué manera acercarse a ti sin incomodarte más."

            "Entonces vuelve a acercar su mano, más despacio ahora, con una paciencia que resulta casi irritante."

            with hpunch
            show solei casual shocked
            player "¡No me toques!"

            "Apartas su mano con brusquedad y consigues ponerte de pie por tu cuenta, sacudiendo el polvo de tu ropa con movimientos secos."

            "El muchacho se queda inmóvil por un instante."

            show solei casual ashamed

            "Luego mueve los brazos torpemente, como si no supiera qué hacer con ellos, y golpea el suelo con la punta de la bota en pequeños toques nerviosos."

            "Luce apenado, casi herido, con el rostro sonrojado de vergüenza. Finalmente baja la mirada y se refugia detrás de su yegua, como si el animal pudiera ocultarlo por completo de ti."

            "Viéndolo así, suspiras. Tu mal humor no desaparece, pero la idea de seguir [player_form('solo', 'sola', 'sole')] en aquel campo interminable de girasoles resulta todavía peor."

            "Así que te acercas más a él, [player_form('dispuesto', 'dispuesta', 'dispueste')] a aceptar no tanto su ayuda, sino la oportunidad de salir de ese lugar."

    show solei casual neutral

    play music "audio/ms_solei.mp3" fadein 2.0 volume 0.55

    "Tu mirada se cruza con la suya por un instante. El contacto se prolonga porque apartar la vista parece imposible. El desconocido parece dudar por unos segundos si debe hablarte o no."

    "El silencio que se forma es incómodo. Sientes que podrían quedarse allí durante horas, frente a frente, esperando que alguien tenga el valor de romperlo."

    "Pero no tienes tiempo. La noche se acerca, y definitivamente no piensas quedarte ahí a dormir en medio del campo de girasoles. Así que respiras hondo y decides..."

    #2-OPCIONES / conversación campo de girasoles
    menu:
        "Calmar la situación":
            player "Tranquilo, no le des más vueltas. Al final, lo importante es que estamos bien."
            "El muchacho suspira de alivio y sonríe."
            show solei casual happy
            unknown "¡Qué alivio! De verdad. E-Estaba preocupado."
            "La yegua relincha, interrumpiendo la conversación apenas iniciada, llamando de nuevo la atención de su jinete."
            show solei casual neutral
            unknown "Oh, sí. Girasol te pide disculpas... es que estábamos apurados."

        "Romper el silencio.":
            player "Oye... Agh, no tengo tiempo para esto. Sé que no lo hiciste con mala intención, ¿verdad?"
            show solei casual shocked
            "Él se tensa por un segundo antes de negar con la cabeza muy rápidamente."
            unknown "¡Claro que no! De verdad, fui un despistado."
            player "¿Acaso no miras por donde vas? Tienes que ser más consciente, sobre todo teniendo un caballo."
            show solei casual ashamed
            unknown "¡Y tienes razón! ¡Perdón! Es que... estábamos apurados. Girasol y yo tendremos más cuidado, lo prometo. Te debo una disculpa."
            "Notas cómo la cara del desconocido se va poniendo más roja, hasta que el color alcanza la punta de sus orejas."


    player "¿Girasol? ¿Apurados?"

    show solei casual happy
    unknown "Es mi yegua, je, je. Podrías decir que es tan revoltosa como yo. Es mi confidente en mis locuras.{nw}"

    play audio "solei_giggle_1.mp3"

    extend " ¡Ja, ja!"

    unknown "Perdón... ¡¿Dónde están mis modales?! Permíteme presentarme."

    voice "es_solei_phrase_1.mp3"

    thesun "Soy Solei. ¡Encantado de conocerte! ¿Cómo te llamas, semillita?"

    player "Me llamo [player_name]."

    thesun "¡Un gusto, [player_name]! ¿Qué te trae por aquí?"

    #3-OPCIONES / post presentación
    menu:
        "Me perdí.":
            player "No estoy muy [player_form('seguro', 'segura', 'segure')]. Creo que me perdí."
            show solei casual happy
            thesun "Se nota que no eres de por aquí. [player_form('Tranquilo', 'Tranquila', 'Tranquilízate')], en Limfool es normal perderse si no te conoces bien."

        "Mi instinto.":
            player "Honestamente, no lo sé. Solamente seguí mi intuición. Pensé que eventualmente encontraría la salida."
            show solei casual shocked
            thesun "¡Eres [player_form('un forastero', 'una forastera', 'une forastere')]!"
            show solei casual happy
            thesun "En Limfool es normal perderse \"a menos que sepas quién eres\". Tienes suerte de que yo aparezca, ¿no?"

    "Solei mira el cielo, fijando su mirada en el sol que empieza a caer en el horizonte."

    show solei casual shocked

    thesun "¡Se me hace tarde!"

    show solei casual neutral

    thesun "Ven, súbete a Girasol. No te pienso dejar aquí. ¡Vamos!"

    player "¡Espera! Nunca me he subido a un caballo."

    show solei casual happy

    thesun "Siempre hay una primera vez. Ven, déjame ayudarte, no quiero que te pierdas."

    thesun "El campo de girasoles es bastante amplio. Además, Zoloto está cerca. Aprovechemos."

    player "((¿Zoloto?))"

    player "¿A dónde me llevas?"

    thesun "Ya verás, es un pueblito muy lindo. Te gustará."

    scene bg sunflower_rush
    with fade

    play sound "sfx_horse-galloping-2.mp3" loop volume 0.7 fadein 0.2
    camera at horse_gallop_1

    "En cuanto te subes a la montura, Girasol inicia el galope con una prisa feroz. Cierras tus ojos mientras el aire golpea tu rostro y agita el cabello de ambos."

    show closed_eyes zorder 100
    with Dissolve(0.15)

    player "((No me quiero caer, no me quiero caer... ¡No me quiero caer!))"

    "Presa del miedo, mientras la yegua acelera cada vez más, intentas aferrarte a lo primero que encuentras, que resulta ser..."

    #4-OPCIONES / Cabalgata fuera del campo de girasoles
    menu:
        "Su cintura":

            "Antes de que puedas pensarlo mejor, tus brazos rodean con fuerza la cintura de Solei."

            play audio "solei_whow.mp3"

            "Apoyas tu mejilla contra su espalda, y, por alguna razón que no comprendes, te sientes a salvo."

            hide closed_eyes
            with Dissolve(0.3)

            "Un reflejo de luz cruza tu rostro, cálido como una caricia. Te atreves a abrir los ojos."

            "El campo de girasoles que antes parecía atraparte ya no es un laberinto interminable, sino una mancha dorada que se extiende a tu alrededor y se desdibuja con la velocidad del galope."

            "Logras percibir, a pesar del grosor de su ropa, cómo su cuerpo se tensa al recostarte sobre él."

            thesun "Y-ya casi llegamos. Aguanta."

            player "((Es más cálido de lo que esperaba, hasta suave. Qué curioso...))"

        "Sus hombros":

            "Temiendo caerte y sin poder pensar en algo mejor para sujetarte, pones tus manos sobre los hombros de Solei."

            play audio "solei_hey.mp3"

            "Te sujetas a ellos como si fueran lo único entre tú y una muerte ridícula. Tus dedos se tensan, tus uñas se clavan en su ropa... y quizá un poco más allá."

            thesun "¡AHHH! ¡No te asustes, tengo todo bajo control!"
            hide closed_eyes
            with Dissolve(0.3)

            "Un reflejo de luz cruza tu rostro, cálido como una caricia. Te atreves a abrir los ojos."

            "El campo de girasoles que antes parecía atraparte ya no es un laberinto interminable, sino una mancha dorada que se extiende a tu alrededor y se desdibuja con la velocidad del galope."

            "Solei se encoge apenas al sentir tus uñas. Intenta mantener la vista fija en el camino, sujetar las riendas y no reaccionar para que no te asustes más."

            "Pero está claro que le está costando."

            player "¡LO SIENTO! ¡ES QUE VAS MUY RÁPIDO!"

            "Aunque dices eso, no te ves capaz de soltarlo."

    "Cuando compruebas que, pese a la velocidad, sigues sobre la montura, el miedo comienza a ceder."

    "Dejas que tu mirada se pierda en el campo de girasoles y en la belleza sencilla de la naturaleza."

    "La brisa roza tu rostro y, poco a poco, te arrastra hacia el recuerdo de quien alguna vez fuiste: un pasado tan lejano que casi parece no pertenecerte."

    stop sound fadeout 0.3
    camera at stop_horse_gallop_1
    scene bg fair
    with fade
    play music "audio/ms_moment_relaxing.mp3" fadeout 2.0 fadein 2.0 volume 0.6
    camera at horse_trot
    play sound "sfx_horse-galloping-2.mp3" loop volume 0.25 fadein 0.2

    "Al llegar al pueblo, Girasol disminuye la velocidad hasta avanzar con un trote suave. Te quedas observando todo con una mezcla de curiosidad y desconcierto."

    "Ante tus ojos se extiende Zoloto, un pueblo lleno de vida."

    "Una feria de comerciantes ocupa sus calles, llenándolas de voces, colores y movimiento."

    thesun "¡Te doy la bienvenida a Zoloto, [player_name]!"

    "Los puestos se extienden a ambos lados del camino, cubiertos de telas coloridas. Sobre las mesas descansan prendas y accesorios, junto a frutas brillantes y verduras tan frescas que parecen recién cosechadas."

    "Aun así, no puedes evitar sentirte fuera de lugar. No conoces a nadie ni sabes dónde estás."

    stop sound fadeout 0.3
    camera at stop_horse_trot

    "Al bajar de la yegua con la ayuda de Solei, varios pueblerinos se acercan hasta rodearlo. Está claro que lo reconocen."

    "Algunos solo buscan saludarlo; otros, más reservados, sonríen al verte junto a él y te dan la bienvenida con una familiaridad que no sabes cómo corresponder."

    "Poco a poco, el bullicio de Zoloto termina por envolverte entre risas, saludos y ofertas lanzadas desde los puestos. Por un momento, sientes como si el pueblo ya te hubiera hecho un espacio entre los suyos."

    "Aunque esa sensación se desvanece rápidamente."

    "Mientras Solei empieza a conversar con algunos niños y comerciantes del lugar, tu atención se desvía hacia una mujer cerca de una fuente."

    "La mujer intenta transportar dos cubos de agua suspendidos de una vara de madera. El peso la obliga a inclinarse tanto que parece a punto de caer."

    #5-OPCIONES / escena de aparición de los arcanos menores I
    menu:
        "Ayudar":
            "Sin dudarlo, decides acercarte para ayudarla antes de que pierda el equilibrio."

            player "Déjeme ayudarle. Eso parece muy pesado."

            show vell at vell_position
            with dissolve

            "La mujer levanta la mirada hacia ti, sorprendida. Sus manos aún sujetan la vara de madera, como si temiera soltarla."

            unknown "Oh, disculpe, no quiero causarle molestias."

            "Sin embargo, el temblor de sus brazos bajo el peso de los cubos contradice sus palabras."

            player "No se preocupe. Es un placer ayudar."

            "Tomas la carga con cuidado. El peso tira de tus hombros de inmediato, pero la presión de la vara te resulta extrañamente familiar."

            player "((Esta sensación... me resulta familiar.))"

            stop music fadeout 2.0

            show mc_memories zorder 100
            with Dissolve(0.35)

            "Por un instante, pequeños fragmentos cruzan tu memoria."

            "Tus manos levantando una caja, una bolsa pesada colgando de tu hombro, el cansancio conocido de cargar algo durante demasiado tiempo."

            "Son recuerdos incompletos, apenas destellos, pero bastan para dejar una inquietud suave en tu pecho."

            hide mc_memories
            with Dissolve(0.35)

            play music "audio/ms_moment_relaxing.mp3" fadein 2.0 volume 0.6
            player "((¿Acaso esto era parte de mi trabajo?))"

            "Cuando vuelves en ti, ya has llegado hasta una pequeña tienda cercana. Dejas los cubos junto a la entrada, y la mujer suspira de alivio."

            "Cuando te giras para volver con Solei, notas que tiene la mirada clavada en ti. En una mano sostiene una manzana, probablemente un regalo de algún comerciante."

            "Sin apartar la mirada, le da una mordida distraída y, acto seguido, sonríe levantando un poco la comisura de sus labios."

            "No parece sorprendido por tu fuerza. Más bien, parece concentrado en otra cosa, aunque aún no logras saber en qué."

            show vell at right:
                zoom 0.8
            with move

            show fill at left:
                zoom 0.8
            with dissolve

            unknown_2 "¿Y [player_form('este', 'esta', 'este')] [player_form('desconocido', 'desconocida', 'desconocide')]?"

            unknown "Es [player_form('un', 'una', 'una')] [player_form('jovencito', 'jovencita', 'personita')] amable que me dio una mano."

            unknown_2 "Vaya, tienes una gran fuerza."

            unknown_2 "Muchas gracias por ayudar a mi hermana."

            player "Es un placer. Me preocupó verla esforzándose. Además, no me costaba nada ayudarla."

            unknown_2 "Normalmente yo llevo el agua... pero mi cuerpo ya no coopera demasiado."

            "El hombre se lleva una mano al costado de la cintura antes de soltar una pequeña risa cansada."

            player "Con más razón tenía que hacerlo."

            gold5_2 "[player_form('Bienvenido', 'Bienvenida', 'Bienvenide')] a Zoloto. Me presento: soy Vell y este es mi hermano Fill."

            player "Un placer conocerlos. Soy [player_name]."

            gold5_1 "El gusto es nuestro. Y de nuevo, gracias."

            "Un suave carraspeo a tu espalda llama tu atención. Das un pequeño respingo antes de girarte hacia el sonido."

            hide fill
            hide vell
            show solei casual neutral

            "Entonces notas a Solei parado justo a tu lado. Debió acercarse mientras hablabas con los hermanos, pero no había hecho el menor sonido para anunciar su presencia; no hasta ahora."

            player "¡AH! ¿Cómo haces eso?"

            show solei casual happy

            thesun "¿Qué cosa?"

            "Mientras habla, inclina un poco la cabeza con una bella sonrisa y, por un instante, olvidas lo que ibas a decir."

            player "N-nada, olvídalo."

            "Para cambiar de tema y evadir la mirada intensa de Solei, te despides de Fill y Vell con un suave asentimiento de cabeza y te internas entre los puestos, para poner algo de distancia entre él y tú"

            hide solei

        "No es mi problema":
            show vell at vell_position
            with dissolve

            "La ves batallar con los cubos de agua durante unos segundos. El esfuerzo por equilibrarlos la obliga a inclinarse aún más, pero al final logra recuperar la postura."

            "Decides quedarte en tu lugar, aunque no dejas de observarla."

            play sound "<from 0 to 1>sfx_apple_bite.mp3"
            "Un mordisco crujiente suena a tu lado, obligándote a apartar la mirada de la mujer."

            show vell at left:
                zoom 0.8
            with move

            show solei casual neutral at right
            with dissolve

            "Solei aparece junto a ti con una manzana en la mano, probablemente un regalo de alguno de los muchos comerciantes que lo rodeaban hace unos momentos. Aún no termina de tragar cuando te mira con curiosidad."

            thesun "¿No quieres ayudarla?"

            player "No. No la conozco... ¿Por qué tendría que...?"

            "No alcanzas a terminar la pregunta. Solei traga de golpe y levanta una mano frente a ti. Luego, con una naturalidad casi irritante, posa el índice en la punta de tu nariz."

            show solei casual happy

            thesun "Porque es lindo ayudar."

            "Solei baja la mano con lentitud y dirige la mirada hacia la mujer."

            show solei casual neutral

            thesun "Cuando ayudas a alguien, haces que su día sea un poco menos pesado. Además... el mundo sería un lugar muy lúgubre si nadie se ayudara."

            "Por un segundo, su mirada parece ir más allá de la mujer, hacia algún punto lejano. Luego parpadea, vuelve en sí y te sonríe como si nada."

            show solei casual happy

            thesun "Al menos, eso es lo que mi madre suele decir."

            "Apoya una mano en la cintura, como si intentara convencerse a sí mismo de que lo ha explicado bien."

            thesun "Y no es como si ayudar fuera inútil. Es lindo dibujar una sonrisa en el rostro de alguien. Además, todos en Zoloto son agradecidos."

            "Sin decir nada más, Solei deposita la manzana mordida en tus manos y se apresura hacia la mujer."

            show solei casual happy at center
            with move

            "Tal como dijo, en cuanto toma la vara de sus hombros y carga el peso por ella, una sonrisa de alivio aparece en el rostro de la mujer."

            "Sus labios tiemblan al curvarse en un gesto de agradecimiento silencioso, y Solei le responde con esa calidez absurda que parece llevar encima como si fuera parte de su ropa."

            player "((Demasiado cálido. ¡Puaj!))"

            "Incapaz de seguir mirando aquella escena empalagosa, bajas la mirada hacia la manzana que te entregó. Tus dedos se cierran alrededor de ella casi sin que te des cuenta."

            player "((¿Cuál es el punto de ayudar a los demás a cambio de una simple sonrisa? Tarde o temprano querrán más. Siempre quieren más.))"

            hide vell
            with dissolve

            hide solei
            with dissolve

            "Entonces sientes un leve dolor en la parte baja de la espalda y, por un instante, el bullicio de Zoloto parece distorsionarse."

            stop music fadeout 2.0
            "Esas jornadas de trabajo agotadoras..."

            show closed_eyes zorder 100
            with Dissolve(0.35)

            player "Ugh... Mi espalda me está matando..."

            unknown_2 "¿Otra vez quejándote?"

            player "Solo... necesito un momento."

            unknown_2 "¡Oye! Deja de holgazanear y vuelve al trabajo."

            player "S-sí, ya voy..."

            window hide
            hide closed_eyes
            with Dissolve(0.12)
            pause 0.30
            show closed_eyes zorder 100
            with Dissolve(0.12)
            window auto

            unknown_3 "¿Aún no has terminado con eso?"

            unknown_3 "¡Era para ayer, [player_name]!"

            player "Estoy en eso, solo que—"

            play sound "sfx_paper_rip.mp3"
            with hpunch

            unknown_3 "No quiero excusas, ¡quiero resultados!"

            window hide
            hide closed_eyes
            with None
            window auto

            player "((Ellos no van a devolverte la ayuda.))"

            play music "audio/ms_moment_relaxing.mp3" fadein 2.0 volume 0.6
            "Vuelves a Zoloto con los puños apretados y la espalda tensa, como si el peso de aquellas voces siguiera colgando de ti."

            "En un acto de pura frustración, arrojas la manzana mordida a un borde del camino."

    "Al notarte [player_form('rodeado', 'rodeada', 'rodeade')] por los pueblerinos absortos en sus propias vidas, intentas ordenar los fragmentos de tu pasado que acaban de emerger."

    stop music fadeout 2.0
    play sound "sfx_heartbeat.mp3" loop volume 0.35 fadein 0.40
    camera at anxiety_vibration
    show anxiety_haze at anxiety_haze_in zorder 100

    "Pero, en cuanto intentas volver a pensar en ellos, una punzada de dolor recorre tu cabeza."

    "Las voces del pueblo, las risas, los pasos... todo empieza a mezclarse hasta volverse demasiado."

    "Buscas con la mirada alguna salida de ese lugar que empieza a sentirse asfixiante, cualquier rincón menos lleno, cualquier lugar donde puedas respirar."

    show solei casual neutral at right
    with dissolve

    "Pero antes de que logres moverte, Solei llama tu atención desde el otro lado del mercado, y, sin saber bien por qué, el solo hecho de verlo logra tranquilizarte un poco."

    camera at stop_anxiety_vibration
    stop sound fadeout 0.40
    hide anxiety_haze
    with Dissolve(0.60)

    "Levanta una mano con una pequeña bolsa de tela. A través del tejido alcanzas a distinguir varias formas redondas, rojizas y brillantes."

    "Manzanas."
    play music "audio/ms_moment_relaxing.mp3" fadein 2.0 volume 0.6
    show solei casual happy

    "Solei te mira con una sonrisa suave, como si hubiese notado tu incomodidad, sin mencionarla directamente."

    play sound "sfx_hungry.mp3"
    player "((Mmm... qué hambre tengo. Ahora que lo pienso, no he comido nada en todo el día...))"
    stop sound

    "Solei parece querer acercarse a ti, pero antes de que pueda hacerlo, un carpintero de aspecto preocupado lo intercepta."

    show solei casual neutral

    "Tras intercambiar unas palabras con él, Solei dirige una breve mirada en tu dirección antes de volver a centrar su atención en la conversación."

    "Por la expresión de ambos, no parece que vaya a liberarse pronto."

    hide solei

    player "((Ugh... Bien, [player_name]. Soluciónalo [player_form('tú mismo', 'tú misma', 'por tu cuenta')].))"

    #6-OPCIONES / Escena de aparición de los arcanos menores II
    menu:
        "Pedir ayuda":

            player "((Solei parece un buen chico, me pregunto si...))"

            "Con algo de incomodidad, decides acercarte a ellos."

            show solei casual neutral

            "Justo cuando llegas a su lado, el carpintero se despide, dejándolos solos."

            player "Solei, me da algo de vergüenza pedirte..."

            thesun "¿Qué pasa, mi pequeña semillita? Soy todo oídos."

            player "Verás..."
            play sound "sfx_hungry.mp3"

            "Antes de que puedas responder, tu estómago vuelve a sonar."
            stop sound

            show solei casual shocked
            "Esta vez, el ruido es lo bastante claro como para captar la atención de Solei, que abre los ojos con una mezcla de sorpresa y preocupación."

            player "Muero de hambre. ¿Crees que podrías ayudarme a conseguir una de esas manzanas? Yo... No tengo dinero."

            thesun "¡Ay! Claro que tienes hambre."

            "Solei se apresura a abrir la bolsa que lleva en la mano."

            thesun "Toma, toma, come. No dudes en pedirme ayuda, ¿sí? Ya habrá forma de compensarlo después."

            "Te entrega un par de manzanas sin pensarlo dos veces. Tomas una y le das un mordisco con más entusiasmo del que te habría gustado mostrar."

            show solei casual happy

            "Es dulce, fresca y jugosa; está tan rica que no puedes evitar suspirar de gusto."

            player "Esto es un mercado..."

            "Miras la fruta entre tus manos, acariciando suavemente la superficie tersa de la manzana con tu pulgar."

            player "Eso significa que alguien tuvo que pagar por esto. Y si voy a pagarte por el gesto, necesito dinero."

            player "Cosa que no tengo."

            "Solei sonríe, como si justo hubiera estado esperando esa oportunidad."

            "Su mirada, en realidad, se dirige más allá de ti, como si hubiese alguien detrás."

            thesun "Pues estás de suerte. Creo que alguien puede ayudarnos con eso."

            "Sigues la dirección de su mirada."

            "Un hombre, un poco más alto que Solei, parece haber escuchado parte de la conversación."

            "Se acerca con curiosidad, observándolos a ambos como si acabara de encontrar algo interesante."

            show solei casual happy at left
            with move

            show sixs at right
            with dissolve

            unknown "Bueno, bueno, ¿a quién trajiste esta vez, Solei?"

            thesun "¡Ah, Sixs! Qué alegría verte aquí."

            thesun "Se llama [player_name], [player_form('es nuevo', 'es nueva', 'no es de')] por aquí, así que le estoy ayudando."

            thesun "[player_name], él es Sixs, banquero de Zoloto. Él nos puede ayudar."

            gold6 "Tú nunca cambias, muchacho. Siempre eres un sol con todos."

            gold6 "Un placer conocerte, [player_form('querido', 'querida', 'queride')]."

            gold6 "Te doy la bienvenida a Zoloto."

            gold6 "\"El pueblo en donde encontrarás frutas tan deliciosas que ni todo el oro del mundo podría pagarlo.\""

            player "No es mentira. Hace tiempo que no disfruto tanto una buena fruta."

            gold6 "Me alegra que lo veas así."

            gold6 "Zoloto siempre está abierto para quienes sepan comportarse."

            gold6 "Estoy seguro de que te veremos dando vueltas por aquí, igual que Solei."

            gold6 "Este siempre se escapa del circo."

            show solei casual neutral at left

            "Sixs posa su mano sobre la cabeza de Solei y lo acaricia como si se tratara de un cachorro."

            "Luego se detiene, como si hubiera recordado algo."

            gold6 "Hmmmm, querido Sol. ¿No crees que tu madre podría guiar a esta nueva personita?"

            gold6 "No tengo problema con que se quede aquí, pero tengo la sensación de que tu madre será de más ayuda."

            thesun "Ahora que lo mencionas, no es una mala idea. Tenemos espacio tanto aquí como en el circo."

            player "¿El circo? ¿Existe un circo aquí?"

            show solei casual happy at left
            thesun "¡Sí! El Circo Golden. Es mi hogar y no está lejos de aquí."

            thesun "Si quieres puedo llevarte."

            "Sixs ríe al notar la expresión de desconcierto en tu rostro mientras continúas comiendo."

            gold6 "Adorable. Se nota que estás como pez fuera del agua, [player_form('querido', 'querida', 'queride')], jajaja."

            gold6 "No te preocupes, poco a poco te irás acostumbrando a este lugar. Aunque todavía tienes mucho que explorar y aprender."

            "Tu mirada baja a la manzana mordida que aún sujetas. El breve descanso ha sido agradable."

            "Pero la sensación de recibir las cosas sin hacer nada empieza a incomodarte."

            player "Pues..."

            player "Necesito trabajar. No quiero quedarme sin hacer nada, honestamente."

            gold6 "Esa es la actitud, suenas [player_form('confiado', 'confiada', 'confiade')]. Pues bien, pagarás tu deuda por las manzanas."

            "Sixs ríe mientras saca de su bolsillo una bolsa con monedas de oro para dártela con una sonrisa."

            show goldens_bag at center

            gold6 "También noté que no llevas Goldens."

            hide goldens_bag
            player "¿Goldens?"

            gold6 "Es nuestra moneda."

            "Tomas aquella bolsa entre tus manos con sorpresa. Sixs te hace un pequeño gesto para que la abras."

            show mc_hands_six_goldens zorder 100
            with Dissolve(0.35)

            "Al abrirla, seis monedas de oro caen sobre tus manos."

            gold6 "Es lo que usamos para hacer un intercambio justo."

            hide mc_hands_six_goldens
            with Dissolve(0.35)

            "Sin pensártelo demasiado, le entregas dos monedas a Solei por la bolsa de manzanas, esperando que sean suficientes."

            gold6 "Ya no le debes manzanas a Solei. Puedes escaparte de sus locuras."

            show solei casual shocked at left
            thesun "¡Ah! ¡No es justo!"

            show solei casual happy at left
            "Sixs y Solei empiezan a reír. Su alegría te resulta difícil de ignorar; es... contagiosa."

            thesun "¡Bien! Está decidido."

            hide solei
            with dissolve

            "Mientras Solei va por Girasol para llevarte al circo, miras las monedas una vez más y las cuentas con cuidado."

            "Te quedan cuatro, después de las dos monedas que acabas de entregarle a Solei."

            show solei casual neutral at left
            play sound "sfx_girasol_snort.mp3" volume 0.2
            "Escuchas un resoplido suave a tu lado y guardas nuevamente las monedas en la bolsa de cuero."

            "Al alzar la vista, Solei ya ha llegado a tu lugar, a lomos de Girasol."

            "Solei extiende su mano hacia ti."

            thesun "¿Estás [player_form('listo', 'lista', 'liste')] para ver a mi madre?"

            "No puedes evitar sonreír ante la escena familiar."

            player "Supongo que podría conocer a tu madre..."

            "Tomas su mano para subirte y él sonríe de vuelta."

            thesun "¡Así se habla!"

            "En cuanto te acomodas en el lomo de Girasol, Sixs se acerca, con calma."

            gold6 "Descuida, sé que trabajarás muy duro, ¿verdad?"

            player "Pues... esa es la idea."

            player "No tengo nada, estoy [player_form('vacío', 'vacía', 'vacíe')]. Sin dinero o ropa decente."

            "Te ríes con algo de vergüenza mientras vuelves a acomodarte."

            "Tras un instante de duda, terminas sujetándote a la cintura de Solei para no perder el equilibrio."

            thesun "¿Quieres progresar? Se escucha lindo viniendo de ti."

            "Solei toma las riendas y Girasol relincha con emoción."

            gold6 "Saludos a Regina de mi parte."

            "El banquero los despide con una sonrisa mientras los aldeanos les dejan el camino libre para salir del pueblo."

            thesun "Lo haré."
            thesun "¡Adiós, Sixs!"

            "Solei se despide agitando la mano."

            hide solei
            with dissolve

            hide sixs
            with dissolve

            play music "audio/ms_solei.mp3" fadeout 2.0 fadein 2.0 volume 0.6
            scene bg sunflower_rush
            camera at horse_gallop_1
            play sound "sfx_horse-galloping-2.mp3" loop volume 0.7 fadein 0.2

            "En cuanto la yegua pisa fuera del pueblo, su trote se acelera hasta convertirse en un galope veloz."

            thesun "Sujétate fuerte, [player_name]. Estoy un poco apurado..."

            "Su risa llega hasta ti, incluso a pesar del viento."

            player "¡Por lo menos ya me avisas!"

        "Aguantarte el hambre":

            "Sacudes la cabeza para despejarte y poder ignorar el hambre."

            "Pero, a los pocos segundos, el vacío en tu estómago se intensifica hasta hacer que te dobles mientras sujetas tu abdomen."

            "Un lugareño nota que estás [player_form('pálido', 'pálida', 'pálide')] y se acerca."
            show chuu at center
            with dissolve
            play music "audio/ms_moment_philosophical.mp3" fadeout 2.0 fadein 2.0 volume 0.6
            unknown "Oye, ¿estás bien? ¿Necesitas ayuda?"

            player "No, solo... es un malestar. Ya se me pasará."

            unknown "Pero no te notas bien."
            unknown "¿Te sientes [player_form('incómodo', 'incómoda', 'incómode')] o algo?"

            player "Un poco... Es que no conozco a nadie aquí. Todos parecen estar tranquilos, ocupados con lo suyo, y no quiero molestar a nadie por algo como esto."

            "Tu mano se aferra a tu abdomen mientras una nueva punzada de hambre te obliga a inclinarte un poco más."

            player "Ugh... lo siento, esta sensación no me ayuda..."

            unknown "Entiendo, estás como pez fuera del agua. Me pasaba lo mismo incluso cuando ingresé al Circo Golden."

            player "¿Circo Golden?"

            unknown "Correcto, es de donde viene ese muchacho."

            "El desconocido señala a Solei con una sonrisa."

            player "¿Solei?"

            player "¿Trabaja en un circo?"

            player "..."

            player "¿Se conocen?"

            "La sonrisa del desconocido se ensancha de inmediato."

            unknown "¿Conocerlo? ¡Somos compañeros! A veces actuamos juntos."

            "Mientras habla, el tono de su voz es más animado con cada palabra."

            unknown "Yo soy malabarista y él es trapezista…"

            "En un mal intento de disimular su emoción, el desconocido se aclara la garganta."

            unknown "Lo siento, me desvié del tema."

            unknown "¿Cuál es tu nombre?"

            player "Me llamo [player_name]."

            gold2 "Un placer, [player_name]. Me llamo Chuu."

            play sound "sfx_hungry.mp3"
            "Justo cuando extiendes tu mano hacia él para saludarlo, un nuevo gruñido de tu estómago te interrumpe."
            "Esta vez duele, al punto de hacerte doblar ligeramente sobre ti [player_form('mismo', 'misma', 'misme')]."
            stop sound

            "Al verte mal, Chuu te ofrece una hogaza de pan y un odre con agua para que recuperes fuerzas."

            show bread at bread_position
            show water at right
            player "Oh, gracias, pero no puedo aceptarlo..."

            hide bread
            hide water
            gold2 "Vamos, {sc=3}{b}¿Cuánto más vas a aguantar sin pedir ayuda?{/b}{/sc}"

            gold2 "Mira cómo estás, [player_form('doblado', 'doblada', 'doblade')] sobre ti [player_form('mismo', 'misma', 'misme')] y todavía intentas convencerme de que estás bien."

            "Chuu suelta un suspiro sospechosamente dramático."

            gold2 "Ahh… tienes que ordenar tus prioridades. No puedes poner siempre lo que quieres por encima de lo que necesitas."

            gold2 "Y lo que necesitas ahora es ayuda."

            "Él desliza suavemente la hogaza de pan en tus manos junto con el agua."

            gold2 "Así que toma."

            gold2 "Y ni se te ocurra decir que no."

            gold2 "Te aviso que aceptar ayuda de vez en cuando no es ilegal."

            "El aroma del pan recién horneado invade tus sentidos. Tu estómago no tarda en recordarte lo [player_form('hambriento', 'hambrienta', 'hambriente')] que estás."

            "La primera mordida resulta bastante más desesperada de lo que te habría gustado."

            "Al verte comer, Chuu ríe suavemente. Después saca otra porción para él y, a tu lado, le da un mordisco a su propio pan."

            "Con cada bocado, la incomodidad inicial empieza a disiparse y tu humor mejora casi de inmediato."

            thesun "¡Aquí estás, [player_name]! Lo siento por tardarme."

            show chuu at left
            with move

            show solei casual neutral at right
            with dissolve

            "La mirada de Solei pasa de ti a la hogaza de pan en tu mano, luego de nuevo a ti, y sonríe. Después se detiene en el chico a tu lado."

            thesun "¡Oh, Chuu!"

            "Solei ni siquiera duda antes de abrazar y saludar a Chuu."

            thesun "¿Qué haces aquí?"

            gold2 "Pues, además de venir a conseguir algunas cosas…"

            gold2 "Me mandaron a buscarte. Regina sospechó que podrías estar aquí."

            show solei casual shocked at right
            thesun "Ay no…"

            "Solei ríe nerviosamente mientras se frota la nuca."
            show solei casual ashamed at right

            thesun "¿Mamá está enojada?"

            player "Me huele que estás en problemas."

            "Al notar hacia dónde va la conversación, Solei lleva un dedo a sus labios y te dedica una sonrisa algo vacilante."

            "Claramente no quiere que sigas por ese camino."

            gold2 "No puedes estar {i}haciendo malabares{/i} con el circo, Solei. ¿Sabes?"

            gold2 "Regina va a empezar a atarte a una silla si sigues desapareciendo así."

            player "Si así conduce un caballo, no quiero ni imaginar cómo hace el resto de las cosas."

            "Chuu hace un esfuerzo para evitar reírse ante tu comentario."

            "Fracasa."

            thesun "¡N-No digas eso!"

            "Solei agita sus manos en un intento por hacer que te calles, pero es demasiado tarde."

            "Rendido, termina haciendo un puchero y cruzándose de brazos."

            show solei casual pout angry at right
            thesun "¡Hmp! Bueno, ahora por eso me acompañarás al circo."

            player "¡¿Qué?! Ni [player_form('loco', 'loca', 'se te ocurra')]."

            player "¡¿De dónde sacaste tanta confianza?!"

            "Esta vez, Chuu ya no se esfuerza por no reírse."

            gold2 "Bueno, para ser justos, Solei tiene la extraña costumbre de invitar a personas al circo apenas las conoce."

            gold2 "Un día de estos va a invitar a una piedra a unirse al circo…"

            "Lejos de tranquilizarte, la explicación de Chuu te genera nuevas dudas cuyas respuestas no sabes si quieres conocer."

            gold2 "Pero puede que por esta ocasión tenga razón."

            gold2 "No tienes a dónde regresar, ¿o me equivoco?"

            player "..."

            player "Buen punto."

            show solei casual neutral at right
            thesun "Entonces, ¿qué dices?"

            player "Pues…"

            player "((Si no fuera por mi necesidad, no sabría qué contestar, pero no conozco a nadie de aquí.))"

            # Menu broma
            menu:
                "Sí":
                    player "((Solo me queda confiar…))"
                "Sí":
                    player "((Solo me queda confiar…))"
                "Sí":
                    player "((Solo me queda confiar…))"

            "Te encoges de hombros, aceptando con resignación."

            player "¿Tengo opción?"

            show solei casual happy at right

            thesun "Nop, yo te encontré primero. Ahora tendrás que confiar en mí."

            player "Supongo que esta es tu forma de compensarme por nuestro primer encuentro, ¿eh?"

            thesun "¡OYE!"

            "Comienzas a reír y Chuu hace lo mismo."

            "Terminas el último bocado de pan antes de devolverle a Chuu su odre."

            "Él lo recibe con una sonrisa."

            gold2 "Me agradas, [player_form('forastero', 'forastera', 'forastere')]. Aún tengo cosas que hacer aquí, pero los veré en el circo más tarde."

            gold2 "Nos vemos, [player_name]. Te veo al rato, Solei."

            hide chuu
            with dissolve

            show solei casual happy at center
            with move

            thesun "Muy bien, semillita traviesa, es hora de marcharnos."

            player "¿Para ver cómo tu madre te castiga?"

            show solei casual pout angry

            "Solei hace un puchero ante tu risa, pero al ver tu sonrisa su gesto se desvanece hasta volverse una sonrisa cálida."

            thesun "Ja, ja... [player_form('chistosito', 'chistosita', 'chistosite')]."

            "Mientras Solei se aleja para ir por su yegua, tu mirada se posa en el mercado, que continúa lleno de vida."

            player "((Quizá acompañar a Solei no sea tan malo después de todo.))"

            "En un par de minutos, Solei vuelve a ti a lomos de Girasol."

            thesun "Es hora de partir. Súbete."

            "Extiende su mano hacia ti, y en cuanto la tomas te ayuda a subirte."

            thesun "Por cierto, estoy apurado, así que sujétate."

            "Algo en su tono te hace sentir un peligro inmediato."

            play music "audio/ms_solei.mp3" fadeout 2.0 fadein 2.0 volume 0.6
            scene bg sunflower_rush
            camera at horse_gallop_1
            play sound "sfx_horse-galloping-2.mp3" loop volume 0.7 fadein 0.2
            "En cuanto la yegua pisa fuera del pueblo, Solei golpea suavemente los costados de Girasol y su trote se acelera hasta convertirse en un galope veloz."

            player "¡¿Quieres matarnos o qué?!"

            "Te sostienes con fuerza mientras Solei se ríe de tus gritos. Su risa logra alcanzarte pese al viento."

            "A pesar de la velocidad, da la impresión de saber exactamente lo que está haciendo."


        "Robar":

            "El curso del pueblo vuelve a sentirse demasiado pesado. Notas por un momento que la mayoría de las miradas se dirigen a Solei. Quieres acercarte, pero de pronto te sientes fuera de lugar, como un pez fuera del agua."

            play sound "sfx_hungry.mp3"
            "Tu mano se extiende para llamar su atención, pero el rugido de tu propio estómago te detiene a medio movimiento."
            stop sound

            "De pronto, sientes... un vacío."

            camera at anxiety_vibration
            show anxiety_haze at anxiety_haze_in zorder 100
            play music "audio/ms_moment_tense.mp3" fadeout 2.0 fadein 2.0 volume 0.6
            "Esta vez tu mirada es más desesperada al observar a tu alrededor. Nadie te presta atención, como si no existieras."

            "De pronto, tus ojos se posan en una canasta de manzanas que un hombre acaba de poner en el escaparate de su tienda."

            player "(({b}Parece agotado...{/b}))"

            "A tu alrededor, la vida del mercado continúa sin prestarte atención."

            "El ruido de tu estómago te urge a actuar. El hombre se ha movido al puesto del frente."

            "No sigues observándolo."

            "Las manzanas son lo único que logras ver."

            "Sientes tu corazón desbocado cuando te mueves en dirección al puesto."

            player "{sc=3}{b}((Seguramente no va a extrañar una sola manzana...)){/b}{/sc}"

            "Tu pulso tiembla al tomar la manzana de la cesta."

            show apple at center:
                zoom 0.8

            "De repente, una mano se posa en tu hombro y te gira bruscamente."

            "Es el dueño del negocio."

            hide apple
            camera at stop_anxiety_vibration
            hide anxiety_haze
            with Dissolve(0.60)

            show week at center:
                zoom 0.85

            unknown "¡OYE, [player_form('FORASTERO', 'FORASTERA', 'TÚ')]! ¡ALÉJATE DE MIS MANZANAS!"

            "El impulso repentino te hace perder el equilibrio y caes hacia atrás."
            window hide
            play sound "sfx_dry_impact.wav"
            with hpunch
            with Fade(0.05, 0.55, 0.15, color="#000")
            window auto
            "Junto a ti está la canasta volcada, mientras las manzanas ruedan por el suelo."

            player "L-Lo lamento mucho. Yo… no tenía con qué pagar y... creí..."

            "Ante el alboroto, varios pueblerinos empiezan a acercarse, murmurando, demasiado atentos a lo que está por ocurrir."

            "Miras al suelo un momento. Una de las manzanas quedó ligeramente aplastada por la caída."

            player "Tenía hambre..."

            "Al volver a levantar la mirada hacia él, no parece violento, solo molesto."

            unknown "Sé que la necesidad es importante."

            unknown "Pero no es buena idea llegar a este punto."

            "Aquel hombre extiende su mano hacia ti y te ayuda a levantarte."

            "Luego inclina la cabeza hacia el suelo."

            "Tu mirada vuelve al suelo donde las manzanas acaban de caer."

            unknown "Vamos, ayúdame a recogerlas."

            hide week
            scene bg fair floor
            call apple_collection_sequence

            scene bg fair
            show week at center:
                zoom 0.85
            "El dueño te acerca una bolsa y comienzas a guardar en ella las manzanas que se cayeron durante el alboroto."

            "Asientes e intentas ponerlas dentro con cuidado."

            unknown "¿Cuál es tu nombre, [player_form('forastero', 'forastera', 'forastere')]?"

            player "Mi nombre es... [player_name]"

            gold7 "Soy Week."

            "Week da una mirada a su puesto y resopla."

            gold7 "Mira, no sé qué es lo que está pasando en tu vida. Pero este no es el camino."

            "Su mano apunta a la manzana que se aplastó contra el suelo."

            gold7 "He trabajado muy duro para conseguir una cosecha decente."

            gold7 "Y justo ahora la situación es… complicada."

            player "En serio lo siento, no quise robar por maldad, yo… tenía hambre y no conozco a nadie aquí…"

            player "Me sentí..."

            gold7 "Como un pez fuera del agua."

            "Concluye él antes de que puedas terminar la frase."

            gold7 "Es normal sentirse perdido en tierras nuevas."

            gold7 "Yo viví gran parte de mi vida en Faintworld."

            gold7 "Allí el frío mataba todo lo que sembramos."

            gold7 "Trabajamos una y otra vez…"

            gold7 "Y la tierra nunca nos devolvía nada."

            gold7 "Por eso no me tomo esto a la ligera. La próxima vez no voy a escuchar explicaciones."

            gold7 "{b}Te cortaré las manos.{/b}"

            gold7 "..."

            player "..."

            gold7 "Hablo en serio."

            "No sabes si es simplemente una broma demasiado cruel o si lo dice en serio. Prefieres no preguntar."

            "El silencio entre los dos se vuelve tenso de pronto."

            "De pronto, Solei aparece con una expresión mezcla de nerviosismo y preocupación."

            thesun "¡Aquí estás, [player_name]! ¡Te estaba buscando!"

            show week at left:
                zoom 0.85
            with move

            show solei casual neutral at right
            with dissolve

            "Él aparece a tu lado tan rápido que casi no lo notas hasta que su mano se posa sobre tu hombro."

            "Su mirada pasa de ti a Week por un instante."

            thesun "¡Hola, Week! Muy buenas tardes. ¿Por qué esa cara?"

            gold7 "Encontré a [player_form('este tipo', 'esta tipa', 'esta persona')] robando mi mercadería..."

            show solei casual shocked at right
            thesun "¡¿QUÉ HIZO QUÉ?!"

            show solei casual angry at right
            thesun "¡[player_name]!"

            show solei casual shocked at right
            player "¡No fue por gusto!" with hpunch

            "Tu grito repentino sobresalta a Solei."

            player "Llevo todo el día sin comer..."

            "Week parece cada vez menos interesado en continuar aquella conversación."

            gold7 "¿[player_form('Es amigo tuyo', 'Es amiga tuya', 'Se conocen')]?"

            thesun "Emm... bueno..."

            show solei casual neutral at right
            "Su mirada vuelve a recorrerte, como si estuviera buscando las palabras correctas."

            thesun "Podrías decir que está en proceso..."

            thesun "El vínculo quiero decir."

            player "¿Vínculo?..."

            player "¡¿Qué?!"

            show solei casual happy at right
            thesun "¡Cuestión!"

            "Solei aplaude, haciendo que vuelvas la mirada hacia él y cortando tu pregunta en el acto."

            thesun "¡[player_name]! ¿Por qué no le pagaste?"

            player "¡¿CÓMO QUIERES QUE PAGUE SI NO TENGO DINERO, GENIO?!"

            show solei casual neutral at right
            thesun "..."

            show solei casual ashamed at right
            thesun "Claro, me había olvidado de ese pequeño detalle."

            thesun "Lo siento."

            show solei casual neutral at right
            gold7 "Te lo perdono por la otra vez que me ayudaste, Solei."

            "Week te apunta."

            gold7 "Pero pagarás por [player_form('él', 'ella', 'elle')]."

            thesun "Es justo. Discúlpame."

            "Solei paga apenado y Week le entrega la bolsa de las manzanas que ayudaste a recoger."

            show solei casual ashamed at right
            thesun "No se volverá a repetir. Lo prometo."

            "Solei se sonroja un poco de vergüenza."

            player "Perdón por todo. En serio."

            gold7 "Solo trata de no actuar desde la sombra la próxima vez."

            player "((¿Que no actúe desde la sombra?))"

            hide week
            with dissolve

            show solei casual happy at center
            with move

            "Solei toma tu brazo y comienza a alejarte del puesto de Week mientras sostiene la bolsa con las manzanas que tiraste."
            play music "audio/ms_moment_relaxing.mp3" fadeout 2.0 fadein 2.0 volume 0.6
            "Sientes una punzada de culpa que se desvanece rápidamente al recordar la forma en que esperaba que pagaras sin tener dinero."

            "En cuanto se acercan a Girasol, Solei te entrega una de las manzanas."

            show apple at center:
                zoom 0.8
            thesun "Aún no has comido, ¿no?"
            hide apple

            "Das la primera mordida a la manzana mientras Solei acomoda unas cuantas cosas en la montura."

            "La frase de Week continúa dando vueltas en tu cabeza."

            player "((Que no actúe desde la sombra… ¿Qué quiso decir?))"

            show solei casual neutral
            thesun "No vuelvas a hacer eso. Te meterás en problemas."

            player "Ya dije que lo sentía."

            thesun "Por ahora tengo que hacerme responsable de ti."

            "Suspira suavemente. Por un segundo, crees notar que realmente está escogiendo sus palabras."

            thesun "Por lo que veo, aún sigues [player_form('desorientado y perdido', 'desorientada y perdida', 'sintiéndote fuera de lugar')]. Puedo ayudarte, pero necesito que me escuches y me hagas caso."

            player "Pues es muy obvio que no tengo otra opción, ¿no?"

            player "Apenas recuerdo mi nombre y que tenía hambre."

            thesun "Bueno, puedes venir al circo con nosotros, al menos hasta que puedas poner en orden tus… pensamientos."

            player "No me queda otra… ¿Qué hay que hacer?"

            thesun "Primero, hablar con mi madre."

            "Por un momento, sus manos, que ajustaban la correa de la montura de Girasol, se detienen."

            "Luego levanta la mirada al cielo y la desvía hacia la puesta de sol."

            show solei casual shocked
            thesun "¡AHH! ¡Estrellas, ahora sí estoy en problemas!"

            "La manzana queda a medio camino de tu boca cuando Solei trepa a su yegua casi de un brinco y extiende su mano hacia ti."

            thesun "¡[player_name], tenemos que irnos!"

            "Subes con algo de dificultad al tener una mano ocupada con la manzana y, en cuanto te sientas y vas a dar otra mordida, sientes el galope veloz de Girasol."

            show solei casual happy
            thesun "Por cierto, estoy apurado, así que sujétate."

            player "¿Pero qu-?"

            "En cuanto se alejan de los aldeanos, el galope de Girasol se hace aún más veloz."

            scene bg sunflower_rush
            camera at horse_gallop_1
            play sound "sfx_horse-galloping-2.mp3" loop volume 0.7 fadein 0.2

    "El viento golpea tu rostro y te obliga a mantener los ojos cerrados. Unos minutos después, finalmente los abres."

    "Ante ti se extiende nuevamente el campo de girasoles. Al mirar atrás, el pueblo de Zoloto se hace cada vez más pequeño hasta perderse en el mar de pétalos amarillos."

    player "((Supongo que Solei tenía razón, es un pueblo muy lindo))"

    scene bg golden circus tent away at circus_approach

    "Tras un rato, los girasoles empiezan a dar paso al trigo. Poco a poco, los tonos amarillos de las flores son reemplazados por el dorado de las espigas."

    "Las espigas se extienden hasta el horizonte, aunque no notas a nadie trabajando los campos. Parecen haber surgido de forma natural."

    player "((¿Tan fértil es este lugar?))"

    "Entre las espigas empieza a surgir una carpa amarilla. Mientras más se acercan, logras distinguir varias tiendas a su alrededor. Parece un pueblo, aunque mucho más pequeño que Zoloto."

    "A lo lejos, algunas personas los ven acercarse y se aglomeran en la entrada. Finalmente, Solei se detiene."

    camera at stop_horse_gallop_1
    stop sound fadeout 0.3
    play music "audio/ms_ambience_circus.mp3" fadeout 2.0 fadein 2.0

    scene bg circus
    show gharlequin neutral at center:
        zoom 0.75

    goldhelper "Buenas tardes, mi señor. Nos alegra ver que ha vuelto..."

    "La mirada del ayudante se fija en ti y luego vuelve a Solei."

    show solei casual neutral at left
    show gharlequin neutral at right:
        zoom 0.75
    with move
    goldhelper "Veo que no viene solo."

    thesun "Es complicado explicarlo ahora. Tengo que ver a mi madre."

    show gharlequin happy:
        zoom 0.75
    goldhelper "Entiendo, mi señor."

    show gharlequin nervous:
        zoom 0.75
    goldhelper "Aunque debo decirle que la reina está muy..."

    show solei casual ashamed

    thesun "¿Furiosa?"

    show gharlequin worried:
        zoom 0.75
    "El ayudante solo lo observa por un segundo como respuesta."

    thesun "Sí, lo supuse."

    show solei casual neutral

    thesun "Es que llegó alguien nuevo a Limfool."

    "El ayudante vuelve a observarte antes de asentir."
    show gharlequin happy:
        zoom 0.75
    goldhelper "Ya veo, una nueva alma en busca de un guía y probablemente un vínculo."

    player "((¿Alma…?))"
    $ renpy.music.set_volume(0.10, delay=3.0, channel="music")

    "Esa palabra resuena en tu cabeza por un momento."

    "Tu mano se posa instintivamente sobre tu pecho."

    "Es extraño. Sabes que te mueves, respiras e incluso has sentido el viento sobre tu rostro durante la cabalgata."

    "Y, aun así, algo no termina de encajar."

    player "((Estoy [player_form('vivo', 'viva', 'con vida')]. Entonces… ¿Por qué?))"

    "La sensación en tu pecho sigue siendo incompleta, como si algo en tu existencia estuviese fuera de lugar o faltara."

    "Aunque no puedes definir del todo qué es."

    hide solei
    hide gharlequin
    scene bg sunflowers at recent_memory
    with Dissolve(0.5)
    player "((Un campo de girasoles casi infinito…))"

    scene bg golden circus tent away at recent_memory
    with Dissolve(0.5)
    player "((Un cultivo de trigo que nadie trabaja…))"

    scene bg_golden_circus_tent at recent_memory
    with Dissolve(0.5)
    player "((Y un circo surgiendo en medio de ambos…))"

    scene bg circus
    with Dissolve(0.3)
    show solei casual neutral at left
    show gharlequin worried at right:
        zoom 0.75

    "Al volver a fijarte en Solei, notas lo extravagante de su atuendo."

    "Ahora que finalmente logras darte un respiro, todo empieza a sentirse extraño e irreal."

    "Apoyas la otra mano sobre Girasol. El tacto de su piel te ancla apenas un poco."
    $ renpy.music.set_volume(1.0, delay=2.0, channel="music")
    "Ni siquiera percibes cuándo Solei baja del caballo. Solo vuelves a reaccionar cuando apoya una mano sobre la tuya."

    thesun "¿Estás bien, Semillita?"

    thesun "Ven, déjame ayudarte."

    "Con cuidado, te ayuda a apoyarte en el estribo para que puedas bajar de la yegua."

    "Una vez abajo, Solei te observa por unos segundos, asegurándose de que estés bien."

    "Recorres el lugar con la mirada una vez más: los campos de trigo, la enorme carpa amarilla y, finalmente, los ojos azules de Solei."

    "No lo habías pensado antes, pero son de un color tan intenso que parecen irreales, casi como todo el lugar."

    "A pesar de lo extraño e irreal que resulta todo, sientes que una pequeña parte de ti quiere quedarse y dejarse llevar."

    player "Sí, solo estoy [player_form('pensativo', 'pensativa', 'pensando')]."

    "Solei toma tus manos entre las suyas con cuidado."
    show solei casual happy
    show gharlequin happy:
        zoom 0.75

    thesun "Hey, todo está bien. [player_form('No estás solo', 'No estás sola', 'Estoy aquí')]."

    thesun "Por ahora, ¿qué tal si te presento al grupo?"

    "Solei te presenta a sus compañeros entre risas antes de empezar a caminar hacia la carpa principal, que asumes que pertenece a su madre."

    hide gharlequin
    show solei casual awkward at center
    with move
    "Antes de entrar, se detiene un momento y se frota la nuca."

    thesun "Bueno, espero que no esté… tan enojada."

    "Después de decirlo, su mirada se dirige a ti con complicidad."

    show solei casual neutral

    thesun "Aunque ahora que lo pienso..."

    show solei casual happy

    thesun "Podré usarte como excusa, ya que me distraigo bastante en el pueblo."

    player "((¿Mi opinión no cuenta o qué?))"

    "Ves a Solei asomarse un poco dentro de la carpa."

    "Miras por encima de su hombro y logras divisar a tres mujeres dentro, pero Solei se aleja antes de que puedas distinguirlas mejor."

    player "Oh no… Dime que no piensas hacer lo que creo que harás."

    show solei casual neutral

    thesun "¿Qué cosa?"

    "Al escucharte, se gira hacia ti y finge no entender a qué te refieres."

    player "No puedo creerlo."

    player "Solei, esto es una pésima idea."

    "Al escucharte, pasa un brazo por encima de tus hombros con una sonrisa."

    show solei casual happy
    thesun "Bueno, estas son las consecuencias de que yo te haya encontrado."

    "Se aparta de ti y te toma por la muñeca, arrastrándote con la emoción de un niño a punto de hacer una travesura."

    thesun "¡Ven conmigo [player_name]!"

    "Reaccionas justo a tiempo para apartarte y te llevas una mano al pecho por puro instinto."

    player "¡Ni [player_form('loco', 'loca', 'se te ocurra')]!"

    show solei casual shocked
    player "Sé que te la debo por llevarme al pueblo, pero… parece que haces esto muy seguido. ¿Cómo se dice? ¡Ah, sí! ¡Escaparte!"

    "Lo señalas con el índice mientras hablas. El gesto parece avergonzarlo un poco."

    show solei casual ashamed
    thesun "Por favor, sé que nos conocemos desde hace poco, pero necesito que me ayudes con esto."

    "Verlo así te hace vacilar. Tu postura se relaja ligeramente."

    player "¿Qué? ¿Tanto miedo le tienes a tu mamá?"

    thesun "No es que le tenga miedo exactamente. Solamente… emmm… no me gusta que me regañen."

    "Mientras habla, empieza a jugar con sus dedos, evitando mirarte."

    thesun "Es todo."

    thesun "Luego tengo que escuchar el mismo “bla, bla, bla” de siempre, ¿sabes?"

    player "Pues es tu madre. Así se supone que se comporte."

    "Te encoges de hombros y Solei se tensa un poco ante la mención de la palabra “madre”."

    "Su cabeza gira hacia ti con lentitud. Tienes un mal presentimiento al instante."

    thesun "Eso… y que…"

    thesun "Mi madre es… ¿la… líder de este lugar?"

    player "¡¿Qué?!"

    "Haces un esfuerzo por no levantar demasiado la voz, algo que ya resulta demasiado difícil por sí solo."

    player "¡Solei! ¿No te parece que debiste empezar por ahí? ¡Con razón te está buscando!"

    "De pronto, escuchas una voz femenina y autoritaria desde el interior de la carpa."

    unknown "¿Solei?"

    unknown "¿Eres tú?"

    show solei casual shocked

    thesun "¡Agh, mierda! Nos descubrieron."

    thesun "Es hora del plan B."

    show solei casual happy

    "Sin darte tiempo a rechistar, Solei te toma por los hombros y te empuja al interior de la carpa."

    "Intentas clavar tus talones en el suelo para frenar su avance, pero acaba llevándote igual, pese a tus quejas frustradas."

    "Cuando finalmente logra arrastrarte al interior, acabas frente a la mujer que habló antes."

    scene bg sun tent

    unknown "¿Qué es todo este escándalo?"

    play music "audio/ms_moment_philosophical.mp3" fadeout 2.0 fadein 2.0 volume 0.6

    show solei casual shocked at solei_group_side
    with move

    show regina angry at arcana_group_center zorder 3
    with move

    "Al mirar al frente, notas a una mujer sentada en un imponente trono de respaldo alto."

    "Suaves telas caen a sus costados como cascadas de seda."

    thesun "Pues…"

    "Solei te da una ligera palmada en el hombro para animarte a hablar."

    #7-OPCIONES / encuentro con los arcanos mayores I
    menu:
        "Seguirle el juego":
            player "Nosotros estábamos debatiendo algo..."

            "En cuanto empiezas a hablar, sientes la mirada afilada de la mujer sobre ti. Los nervios te traicionan y terminas balbuceando."

            player "Pero no se preocupe. No es nada serio."

            "Ella no parece creerse una palabra de lo que dices."

            "Su ceño se frunce y su mirada busca a Solei, que sigue parado detrás de ti."

            unknown "¿Debatir? ¿Qué cosas?"

            show solei casual ashamed

            "Sientes los dedos de Solei tamborilear sobre tus hombros."

            thesun "Nada, mamá, emmm…"

            show solei casual happy

            thesun "¡Mira! Llegó una nueva alma al circo."

            "Al decirlo, te da un ligero empujón que te deja casi frente al trono."

            show solei casual proud

            "Al girarte para reclamarle, notas que ha puesto las manos en la cintura y se ha erguido con... ¿orgullo?"

            thesun "Y fui muy responsable al [player_form('cuidarlo y traerlo', 'cuidarla y traerla', 'cuidarle y traerle')] hasta aquí para que reciba mejor supervisión y guía."

            "Las otras dos mujeres, sentadas junto al trono, dejan a un lado sus aperitivos para fijar la mirada en ti."

            unknown "¿Un alma nueva, dices?"

            "La madre de Solei se levanta de su trono de telas y se aleja de sus compañeras."

            "Su presencia imponente casi te hace encogerte cuando la tienes cerca."

            "Te toma del mentón y, con una delicadeza inesperada, hace que levantes la mirada hacia ella."

            "Mantiene la mirada fija en ti durante unos segundos, hasta que finalmente sonríe y se aparta."

            show regina neutral
            unknown "Ya veo."

            unknown "Su aura está un poco cansada y densa."

            unknown "Se nota que todavía tiene mucho en qué trabajar."

            show solei casual happy

            play sound "solei_giggle_2.mp3"
            thesun "Para eso estoy. Ya me conoces: siempre guiando hacia la luz."

            show regina angry

            unknown "Y escapando de tus responsabilidades, hijo."

            show solei casual shocked

            "Solei deja de reír casi de inmediato en cuanto su madre empieza a hablar."

            unknown "Solei… Otra vez tarde."
            show regina ashamed
            "Ella suelta un suspiro, como si esa fuera una conversación que ha tenido demasiadas veces."
            show solei casual ashamed
            unknown "¿No te da vergüenza?"

            "Al mirar a Solei, notas cómo se encoge ligeramente bajo la reprimenda."

            "Una mujer de cabellos rojizos se acerca desde los tronos y posa una mano sobre el hombro de la madre de Solei."

            show routa neutral at arcana_group_left
            unknown_2 "Regina, querida. Tenemos [player_form('un nuevo invitado', 'una nueva invitada', 'una visita')], ¿recuerdas?"

            unknown_2 "Modales~"
            show regina neutral

            "La mujer que acaba de hablar se cruza de brazos mientras te observa."

            unknown_2 "Mira lo que nos ha traído el destino."

            show alicia happy at arcana_group_right

            "La otra mujer suelta una risita por lo bajo y asiente antes de dar un pequeño aplauso."

            unknown_3 "Routa tiene razón, mi reina. Sé que Solei es revoltoso y todo un “Fool”."

            unknown_3 "Pero lo importante es que está aquí."

            "Su mirada se desvía hacia ti por un segundo antes de volver a Regina."

            unknown_3 "¿Se tardó? Bastante. Pero de que llegó… llegó."
            show regina ashamed
            "La madre de Solei se lleva una mano a la frente, soltando otro suspiro."

            thequeen "Siempre es la misma conversación con ustedes dos. Dejen de defenderlo."

            show alicia neutral
            "Das unos cuantos pasos hacia Solei mientras ellas conversan. La mujer de vestido verde cruza sus brazos sin perder su sonrisa."

            unknown_3 "Tengo que recordarte que tu bebé mayor también se escapa y lo perdonas igual que al menor."

            show solei casual frozen
            "Te inclinas para poder susurrarle a Solei, que parece una estatua ahora."

            player "¿Tienes hermanos?"

            thesun "Sí. Tengo un hermano. Se llama Chariot…"

            "Ni siquiera se gira para responderte. Su mirada sigue fija en su madre."

            thequeen "Alicia, basta. No quiero alargar esto más."

            thequeen "Estrellas, ya estoy vieja para lidiar con esto."
            show alicia giggle
            show routa giggle
            "Las otras dos mujeres sueltan una risa casi coordinada, pero la mirada de la reina vuelve a ustedes."

        "Acusarlo con su madre":
            player "A mí no me metas."

            "Con un movimiento, te zafas de las manos de Solei y tu primer instinto es inclinar ligeramente la cabeza ante la mujer."

            player "Solo quiero poder trabajar aquí, si es posible."

            "La mujer del trono no se mueve. Su mirada se dirige a Solei, que se ha quedado quieto después de que te zafaras de su agarre."

            unknown "¿Qué hiciste esta vez, Solei?"

            "Solei no parece tener mucha intención de responder."

            player "Pues me llevó a Zoloto."

            "Solei suelta un quejido como si tus palabras le hubiesen causado daño físico."

            show solei casual angry
            "Se cruza de brazos con una velocidad absurda."

            thesun "[player_form('Traidor...', 'Traidora...', 'Traición...')]"

            "La madre de Solei se levanta con calma del trono de telas."

            unknown "¿Por qué no me sorprende?"

            show solei casual ashamed
            "En cuanto la mujer empieza a caminar hacia él, Solei descruza los brazos y esconde las manos detrás de la espalda."

            thesun "Solo me di una vuelta para tomarme un respiro."

            "Ella asiente lentamente. Luego niega con la cabeza, frunciendo el ceño."

            unknown "¿Y esa vuelta tuvo que durar toda la tarde?"

            player "No solo eso. Casi me atropella con Girasol, por bruto."

            show solei casual angry
            "Solei protesta casi de inmediato."

            thesun "¡Ya te dije que lo sentía! ¡Suelta el pasado!"

            show regina ashamed
            "La mujer se toma el puente de la nariz con cansancio."

            unknown "Agh, Solei."

            unknown "Si sigues así, te voy a castigar. ¿De verdad volveremos a eso?"

            thesun "¡No es justo!"

            "Solei lanza una mirada indignada hacia la entrada de la carpa."

            thesun "Cuando Chariot se va a “polinizar” flores por ahí como una abeja, no le dices nada."

            player "¿Chariot?"

            "Solei refunfuña antes de responderte."

            thesun "Mi hermano mayor."

            "Sus amigas, que hasta ahora no habían dicho nada, sueltan una carcajada."

            show routa giggle at arcana_group_left
            show alicia giggle at arcana_group_right
            show regina angry
            "La carcajada parece irritar todavía más a la madre de Solei, cuya mirada severa recae sobre él y sobre ti."

            show solei casual frozen
            player "((¡¿Y yo qué hice?!))"

            unknown_2 "No puedo creerlo, Regina… Solei dijo algo coherente."

            thequeen "Routa, no es momento."

            unknown_3 "Van a espantar [player_form('al invitado', 'a la invitada', 'a la visita')] con tanto drama."

            unknown_3 "El alma nueva va a pensar que este circo está maldito."

            thequeen "Alicia…"

    show regina ashamed
    thequeen "Recapitulemos, Solei."

    "Regina aparta la mano de su rostro, todavía concentrada en Solei."

    show regina angry
    thequeen "Otra vez llegaste tarde."

    "Regina levanta un primer dedo."

    "Solei empieza a negar con la cabeza mientras su madre habla, sin despegar la mirada del suelo, como si ya hubiera escuchado aquella conversación demasiadas veces."

    thequeen "Tu hermano avisó a los pueblos cercanos de que el show se retrasaría. Lo reprogramamos para cuando la Luna alcance el cielo nocturno."

    "Alza un segundo dedo, aunque enseguida baja la mano. No parece estar disfrutando de la conversación."

    thequeen "No me gusta que hagas eso porque…"

    thesun "“De nuestros shows obtenemos la recompensa por todo el esfuerzo que invertimos”."
    thesun "Lo sé, mamá."

    "Alicia le da un suave codazo a Routa y ambas clavan la mirada en ti."
    show alicia neutral
    show routa neutral
    player "((Las otras señoritas que acompañan a Regina no paran de observarme.))"

    "Empiezas a observar las paredes de la carpa en un intento por no mirar en esa dirección."

    player "((Qué incómodo…))"

    "Entonces, como si Solei hubiera recordado tu existencia, vuelve a poner sus manos en tus hombros."

    show solei casual happy
    thesun "¡Ah, mamá! No te dije el nombre de la nueva alma, ¿no?"

    thesun "Se llama [player_name]."

    "Frota tus hombros mientras te sacude suavemente."

    thesun "[player_form('Lo', 'La', 'Le')] encontré en el campo de girasoles y, como es [player_form('forastero', 'forastera', 'forastere')], no pude evitar [player_form('ayudarlo', 'ayudarla', 'ayudarle')]."

    "Routa se acerca a examinarte con una pequeña sonrisa."

    thewheel "¡Me parece maravilloso!"

    show routa happy
    thewheel "¡[player_form('Un nuevo integrante', 'Una nueva integrante', 'Una nueva alma')]! Recuerdo cuando Chariot me encontró y me trajo aquí… Qué nostalgia."

    "Alicia, por su parte, se acerca y apoya una mano en el brazo de Solei, haciendo que te suelte los hombros."

    wlover "Regina, seguro que para compensar sus errores dará un buen show esta noche."

    wlover "¿O no, Solecito?"

    show solei casual happy
    thesun "¡Sí! Ya sabes que siempre se deja lo mejor para el final."

    show solei casual neutral
    thesun "Nunca decepciono."

    show regina angry
    "Dice esa última frase mientras mira directamente a su madre."

    show regina neutral
    thequeen "Igual te voy a poner límites."

    thequeen "A ti y a tu hermano."

    "Regina se da la vuelta y vuelve a sentarse en su trono, apoyando la cabeza en una mano."

    thequeen "Cuando eran más jóvenes, podía perdonar este tipo de errores, pero ahora son adultos y se van a comportar como tales."

    thequeen "Quiero responsabilidad."

    thequeen "Ahora ve y prepárate, Solei."

    show solei casual ashamed
    "Solei asiente y te toma de la muñeca para llevarte con él, pero la voz de Regina interrumpe su movimiento."

    thequeen "Espera."

    show solei casual shocked
    thequeen "Deja a [player_name] aquí."

    show solei casual ashamed
    thesun "Pero..."

    thequeen "Quiero que nos conozcamos un poco más."

    "Sin decir más, Solei te suelta la muñeca y te dedica una última mirada antes de salir de la carpa."

    show solei casual ashamed at solei_exit_left
    pause 1.1
    hide solei

    $ speaker_zorder_group = {"routa": 1, "alicia": 2, "regina": 3}
    $ speaker_zorder_enabled = True
    $ _set_speaker_zorder(None)

    show routa happy at arcana_focus_left zorder 1
    show regina neutral at arcana_focus_center zorder 3
    show alicia neutral at arcana_focus_right zorder 2
    pause 0.8

    "De pie, ante la mirada atenta de la reina, enderezas tu postura, casi por reflejo."

    player "¿Cómo puedo dirigirme a usted? si no le molesta."

    "La pregunta parece complacerla ligeramente, y ves una pequeña sonrisa marcarse en sus labios, aunque rápidamente desaparece."
    show regina happy at arcana_focused_regina zorder 3
    thequeen "No pido mucho solo educación, si yo te trato con respeto quiero lo mismo de tu parte."

    show regina neutral at arcana_focused_regina zorder 3
    "Los miembros del circo me dicen Regina o “mi reina” en señal de respeto y cariño."

    player "Muy bien lo tendré en cuenta, muchas gracias."

    "Regina asiente, antes de enderezar su postura en el trono."

    thequeen "Voy a ser directa contigo, [player_form('querido', 'querida', 'dulzura')]. Aunque no lo parezca, Solei no suele traer a cualquiera aquí."

    thequeen "Sólo hacemos excepciones con nuestro público o elenco especial."

    thequeen "Así que quiero una respuesta honesta."

    "El aire en la habitación de pronto se siente más pesado"

    thequeen "¿Cómo conseguiste que mi hijo te trajera aquí?"

    "Su pregunta te toma con la guardia baja"

    "Hasta ese momento realmente no te habías detenido a preguntarte por qué habías acabado allí."

    #8-OPCIONES/ encuentro con los arcanos mayores II
    menu:
        "El destino":
            "Te aclaras la garganta por reflejo antes de responder."

            player "Mi reina, yo sólo desperté bajo un gran árbol."

            player "No sé ni lo que quiero, solamente me estoy dejando llevar."

            "Al escuchar tu respuesta, Routa parece complacida y da un paso hacia ti."

            show routa happy at arcana_focused_routa zorder 1
            thewheel "¡Vaya, qué privilegio!"

            "A medida que se acerca, su dedo hace pequeños círculos en el aire."

            "Su mirada te recorre como si intentara resolver un acertijo."

            show routa neutral at arcana_focused_routa zorder 1
            thewheel "Una pregunta: ¿Aquel árbol estaba cerca de un campo de girasoles?"

            "La mujer inclina ligeramente la cabeza."

            "En sus labios percibes la sombra de una sonrisa divertida."

            "Das un paso hacia atrás instintivamente."

            player "Sí, creo que lo que me despertó fue la luz. Luego caminé por el campo toda la mañana."

            player "Ahí me encontré a Solei."

            "Regina, desde su trono, levanta una ceja, expectante."

            show regina disappointed at arcana_focused_regina zorder 3
            thequeen "¿Ya vas a empezar con tus preguntas, Routa?"

            "Routa le dedica una sonrisa inocente antes de volver a mirarte."

            thewheel "Sabes que soy muy curiosa."

            thewheel "No puedo quedarme quieta ante una sola respuesta; necesito saber más."

            "Alicia se acerca a Regina con calma."

            wlover "Routa tiene razón, mi reina."

            wlover "Cuanto más agradable sea el ambiente, mejor fluyen la energía y la armonía."

            show alicia happy at arcana_focused_alicia zorder 2
            show regina neutral at arcana_focused_regina zorder 3
            "Te lanza una mirada rápida."

            wlover "Además, para ser sincera, yo también tengo curiosidad."

            "Sus manos empiezan a peinar su cabello con lentitud, despreocupada."

            wlover "[player_form('Este forastero', 'Esta forastera', 'Este forastere')] me llama la atención. Tiene algo… mmm… ¿encantador? Ya me entienden."

            show routa giggle at arcana_focused_routa zorder 1
            "Routa asiente un par de veces. De nuevo, su dedo gira, marcando un círculo en el aire."

            show routa neutral at arcana_focused_routa zorder 1
            thewheel "Escucha… [player_name], ¿verdad?"

            thewheel "Sé que justo ahora no lo entiendes, y está bien. La primera vez que llegamos aquí también nos sentimos así."

            show routa happy at arcana_focused_routa zorder 1
            thewheel "No te preocupes, no estoy tratando de asustarte o algo así."

            thewheel "Lo habitual es que las almas aparezcan cerca del pueblo o no muy lejos de la carpa."

            thewheel "Que tú hayas despertado bajo el árbol y que, además, haya sido Solei quien te encontrara…"

            show routa giggle at arcana_focused_routa zorder 1
            "Suelta una pequeña risa que te hace fruncir el ceño casi de inmediato."

            player "¿Eso es importante?"

            show routa neutral at arcana_focused_routa zorder 1
            "Routa guarda silencio un momento."

            thewheel "Tal vez sí, tal vez no. Las coincidencias ocurren, eso está claro."

            thewheel "Pero cuando las coincidencias empiezan a repetirse y a apuntar en una misma dirección…"

            show routa happy at arcana_focused_routa zorder 1
            thewheel "Me gusta empezar a llamarlo destino."

            player "Lo siento, pero apenas conozco a Solei."

            player "¿No crees que es algo exagerado llamarlo destino?"

            "Ella levanta un dedo y lo mueve de lado a lado antes de acompañar el gesto con la cabeza y un chasquido de desaprobación."

            thewheel "Al contrario, [player_name]. La vida tiene su propia forma de ponernos en el camino que necesitamos recorrer."

            thewheel "Y eso es lo lindo, dulzura. Que Solei, nuestro Solei, te haya guiado y se haya hecho responsable de ti… bueno."

            thewheel "Significa que algo tiene que salir a la luz. Tal vez sea parte de tu recorrido en estas tierras."

            thewheel "Regina, si me preguntas a mí, es posible que estén empezando a forjar un vínculo."

            player "((“Vínculo”… esa palabra de nuevo. ¿Qué se supone que significa?))"

            "Regina se levanta de su lugar y su voz es solemne, como si estuviese recordando alguna norma."

            show regina neutral at arcana_focused_regina zorder 3
            thequeen "“Quienes despierten bajo el gran árbol de Limfool están destinados a encontrar su propio destino, elegir su camino y ser su propio arcano.”"

            player "¿“Ser su propio arcano”? ¿Qué quieren decir con eso?"

            "Ahora es Alicia quien niega con la cabeza."

            show alicia giggle at arcana_focused_alicia zorder 2
            wlover "Significa que eres un misterio profundo, [player_form('forastero', 'forastera', 'forastere')]."

            show alicia happy at arcana_focused_alicia zorder 2
            wlover "Algo reservado e inaccesible para la mayoría."

            wlover "Hace un tiempo que no veíamos a alguien como tú, ¿no es así, Regina?"

            player "((Demasiado místico para mi pobre cabeza…))"

            "Tu mirada de desconcierto debió ser demasiado evidente, porque Regina baja el tono de su voz."

            show regina happy at arcana_focused_regina zorder 3
            thequeen "Ser “arcano” significa ser una persona reservada, difícil de descifrar o que parece guardar secretos profundos."

            player "((Eso explica exactamente nada.))"

            thewheel "Tu percepción intenta alcanzar algo que tu mente agotada todavía no puede comprender."

            thequeen "Es tu primer amanecer."

            thequeen "Date el tiempo de acomodarte en estas tierras antes de responder a todas tus preguntas, [player_name]."

            wlover "¡Mhm! Es tu primer día aquí {i}existiendo{/i}, no te sobrestimules."

            "Tu mirada pasa entre las tres mujeres. No crees haber entendido ni la mitad de lo que te acaban de decir."

            player "[player_form('No estoy seguro de', 'No estoy segura de', 'No creo')] haber entendido bien."

            thewheel "Descuida."

            thewheel "Lo entenderás a su debido tiempo."

            thewheel "Por ahora, déjate llevar. Tarde o temprano, cada río llega al mar."

            player "((Eso suena demasiado fantasioso… pero supongo que en este lugar todo podría pasar.))"


        "No lo sé":

            "Tu mirada se desvía hacia una de las paredes de la carpa antes de contestar."

            player "No sé. Solei me trajo aquí y dijo que podrían ayudarme."

            player "Y yo… no pensé demasiado en eso."

            show alicia giggle at arcana_focused_alicia zorder 2
            "Alicia cubre su boca en un intento de ocultar una sonrisa."

            wlover "Mi reina, por favor, no sea tan dura con la nueva alma."

            wlover "¿Y si solecito solo ha hecho [player_form('un nuevo amigo', 'una nueva amiga', 'una nueva amistad')]?"

            "Regina relaja los hombros, niega con la cabeza y suspira pesadamente."

            show regina disappointed at arcana_focused_regina zorder 3
            thequeen "Alicia, tu solecito ya es adulto y no puede seguir tratando todo como un juego."

            thequeen "Pone su fachada de inocente, luego se escapa y, de pronto, aparece aquí con [player_form('el forastero', 'la forastera', 'une forastere')] sin avisar."

            thewheel "Regina, querida, empiezo a preguntarme si lo que te preocupa no es tanto la presencia de una nueva alma en nuestro circo como que Solei empiece a actuar igual que Chariot."

            "Las tres parecen tan inmersas en su conversación que se han olvidado de que sigues de pie frente a ellas."

            show alicia neutral at arcana_focused_alicia zorder 2
            wlover "¿Una fachada? Podría ser."

            "De pronto, la mirada de Alicia vuelve a buscarte."

            wlover "Aunque también es posible que simplemente quiera desarrollar un vínculo con [player_name]."

            player "((“Vínculo”… esa palabra de nuevo. ¿Qué se supone que significa?))"

            player "Perdón… ¿acabas de decir “vínculo”?"

            show alicia shocked at arcana_focused_alicia zorder 2
            wlover "¡Oh! ¿Solei no te lo ha explicado?"

            "Alicia niega con la cabeza antes de empezar a peinar su cabello con las manos."

            show alicia amused at arcana_focused_alicia zorder 2
            wlover "El “vínculo” es una elección consciente y profunda."

            wlover "No puedes compararlo con un destino trazado. Es una elección del corazón y la forma en que nuestro amor se refleja en el mundo."

            wlover "Por ejemplo: los valores que compartes con alguien especial o la forma en que dos opuestos acaban complementándose y potenciándose al estar juntos."

            show alicia dreamy at arcana_focused_alicia zorder 2
            "A medida que habla, Alicia relaja la postura y cierra los ojos, perdida en sus pensamientos."

            wlover "Luego te das cuenta de que la chispa de ese vínculo te ayuda a equilibrar tu mente y tu deseo."

            "Sus mejillas adquieren un suave tono rojizo y su sonrisa toma matices más tímidos."

            show alicia bashful at arcana_focused_alicia zorder 2
            wlover "Entonces empiezas a hacerte las preguntas correctas: ¿Qué deseas construir con tu amor? ¿Una vida feliz, grandes proyectos, un amor verdadero, tal vez?"

            wlover "El mundo se abre ante ti con posibilidades infinitas cuando finalmente forjas un vínculo."

            player "Ahora que lo planteas así, nunca lo había pensado de esa manera…"

            "Tu voz parece sacarla de sus pensamientos. Sus manos vuelven a peinar su cabello, ahora con más atención."

            show alicia blushing at arcana_focused_alicia zorder 2
            wlover "¡Oh! Lo lamento, [player_name]."

            show alicia ashamed at arcana_focused_alicia zorder 2
            wlover "Empecé a divagar."

            player "Lo noté. Descuida."

            player "Aunque lamento decirte que no me ha quedado muy claro este tema del vínculo."

            "Regina se endereza apenas en su trono, pero eso basta para dirigir tu atención hacia ella."

            show regina neutral at arcana_focused_regina zorder 3
            thequeen "Dime algo, [player_name]. ¿Sueles dejarte llevar por la inercia?"

            player "Yo, eh… supongo que podrías decir que sí."

            show alicia happy at arcana_focused_alicia zorder 2
            wlover "Oh, entonces lo explicaré de otra forma."

            "Alicia vuelve a observarte, esta vez levantando un dedo."

            wlover "Solei te empuja hacia la luz para que puedas brillar y ver la verdad."

            "Levanta otro dedo, ahora un poco más dudosa."

            wlover "Su hermano Chariot, por otro lado, suele ayudar a quienes necesitan salir de su zona de confort para encontrar nuevos horizontes."

            player "¿Solei? ¿Por qué él?"

            player "Quiero decir, entiendo que es una persona luminosa."

            player "Pero parece ser demasiado… Solei."

            wlover "Digamos que podría ayudarte… quizá como algo más que un amigo. ¿Lo entiendes?"

            player "No, la verdad no…"

            show alicia resigned at arcana_focused_alicia zorder 2
            show routa giggle at arcana_focused_routa zorder 1
            thewheel "En palabras simples, Solei podría ayudarte con algo que tengas que “solucionar” o “soltar”…"

            "Ante la mención de la palabra “soltar”, miras casi automáticamente a tus manos."

            player "((¿Soltar? ¿Cómo se supone que suelte algo si apenas recuerdo mi propio nombre?))"

            show alicia giggle at arcana_focused_alicia zorder 2
            wlover "O quizá solo [player_form('te vio guapo', 'te vio linda', 'pensó que eras su tipo')] y eso le llamó la atención."

            wlover "Yo veo cierto potencial…"

            player "Emmm…"

            player "((¿Que yo qué? ¡No, no, no, no!))"

            show alicia shocked at arcana_focused_alicia zorder 2
            wlover "¡No puede ser! ¡De verdad se sonrojó!"

        "Trabajar":

            player "Quiero trabajar."

            player "Solei ha hablado mucho de usted, mi reina."

            player "Dijo que le suele dar oportunidades a los forasteros como yo."

            show regina disappointed at arcana_focused_regina zorder 3
            thequeen "Lo hace sonar como si aceptara gente aquí constantemente…"

            "Por primera vez desde que entraste a la carpa, la voz de la reina suena apagada, agotada."

            show regina neutral at arcana_focused_regina zorder 3
            thequeen "Aunque supongo que debo reconocer que su intención siempre ha sido apoyar a este circo."

            "Ella se acerca a ti y toma tu mano con delicadeza. Sus dedos recorren tu palma mientras mantiene la mirada fija en ella."

            thequeen "Te guió hasta aquí… Mmm… ahora entiendo."

            "Su mano se cierra sobre tus dedos y los obliga a flexionarse contra tu palma hasta formar un puño."

            thequeen "Bien, notarás que tus manos ya no llevan las marcas del trabajo [player_form('al que estabas acostumbrado', 'al que estabas acostumbrada', 'que solías hacer')]."

            "Por mero impulso, llevas las manos detrás de la espalda."

            show regina happy at arcana_focused_regina zorder 3
            thequeen "Pero estoy segura de que cambiarás eso en poco tiempo."

            player "((Sus manos son cálidas como las de su hijo, y mucho más suaves…))"

            "Regina se aclara la garganta ante tu gesto de desconfianza y su mirada se suaviza un poco."

            show regina neutral at arcana_focused_regina zorder 3
            thequeen "¿Te sientes bien?"

            player "S-sí, discúlpeme, mi reina. Es que ha sido un día largo…"

            thequeen "Ya veo. [player_form('Pareces abrumado', 'Pareces abrumada', 'Parece que estás pensando en muchas cosas')]."

            thequeen "Pero no te preocupes, te daremos un espacio aquí en el circo. No es problema."

            player "¡¿De verdad?!"

            show regina happy at arcana_focused_regina zorder 3
            "Ella asiente suavemente con una sonrisa cálida."

            "Las manos de la reina vuelven a su postura habitual."

            show regina neutral at arcana_focused_regina zorder 3
            thequeen "Me gusta tu actitud. Solo te pediré que no causes problemas."

            player "Sí, perdón. Me da tranquilidad saber que tengo un lugar donde quedarme temporalmente."

            "Miras hacia la entrada de la carpa, por donde se cuelan los últimos rayos del sol."

            player "No me gusta mucho la noche."

            thequeen "Haces bien, la oscuridad en este pueblo es algo que hay que respetar."

            thequeen "Si se es descuidado al caminar o al tomar decisiones… Bueno, ese es otro tema que no necesitamos tratar hoy."

            player "((Primero los vínculos y ahora las decisiones. Las personas de aquí no parecen saber cómo dar una advertencia directa.))"

            show alicia happy at arcana_focused_alicia zorder 2
            wlover "¡Pero si es una cosita!"

            wlover "Muy bien."

            wlover "Puedes ponerle a trabajar con mi amorcito para que le eche una mano."

            show routa happy at arcana_focused_routa zorder 1
            thewheel "Sé [player_form('bienvenido', 'bienvenida', 'bienvenide')] al circo, pequeña alma. Espero que puedas disfrutar tu estadía aquí."

            player "Muchas gracias, lo haré."

    show regina neutral at arcana_focused_regina zorder 3
    thequeen "Muy bien visitante,ya con todo ya aclarado."

    thequeen "El esposo de Alicia; Homero, te ayudará a guiarte en los campos del circo y te explicara las reglas que debes seguir."

    "La mirada de Regina pasa por un  segundo hacia la entrada de la carpa."

    "Sus ojos se agudizan por un momento, luego suspira separando su vista de la entrada."

    thequeen "Ve con mi hijo, seguro que te está esperando."

    player "De acuerdo, muchas gracias."

    $ speaker_zorder_enabled = False
    $ speaker_zorder_group = {}
    $ current_group_speaker = None

    hide alicia
    hide regina
    hide routa
    scene bg circus night

    play music "audio/ms_ambience_circus.mp3" fadein 2.0

    "Al salir de la carpa, Solei se levanta de un barril cercano casi de un brinco, antes de acercarse a ti con una sonrisa"

    show solei casual neutral
    thesun "¿Y bien? ¿Cómo te fue?"

    "Te encoges de hombros ligeramente"

    player "No puedo quejarme, por la forma en que la describías pensé que sería mucho más aterradora."

    player "Pero al final solo hablamos un poco."

    show solei casual happy
    thesun "Bueno, ¡me alegro que haya ido bien!"

    thesun "¿Qué te dijeron?"

    player "Tu madre me dijo que debía buscar al esposo de Alicia, ¿Homero?"

    "Al mencionar a Homero sus cejas se levantan pero casi automáticamente una sonrisa relajada aparece en su rostro"

    player "Dijo que él podría enseñarme un poco más sobre todo… este tema de estar en el circo."

    "La sonrisa de Solei se ensancha aún más ante tus palabras. Antes de que lo notes, ya ha apoyado su mano en tu hombro."

    show solei casual proud
    thesun "¡Uy, uy! Hay tanto que te quiero mostrarte, podría mostrarte los terrenos o…"

    thesun "¿quieres ver mi acto? no, espera, podrás verlo mejor esta noche"

    thesun "¡Agh! no sé por dónde empezar."

    "Tomas la muñeca de él para apartarla con cuidado de tu hombro"

    player "No quiero distraerme ahora."

    thesun "¡Oh, lo siento! Tienes razón"

    thesun "Una disculpa, estoy contento de que vayas a quedarte conm…"

    show solei casual shocked
    thesun "¡Con nosotros!"

    show solei casual happy
    thesun "Jejeje, vamos entonces. Creo que sé donde podría estar."

    "Su mano vuelve a buscarte, aunque esta vez se posa en tu brazo y empieza a caminar hacia una carpa un poco más alejada."

    thesun "Homero es el que se encarga de preparar a los asistentes y los actos del circo."

    player "Pareces bastante informado. No pensé que realmente prestaras atención a la forma en que suceden las cosas por aquí."

    show solei casual pout blushing
    thesun "Oye, sé que no dí una primera buena impresión, pero realmente me interesa el circo."

    thesun "Incluso si mi madre y los demás tienden a pensar que soy… ¿Cómo decirlo?"

    #9-OPCIONES /opinión sobre Solei
    menu:
        "El consentido.":
            player "¿El consentido? Sí"

            player "Se nota que te aprecian bastante."

            show solei casual awkward
            "Solei se pasa una mano por el cuello una sola vez, y un pequeño sonrojo aparece en sus mejillas."

            thesun "Puedes decirlo de esa forma, supongo."

            show solei casual ashamed
            thesun "No es que quiera dar esa impresión, en serio. Simplemente me gusta ayudar a todos a estar felices, es todo."

            "Lo observas por un segundo, ese comentario acaba  de ser bastante autoconsciente."

            player "¿Quieres decir que sólo te nace y ya?"

            show solei casual happy
            thesun "Sí, me gusta la idea de ser parte de algo en la vida de los otros."

            "Su mirada se dirige al cielo, que empieza a tornarse del azul profundo de la noche."

            thesun "Lo que trato de decir en general, es que si alguna vez necesitas a alguien que solamente esté ahí, no dudes en buscarme, ¿Si?"

            player "Esa es una propuesta que sí puedo aceptar."

            show solei casual pout blushing
            player "Bien, lo tendré en cuenta."

            "Bromeas un poco con él, poniendo tu mano sobre su hombro de la misma forma en que él lo hizo hace unos momentos."

            player "Tal vez me anime a escucharte más."

            show solei casual happy
            "Solei suelta una pequeña risita"

            thesun "Eso suena lindo, [player_name]. Gracias"

        "El irresponsable.":
            player "¿El irresponsable? Sí, se nota que huyes de los problemas y de las responsabilidades."

            player "No llevo un día de conocerte y ya sé que es normal que te escapes."

            show solei casual awkward
            "Solei se pasa una mano por el cuello una sola vez, y un pequeño sonrojo aparece en sus mejillas."

            thesun "Puedes decirlo de esa forma, supongo."

            show solei casual ashamed
            thesun "No es que quiera dar esa impresión, en serio. Me gusta jugar y explorar, sí."

            thesun "Es solo que a veces pensar en tantas responsabilidades me angustia y siento que necesito un momento para poder ser yo mismo, es todo."

            player "Si sabes que no puedes simplemente huir de todo, ¿no?"

            show solei casual frozen
            thesun "Sí, lo entiendo. Es solo que a veces no siento que exista un límite entre las responsabilidades y quien realmente soy."

            thesun "Me… me preocupa."

            thesun "Puede que ya lo hayas notado, pero soy bastante sensible en general y no soporto la… ¿incomodidad? que siento cuando las dificultades aparecen de pronto."

            show solei casual awkward
            thesun "Me hace sentir inútil, como un “Fool” je…"

            "Lo observas por un segundo, ese comentario acaba  de ser bastante autoconsciente."

            player "Se me hace curioso que hagas comentarios como esos, considerando lo sociable que eres."

            show solei casual ashamed
            "Su mirada se dirige al cielo, que empieza a tornarse del azul profundo de la noche."

            thesun "Es algo que me avergüenza."

            "[player_form('No soy experto', 'No soy experta', 'No es que sepa mucho')], pero, si puedo darte una opinión… Creo que es normal sentirse así de vez en cuando."

            "Apoyas tu mano sobre el hombro de él, de la misma forma que lo hizo contigo hace unos momentos."

            show solei casual happy
            thesun "Me alegra escuchar eso, gracias"

    player "Ah, pero que quede claro que la próxima vez que sepa que vas a escaparte iré a avisarle a la reina."

    show solei casual pout angry
    thesun "¿Otra vez con eso?"

    show solei casual ashamed
    thesun "Parece que todos olvidan que soy un adulto."

    show solei casual happy
    thesun "En fin… ¡MUCHA CHARLA!"

    "Su mirada vuelve a fijarse en el cielo, luego a ti y de vuelta al cielo"

    show solei casual shocked
    thesun "¡Oh, ya está oscureciendo!"

    thesun "Rápido, [player_name]. Tenemos que enseñarte que hacer."

    "Sin esperar a tu respuesta, acelera el paso hacia la otra carpa."

    thesun "¡No perdamos el tiempo!"

    "Solei te guía con paso apurado, a tu lado pasan  varias personas, algunos cargando objetos como aros y telas, otros con cajas que lucen pesadas."

    "Todos parecen estar preparándose para abrir al público."

    "Finalmente, Solei se detiene frente a un hombre que esta ofreciendo instrucciones y guiando a varios miembros del circo."

    "En cuanto están lo suficientemente cerca para que los note, el hombre sonríe."

    show solei casual neutral at left
    with move

    show homero happy at right
    with move

    unknown "Bueno, miren quién apareció."

    "Su mirada vuelve a los integrantes del circo y da una última indicación antes de que se retiren."

    unknown "Muy buenas noches, Solecito. Oh, espera, no me digas."

    unknown "Regina volvió a regañarte"

    show solei casual ashamed
    thesun "¡Homey! ¿Si ya lo sabes porque lo dices?"

    mlover "Porque comparto el mismo sentido del humor que Chariot, me parece divertido ver que te atrapen"

    "La risa del hombre resuena desde su pecho, y hace que quieras reír tú también."

    player "((Ni siquiera fue una pregunta, ya sabe que lo regañaron. Increíble))"

    mlover "Además. Volviste a faltar a las prácticas, así que puedes considerarlo una pequeña venganza."

    show homero neutral
    "Sus manos se cruzan detrás de su espalda, y se inclina suavemente hacia él."

    mlover "Pero, imagino que si escapaste desde tan temprano es porque darás lo mejor hoy, ¿no es así?"

    show solei casual neutral
    thesun "No pasa nada, tengo el acto estudiado y practicado. Podría hacerlo hasta dormido"

    player "¿Eso significa que va a improvisar?"

    "Tu comentario arranca una nueva carcajada de Homero"

    show homero happy
    mlover "Eso suele ser algo frecuente en él, pero siempre se las arregla para hacer lo que quiere"

    "La postura de Homero vuelve a enderezarse."

    show homero neutral
    mlover "Pero hablando en serio, Solei."

    mlover "No quiero que la próxima vez tu madre decida castigarte tan en serio que acabes con Zoloto fuera de tus proyectos por un largo periodo."

    show solei casual ashamed
    thesun "No digas cosas como esas, Homey. Sabes que visitar Zoloto es el comienzo de mi día."

    "Él gira su cabeza hacia tí haciendo un puchero. Entonces sus ojos se fijan en ti."

    show solei casual happy
    thesun "¡Oh, es cierto! Vine a dejarte un nuevo aprendiz, alégrate Homey, tienes más manos para ayudarte a organizar."

    player "Hola, un placer. Soy [player_name]."

    show homero happy
    mlover "Un placer conocerte, nueva alma."

    mlover "Te doy la Bienvenida al Circo Golden"

    mlover "{i}Donde las estrellas descienden a la tierra y cada función se convierte en un recuerdo que llevarás contigo.{/i}"

    player "Que poético…"

    mlover "Jajaja, creeme lo sé."

    "Él desvía la mirada, pasándose la mano por el cabello. Despeinándolo ligeramente."

    show homero ashamed
    mlover "Mi hermosa esposa creó esa frase."

    mlover "Es toda una poeta."

    player "((Si, creo que suena a algo que diría Alicia… Se nota que la quiere mucho))"

    show homero neutral
    mlover "Solei, ve y termina de prepararte, yo me encargo a partir de aquí."

    show solei casual happy
    thesun "Claro, ¡Nos vemos, Homey!"

    "Sin darte tiempo de despedirte, Solei corre hacia una carpa, agitando su mano."

    show solei casual happy at solei_exit_left
    pause 1.1
    hide solei

    show homero neutral at center
    with move

    player "¿Homey? Perdona, pero ¿tu nombre no es “Homero”?"

    mlover "Sí, pero “Homey” es un apodo que me puso Solei cuando era más joven, y así me llaman todos."

    player "Oh, entiendo."

    mlover "Muy bien, [player_name], ¿necesitas que te aclare algo?"


label act_i_homerhelper:

    show homero neutral at right

    #10-Multiple-choice con Homero. Pueden hacerse una, dos o las tres preguntas. No es obligatorio responderlas todas.
    menu:
        "¿Cómo se trabaja?" if not homero_work_question_asked:
            $ homero_work_question_asked = True

            mlover "Es una excelente pregunta. Mmm…"

            "Homero se lleva una mano al mentón e inclina la cabeza."

            mlover "Fácil. No tendrás una tarea fija; dependerá de lo que necesiten los artistas o el circo mismo."

            mlover "Es posible que un día trabajes como vendedor de comida y, al siguiente, formes parte de la seguridad para evitar que las personas entren gratis al circo."

            mlover "Incluso puede que tengas que retirar el aserrín viejo para reemplazarlo por uno nuevo en la carpa."

            mlover "A menos que te destaques en algo particular, irás rotando entre posiciones a lo largo de tu estadía."

            mlover "Al final de la semana, Tenesis, nuestro tesorero, te pagará diez monedas de oro."

            mlover "Quiero ser bastante claro con esto: la colaboración y el sentido de comunidad son esenciales en Golden. Forman parte de las normas y del ambiente de este circo."

            mlover "Para que lo tengas presente."

            player "((Muy bien. Suena a que aquí podré descubrir mis talentos y aquello que se me da bien.))"

        "¿Servicios básicos?" if not homero_services_question_asked:
            $ homero_services_question_asked = True

            show homero shocked
            mlover "¿Quieres saber si tendrás un lugar donde comer y dormir?"

            show homero neutral
            mlover "Ah, no te preocupes."

            mlover "Aquí cubrimos todo, pero primero te pondremos a prueba y firmarás un contrato de exclusividad."

            mlover "El circo incluso te proporcionará una carpa para tu propia privacidad."

            player "Wow… Es una oferta muy buena. Pero ¿por qué la exclusividad?"

            mlover "Se trata de una forma de protección. No deseamos permitirle la entrada a cualquiera en estas tierras."

            "Homero señala hacia la carpa de la que salieron tú y Solei luego de hablar con su madre."

            mlover "Regina es bastante cuidadosa con eso."

            mlover "Como ya habrás notado, este circo también es el hogar de muchos de los que colaboran con nosotros."

            mlover "Regina, nuestra reina, no solo creó el circo. También es quien mantiene en marcha este pequeño y sencillo lugar."

            show homero happy
            mlover "Aunque yo suelo llamarla “La Emperatriz”. Le queda mejor."

            show homero neutral
            mlover "Y, por encima de todo, es quien más se preocupa por cada uno de nosotros."

            mlover "{i}“De nuestros shows obtenemos la recompensa por todo el esfuerzo que invertimos.”{/i}"

            player "Creo que ya había escuchado a Solei decir exactamente esa frase."

            show homero happy
            mlover "No me extraña que ya la hayas escuchado. Esa frase es nuestro mantra."

            show homero neutral
            mlover "Regina nos lo recuerda cada vez que tiene la oportunidad. Quiere decir que un pueblo unido podrá superar todas las adversidades."

            mlover "Por eso el circo intenta cuidar a quienes forman parte de él."

            mlover "Ella nutre nuestra abundancia. Por eso el circo aporta a los empleados y artistas comida, luz, agua, alojamiento…"

            mlover "Lo único que pedimos a cambio es compromiso. Un circo no puede levantarse día con día con gente distinta cada vez."

            mlover "Claro que los pocos elegidos son libres de irse si así lo desean. Nos gusta dejar esa decisión en sus manos."

            player "Espera, ¿“los pocos elegidos”?"

            player "¿Me estás diciendo que soy una especie de [player_form('privilegiado', 'privilegiada', 'privilegiade')]?"

            mlover "¡Bingo!"

            mlover "Los miembros del circo escogemos a quién traer aquí, por supuesto, asumiendo la responsabilidad de ello."

            show homero happy
            mlover "Sé que Solei puede parecer un muchacho revoltoso, pero es bastante consciente de a quién introduce en el circo."

            mlover "Créelo o no, Solei no va por ahí adoptando forasteros desamparados y trayéndolos a la carpa."

            "Su mirada se fija en la entrada del circo."

            show homero neutral
            mlover "Bueno… ahora que lo pienso, conmigo hizo exactamente eso. Él era bastante joven cuando me dio un nuevo comienzo en este lugar."

            mlover "Llegué sin saber nada, pero él y mi amada Alicia me ayudaron a encontrar mi lugar."

            mlover "Me tardé en adaptarme, pero nadie me recriminó mis errores. Con el tiempo, te das cuenta de que equivocarte forma parte del proceso de todos."

            mlover "Siempre que estés dispuesto a aprender, el circo va a tener espacio para ti."

            mlover "No es una oportunidad que aparece todos los días."

            "De pronto suelta una risa."

            show homero happy
            mlover "Lo menos que podemos hacer es estar agradecidos."

            mlover "Routa te diría que es momento de agradecer al universo por darte la oportunidad de estar aquí."

            player "Ya veo. Entonces… somos como los bufones de la corte. ¿Repartimos felicidad a los demás y, a la vez, celebramos al universo?"

            mlover "Estás entendiendo la vibra. Me caes bien."

        "¿Por qué un circo?" if not homero_circus_question_asked:
            $ homero_circus_question_asked = True

            show homero neutral
            mlover "Es una historia bastante larga. Tanto que hemos creado la pequeña “tradición” de contarla cada doce días."

            show homero shocked
            mlover "Ahora que lo pienso, justo hoy es ese día."

            show homero neutral
            mlover "Qué curioso… Parece que terminaste llegando en el momento perfecto."

            mlover "Por lo tanto, creo que me guardaré la historia para esta noche. No quisiera arruinarte la sorpresa."

            player "¿Hoy? Estás bromeando. Mi llegada no puede ser tan conveniente."

            "Homero se encoge de hombros."

            mlover "Hay veces en que uno llega sin planearlo y termina encontrando justo lo que necesitaba. Las casualidades son parte de la vida."

            mlover "Honestamente, creo que tienes muy buena suerte, [player_name]."

            player "Suerte, vínculos, destino… todos ustedes hablan de una forma muy mística."

            "Él niega con la cabeza."

            show homero happy
            mlover "Pues [player_form('bienvenido', 'bienvenida', 'bienvenide')]. Ya tendrás tiempo para descubrir por qué hablamos así."

            "Extiende sus manos a su alrededor. Pareciera querer englobar todo lo que los rodea."

            mlover "Todavía tienes mucho camino por recorrer como {i}“Fool”{/i}."

            player "((Okey, estoy [player_form('convencido', 'convencida', 'convencide')] de que puedo trabajar aquí.))"

            player "((Me gusta el ambiente, no voy a negarlo.))"

#9-OPCIONES/ligado a las opciones 8
label act_i_homerhelper_break:

    if homero_work_question_asked and homero_services_question_asked and homero_circus_question_asked:
        jump act_i_end

    mlover "¿Algo más?"

    menu:
        "Sí":
            jump act_i_homerhelper

        "No":
            jump act_i_end

label act_i_end:

    show homero happy
    mlover "Muy bien, [player_name]. Si no tienes más dudas, tengo que seguir trabajando, pero te dejaré esto. Vive la experiencia y disfruta la magia."

    "Homero saca de sus bolsillos un ticket dorado y te lo entrega."

    show gold_ticket at center

    player "Wow… Gracias, pero ¿por qué?"

    hide gold_ticket
    show homero neutral
    mlover "Sencillo: si vas a ser [player_form('uno de nosotros', 'una de nosotras', 'parte de nosotros')] en el futuro…"

    mlover "Si es que lo logras."

    mlover "Tienes que familiarizarte con el entorno, desde la forma en que lo preparamos hasta cómo interactúan los invitados con él durante la noche."

    mlover "Es, más que nada, para que te hagas una idea de lo que vendrá para ti. Así que ve. Sé libre por hoy. Nos vemos pronto."

    show gold_ticket at center
    "Al observar el boleto, notas que, incluso bajo la escasa luz del anochecer, emite un suave brillo."

    hide homero
    "Parece oro real, casi como si tus buenos modales acabaran de ser recompensados."

    hide gold_ticket
    "Al levantar la vista para agradecerle a Homero, descubres que ya no está ahí."

    "Una búsqueda rápida con la mirada te permite encontrarlo conversando con uno de los ayudantes que estaban con él antes de que llegaran tú y Solei."

    "En la entrada del circo, algunas personas ya empiezan a ingresar."

    player "((Supongo que puedo darme un paseo por el circo antes de entrar a la carpa.))"

    "No has dado más que unos cuantos pasos cuando escuchas el relincho de Girasol."

    "Al girarte para buscarla, logras verla a lo lejos, dejándose acariciar por una fila de niños que parecen sorprendentemente pacientes como para esperar su turno."

    "Un muchacho fornido, vestido a juego con los demás integrantes del circo, mantiene la atención del público para que todo se haga con las debidas precauciones."

    player "((¡Wow! Es increíble la cantidad de gente que está ingresando al circo.))"

    "Mientras caminas, notas que cada vez más gente empieza a ingresar y a congregarse alrededor de las distintas carpas."

    player "((“Familiarízate con el entorno”, dijo Homero. Quizá debería visitar todo el circo.))"

label act_i_circus_exploration:

    "¿Por dónde podría ir…?"

    #10-Opciones/conocer el circo
    menu:
        "Feria de artesanías" if not circus_crafts_visited:
            $ circus_crafts_visited = True
            scene bg circus night

            "El camino te lleva hasta una zona llena de pequeños puestos."

            "Algunos están decorados con telas coloridas, otros apenas tienen una mesa improvisada. Hay máscaras, figuras talladas, pequeñas piezas de cerámica y adornos hechos a mano."

            "Te detienes frente a uno de los puestos. Algunas piezas parecen haber sido hechas por los propios artistas del circo."

            player "((Supongo que no todo lo que hacen aquí ocurre sobre un escenario.))"

            player "((Me pregunto si alguno de los que conocí tiene otro talento además del acto circense.))"

            "Continúas caminando entre los puestos, observando los objetos y escuchando las conversaciones de quienes los atienden."

            jump act_i_circus_exploration_break

        "Carpas de comida" if not circus_food_visited:
            $ circus_food_visited = True
            scene bg circus night

            "El olor a comida recién preparada te guía hasta una zona llena de pequeños puestos. Hay mesas repartidas por los alrededores y varias personas comen mientras conversan entre ellas."

            "Algunos artistas se mueven entre la multitud, conversando y haciendo bromas ocasionales."

            player "((Ahora que lo pienso… ¿todos comen aquí?))"

            "Mientras observas el movimiento a tu alrededor, notas que nadie parece tener demasiada prisa. Algunos conversan con sus compañeros; otros simplemente disfrutan de su comida antes de regresar a sus labores."

            player "((Definitivamente parece más un pueblo que un circo.))"

            "Después de recorrer un poco la zona, decides continuar explorando."

            jump act_i_circus_exploration_break

        "Zona de animales" if not circus_animals_visited:
            $ circus_animals_visited = True
            call animal_selection_sequence

            "En el espacio destinado a los animales, te encuentras con una buena cantidad de criaturas: cabras, ovejas, un par de cerdos y varias jaulas grandes con distintos tipos de aves."

            "De repente, sientes algo pesado golpearte una pierna. El movimiento te desestabiliza antes de que puedas agarrarte de las vallas de los corrales."

            "Cuando reaccionas, encuentras sobre ti a un enorme pitbull adulto que parece demasiado emocionado de verte. Antes de darte cuenta, ya está lamiendo tu mejilla."

            play sound "audio/sfx_duke_bark.mp3"
            "La pesada cola del perro golpea tu pierna. Tratas de apartarlo suavemente, pero vuelve a lamerte, ahora con más insistencia."

            player "¡Wow, wow! Tranquilo, chico…"

            play sound "audio/sfx_calling_whistle.mp3"
            "Escuchas un silbido a lo lejos, y el perro se detiene casi inmediatamente. Intentas levantarte, y entonces una mano enguantada en negro se extiende frente a ti."

            unknown "Disculpa a Duke, por favor."

            show chariot circus masked neutral at chariot_first_encounter

            "Al levantar la vista, notas a un chico con máscara. Duke se sienta obedientemente a su lado. El sujeto acaricia la cabeza del animal con la otra mano, y este empieza a mover la cola."

            unknown "Le encanta conocer gente nueva y, a veces, no mide su fuerza."

            unknown "Déjame ayudarte a levantarte."

            "Antes de que puedas responder, te toma de la mano y te ayuda a ponerte de pie con cuidado. Parece asegurarse de que mantengas el equilibrio antes de soltarte."

            unknown "Te aseguro que lo siente."

            "El desconocido hace una pequeña indicación, y Duke levanta una de sus patas hacia ti como si se estuviera disculpando."

            "El gesto te provoca una pequeña sonrisa."

            player "¿Es tuyo?"

            "El desconocido asiente y, con un gesto amplio de la mano, señala todo el lugar."

            show chariot circus masked confident at chariot_first_encounter

            unknown "Él y todos los demás."

            "Notas a los otros visitantes interactuando con distintos perros de diferentes razas que rondan por el corral."

            player "Los tienes bien entrenados."

            "El desconocido rasca las orejas de Duke, y el perro ladra pidiendo más caricias."

            unknown "Es lo que pasa cuando te crías en una granja. Desde joven aprendes a moverte entre ellos."

            "El desconocido inclina la cabeza en una dirección, invitándote a seguirlo, y emprende rumbo hacia el fondo de la zona de los animales."

            "No vuelve la vista atrás. Camina con calma, como dando por hecho que terminarás alcanzándolo."

            "Al final de la zona, encuentras un pequeño establo con tres compartimentos."

            unknown "Aunque mis animales favoritos son los caballos. Lo supe desde el momento en que encontré un potrillo."

            "En los establos, dos caballos relinchan al verlos llegar. El primero en captar tu atención es un potro negro y fornido; su melena parece reflejar la luz de la luna con destellos azules. A su lado hay una yegua más delicada, blanca como la nieve y muy parecida a Girasol, aunque enseguida notas que no es ella."

            player "((¿Quizá Girasol sea su cría?))"

            "El hombre de la máscara abre el corral. Ambos caballos salen con un trote entusiasmado y lo rodean en círculos suaves, acortando la distancia mientras resoplan en busca del roce de sus manos."

            "La yegua es la primera en acercar el hocico lo suficiente para que él la acaricie."

            unknown "Jajaja, buena chica~"

            unknown "¿Te has portado bien?"

            play sound "audio/sfx_girasol_snort.mp3"
            "La yegua relincha en respuesta."

            unknown "Así me gusta, te daré una manzana después."

            "El potro negro relincha en protesta, el desconocido ríe y lo acaricia, parece que te ha olvidado por un momento, pero no te molesta."

            "La escena parece entrañable, incluso tienes la tentación de acariciarlos tú también, pero sabes que probablemente debas pedir permiso, y no quieres interrumpir."

            play sound "audio/sfx_horse-galloping-2.mp3" volume 0.6
            "Desde detrás de los corrales, Girasol aparece y, al ver al desconocido, galopa hacia él. Una vez lo suficientemente cerca, posa la mirada en ti. Parece recordarte."

            "Se acerca a ti con lentitud. El desconocido y los demás caballos vuelven la mirada hacia ti. Extiendes la mano hacia la yegua, pero vacilas antes de tocarla."

            player "¿Supongo que no hay problema si ya te conozco…?"

            "Le murmuras a la potra. La risa del desconocido te hace observarlo de vuelta."

            unknown "Bueno, algo es algo. El primer avance con un animal es conocerlo."

            unknown "Ah… Así que tú eres la nueva alma que encontró mi hermano."

            "Tu mano se queda congelada a medio camino del cuello de Girasol."

            player "¿Solei? ¿Tu hermano?"

            unknown "Correcto, [player_form('pequeño lucero', 'pequeña estrella', 'pequeña luz')]. Me presento."

            thechariot "Soy Chariot, domador e instructor de animales."

            thechariot "“Hermano mayor de Solei” a tiempo completo."

            "Su mano se extiende hacia ti."

            player "Un placer, Chariot. Mi nombre es [player_name]."

            "Al responder a su saludo, sus dedos se cierran sobre tu mano con delicadeza."

            thechariot "¿[player_name]? Lindo nombre; te sienta bien."

            thechariot "Espero que disfrutes de tu primera noche en el circo."

            "Su mano guía la tuya hacia uno de sus caballos y te permite acariciarlo."

            thechariot "Noté que los estabas viendo, descuida. Puedes acariciarlos."

            "Al apoyar tu mano sobre el caballo, empieza a escarbar suavemente en el suelo con la punta de su casco."

            "Sonríes al notar que la yegua también se acerca a ti ahora que el caballo parece confiar en ti."

            "De pronto, la voz de Chariot llama tu atención."

            thechariot "Lo siento, ya debo irme a preparar para el show."

            thechariot "Puedes quedarte un rato más con ellos si quieres, pero no olvides que la función empezará pronto."

            "Sin decirte mucho más, gira sobre sus talones y se va."

            hide chariot

            "Tras un rato más acariciando a los caballos, te vas de vuelta a la zona central del circo."

            jump act_i_circus_exploration_break

label act_i_circus_exploration_break:

    if circus_crafts_visited and circus_food_visited and circus_animals_visited:
        jump act_i_after_circus_exploration

    player "((¿Quiero visitar algún otro lugar antes de continuar?))"

    menu:
        "Sí":
            jump act_i_circus_exploration

        "No":
            jump act_i_after_circus_exploration

label act_i_after_circus_exploration:

    "Continúas explorando las atracciones y el pequeño mercado de artesanías, tratando de anotar mentalmente las posibles tareas que tendrás que hacer a partir de mañana."

    "Por un momento te detienes en medio del camino solo para inhalar el aire fresco de la noche."

    "Cuando despertaste bajo aquel árbol esa mañana, no habrías imaginado que acabarías en un circo al caer la noche."

    "Mientras observas el entorno, escuchas unos pasos detrás de ti."
    play sound "audio/sfx_horror_string.mp3"
    show solei circus masked nervous at solei_scare
    with vpunch
    pause 0.20
    hide solei
    show solei circus masked nervous
    "Al girarte, te encuentras con Solei, que lleva una máscara de sol."

    player "¡Ah! Cómo te gusta aparecer así de la nada, ¿no?"

    "Te llevas una mano al pecho por un momento. Solei se retira la máscara con una mano."

    player "Casi me da algo…"

    show solei circus ashamed
    thesun "Je, je… Perdón. No pensé que fuera a asustarte tanto."

    thesun "Pero cuando te vi paseando, me ganó la curiosidad."

    show solei circus neutral
    thesun "¿De qué hablaste con Homero?"

    thesun "¿Te dijo algo interesante?"

    player "Nada relevante."

    player "Más que nada, contestó mis preguntas y hablamos del circo en general."

    show solei circus happy
    thesun "Bien. Ya no te sientes como pez fuera del agua, ¿no?"

    player "Supongo que se puede decir que no estoy tan [player_form('desorientado', 'desorientada', 'desorientade')] como esta mañana, pero aún me estoy adaptando."

    thesun "Eso es bueno. Sé que podrás adaptarte. Creo que hice bien en traerte."

    "En ese momento, recuerdas las palabras de Homero: “Solei no va por ahí adoptando forasteros desamparados”."

    player "…"

    player "¿Por qué lo hiciste?"

    "Él inclina levemente la cabeza."

    thesun "¿Hacer qué?"

    player "Traerme aquí. ¿Qué te hizo creer que sería una buena idea?"

    "Solei observa la máscara entre sus manos y la acaricia con suavidad, haciendo tiempo para organizar sus palabras."

    show solei circus ashamed
    thesun "Bueno… solo seguí mi intuición."

    player "¿Realmente eso es todo?"

    "Él abre la boca para responderte, pero justo en ese momento la voz de Homero resuena por todo el circo."

    mlover "Damas y caballeros, el show principal de la noche está a punto de iniciar. Por favor, diríjanse a la carpa principal."

    "Solei suspira e intenta ponerse la máscara, pero se detiene a medio movimiento antes de observarte."

    thesun "[player_name], sé que todavía tienes muchas dudas y prometo responderlas todas, ¿sí?"

    thesun "Solo… no ahora."

    "No sabes si creerle. Él lo nota y se apresura a hablar de nuevo."

    show solei circus neutral
    thesun "Después del show, te explicaré todo. ¿Qué opinas?"

    "No te da tiempo de responder. Solei ya está corriendo hacia la carpa principal mientras vuelve a colocarse la máscara."

    show solei circus masked neutral
    thesun "¡Te veré después del show! ¿Okey?"

    "Intentas seguirle el paso, pero él ya se ha desvanecido entre la multitud. Solo te queda observar cómo la fila comienza a formarse frente a la entrada de la carpa."

    hide solei
    player "((Después del show…))"

    "Te unes a la fila de visitantes y esperas con paciencia tu turno para cruzar el umbral de la gran carpa."

    scene bg circus show
    "En la entrada, un miembro del circo corta tu boleto y te indica una hilera de asientos cerca del escenario. El aroma de las palomitas y los murmullos del público llenan la carpa."

    "Al sentarte, notas a varios niños que corean el nombre de Solei. Algunos sostienen girasoles en su honor y los agitan como si fueran pompones."

    player "((Solei tiene muchos fans. Bueno… no puedo juzgarlos, se hace querer.))"

    "De pronto, las luces se apagan y un único foco ilumina el centro del escenario. Allí, de pie, Homero ya está esperando."

    call screen circus_show_selection(first_show=True)

    if _return == "homero":
        call homero_circus_presentation
        $ homero_presentation_seen = True

    while not (solei_show_seen and routa_show_seen and alicia_show_seen and chariot_show_seen):

        call screen circus_show_selection

        if _return == "solei":
            call solei_circus_presentation
            $ solei_show_seen = True

        elif _return == "chariot":
            call chariot_circus_presentation
            $ chariot_show_seen = True

        elif _return == "routa":
            call routa_circus_presentation
            $ routa_show_seen = True

        elif _return == "alicia":
            call alicia_circus_presentation
            $ alicia_show_seen = True

        play music "audio/ms_circus_intro.mp3" fadeout 1.0 fadein 1.0

    call screen circus_show_selection(first_show=True)

    if _return == "homero":
        call final_show

    play music "audio/ms_ambience_circus.mp3" fadein 1.0
    scene bg circus show
    with fade

    "Te quedas en silencio mientras el público se levanta y aplaude, de alguna forma sentiste que el acto no solo era una forma en que se presentaba el circo."

    "Sino que también de cierta forma te estaban dando la bienvenida al circo Golden."

    "La calidez del lugar parece haberse asentado en tu pecho."

    player "((este mundo… ¿tiene tanto que ofrecer?))"

    "Te quedas tan metido en tus pensamientos que no notas cómo el público se va de las bancas. Hasta que al mirar alrededor notas que eres la última persona en salir."

    "Justo cuando te levantas, escuchas la voz de Solei llamarte y acercarse a tí a toda prisa pasando por en medio del escenario."

    show solei circus masked neutral
    thesun "¡[player_name]! ¿Qué te pareció?"

    player "Yo…"

    #11-Opciones / reacción al show
    menu:
        "¡Lo amé!":
            player "¡Me encantó, Solei!"

            show solei circus masked confident
            player "¡Todos estuvieron tan geniales!"
            player "Es increíble el nivel de producción que tienen"

            thesun "Jeje, eso es gracias a Homey y las increíbles ideas de Alicia..."
            thesun "¡Juntos son un gran equipo!"
            thesun "Se inspiran mutuamente..."
            thesun "Creo que eso hace nuestros shows tan especiales"

        "No sé como describirlo":
            player "Son tantas cosas que no sé por dónde empezar, me quede con la boca abierta"

            show solei circus masked confident
            "Miras a los lados, y notas que no queda nadie más dentro del recinto"

            player "Como que ya se fueron todos de la carpa"

            player "¿seguro que está bien quedarnos hablando a esta hora?"

            show solei circus masked nervous
            thesun "Descuida, es muy común que algunos se queden un rato pensando la primera vez que ven el show"

            show solei circus masked neutral
            thesun "¿Te imaginas ser parte de esto?"

        "...":
            player "..."

            thesun "..."

            show solei circus masked guarded
            player "..."

            show solei circus masked nervous
            thesun "..."

            player "..."

            show solei circus masked confident
            thesun "¡Hola, holaaaaa! Tierra llamando a girasol. Creo que te impresionó todo lo que viste, ¿no?"

            player "No voy a mentirte: después de tanta magia y tantos colores... es difícil no tomarse un tiempo para pensar."

    thesun "Siempre hay una primera vez para todo..."

    "Solei se retira la máscara lentamente."

    show solei circus happy
    thesun "Pero, por ahora, te pediré que nos retiremos."

    thesun "Tengo que mostrarte tu nuevo hogar."

    player "Ah… ¿hablaste con Homey?"

    thesun "Sí, sí. Hablé con él antes de que se marchara a encargarse del cierre. Ya sabes, es un maestro de ceremonias muy comprometido."

    thesun "Me pidió que te llevara a tu carpa para que pudieras pasar la noche y descansar."

    thesun "Él se queda hasta tarde cuando terminan los shows y no quería que tuvieras que esperarlo."

    player "Se nota que le gusta tener todo preparado."

    thesun "Siempre tenemos carpitas extra para este tipo de situaciones o para dar una mano amiga. Homey siempre es así de aplicado, al igual que mi madre. Pero bueno... ¡vamos!"

    play music "audio/ms_ambience_circus_night.mp3" fadein 1.0
    scene bg circus night
    show solei circus neutral
    "Sales de la carpa junto a él y notas cómo el circo va cerrando sus puertas."

    "Solei te guía por un pequeño sendero hasta una zona donde los trabajadores charlan y se despiden antes de irse a dormir."

    "Finalmente, te indica una carpa casi al fondo."

    thesun "¡Esta es toda tuya, [player_name]! Puedes personalizarla como quieras cuando empieces a ganar tu propio dinero."

    thesun "Aquí tienes una cama y espacio para guardar tus cosas; incluso puedes cambiarte de ropa."

    thesun "Hay tantas cosas que quiero enseñarte."

    thesun "Ven, ven. Vas a ver que es mucho mejor por dentro."

    "Solei aparta la entrada de la carpa y te hace una seña para que pases."

    "El interior está casi a oscuras y apenas puedes distinguir lo que te rodea."

    scene bg sun tent
    stop music
    show solei circus neutral
    thesun "Ten cuidado, no quisiera que te cayeras."

    "Una vez en el centro de la carpa, te giras hacia Solei y cruzas los brazos."

    show solei circus shocked
    thesun "¿[player_name]...?"

    player "Espera, dijiste que me responderías por qué me trajiste al circo después del show, ¿no?"

    show solei circus ashamed
    player "Bueno, el show ya terminó y quiero saberlo... ¿Por qué me trajiste aquí?"

    thesun "No sé."

    player "¿Cómo no vas a...?"

    "Antes de que continúes, Solei levanta una mano y espera a que lo dejes terminar."

    thesun "No sé cómo explicarlo. Pensé que quizá Routa tenía razón y que, a veces, los cambios son inevitables."

    thesun "Cuando te vi, captaste mi atención. Fue como si ya te conociera... como si te hubiera visto en algún sueño."

    thesun "Lo noté cuando casi… te piso con Girasol."

    player "Eso me parece bastante ambiguo. Digo..."

    player "¿Pasar casi por encima de mí con Girasol es una buena señal?"

    show solei circus shocked
    thesun "No quise decir eso. Lo que trato de decir es..."

    show solei circus ashamed
    thesun "Conocerte se sintió como algo que debía pasar."

    show solei circus neutral
    thesun "En la filosofía de este circo, todos creen que lo que nos sucede ocurre por una razón. Homey lo llama suerte; Routa habla de coincidencias y destino..."

    thesun "Solo sé que, cuando te vi, noté algo diferente en ti. Tu aura era distinta."

    thesun "Y pensé que, si había un lugar adecuado para ti, era el circo."

    player "¿Y qué tengo yo de especial…?"

    thesun "¡Pues eres [player_form('único', 'única', 'únique')]! No hay nadie como tú aquí."

    thesun "Estoy seguro de que ha pasado mucho tiempo desde que alguien como tú llegó a estas tierras."

    player "Ni siquiera sé quién soy, Solei."

    player "¿Cómo esperas que crea que en mí hay algo especial?"

    thesun "Probablemente todavía no lo ves, pero lo harás. Estoy seguro."

    thesun "Déjame acompañarte mientras encuentras tu lugar aquí. Puedo escucharte y ayudarte si me lo permites."

    play music "audio/ms_ending.mp3" fadein 2.0

    #10-OPCIONES
    menu:
        "Aceptar su compañía":
            player "Eso… suena bastante íntimo viniendo de ti."

            player "Pero no puedo negar que, de no haberte encontrado, es posible que todavía estuviera dando vueltas en el campo de girasoles."

            player "No sé si podrías ser mi guía, pero supongo que, al menos, podrías ser un buen guía turístico."

            thesun "Ya te lo dije: en Limfool es difícil no perderte si no te conoces [player_form('a ti mismo', 'a ti misma', 'a ti misme')]. Apenas es tu primer día; tómalo con calma."

            "Al escucharlo, no puedes evitar soltar una pequeña risita."

            player "Tu madre y sus amigas me dijeron lo mismo esta tarde."

            show solei circus happy
            thesun "Bueno, quizá así me creas cuando digo que paso más tiempo aquí que escapándome a Zoloto."

            player "Tengo mis dudas..."

            thesun "Ay, vamos. Tú tuviste la oportunidad de nacer de nuevo, ¿y yo no?"

            player "¿Nacer de nuevo?"

            thesun "Cuando despertaste bajo el árbol. ¿No te sentiste como si volvieras a nacer?"

            player "Ahora que lo dices... sí."

            player "Como si hubiera nacido [player_form('limpio', 'limpia', 'limpie')], sin ataduras, lanzándome desde el borde de un acantilado con fe y sin miedo a caer."

            thesun "¿Ya lo ves? Es parte de cómo funciona este mundo: siempre volvemos a empezar."

            player "((No sé por qué me siento… ¿[player_form('conmovido', 'conmovida', 'conmovide')]? Es como si llevara menos peso sobre la espalda.))"

            "No lo habías notado hasta ahora, pero el cabello de Solei ondea en el interior de la carpa, aunque no hay brisa."

            player "Y-yo… No recuerdo ni lo que fui antes."

            "Sientes cómo te tiemblan las manos. Al notarlo, Solei abre un poco los brazos, pero permanece donde está. Su sonrisa es un tanto tímida."

            show solei circus neutral
            thesun "No sé quién fuiste ni qué tuviste que soportar. Pero no tienes que recordarlo todo esta noche."

            thesun "Si quieres que me quede contigo mientras lo descubres, puedo hacerlo."

            "Las lágrimas terminan por nublarte la vista. Tras un instante de duda, eres tú quien cierra la distancia y acepta el abrazo de Solei, aprovechando para esconder el rostro y dejar que las lágrimas fluyan."

            hide solei
            scene bg the sun hug
            with fade

            "En cuanto lo abrazas, notas, incluso con los ojos cerrados, una luz que te rodea."

            "Permaneces entre sus brazos durante un momento, hasta que finalmente se aparta y te observa con una sonrisa."

            "Tú aprovechas para limpiarte el rostro."

            scene bg sun tent
            with fade
            show solei circus neutral
            thesun "¿Mejor?"

            player "Un poco."

            show solei circus happy
            thesun "Bien, me alegra oír eso."

            "Solei da un pequeño bostezo."

            thesun "Bueno, creo que ya hemos tenido suficientes emociones por hoy."

            thesun "Así que... Buenas noches, querido girasol. El Sol saldrá mañana para que vayas hacia la luz."

            "Mientras sale de la carpa, Solei agita una mano para despedirse."

            hide solei
            with fade
            player "((Puede que quedarme en este circo no sea tan malo...))"

        "Negar":

            "Escucharlo decir cosas tan profundas te provoca cierto nerviosismo. Involuntariamente, empiezas a reírte."

            show solei circus shocked
            "Solei te observa en silencio. Probablemente no se esperaba esa reacción."

            player "¡¿Cómo puedes decirme eso?! Apenas te conozco, no sé ni quién eres en realidad."

            player "¡Ni siquiera sé quién soy [player_form('yo mismo', 'yo misma', 'yo')]!"

            show solei circus neutral
            thesun "Se nota que quieres la verdad. Bueno, estás en tu derecho."

            "Solei da un paso hacia atrás para darte algo de espacio. Su mirada, sin embargo, refleja una mezcla de incomodidad y preocupación."

            player "No, no, no. Yo no tengo nada de especial, esto es ridículo."

            player "Este sitio es ridículo..."

            "Sientes que las lágrimas amenazan con brotar de tus ojos, pero te limpias el rostro con el dorso de la mano antes de que tengan la oportunidad de desbordarse."

            show solei circus ashamed
            thesun "¿Cuánto te han lastimado...?"

            "Solei extiende una mano hacia ti, pero, a medio camino, él mismo se sujeta la muñeca y se obliga a bajar el brazo."

            player "No te atrevas, Solei. No te atrevas a mirarme como un animal herido al que tienes que ayudar."

            player "No sé quién te crees que eres, pero..."

            thesun "Soy el Sol."

            player "¿Disculpa?"

            thesun "Soy el Sol."

            "Esta vez, su afirmación suena más convencida."

            thesun "Es lo que hago: iluminar a las personas, incluso a quienes no quieren ver la luz; a quienes están demasiado ocupados intentando sobrevivir..."

            show solei circus shocked
            player "¿Qué vas a saber tú de sobrevivir?"

            player "Tienes una vida resuelta, gente que te aprecia, una madre que se nota que te ama y se preocupa por ti. Estás acostumbrado a que la vida se te resuelva con un simple chasquido y una orden."

            thesun "Que yo tenga la luz y la suerte de poder elegir no significa que..."

            player "Solei, no quiero hablar más de esto."

            show solei circus ashamed
            thesun "Solo digo que veo potencial en ti, y..."

            player "Solei."

            "Solei no intenta acercarse de nuevo. Solo entonces dejas caer un poco los hombros."

            thesun "..."

            show solei circus neutral
            thesun "Entiendo."

            "Solei empieza a caminar hacia la salida de la carpa. Pero, antes de marcharse, vuelve la mirada una última vez."

            thesun "Si mañana quieres hablar... estaré aquí."

            "Finalmente, Solei sale de la carpa."

            hide solei
            with fade

    "Una vez sin compañía, no dudas en tumbarte sobre la cama."

    "Sorprendentemente, es mucho más cómoda de lo que parece."

    "Abrazas la almohada y se te escapa un bostezo. Ha sido un día pesado, después de todo."

    "Tus párpados caen lentamente y dejas escapar un último suspiro antes de sumirte en un sueño profundo."

    scene bg black
    with fade

label act_i_cliffhanger:
    # Finaliza el juego:
    # scene bg end demo
    # with fade

    thesun "¡Hola…! Sé que no nos conocemos, pero, si estás aquí, créeme que la vida nos juntó…"

    thesun "El Sol se está ocultando, pero no será la última vez que nos veamos. Solo es el comienzo del giro de nuestro destino."
    thesun "Buenas noches, mi girasol."

    "FIN DE LA ALPHA."

    "GRACIAS POR JUGAR."

    return
