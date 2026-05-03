define m = Character("You")

default read_notes = False
default read_monologue = False
default gave_resume = False

default stress = 0
default skill = 0
default reputation = 0
default passion = 5
default role = "none"
label start:
    scene room

    "Your room. Audition day is tommorow."

menu:
    "Do you check your audition notes?":

    "Yes": 
        $ read_notes = True
    "Your review the notes carefully."

    "No":
        "You decide to wing it."

menu:
    "Do you review your monologue?":

    "Yes": 
        $ read_monologue = True
    "You read and reahearse your monologue."

    "No":
        "You think you got it memorized just fine."

"You fall asleep..."

jump morning

label morning:
    scene black
    "Your alarm rings."


menu:
    "What do you do?":
        "Get up":
            "You drag yourself out of bed and get ready for the audition."
            jump audition 

        "Ignore it":
            jump lose_alarm

label lose_alarm:

    scene black

    "You fall back asleep."

    "You miss your audition."

    "Sometimes, the biggest opportunities slip away quietly."

    return


label audition:
    scene stage
    "You step onto the stage."

    if read_monologue:
        "The lines come naturally."
        jump good_monologue
    else:
        jump bad_monologue
    
    label bad_monologue: 
    "You stumble over your lines."
    "The panel looks unimpressed."
    jump after_audition 
    label good_monologue:

    "You deliver your monologue perfectly."
    "The room is silent when you finish."

    jump after_audition

    label after_audition:

    menu:
        "Do you leave immediately?":

            "Yes":
                "You walk out, unsure how it went."
                jump results

            "No":
            "You linger."

                if read_notes:
                    "You remember something from your notes..."
                    jump give_resume
                else:
                    "You feel like you're forgetting something."
                    jump results
                    label give_resume:

    menu:
        "Give your resume to the staff?":

            "Yes":
                $ gave_resume = True
                "You hand over your resume confidently."

            "No":
                "You hesitate and walk away."

    jump results












    label results:
    scene room

    "Later that night..."
    "You check your phone."

    if gave_resume:
        "You got the lead role!!!"
        $ role = "lead"
        

    else:
        menu:
            "You didn't stand out too much...":


        "Accept background role":
            $ role = "background"
         
        "Join stage crew instead":
                    $ role = "crew"

    jump rehearsal_day_1



        label lead_path
        "You got the role youve always wanted!"
        "But can you face the pressure?"

       