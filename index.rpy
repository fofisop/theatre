define m = Character("You")
default read_notes = False
default read_monologue = False
default gave_resume = False
default stress = 0
default skill = 0
default reputation = 0
default passion = 0
default role = "none"
default max_days = 5
default day = 1

image room = "room.png"
image audition = "audition.png"
image lobby = "lobby.png"
image mon = "mon.png"
image notes = "notes.png"
image dressing_room = "dressing_room.png"
image tech_booth = "tech_booth.png"
image stage = "stage.png" 
image womp = "womp.png"
image win = "win.png"
image door = "door.png"

label show_day:
    if role == "lead":
        jump show_day_lead
    elif role == "background":
        jump show_day_background
    else:
        jump show_day_crew
label start:
    $ read_notes = False
$ read_monologue = False
$ gave_resume = False
$ stress = 0
$ skill = 0
$ reputation = 0
$ passion = 0
$ role = "none"
$ day = 1
scene room
    "Your room. Audition day is tomorrow." 
    "Do you check your audition notes?"
    menu:
    
            "Yes":
                scene notes 
                $ read_notes = True
                "You read the words carefully"
            "No":
                "You decide to wing it."
    scene room
    "Do you review your monologue?"
    menu:
            "Yes": 
                scene mon
                $ read_monologue = True
                "You read and reahearse your monologue."
            "No":
                "You think you got it memorized just fine."
    scene room
    "You fall asleep..."
    jump morning



label morning:
    scene black
    "Your alarm rings."
    "What do you do?"
    menu:
            "Get up":
                "You drag yourself out of bed and get ready for the audition."
                jump audition 
            "Ignore it":
                "You're tired."
                jump lose_alarm

label lose_alarm:

    scene black

    "You fall back asleep."

    "You miss your audition."
    "Sometimes, the biggest opportunities slip away quietly."

    return


label audition:
    scene audition
    "You step onto the floor."

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
    "Do you leave immediately?"
    menu:
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
    "Give your resume to the staff?"
    menu:
       
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
        jump rehearsal_loop
    else:
        "You didn't stand out too much..."
    menu:
            "Accept background role":
                $ role = "background"
            "Join stage crew instead":
                $ role = "crew"
    jump rehearsal_loop
label rehearsal_loop:
    if day > max_days:
        jump show_day
    scene stage
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
        scene stage
        "You step into rehearsal. The director eyes you carefully."
        "She hands you the script."
        "You are asked to do a cold read."
        "How do you respond?"
        menu:
            
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
        "What do you do?"
        menu:
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
        "You feel like you just started memorising the script, and now they expect you to know it by heart?"
        "How do you react?"
        menu:
            
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
        "You're doing well, but the exhaustion is overwhelming."
        "The fact that everyone can tell stresses you out even more."
        "How do you handle it?"

        menu:
            
                "Keep committing. It's stressful, but worth it.":
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
        "What's your approach?"
        menu:
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
        "What do you do?"
        menu:
                "Observe and learn":
                    $ skill += 2
                "Try to stand out":
                    $ reputation += 2
                    $ stress += 1
    elif day == 2:
        "You finally get direction."
        "It feels good to be able to do something."
        "Your response?"
        menu:
          
                "Take it seriously":
                    $ skill += 2
                "Half-listen":
                    $ passion -= 1
    elif day == 3:
        "You feel ignored again."
        "You have to spend an hour at rehearsal just sitting backstage."
        "How do you cope?"
        menu:
                "Stay focused":
                    $ skill += 1
                "Get discouraged":
                    $ passion -= 2
    elif day == 4:
        "Some of the other actors are being kind to you."
        "They hype you up even when you get a small spot on stage!"
        "What do you do when you get to be in a small scene?"

        menu:
          
                "Make it count":
                    $ reputation += 3
                "Play it safe":
                    $ skill += 1
    elif day == 5:
        "Final day, it's dress rehearsal."
        "You can't believe how quickly time flew by, but here you are."
        "What's your mindset?"
        menu:
                "I belong here":
                    $ passion += 2
                "I don't matter here":
                    $ passion -= 2
    return
