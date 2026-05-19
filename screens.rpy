screen main_menu():

    tag menu

    add "menu_bg"

    frame:
        background None
        xalign 0.08
        yalign 0.5





        vbox:
            spacing 20
            textbutton "Start" action Start()
            textbutton "Load" action ShowMenu("load")
            textbutton "Preferences" action ShowMenu("preferences")
            textbutton "Quit" action Quit(confirm=True)
            

