




# Typing Speed Test - IDE Style for Ren'Py

init python:
    import time
    class TypingTest:
        def __init__(self, prompt):
            self.prompt = prompt
            self.start_time = None
            self.end_time = None
            self.user_input = ""
            self.finished = False
            self.wpm = 0
            self.accuracy = 0
        def start(self):
            self.start_time = time.time()
            self.finished = False
            self.user_input = ""
        def finish(self):
            self.end_time = time.time()
            self.finished = True
            self.calculate_results()
        def calculate_results(self):
            elapsed = max(1, self.end_time - self.start_time)
            words = len(self.user_input.split())
            self.wpm = int(words / (elapsed / 60))
            correct = sum(1 for a, b in zip(self.user_input, self.prompt) if a == b)
            self.accuracy = int(100 * correct / max(1, len(self.prompt)))
        def get_colored_prompt(self):
            # Returns a list of (char, color) tuples for prompt rendering
            result = []
            for i, c in enumerate(self.prompt):
                if i < len(self.user_input):
                    if self.user_input[i] == c:
                        result.append((c, "#ffffff")) # correct: white
                    else:
                        result.append((self.user_input[i], "#ff3c3c")) # incorrect: red, show wrong char
                else:
                    result.append((c, "#b8b8b8")) # untouched: gray
            # Auto-finish if all characters typed
            if not self.finished and len(self.user_input) >= len(self.prompt):
                self.finish()
            return result
    typing_test_prompt = "def hello_world():\n    print('Hello, world!')"
    typing_test = TypingTest(typing_test_prompt)

screen typing_test_ide():
    tag ide_typing_test
    modal True
    frame:
        background Solid("#23272e")
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        vbox:
            spacing 20
            text "Typing Speed Test" style "ide_title"
            text "Type the code below as fast and accurately as you can:" style "ide_label"
            frame:
                background Solid("#181a20")
                padding (20, 20)
                hbox:
                    spacing 0
                    for char, color in typing_test.get_colored_prompt():
                        text char style "ide_code" color color
                input value VariableInputValue("typing_test.user_input") length 200 style "ide_input_hidden" multiline True
            if typing_test.finished:
                text "WPM: [typing_test.wpm]" style "ide_result"
                text "Accuracy: [typing_test.accuracy]%" style "ide_result"
                textbutton "Close" action Hide("typing_test_ide") style "ide_button"
            else:
                textbutton "Submit" action Function(typing_test.finish) style "ide_button"

style ide_input_hidden is default:
    font "gui/FiraCode-Regular.ttf"
    size 24
    color "#00000000" # transparent text
    background Solid("#23272e")
    xmaximum 600

style ide_title is default:
    font "gui/FiraCode-Regular.ttf"
    size 40
    color "#7ec7ff"
    bold True

style ide_label is default:
    font "gui/FiraCode-Regular.ttf"
    size 22
    color "#b8b8b8"

style ide_code is default:
    font "gui/FiraCode-Regular.ttf"
    size 24
    color "#b8b8b8"
    background None

style ide_input is default:
    font "gui/FiraCode-Regular.ttf"
    size 24
    color "#e3e3e3"
    background Solid("#23272e")
    xmaximum 600

style ide_result is default:
    font "gui/FiraCode-Regular.ttf"
    size 28
    color "#7ec7ff"

style ide_button is default:
    font "gui/FiraCode-Regular.ttf"
    size 24
    background Solid("#7ec7ff")
    color "#e3e3e3"
    padding (10, 10)

label typing_test:
    $ typing_test.start()
    show screen typing_test_ide
    "Ready to test your typing speed?"
    "Type the code and submit when done."
    $ renpy.pause(0.5)
    while not typing_test.finished:
        $ renpy.pause(0.1)
    $ renpy.pause(1.0)
    hide screen typing_test_ide
    "Test complete."