label crew_rehearsal_day:
    if day == 1:
        "You're learning how everything works backstage."
        "What do you focus on?"
        menu:

                "Learning how things work":
                    $ skill += 2
                "Helping people out even if you don't really know how":
                    $ reputation += 2
    elif day == 2:
        "Something goes wrong."
        "What is your reaction?"
        menu:
           
                "Fix it quickly":
                    $ skill += 2
                    $ stress += 1
                "Call for help":
                    $ reputation += 1
    elif day == 3:
        "You feel disconnected from the stage."
        "What do you do?"
        menu:
                "Watch rehearsals":
                    $ passion += 2
                "Stay busy":
                    $ skill += 1
    elif day == 4:
        "You are trusted with being the head of stage crew."
        "How do you handle it?"
        menu:

                "Take it seriously":
                    $ reputation += 2
                "Don't put too much of an effort into it":
                    $ stress += 1
    elif day == 5:
        "Final tech rehearsal before the real deal."
        "What's your mindset?"
        menu:
                "This matters":
                    $ passion += 2
                "I'm just background":
                    $ passion -= 2
    return
label show_day_lead:
    scene room
    "It's opening night."
    "You wake up before the alarm."
    "You are  already feeling nervous."
    "How do you start the day?"
    menu:
            "Practice immediately":
                $ skill += 1
                $ stress += 1
            "Try to relax":
                $ stress -= 1
            "Avoid thinking about the show":
                $ passion -= 1
    scene lobby
    "People keep wishing you luck."
    "They don't calm your nerves."
    scene dressing_room
    "The room feels loud, overwhelming."
    "You try to joke and laugh with your fellow actors, but it doesn't seem to break the tension."
    "What do you do?"
    menu:
        
            "Chat with the others in the room":
                $ reputation += 2
            "Focus quietly":
                $ skill += 1
            "Panic internally":
                $ stress += 2
                                        
    scene stage
    "The curtian rises."
    "Thousands of eyes stare at you."
    "Your first line approaches."
    "How do you deliver it?"
    menu:
       
            "With confidence":
                $ skill += 2
            "Carefully":
                $ stress -= 1
            "In a rushed manner":
                $ reputation -= 1

    "The emotional climax of the play arrives."
    "What drives your performance?"
    menu:
        
            "Passion":
                $ passion += 2
            "Perfection":
                $ stress += 2
            "Fear":
                $ stress += 3
    scene lobby
    "The show is over."
    "The applause still echoes in your head."
    "People laugh, cry, hug."
    "And you finally have a moment to think."
    jump final_outcome
      
                                           
label show_day_background:
    scene room
    "Opening night."
    "Your name isn't on the posters."
    "Most people probably won't even remember your role."
    "But at least you're in it."
    "How do you feel?"
    menu:
       
            "Proud to be here":
                $ passion += 2
            "Nervous":
                $ stress += 2
            "Useless":
                $ passion -= 1
    scene lobby
    "The lobby is packed."
    "People talk excitedly about the lead actor."
    "No one notices you walk in."
    "What do you do?"
    menu:
       
            "Keep your head down":
                $ stress -= 1
            "Talk to other ensemble members":
                $ reputation += 2
            "Watch the lead longingly from afar":
                $ passion -= 1
    scene dressing_room
    "The dressing room is pure chaos."
    "You overhear someone say the lead is amazing."
    "What's your reaction?"
    menu:
            "Use it as motivation":
                $ skill += 2
            "Feel jealous":
                $ passion -= 2
            "Focus on your own role.":
                $ stress -= 1 
                $ skill += 1
    "It's time for you to go on stage."
    scene stage
    "Everyone applauded the lead, but will they applaud you?"
    "What keeps you going?"
    menu:
       
            "Your love for performing": 
                $ passion += 2
            "Hope someone notices":
                $ reputation += 2
            "Pure obligation":
                $ stress += 2
    "The scene changes."
    "For the first time, the spotlight briefly shines in your eyes, and it feels good."
    "You have one line in the spotlight."
    "How do you deliver it?"
    menu:
            "Confidently":
                $ skill += 2
            "Carefully":
                $ stress -= 1
            "Quietly":
                $ reputation -= 1
    scene lobby
    "The performance ends."
    "The lead gets surrounded by applause and flowers."
    "You stand off to the side."
    "Suddenly, someone from the audience stops you. They complement you, and tell you that you did well."
    "It feels worth it now just because of that one person."
    jump final_outcome



