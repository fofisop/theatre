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

    default day = 1

label rehearsal_loop:

if day > max_days:
        jump final_outcome
scene rehearsal
"Day [day] of rehearsals."
if role == "lead":
        call lead_rehearsal_day
    elif role == "background":
        call background_rehearsal_day
    else:
        call crew_rehearsal_day
    $ day += 1
    jump rehearsal_loop









    label lead_rehearsal_day:
    if day == 1:
        "You step into rehearsal. The director eyes you carefully."
        "She hands you the script."
        "You are asked to do a cold read."
        menu:
            "How do you respond?":
                "Give it everything":
                    "You throw yourself into the role, despite the fact that it's just a cold read."
                    $ skill += 2
                    $ stress += 1
                "Play it safe":
                    "You keep it controlled."
                    $ skill += 1

                    "Ask for direction":
                    "You pause. 'Any notes before I start?'"
                    $ reputation += 2

                    elif day == 2:
                        "You are enjoying yourself..."
                        "But starting to feel the pressure."
                        "You mess up a line mid scene."
                        menu:
                            "What do you do?":
                                "Keep going":
                    "You recover quickly, and continue the scene."
                    $ skill += 2
                    $ reputation += 1
                "Apologize":
                    "You stop and reset."
                    $ stress += 1

                    "Laugh it off":
                    "Some people smile. The director doesn't."

                    $ reputation -= 1


    elif day == 3:

        "The director starts pushing you harder."
        "They tell you that you aren't doing enough."
        "You feel like you just started memorising the script, and now they exepct you to know it by heart?"
        menu:
            "How do you react?":

                "Push yourself harder":
                    $ skill += 2
                    $ stress += 2

                "Internalize it":
                    $ passion -= 2
                    $ stress += 1

                    "Push back slightly":
                    $ reputation += 1
                    $ stress += 1


                    elif day == 4:
                        "You're doing well, but the exastion is overwhelming."
                        "The fact that everyone can tell stresses you out even more."
                        menu:
                            "How do you handle it?":
                                "Keep commiting. It's stressful, but worth it."
                                $ stress += 1
                                
                                $ skill += 1
                                "Take a break":
                                    $ stress -= 2
                                    "Talk to someone":
                                        $ passion += 2
                                        $ reputation += 1

                                        elif day == 5:
                                            "Dress rehearsal."
                                            "Everything has to be perfect."

                                            menu:
                                                "What's your approach?"
                                                "Give everything you have":
                                                    $ skill += 3
                                                    $ stress += 2

                                                    "Stay calm and focused":
                                                    $ stress -= 1
                                                    $ skill += 1
                                                        return
label background_rehearsal_day:

    if day == 1:
        "You're barely noticed."

        menu:
            "What do you do?":

                "Observe and learn":
                    $ skill += 2

                "Try to stand out":
                    $ reputation += 2
                    $ stress += 1

                elif day == 2:
                    "You finally get direction."
                    "It feels good to be able to do something."
                    menu:
            "Your response?":

                "Take it seriously":
                    $ skill += 2

                "Half-listen":
                    $ passion -= 1
                    elif day == 3:
                        "You feel ignored again."
                        "You have to spend an hour at rehearsal just sitting backstage."
                        menu:
                            "How do you cope?":

                "Stay focused":
                    $ skill += 1

                "Get discouraged":
                    $ passion -= 2


                    elif day == 4:
                        "Some of the other actors are being kind to you."
                        "They hype you up even when you get a small spot on stage!"
                        menu:
                            "What do you do when you get to be in a small scene?"
                            "Make it count":
                    $ reputation += 3

                "Play it safe":
                    $ skill += 1

                    elif day == 5:
                        "Final day, it's dress rehearsal."
                        "You can't believe how quickly time flew by, but here you are."
                        menu:
                            "What's your mindset?"
                            "I belong here":
                    $ passion += 2

                "I don't matter here":
                    $ passion -= 2

    return



                  




                   
                        

    
