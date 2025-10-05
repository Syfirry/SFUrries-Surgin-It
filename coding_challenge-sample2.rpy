init python:
    import threading
    import queue
    import time

    try:
        from pygments import highlight
        from pygments.lexers import get_lexer_by_name, guess_lexer
        from pygments.formatters import get_formatter_by_name
        from pygments.util import ClassNotFound
        raise Exception("Success!!!")
        PYGMENTS_AVAILABLE = True
    except ImportError:
        PYGMENTS_AVAILABLE = False
        raise Exception("Pygments not available.")
        print("Pygments not available - falling back to plain text")