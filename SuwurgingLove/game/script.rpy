# Defining player
default p_name = ""
define pl = Character("[p_name]", color="#db698b", what_color="#FFFFFF", what_prefix="\"", what_suffix="\"", what_slow_cps=90)

# Defining characters
define st = Character("Stormy", color="#9D3BFF", what_color="#FFFFFF", what_prefix="\"", what_suffix="\"", what_slow_cps=90)
define sp = Character("Sparky", color="#F5BF2A", what_color="#FFFFFF", what_prefix="\"", what_suffix="\"", what_slow_cps=90)
define te = Character("Tired Exec", color="#7ea8df", what_color="#FFFFFF", what_prefix="\"", what_suffix="\"", what_slow_cps=90)
define narrator = Character(None, what_color="#FFFFFF", what_slow_cps=90)

# Defining other variables
default track = ""
default language = ""
default tname = ""
define points = 0
define kahootcount = 0

# Defining audio
define door = "doorrush.wav"
define beep = "scanbeep.wav"


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

# Define Transformations
transform resized:
    zoom 0.20
    yoffset -250

transform shiftright:
    xoffset 160

transform shiftleft:
    xoffset -160

transform flipped:
    xzoom -1.0

transform talk:
    easein 0.2 yoffset -10

transform notalk:
    easein 0.2 yoffset 10



# Tired exec
image exec = "exec/neutral.png"

# Tired exec talking variation
image exec talking = "exec/neutral_talking.png"

# Backgrounds
image bg black = "bg/black.png"
image bg black2 = "bg/black2.png"
image bg asb = "bg/asb.png"
image bg table = "bg/table.png"
image bg kahoot = "bg/kahoot.png"

# CG art
# define cg art here

init python:
    renpy.config.layers.append("blackfade")

