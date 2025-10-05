# Defining player
default p_name = "testname"
define pl = Character("[p_name]")

# Defining characters
define st = Character("Stormy", color="#9D3BFF", what_prefix="\"", what_suffix="\"")
define sp = Character("Sparky", color="#F5BF2A", what_prefix="\"", what_suffix="\"")
define te = Character("Tired Exec", what_prefix="\"", what_suffix="\"")

# Defining transforms
transform half_size:
    zoom 0.5

# Defining images for organizational purposes
# Sparky
image sparky = "sparky/neutral.png"
image sparky happy = "sparky/happy.png"
image sparky sad = "sparky/sad.png"
image sparky stressed = "sparky/stressed.png"

# Sparky talking variation
image sparky talking = "sparky/neutral_talking.png"
image sparky happy talking = "sparky/happy_talking.png"
image sparky sad talking = "sparky/sad_talking.png"
image sparky stressed talking= "sparky/stressed_talking.png"

# Stormy
image stormy = "stormy/neutral.png"
image stormy happy = "stormy/happy.png"
image stormy sad = "stormy/sad.png"
image stormy stressed = "stormy/stressed.png"
image stormy flushed = "stormy/flushed.png"

# Stormy talking variation
image stormy talking = "stormy/neutral_talking.png"
image stormy happy talking = "stormy/happy_talking.png"
image stormy sad talking = "stormy/sad_talking.png"
image stormy stressed talking = "stormy/stressed_talking.png"
image stormy flushed talking = "stormy/flushed_talking.png"

# Tired exec
image exec = "exec/neutral"

# Tired exec talking variation
image exec talking = "exec/neutral_talking.png"

# Backgrounds
image bg black = "bg/black.png"
image bg asb = "bg/asb.png"

# CG art
# define cg art here

# Game start
label start:
    scene bg black

    # <replace audio - running through door>
    st "Heyyyy see if you can accept my pull request plzzzz"
    
    # Call the challenge properly
    call code_challenge_1
    
    sp "Come on! We can't be later than this!"

    scene bg asb at half_size, truecenter
    with Dissolve(1.0)

    "We burst through the doors of the Applied Science Building, still trying to put our backpacks on properly."

    pl "I know! I'm following right behind you!"

    "This weekend is StormHacks 2025, a 24-hour hackathon taking place on our school's campus."

    "Although it started at nine in the morning, we're only showing up just now — fifteen hours late."

    "Normally, we wouldn't even have been able to attend the hackathon at this point because of how much time has already elapsed, but I was able to get both of us in at the last minute."

    "I still have no idea how I managed to convince one of the Execs to check us in this late."

    "Hurriedly, we looked around for the person that was supposed to meet us near the check-in booth, finally having a moment to catch our breaths."

    sp "Now... where is he?"

    pl "I dunno, he said he'd be around here somewhere."

    sp "Go ping him again in the server, tell him we're here."

    pl "Yeah, sure."

    "As I pull out my phone, we are interrupted by a tired voice from behind us."

    te "Hey."

    "We turn to find a nondescript guy waving us over, phone in hand."

    te "You uh... you Sparky and [p_name]?"

    sp "Oh, yeah. You here to check us in?"

    te "Yeah yeah, c'mon. Let's just get this done real quick."

    # play sound "scan.ogg"

    # play sound "scan.ogg"

    te "There. Now happy hacking or whatever. You can get to it."

    pl "Alright alright, thanks."

    "We rush off down the hall, passing teams that are already halfway into their project."

    "It takes us a bit, but miraculously, we find an empty table and drop our bags right down."

    scene bg black
    centered "12 Hours Until Deadline"

    "We take a moment to catch our breaths and settle down."

    sp "Man, alright. At least we're here. Let's just try to get whatever we can done."

    "I nod in agreement, pulling out my laptop and getting it plugged in."

    "Suddenly, someone else sprints through the doors just like we did."

    # play sound "running_doors.ogg"

    "A purple otter with glasses, frantically running towards the check-in booth as well."

    st "Oh god, okay. Um, okay. W-where is..."

    "He looks down at his phone, stressed, as the tired exec calls out to them."

    te "Oi. Stormy?"

    st "Ah— uh, yes? Oh! Hello, yes. Uh, check in, right? Yeah."

    te "Yeah yeah. QR?"

    st "Oh yeah right right right right right, here... here it is."

    play sound "scan.ogg"

    te "Okay, there you go. On your merry way now."

    st "Thanks, I'll uh... I'll... yeah."

    "Stormy comes down the hall, head on a swivel looking for any empty tables."

    "There doesn't seem to be any around."

    "With the only open seats being next to us, Stormy approaches our table shyly, picking the seat farthest away."

    "We both take a glance at him, seeing him slowly pull his laptop out, ever so slightly scooting away from us as well."

    "It would certainly be nice to add another member to our team, but I can't tell whether he's just shy or doesn't want to interact with us... or both."

    "Sparky turns to give me an acknowledging look, then slides over and nudges him."

    sp "Hey there."

    st "Oh... h-hey..."

    sp "You came late too, huh?"

    st "R-right, yeah."

    sp "Would you... like to join us? I mean, the more the merrier, right?"

    st "Could I do that?"

    sp "Of course! I mean, you can, but you don't have to."

    pl "Okay... if that's alright with you two."

    st "I don't think I'd be able to finish a project on my own within the remaining time anyways."

    st "So uh... t-thanks."

    "He makes a good attempt to give us a friendly smile."



    return

# Code challenge label
label code_challenge_1:
    python:
        request_code_challenge(code_prompts["login_system"], "challenge_1", "python")
        challenge_ready = wait_for_code_challenge("challenge_1")
    
    if challenge_ready:
        $ result = show_code_challenge("challenge_1")
        
        if result == "answer_given":
            "You submitted your answer!"
            # Add logic here based on whether player_answer is correct
            if player_answer:
                "Great job! You identified the code correctly."
            else:
                "Nice try! Let's review what you found."
        elif result == "skip":
            "You decided to skip this challenge."
    else:
        "Sorry, the challenge failed to load. Let's continue..."
    
    return
