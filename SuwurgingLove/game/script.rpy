# Defining player
default p_name = ""
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