# Game start
label start:
    $ p_name = renpy.input("What is your name?")
    $ p_name = p_name.strip()

    scene bg black

    play sound door

    sp "Come on! We can't be later than this!"

    scene bg asb at truecenter
    with Dissolve(1.0)

    "We burst through the doors of the Applied Science Building, still trying to put our backpacks on properly."

    pl "I know! I'm following right behind you!"

    "This weekend is StormHacks 2025, a 24-hour hackathon taking place on our school's campus."

    "Although it started at nine in the morning, we're only showing up just now — fifteen hours late."

    "Normally, we wouldn't even have been able to attend the hackathon at this point because of how much time has already elapsed, but I was able to get both of us in at the last minute."

    "I still have no idea how I managed to convince one of the Execs to check us in this late."

    "Hurriedly, we looked around for the person that was supposed to meet us near the check-in booth, finally having a moment to catch our breaths."

    show sparky stressed talking at left, resized, shiftright, flipped, talk
    sp "Now... where is he?"

    show sparky stressed -talking at left, resized, shiftright, flipped, notalk
    pl "I dunno, he said he'd be around here somewhere."

    show sparky stressed talking at left, resized, shiftright, flipped, talk
    sp "Go ping him again in the server, tell him we're here."

    show sparky stressed -talking at left, resized, shiftright, flipped, notalk
    pl "Yeah, sure."

    "As I pull out my phone, we are interrupted by a tired voice from behind us."

    te "Hey."

    "We turn to find a nondescript guy waving us over, phone in hand."

    show exec talking at right, resized, shiftleft, talk
    te "You uh... you Sparky and [p_name]?"

    show exec -talking at right, resized, shiftleft, notalk
    show sparky sad talking at left, resized, shiftright, flipped, talk
    sp "Oh, yeah. You here to check us in?"

    show exec talking at right, resized, shiftleft, talk
    show sparky sad -talking at left, resized, shiftright, flipped, notalk
    te "Yeah yeah, c'mon. Let's just get this done real quick."

    show exec -talking at right, resized, shiftleft, notalk

    play sound beep

    pause 3

    play sound beep

    show exec talking at right, resized, shiftleft, talk
    te "There. Now happy hacking or whatever. You can get to it."

    show exec -talking at right, resized, shiftleft, notalk
    pl "Alright alright, thanks."

    "We rush off down the hall, passing teams that are already halfway into their project."

    "It takes us a bit, but miraculously, we find an empty table and drop our bags right down."

    show expression Solid("#000") as black_overlay onlayer blackfade
    with Dissolve(1.0)

    hide sparky
    hide exec
    window hide

    show bg black
    hide black_overlay onlayer blackfade

    $ _old_cps = preferences.text_cps
    $ preferences.text_cps = 0
    centered "{size=72}{b}12 Hours Until Deadline{/b}{/size}"
    $ preferences.text_cps = _old_cps

    
    scene bg table at truecenter
    with Dissolve(1.0)
    window show

    "We take a moment to catch our breaths and settle down."

    show sparky talking at left, resized, shiftright, flipped, talk
    sp "Man, alright. At least we're here. Let's just try to get whatever we can done."


    show sparky at left, resized, shiftright, flipped, notalk
    "I nod in agreement, pulling out my laptop and getting it plugged in."

    "Suddenly, someone else sprints through the doors just like we did."

    play sound door

    scene bg asb
    with Dissolve(1.0)

    "A purple otter with glasses, frantically running towards the check-in booth as well."

    show stormy stressed talking at left, resized, shiftright, flipped, talk
    st "Oh god, okay. Um, okay. W-where is..."

    show stormy stressed -talking at left, resized, shiftright, flipped, notalk
    "He looks down at his phone, stressed, as the tired exec calls out to them."

    show exec talking at right, resized, shiftleft, talk
    te "Oi. Stormy?"

    show exec -talking at right, resized, shiftleft, notalk
    show stormy stressed talking at left, resized, shiftright, flipped, talk
    st "Ah— uh, yes? Oh! Hello, yes. Uh, check in, right? Yeah."

    show stormy stressed -talking at left, resized, shiftright, flipped, notalk
    show exec talking at right, resized, shiftleft, talk
    te "Yeah yeah. QR?"

    show stormy sad talking at left, resized, shiftright, flipped, talk
    show exec -talking at right, resized, shiftleft, notalk
    st "Oh yeah right right right right right, here... here it is."
    show stormy sad -talking at left, resized, shiftright, flipped, notalk

    play sound beep

    show exec talking at right, resized, shiftleft, talk
    te "Okay, there you go. On your merry way now."
    show exec -talking at right, resized, shiftleft, notalk
    show stormy sad talking at left, resized, shiftright, flipped, talk
    st "Thanks, I'll uh... I'll... yeah."
    show stormy sad -talking at left, resized, shiftright, flipped, notalk
    hide stormy with Dissolve(0.6)
    "Stormy comes down the hall, head on a swivel looking for any empty tables."
    
    "There doesn't seem to be any around."

    scene bg table
    with Dissolve(1.0)
    show sparky at left, resized, shiftright, flipped, notalk
    show stormy sad at right, resized, shiftleft, notalk
    "With the only open seats being next to us, Stormy approaches our table shyly, picking the seat farthest away."

    "We both take a glance at him, seeing him slowly pull his laptop out, ever so slightly scooting away from us as well."

    "It would certainly be nice to add another member to our team, but I can't tell whether he's just shy or doesn't want to interact with us... or both."

    "Sparky turns to give me an acknowledging look, then slides over and nudges him."


    show sparky talking at left, resized, shiftright, flipped, talk
    sp "Hey there."

    show stormy sad talking at right, resized, shiftleft, talk
    show sparky -talking at left, resized, shiftright, flipped, notalk
    st "Oh... h-hey..."

    show stormy sad -talking at right, resized, shiftleft, notalk
    show sparky talking at left, resized, shiftright, flipped, talk
    sp "You came late too, huh?"

    show stormy sad talking at right, resized, shiftleft, talk
    show sparky -talking at left, resized, shiftright, flipped, notalk
    st "R-right, yeah."

    show stormy sad -talking at right, resized, shiftleft, notalk
    show sparky talking at left, resized, shiftright, flipped, talk
    sp "Would you... like to join us? I mean, the more the merrier, right?"

    show stormy sad talking at right, resized, shiftleft, talk
    show sparky -talking at left, resized, shiftright, flipped, notalk
    st "Could I do that?"

    show stormy sad -talking at right, resized, shiftleft, notalk
    show sparky talking at left, resized, shiftright, flipped, talk
    sp "Of course! I mean, you can, but you don't have to."

    show sparky -talking at left, resized, shiftright, flipped, notalk
    show stormy sad talking at right, resized, shiftleft, talk
    st "Okay... if that's alright with you two."

    st "I don't think I'd be able to finish a project on my own within the remaining time anyways."

    st "So uh... t-thanks."

    show stormy -talking at right, resized, shiftleft, notalk
    "He makes a good attempt to give us a friendly smile. We smile back."

    pl "Well, welcome to our team! I don't think I caught your name?"

    show stormy talking at right, resized, shiftleft, talk
    st "Oh, uh, Stormy."

    show stormy -talking at right, resized, shiftleft, notalk
    pl "Nice to meet you, Stormy. I'm [p_name]."
    show sparky talking at left, resized, shiftright, flipped, talk
    sp "And I'm Sparky."
    show sparky -talking at left, resized, shiftright, flipped, notalk
    show stormy talking at right, resized, shiftleft, talk
    st "Uh, nice to meet you two... too, yeah."
    show stormy -talking at right, resized, shiftleft, notalk
    pl "Alright, introductions aside, we probably should consider what track we want to work on. We're really short on time afterall."

    pl "Do either of you have anything in mind?"
    show stormy talking at right, resized, shiftleft, talk
    st "I... I didn't get that far yet. Was uh... rushing to get here..."
    show stormy -talking at right, resized, shiftleft, notalk
    show sparky talking at left, resized, shiftright, flipped, talk
    sp "Don't look at me, you know I'm indecisive."
    show sparky -talking at left, resized, shiftright, flipped, notalk
    pl "Well then..."


