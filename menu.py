from autre.utils import *
from Class.Menu import Menu

pg.init()
fenetre = pg.display.set_mode(RESOLUTION.size)


def quitter():
    pg.quit()
    quit()


def page_choix_theme(_fenetre, theme_defaut: str) -> Menu:
    theme_choisi = theme_defaut

    def themes(theme: tuple):
        global theme_choisi
        fond = pg.Surface(RESOLUTION.size)
        fond.blit(
            pg.image.load(
                "{}/fond.png".format(ACCES_TERRAINS.format(theme[1]))
            ).convert_alpha(),
            (0, 0),
        )

        _fenetre.blit(fond, (0, 0))
        pg.display.flip()

        _menu.ajout_texte(
            None,
            (190, 190, 70),
            "Choix du theme :",
            (RESOLUTION.size[0] // 2, RESOLUTION.size[1] // 2 - 200),
        )
        _menu.ajout_bouton(
            (50, 220, 60),
            (255, 255, 255),
            "Suivant",
            (RESOLUTION.size[0] // 2, RESOLUTION.size[1] // 2 + 150),
            selection_niveau,
            identifiant="start",
        )

        theme_choisi = theme[1]

    def selection_niveau():
        return page_choix_niveau(_fenetre, theme_choisi)

    _menu = Menu(_fenetre, couleur_fond=(105, 105, 105))
    themes((theme_defaut, theme_defaut))

    _menu.ajout_bouton(
        _menu.couleur_fond,
        (255, 255, 255),
        "",
        (RESOLUTION.size[0] // 2, RESOLUTION.size[1] // 2),
        themes,
        type_bouton="select",
        options=[
            ("Bob l'eponge", "bob"),
            ("Mario", "mario"),
            ("Pokemon", "pokemon"),
            ("Star Wars", "star_wars"),
        ],
        identifiant="theme",
    )

    return _menu


def page_choix_niveau(_fenetre, theme: str) -> Menu:
    niveau_choisi = 1

    def niveau(id_niveau: tuple):
        global niveau_choisi

        fond = pg.Surface(RESOLUTION.size)
        fond.blit(
            pg.image.load(
                "{}/{}/rendu.png".format(ACCES_TERRAINS.format(theme), id_niveau[1])
            ).convert_alpha(),
            (0, 0),
        )

        _fenetre.blit(fond, (0, 0))
        pg.display.flip()

        _menu.ajout_texte(
            None,
            (190, 190, 70),
            "Choix du niveau :",
            (RESOLUTION.size[0] // 2, RESOLUTION.size[1] // 2 - 200),
        )
        _menu.ajout_bouton(
            (50, 220, 60),
            (255, 255, 255),
            "Joueur",
            (RESOLUTION.size[0] // 2, RESOLUTION.size[1] // 2 + 150),
            lancer,
            identifiant="start",
        )

        niveau_choisi = id_niveau[1]

    def lancer():
        from main import main

        try:
            main(theme, niveau_choisi)
        except KeyboardInterrupt:
            pg.quit()
            quit()
        except Exception as e:
            crash(fenetre, e)

    _menu = Menu(_fenetre, couleur_fond=(105, 105, 105))
    niveau(("1", "1"))

    _menu.ajout_bouton(
        _menu.couleur_fond,
        (255, 255, 255),
        "",
        (RESOLUTION.size[0] // 2, RESOLUTION.size[1] // 2),
        niveau,
        type_bouton="select",
        options=[
            ("1", "1"),
            ("2", "2"),
        ],
        identifiant="niveau",
    )

    return _menu


def page_accueil(_fenetre) -> Menu:
    def start():
        return page_choix_theme(_fenetre, "bob")

    fond = pg.Surface(RESOLUTION.size)
    _fenetre.blit(fond, (0, 0))
    pg.display.flip()

    _menu = Menu(_fenetre, couleur_fond=(155, 155, 255))

    _menu.ajout_texte(
        _menu.couleur_fond,
        (190, 190, 70),
        "Sourcecodester",
        (RESOLUTION.size[0] // 2, RESOLUTION.size[1] // 2 - 200),
    )

    _menu.ajout_bouton(
        _menu.couleur_fond,
        (255, 255, 255),
        "START",
        (RESOLUTION.size[0] // 2, RESOLUTION.size[1] // 2 - 17),
        start,
        identifiant="start",
    )
    _menu.ajout_bouton(
        _menu.couleur_fond,
        (0, 0, 0),
        "QUIT",
        (RESOLUTION.size[0] // 2, RESOLUTION.size[1] // 2 + 17),
        quitter,
        identifiant="quit",
    )

    return _menu


if __name__ == "__main__":
    clock = pg.time.Clock()
    menu = page_accueil(fenetre)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                pg.quit()
                quit()

        action = menu.bouton_press()

        if action is not None and action[0] != 0:
            if isinstance(action[2], Menu):
                menu = action[2]

        clock.tick(20)
