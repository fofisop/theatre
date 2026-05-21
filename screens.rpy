screen main_menu():

    tag menu

    add "menu_bg"

    frame:
        background "#000000"
        xalign 0.08
        yalign 0.5

        vbox:
            spacing 20

            textbutton "Start" action Start()
            textbutton "Load" action ShowMenu("load")
            textbutton "Preferences" action ShowMenu("preferences")
            textbutton "Quit" action Quit(confirm=True)


screen choice(items):

    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        for i in items:
            textbutton i.caption action i.action
screen main_menu():

    tag menu

    add "menu_bg"

    frame:
        scene stage
        xalign 0.08
        yalign 0.5
        vbox: spacing 20
        text "Will you survive the show?" size 60
        textbutton "Start" action Start()
            textbutton "Load" action ShowMenu("load")
            textbutton "Preferences" action ShowMenu("preferences")
            textbutton "Quit" action Quit(confirm=True)