menu trackchoice:
    "What track should we work towards?"

    "CSSS Rube Goldberg Challenge":
        $ track = "assembly"
        $ language = "c"
        $ tname = "CSSS Rube Goldberg Challenge"
    "ColorStack Most Portable Project":
        $ track = "api_endpoint"
        $ language = "swift"
        $ tname = "ColorStack Most Portable Project"
    "Safe Software Best Modern C++":
        $ track = "security_issue"
        $ language = "cpp"
        $ tname = "Safe Software Best Modern C++"


label after_track_choice:
    $ getcodes()
    pl "Let's go for the [tname] track then. Does that work for everyone?"
    show sparky talking at left, resized, shiftright, flipped, talk
    sp "Works for me."
    show stormy talking at right, resized, shiftleft, talk
    show sparky -talking at left, resized, shiftright, flipped, notalk
    st "Y-yeah, me too."
    show stormy -talking at right, resized, shiftleft, notalk
    pl "Alrighty, let's get started then!"

    show expression Solid("#000") as black_overlay onlayer blackfade
    with Dissolve(1.0)

    hide sparky
    hide stormy
    window hide

    show bg black
    hide black_overlay onlayer blackfade

    $ _old_cps = preferences.text_cps
    $ preferences.text_cps = 0
    centered "{size=72}{b}11 Hours Until Deadline{/b}{/size}"
    $ preferences.text_cps = _old_cps

    
    scene bg table at truecenter
    with Dissolve(1.0)
    window show

    show sparky at left, resized, shiftright, flipped, notalk
    show stormy at right, resized, shiftleft, notalk
    "It's been an hour since we started, but my mind is already getting tired."
    
    "I let out a big stretch."

    pl "Mmmmh, alright. We've been at this for a bit now, and while I know we're under a big time constraint, I also want to go to at least one event."

    show sparky talking at left, resized, shiftright, flipped, talk
    sp "Yeah I agree. Still wanna have some fun at least. What'dya say, Stormy?"

    show sparky -talking at left, resized, shiftright, flipped, notalk
    show stormy sad talking at right, resized, shiftleft, talk
    st "W-well, there's a Tech Kahoot Trivia that starts in... well in just a couple minutes."

    show sparky talking at left, resized, shiftright, flipped, talk
    show stormy sad -talking at right, resized, shiftleft, notalk
    sp "Oh, cool, yeah I'm down for that."

    show sparky -talking at left, resized, shiftright, flipped, notalk
    show stormy -sad at right, resized, shiftleft, notalk
    pl "Me too, I'd love some trivia."

    "We all nod in agreement."

    show sparky talking at left, resized, shiftright, flipped, talk
    sp "Shall we?"

    scene bg kahoot
    with Dissolve(1.0)

    "We arrive at ASB 9703, prepared to have some fun."

    show sparky happy talking at left, resized, shiftright, flipped, talk
    show stormy happy at right, resized, shiftleft, notalk
    sp "Alright! I'm pumped! You ready?"

    show sparky happy -talking at left, resized, shiftright, flipped, notalk
    show stormy happy talking at right, resized, shiftleft, talk
    st "Uh— y-yeah!"

    show stormy happy -talking at right, resized, shiftleft, notalk
    pl "May the best man win!"

    hide stormy happy
    hide sparky happy

    jump kahoot
    
