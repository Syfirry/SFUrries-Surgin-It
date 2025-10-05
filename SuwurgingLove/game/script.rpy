# Defining player
default p_name = ""
define pl = Character("[p_name]")

# Defining characters
define st = Character("Stormy", color="#9D3BFF", what_prefix="\"", what_suffix="\"")
define sp = Character("Sparky", color="#F5BF2A", what_prefix="\"", what_suffix="\"")
define te = Character("Tired Exec", what_prefix="\"", what_suffix="\"")

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
image stormy embarrassed = "stormy/embarrassed.png"

# Stormy talking variation
image stormy talking = "stormy/neutral_talking.png"
image stormy happy talking = "stormy/happy_talking.png"
image stormy sad talking = "stormy/sad_talking.png"
image stormy stressed talking = "stormy/stressed_talking.png"
image stormy embarrassed talking = "stormy/embarrassed_talking.png"

# Backgrounds
image bg black = "bg/black.png"
image bg asb = "bg/asb.png"

# CG art
# define cg art here

# Game start
label start:
    scene bg black

    # <replace audio - running through door>
    jump start_challenge_sequence

    sp "Come on! We can't be later than this!"

    scene bg asb
    with Dissolve(1.0)

    "We burst through the doors of the Applied Science Building, still trying to put our backpacks on properly."

    return
