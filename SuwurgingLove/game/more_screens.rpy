screen ide_screen(code_content, language="python", challenge_id=None, filename="main.py"):
    modal True
    
    # Hide the quick menu during the coding challenge
    on "show" action SetVariable("quick_menu", False)
    on "hide" action SetVariable("quick_menu", True)
    
    # IDE background
    add "#1e1e1e"
    
    # IDE window
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1400
        ysize 900
        background "#252526"
        padding (20, 20)
        
        vbox:
            spacing 10
            
            # IDE title bar
            frame:
                xfill True
                ysize 50
                background "#2d2d30"
                padding (15, 10)
                
                hbox:
                    spacing 20
                    yalign 0.5
                    
                    text "DevStory IDE" color "#cccccc" size 20 bold True
                    text "-" color "#858585" size 16
                    text filename color "#cccccc" size 16
                    
                    null width 1.0  # Push to right
                    
                    text f"Language: {language.title()}" color "#858585" size 14
            
            # File tabs (simulated)
            frame:
                xfill True
                ysize 35
                background "#2d2d30"
                padding (10, 5)
                
                hbox:
                    spacing 5
                    
                    frame:
                        background "#1e1e1e"
                        padding (15, 8)
                        
                        text filename color "#ffffff" size 14
            
            # Code editor area
            frame:
                xfill True
                yfill True
                background "#1e1e1e"
                padding (0, 0)
                
                hbox:
                    spacing 0
                    
                    # Line numbers column
                    python:
                        lines = code_content.split('\n')
                        line_count = len(lines)
                        max_digits = len(str(line_count))
                        line_number_width = max(60, max_digits * 12 + 20)
                    
                    frame:
                        xsize line_number_width
                        yfill True
                        background "#252526"
                        padding (10, 15)
                        
                        viewport:
                            scrollbars None
                            
                            vbox:
                                spacing 0
                                
                                for i in range(len(lines)):
                                    text str(i + 1) color "#858585" size 14 font "gui/FiraCode-Regular.ttf" text_align 1.0 xfill True
                    
                    # Code content area
                    frame:
                        xfill True
                        yfill True
                        background "#1e1e1e"
                        padding (15, 15)
                        
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            
                            vbox:
                                spacing 0
                                
                                python:
                                    highlighted_code = highlight_code_pygments(code_content, language)
                                    highlighted_lines = highlighted_code.split('\n')
                                
                                for line in highlighted_lines:
                                    if line.strip():
                                        text "[line]" size 14 font "gui/FiraCode-Regular.ttf" layout "tex"
                                    else:
                                        null height 21  # Empty line height
            
            # Challenge question and buttons
            if challenge_id:
                frame:
                    xfill True
                    ysize 150
                    background "#2d2d30"
                    padding (20, 20)
                    
                    vbox:
                        spacing 20
                        
                        text "Code Review Challenge" color "#cccccc" size 22 bold True
                        text "Analyze the code above and determine if it's correct or has issues." color "#cccccc" size 16
                        
                        hbox:
                            spacing 30
                            xalign 0.5
                            
                            textbutton "✓ Code is Correct":
                                action [
                                    SetVariable("player_answer", True),
                                    Return("answer_given")
                                ]
                                text_size 18
                                text_color "#ffffff"
                                background "#0e639c"
                                hover_background "#1177bb"
                                padding (25, 12)
                                text_font "gui/FiraCode-Regular.ttf"
                            
                            textbutton "✗ Code has Issues":
                                action [
                                    SetVariable("player_answer", False),
                                    Return("answer_given")
                                ]
                                text_size 18
                                text_color "#ffffff"
                                background "#a74a44"
                                hover_background "#c1554d"
                                padding (25, 12)
                                text_font "gui/FiraCode-Regular.ttf"
                            
                            textbutton "→ Skip Challenge":
                                action Return("skip")
                                text_size 18
                                text_color "#cccccc"
                                background "#404040"
                                hover_background "#505050"
                                padding (25, 12)
                                text_font "gui/FiraCode-Regular.ttf"

# Enhanced loading screen
screen loading_screen(message="Generating code challenge...", show_progress=True):
    modal True
    
    add "#000000e0"
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 500
        ysize 250
        background "#252526"
        padding (40, 40)
        
        vbox:
            spacing 25
            xalign 0.5
            yalign 0.5
            
            # Loading icon (simulated with text)
            text "⚡" color "#569cd6" size 48 text_align 0.5 xfill True
            
            text message color "#cccccc" size 20 text_align 0.5 xfill True
            
            if show_progress:
                # Simple animated dots
                text "Processing your request..." color "#858585" size 16 text_align 0.5 xfill True

# Code preview screen (for showing code without challenges)
screen code_preview_screen(code_content, language="python", filename="preview.py", title="Code Preview"):
    modal True
    
    add "#1e1e1e"
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1200
        ysize 800
        background "#252526"
        padding (20, 20)
        
        vbox:
            spacing 10
            
            # Title bar
            frame:
                xfill True
                ysize 50
                background "#2d2d30"
                padding (15, 10)
                
                hbox:
                    yalign 0.5
                    spacing 20
                    
                    text title color "#cccccc" size 20 bold True
                    text "-" color "#858585" size 16
                    text filename color "#cccccc" size 16
            
            # Code display (reuse the code area from IDE screen)
            frame:
                xfill True
