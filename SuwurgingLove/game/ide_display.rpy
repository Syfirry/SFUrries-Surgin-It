init python:
    import re
    
    # Syntax highlighting patterns for common languages
    SYNTAX_PATTERNS = {
        'python': {
            'keywords': r'\b(def|class|if|else|elif|for|while|try|except|finally|import|from|return|yield|lambda|with|as|pass|break|continue|and|or|not|in|is|None|True|False)\b',
            'strings': r'(["\'])(?:(?=(\\?))\2.)*?\1',
            'comments': r'#.*$',
            'numbers': r'\b\d+\.?\d*\b',
            'functions': r'\b(\w+)(?=\s*\()',
        },
        'javascript': {
            'keywords': r'\b(function|var|let|const|if|else|for|while|do|switch|case|default|try|catch|finally|return|break|continue|class|extends|import|export|async|await|true|false|null|undefined)\b',
            'strings': r'(["\'])(?:(?=(\\?))\2.)*?\1|`[^`]*`',
            'comments': r'//.*$|/\*[\s\S]*?\*/',
            'numbers': r'\b\d+\.?\d*\b',
            'functions': r'\b(\w+)(?=\s*\()',
        },
        'java': {
            'keywords': r'\b(public|private|protected|static|final|abstract|class|interface|extends|implements|if|else|for|while|do|switch|case|default|try|catch|finally|return|break|continue|new|this|super|true|false|null|void|int|String|boolean|double|float|long|short|char)\b',
            'strings': r'"(?:[^"\\]|\\.)*"',
            'comments': r'//.*$|/\*[\s\S]*?\*/',
            'numbers': r'\b\d+\.?\d*[fFdDlL]?\b',
            'functions': r'\b(\w+)(?=\s*\()',
        }
    }
    
    def highlight_code(code, language='python'):
        """Apply syntax highlighting to code"""
        if language not in SYNTAX_PATTERNS:
            language = 'python'
        
        patterns = SYNTAX_PATTERNS[language]
        highlighted = code
        
        # Apply highlighting (replace with color tags)
        for pattern_type, pattern in patterns.items():
            if pattern_type == 'keywords':
                highlighted = re.sub(pattern, r'{color=#569cd6}\1{/color}', highlighted, flags=re.MULTILINE)
            elif pattern_type == 'strings':
                highlighted = re.sub(pattern, r'{color=#ce9178}\g<0>{/color}', highlighted, flags=re.MULTILINE)
            elif pattern_type == 'comments':
                highlighted = re.sub(pattern, r'{color=#6a9955}\g<0>{/color}', highlighted, flags=re.MULTILINE)
            elif pattern_type == 'numbers':
                highlighted = re.sub(pattern, r'{color=#b5cea8}\1{/color}', highlighted, flags=re.MULTILINE)
            elif pattern_type == 'functions':
                highlighted = re.sub(pattern, r'{color=#dcdcaa}\1{/color}', highlighted, flags=re.MULTILINE)
        
        return highlighted

# Define persistent variables
default code_challenge_data = {}
default current_challenge_id = None