label after_kahoot:
    if points > 25:
        show stormy happy talking at right, resized, shiftleft, talk
        show sparky happy at left, resized, shiftright, flipped, notalk
        st "Woah! You did so well!"
        show sparky happy talking at left, resized, shiftright, flipped, talk
        show stormy happy -talking at right, resized, shiftleft, notalk
        sp "Yeah man! Seems like you know your stuff!"
    elif points > 20:
        show sparky happy talking at left, resized, shiftright, flipped, talk
        show stormy happy -talking at right, resized, shiftleft, notalk
        sp "Hey, you did pretty good!"
        show stormy happy talking at right, resized, shiftleft, talk
        show sparky happy at left, resized, shiftright, flipped, notalk
        st "Y-yeah, you did well!"
    elif points > 15:
        show stormy talking at right, resized, shiftleft, talk
        show sparky at left, resized, shiftright, flipped, notalk
        st "That was really fun! We did alright!"
        show sparky talking at left, resized, shiftright, flipped, talk
        show stormy -talking at right, resized, shiftleft, notalk
        sp "Yeah! We should play again next year!"
    elif points > 10:
        show sparky talking at left, resized, shiftright, flipped, talk
        show stormy -talking at right, resized, shiftleft, notalk
        sp "It's alright man, you'll get better!"
        show stormy talking at right, resized, shiftleft, talk
        show sparky at left, resized, shiftright, flipped, notalk
        st "Y-yeah, I just know it!"
    else:
        show stormy sad talking at right, resized, shiftleft, talk
        show sparky at left, resized, shiftright, flipped, notalk
        st "Aw man... y-you did alright... right?"
        show sparky talking at left, resized, shiftright, flipped, talk
        show stormy sad -talking at right, resized, shiftleft, notalk
        sp "Guess you gotta study up on this, huh?"

    "More stuff"

    show expression Solid("#000") as black_overlay onlayer blackfade
    with Dissolve(1.0)

    hide sparky
    hide exec
    window hide

    show bg black
    hide black_overlay onlayer blackfade

    $ _old_cps = preferences.text_cps
    $ preferences.text_cps = 0
    centered "{size=72}{b}To Be Continued...{/b}{/size}"
    $ preferences.text_cps = _old_cps

    python: 
        playgame()
    
    return



menu kahootq:
    "[qstion]"

    "[ans1]":
        python:
            if ans1 == ans:
                points += 1
                renpy.jump("kahoot")
    
    "[ans2]":
        python:
            if ans1 == ans:
                points += 1
                renpy.jump("kahoot")
    
    "[ans3]":
        python:
            if ans1 == ans:
                points += 1
                renpy.jump("kahoot")
    
    "[ans4]":
        python:
            if ans1 == ans:
                points += 1
                renpy.jump("kahoot")


init python:
    def getcodes():
        for i in range(5):
            request_code_challenge(code_prompts[track], f"challenge_{i+1}", language)
        
    
    def playgame():
        for i in range(5):
            challenge_ready = wait_for_code_challenge(f"challenge_{i+1}")
            result = show_code_challenge(f"challenge_{i+1}")
            if result == "answer_given":
                "You submitted your answer!"
                # Add logic here based on whether player_answer is correct
                if player_answer:
                    "Great job! You identified the code correctly."
                else:
                    "Nice try! Let's review what you found."
            elif result == "skip":
                "You decided to skip this challenge."

    