label show_day_crew:
    scene room
    "It's opening night."
    "You have to make sure the show runs smoothly."
    "How do you start the day?"
    menu:
        
            "Review the cue sheet":
                $ skill += 2
            "Try to stay calm":
                $ stress -= 1
            "Avoid thinking about mistakes":
                $ passion -= 1
    scene lobby
    "The theatre is already alive."
    "Props are being moved, lights are being tested, and there are tons of things to do."
    "The stage manager tells you to help out."
    "How do you respond?"
    menu:
        
            "Check lighting":
                $ skill += 2
            "Help the cast":
                $ reputation += 2
            "Double check everything":
                $ stress += 1
                $ skill += 1
    scene tech_booth
    "An important prop goes missing. The stage manager looks concerned."
    "What do you do?"
    menu: 
        
            "Search for it yourself":
                $ skill += 2
                $ stress += 1
            "Ask others for help":
                $ reputation += 2
            "Freeze up":
                $ stress += 2
                $ passion -= 1
    "The curtain rises."
    "Your headset crackles."
    "You try to do everything right on time, but there's a lot to be done."
    "Cue after cue rolls by, and you try your best to focus."
    "How do you handle the pressure?"
    menu:
        
            "Stay focused":
                $ skill += 2
            "Trust your instincts":
                $ passion += 2
            "Panic quietly":
                $ stress += 2
    "Suddenly, an important spotlight goes out."
    "The stage manager is nowhere around."
    "What do you do?"
    menu:
        
            "Dig through wires, and try to see which one could've disconnected.":
                $ skill += 3
            "Choose to not trust yourself with this, and call for help.":
                $ reputation += 1
            "Freeze and hesitate":
                $ stress += 2
    "The show ends."
    "The audience applauds."
    "The actors take their bows."
    "You stay behind the curtain."
    "The stage manager approaches you."
    "They tell you that they couldn't have done it without you."
    jump final_outcome
label final_outcome:

    if stress >= 12 and passion <= 3:
        jump burnout_ending

    if role == "lead":

        if skill >= 7 and passion >= 6:
            jump success_ending

        elif reputation >= 6:
            jump directors_fav

        elif skill >= 5:
            jump steady_ending

        else:
            jump quit_theatre

    elif role == "background":
        if passion >= 7 and stress <= 8:
            jump found_passion
        elif skill >= 7 and reputation >= 6 and passion >= 4:
            jump scene_stealer
        elif skill >= 4:
            jump hidden_talent_ending
        else:
            jump quit_theatre

    elif role == "crew":
        if skill >= 8 and reputation >= 6 and stress <= 6:
            jump manager
        elif passion >= 6 and reputation >= 4:
            jump found_passion
        elif stress >= 10:
            jump burnout_ending

        else:
            jump quit_theatre


label success_ending:
    scene win
    centered "Skill: [skill]\nReputation: [reputation]\nPassion: [passion]\nStress: [stress]"
    centered "You made it. All of the rehearsals, all of the stress finally led somewhere. This is an actor's dream. You finally got your big break, and you will want to keep doing thsi for as long as you can."
    return


label burnout_ending:
    scene door
    centered "Skill: [skill]\nReputation: [reputation]\nPassion: [passion]\nStress: [stress]"
    centered "The show is over. But you feel empty. You need to step away from this path for now. The pressure took more from you than expected."
    return

label quit_theatre:
    scene door
    centered "Skill: [skill]\nReputation: [reputation]\nPassion: [passion]\nStress: [stress]"
    centered "You stand on the empty stage after everyone has left. Somewhere along the way, theatre stopped feeling right. Maybe it's time for something new. You leave the theatre and sigh."
    return

label found_passion:
    scene win
    centered "Skill: [skill]\nReputation: [reputation]\nPassion: [passion]\nStress: [stress]"
    centered "You smile quietly. Maybe you were never chasing the spotlight, and you were just finding a place to belong. Now you have, and it's your passion."
    return

label manager:
    scene win
    centered "Skill: [skill]\nReputation: [reputation]\nPassion: [passion]\nStress: [stress]"
    centered "The stage manager offers you to be co-manager. You pause. This idea feels right. Maybe this is what you are meant to be. You accept."
    return


label directors_fav:
    scene win
    centered "Skill: [skill]\nReputation: [reputation]\nPassion: [passion]\nStress: [stress]"
    centered "You weren't perfect. But you've got a good reputation. Sometimes reliability matters more than brilliance. You are the director's favorite."
    return

label scene_stealer:
    scene win
    centered "Skill: [skill]\nReputation: [reputation]\nPassion: [passion]\nStress: [stress]"
    centered "It was only a small role, but people noticed. You realize small roles might matter more than you thought. Someone hands you a bouquet after you are done."
    return


label steady_ending:
    scene win
    centered "Skill: [skill]\nReputation: [reputation]\nPassion: [passion]\nStress: [stress]"
    centered "You didn't steal the spotlight — but you never missed a beat. Reliability becomes your strength."
    return


label hidden_talent_ending:
    scene win    
    centered "Skill: [skill]\nReputation: [reputation]\nPassion: [passion]\nStress: [stress]"
    centered "Someone noticedd you when no one else did. It might not be your moment yet… but it could be."
    return
