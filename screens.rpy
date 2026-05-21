screen main_menu():

    tag menu
    frame:
        align (0.5, 0.5)

        vbox:
            spacing 20
            text "Will you survive the show?"
            textbutton "Start" action Start()
            textbutton "Load" action ShowMenu("load")
            textbutton "Preferences" action ShowMenu("preferences")
            textbutton "Quit" action Quit(confirm=True)

style choice_button_text:
    xalign 0.5
    text_align 0.5

screen choice(items):


    style_prefix "choice"
    window:
        background "#00000088"
        xalign 0.5
        yalign 0.5
        padding (30, 20)

        has vbox
        spacing 20

        for i in items:
            textbutton i.caption action i.action
   