label kahoot:
    python:
        questions = "What does “HTTP” stand for?,HyperText Transfer Protocol,HighText Transfer Process,Hyper Transfer Text Program,High Transmission Text Protocol,HyperText Transfer Protocol,Which company developed the first iPhone?,Google,Apple,Microsoft,Nokia,Apple,What does CPU stand for?,Central Processing Unit,Computer Primary Unit,Core Processing Utility,Central Power Unit,Central Processing Unit,Which programming language is often referred to as the “mother of all languages”?,Assembly,FORTRAN,C,COBOL,C,What year was Google founded?,1995,1996,1998,2000,1998,What does “GPU” stand for in computing?,General Processing Unit,Graphics Processing Unit,Graphical Program Utility,Global Processing Unit,Graphics Processing Unit,Which was the first social media platform to reach 1 billion users?,Twitter,Facebook,Instagram,YouTube,Facebook,Who is known as the father of the World Wide Web?,Steve Jobs,Tim Berners-Lee,Bill Gates,Vint Cerf,Tim Berners-Lee,Which company created the Windows operating system?,Apple,Microsoft,IBM,Intel,Microsoft,What does “URL” stand for?,Universal Routing Link,Uniform Resource Locator,Unified Retrieval Language,User Reference Link,Uniform Resource Locator,Which was the first video game ever made?,Pong,Space Invaders,Tetris,Tennis for Two,Tennis for Two,What company owns Android?,Samsung,Microsoft,Google,Apple,Google,Which key is often used to refresh a web page?,F2,F5,Ctrl + R,F9,F5,What is the maximum number of characters allowed in a tweet (as of 2023)?,140,200,280,500,280,What does VPN stand for?,Virtual Private Network,Virtual Public Network,Verified Personal Network,Virtual Protected Node,Virtual Private Network,Which programming language is used to build iOS apps?,Swift,Java,Python,C#,Swift,What does “AI” stand for?,Artificial Integration,Automated Intelligence,Artificial Intelligence,Applied Internet,Artificial Intelligence,Which company developed the PlayStation console?,Nintendo,Sony,Microsoft,Sega,Sony,What is the most widely used operating system in the world?,macOS,Linux,Windows,Android,Android,What does HTML stand for?,HyperText Markup Language,High Transfer Machine Language,Hyper Transfer Markup Language,Hyperlink Text Machine Logic,HyperText Markup Language,Who co-founded Microsoft with Bill Gates?,Steve Wozniak,Paul Allen,Larry Page,Mark Zuckerberg,Paul Allen,What year was Facebook launched?,2002,2004,2006,2008,2004,Which was the first search engine on the internet?,Yahoo!,Google,Archie,AltaVista,Archie,Which tech company has the slogan “Think Different”?,Microsoft,Apple,IBM,Samsung,Apple,What is the name of the first computer virus?,Creeper,Brain,ILOVEYOU,Melissa,Creeper,Which programming language runs natively in web browsers?,C++,Java,JavaScript,Python,JavaScript,Which company owns GitHub?,Apple,Google,Microsoft,Amazon,Microsoft,What does “5G” stand for?,5th Generation,5 Gigabytes,5th Grid,Fifth Global,5th Generation,Which device was the first commercially successful personal computer?,Apple I,Commodore 64,IBM PC,Altair 8800,Commodore 64,Which cryptocurrency was the first ever created?,Ethereum,Dogecoin,Bitcoin,Litecoin,Bitcoin".split(",")
        qstion = questions[0 + (kahootcount * 6)]
        ans1 = questions[1 + (kahootcount * 6)]
        ans2 = questions[2 + (kahootcount * 6)]
        ans3 = questions[3 + (kahootcount * 6)]
        ans4 = questions[4 + (kahootcount * 6)]
        ans = questions[5 + (kahootcount * 6)]
        kahootcount += 1
        if kahootcount == 30:
            renpy.jump("after_kahoot")
        renpy.jump("kahootq")




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


    # st "Heyyyy see if you can accept my pull request plzzzz"
    
    # Call the challenge properly
    # call code_challenge_1
    