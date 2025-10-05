init python:
    try:
        from pygments import highlight
        from pygments.lexers import get_lexer_by_name, guess_lexer
        from pygments.formatters import get_formatter_by_name
        from pygments.styles import get_style_by_name, get_all_styles
        from pygments.token import Token
        import pygments.util
        PYGMENTS_AVAILABLE = True
        
        # Get available styles for debugging
        available_styles = list(get_all_styles())
        print("Available Pygments styles:", available_styles)
        
    except ImportError:
        PYGMENTS_AVAILABLE = False
        print("Warning: Pygments not available. Install with: pip install pygments")
    
    class RenpyFormatter:
        """Custom formatter to convert Pygments tokens to Renpy color tags"""
        
        def __init__(self, style_name='monokai'):
            self.style = None
            
            if PYGMENTS_AVAILABLE:
                try:
                    # Try the requested style, fallback to 'monokai', then 'default'
                    style_fallbacks = [style_name, 'monokai', 'default', 'colorful']
                    
                    for style in style_fallbacks:
                        try:
                            self.style = get_style_by_name(style)
                            print(f"Using Pygments style: {style}")
                            break
                        except pygments.util.ClassNotFound:
                            continue
                    
                    if self.style is None:
                        print("Warning: No valid Pygments style found, using manual colors")
                        
                except Exception as e:
                    print(f"Error initializing Pygments style: {e}")
            
            # VS Code Dark theme color mapping (manual fallback)
            self.token_colors = {
                Token.Keyword: "#569cd6",           # Keywords (def, class, if, etc.)
                Token.Keyword.Constant: "#569cd6",  # True, False, None
                Token.Keyword.Namespace: "#569cd6", # import, from
                Token.Keyword.Declaration: "#569cd6", # var, let, const
                Token.Keyword.Type: "#569cd6",      # int, string, etc.
                
                Token.String: "#ce9178",            # String literals
                Token.String.Single: "#ce9178",
                Token.String.Double: "#ce9178",
                Token.String.Doc: "#6a9955",        # Docstrings
                Token.String.Heredoc: "#ce9178",
                Token.String.Regex: "#d16969",
                
                Token.Comment: "#6a9955",           # Comments
                Token.Comment.Single: "#6a9955",
                Token.Comment.Multiline: "#6a9955",
                Token.Comment.Hashbang: "#6a9955",
                Token.Comment.Special: "#6a9955",
                
                Token.Number: "#b5cea8",            # Numbers
                Token.Number.Integer: "#b5cea8",
                Token.Number.Float: "#b5cea8",
                Token.Number.Hex: "#b5cea8",
                Token.Number.Oct: "#b5cea8",
                Token.Number.Bin: "#b5cea8",
                
                Token.Name.Function: "#dcdcaa",     # Function names
                Token.Name.Function.Magic: "#dcdcaa",
                Token.Name.Method: "#dcdcaa",
                
                Token.Name.Class: "#4ec9b0",        # Class names
                Token.Name.Builtin: "#4ec9b0",      # Built-in functions
                Token.Name.Exception: "#4ec9b0",    # Exception names
                Token.Name.Namespace: "#4ec9b0",    # Module names
                
                Token.Operator: "#d4d4d4",          # Operators
                Token.Operator.Word: "#569cd6",     # and, or, not
                
                Token.Punctuation: "#d4d4d4",       # Punctuation
                
                Token.Name: "#9cdcfe",              # Variable names
                Token.Name.Variable: "#9cdcfe",
                Token.Name.Variable.Instance: "#9cdcfe",
                Token.Name.Variable.Class: "#9cdcfe",
                Token.Name.Variable.Global: "#9cdcfe",
                Token.Name.Attribute: "#9cdcfe",
                
                Token.Text: "#d4d4d4",              # Default text
                Token.Text.Whitespace: "#d4d4d4",
                
                Token.Error: "#f44747",             # Errors
                
                # Additional tokens
                Token.Name.Decorator: "#ffb86c",    # Decorators (@property)
                Token.Name.Tag: "#ff79c6",          # HTML tags
                Token.Name.Constant: "#bd93f9",     # Constants
                Token.Name.Entity: "#50fa7b",       # HTML entities
                Token.Name.Label: "#ffb86c",        # Labels
            }
        
        def get_color_for_token(self, token):
            """Get color for a specific token type"""
            # Try exact match first
            if token in self.token_colors:
                return self.token_colors[token]
            
            # Try parent token types
            current_token = token
            while current_token.parent:
                current_token = current_token.parent
                if current_token in self.token_colors:
                    return self.token_colors[current_token]
            
            # Default color
            return "#d4d4d4"
        
        def format_tokens(self, tokens):
            """Format tokens into Renpy markup"""
            result = ""
            for token, value in tokens:
                if not value:  # Skip empty values
                    continue
                    
                # Escape any existing curly braces in the value
                escaped_value = value.replace("{", "{{").replace("}", "}}")
                
                # Skip whitespace-only tokens or apply color
                if value.strip():
                    color = self.get_color_for_token(token)
                    result += "{{color={}}}{}{{/color}}".format(color, escaped_value)
                else:
                    result += escaped_value
                    
            return result
    
    # Initialize the formatter with error handling
    try:
        renpy_formatter = RenpyFormatter('monokai')
    except Exception as e:
        print(f"Error creating RenpyFormatter: {e}")
        renpy_formatter = None
    
    def highlight_code_pygments(code, language='python'):
        """Apply syntax highlighting to code using Pygments"""
        if not PYGMENTS_AVAILABLE or renpy_formatter is None:
            # Fallback to plain text with default color
            escaped_code = code.replace("{", "{{").replace("}", "}}")
            return "{color=#d4d4d4}" + escaped_code + "{/color}"
        
        try:
            # Clean up the code first
            code = code.strip()
            if not code:
                return ""
            
            # Get the appropriate lexer
            lexer = None
            if language and language != 'text':
                try:
                    lexer = get_lexer_by_name(language, stripnl=False, stripall=False)
                except pygments.util.ClassNotFound:
                    print(f"Lexer not found for language: {language}")
                    try:
                        lexer = guess_lexer(code)
                    except:
                        pass
            
            if lexer is None:
                try:
                    lexer = guess_lexer(code)
                except:
                    # Ultimate fallback - treat as plain text
                    escaped_code = code.replace("{", "{{").replace("}", "}}")
                    return "{color=#d4d4d4}" + escaped_code + "{/color}"
            
            # Tokenize the code
            tokens = list(lexer.get_tokens(code))
            
            # Format tokens with our custom formatter
            highlighted = renpy_formatter.format_tokens(tokens)
            
            return highlighted
            
        except Exception as e:
            print(f"Error highlighting code: {e}")
            # Fallback to plain text
            escaped_code = code.replace("{", "{{").replace("}", "}}")
            return "{color=#d4d4d4}" + escaped_code + "{/color}"
    
    def get_language_from_extension(filename):
        """Get language from file extension"""
        if not PYGMENTS_AVAILABLE:
            return 'text'
            
        extension_map = {
            '.py': 'python',
            '.js': 'javascript',
            '.jsx': 'jsx',
            '.ts': 'typescript',
            '.tsx': 'tsx',
            '.java': 'java',
            '.cpp': 'cpp',
            '.cxx': 'cpp',
            '.cc': 'cpp',
            '.c': 'c',
            '.h': 'c',
            '.cs': 'csharp',
            '.php': 'php',
            '.rb': 'ruby',
            '.go': 'go',
            '.rs': 'rust',
            '.html': 'html',
            '.htm': 'html',
            '.css': 'css',
            '.scss': 'scss',
            '.sass': 'sass',
            '.sql': 'sql',
            '.xml': 'xml',
            '.json': 'json',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.sh': 'bash',
            '.bash': 'bash',
            '.zsh': 'zsh',
            '.fish': 'fish',
            '.ps1': 'powershell',
            '.r': 'r',
            '.R': 'r',
            '.m': 'matlab',
            '.swift': 'swift',
            '.kt': 'kotlin',
            '.scala': 'scala',
            '.clj': 'clojure',
            '.hs': 'haskell',
            '.ml': 'ocaml',
            '.fs': 'fsharp',
            '.ex': 'elixir',
            '.exs': 'elixir',
            '.erl': 'erlang',
            '.lua': 'lua',
            '.pl': 'perl',
            '.vim': 'vim',
        }
        
        filename_lower = filename.lower()
        for ext, lang in extension_map.items():
            if filename_lower.endswith(ext):
                return lang
        
        return 'text'
    
    def get_supported_languages():
        """Get list of supported languages"""
        if not PYGMENTS_AVAILABLE:
            return ['text', 'python', 'javascript', 'java']
        
        try:
            from pygments.lexers import get_all_lexers
            lexers = get_all_lexers()
            languages = []
            for name, aliases, filenames, mimetypes in lexers:
                if aliases:
                    languages.extend(aliases)
            return sorted(set(languages))
        except:
            return ['text', 'python', 'javascript', 'java', 'cpp', 'c', 'csharp']

# Define persistent variables
default code_challenge_data = {}
default current_challenge_id = None

# Test the syntax highlighting
init python:
    # Test code to verify highlighting works
    test_code = '''def hello_world(name):
    """A simple greeting function"""
    if name:
        print(f"Hello, {name}!")
        return True
    else:
        print("Hello, World!")
        return False

# Test the function
result = hello_world("Developer")'''
    
    print("Testing syntax highlighting...")
    try:
        highlighted_test = highlight_code_pygments(test_code, 'python')
        print("Syntax highlighting test successful")
    except Exception as e:
        print(f"Syntax highlighting test failed: {e}")