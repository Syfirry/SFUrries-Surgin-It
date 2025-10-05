
init python:
    import urllib.request
    import json
    import os
    import ssl
    
    # TODO: Create seperate config file for these endpoints
    model_endpoints = {
        "gemini-flash":"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=",
    }
    
    def load_api_key(**kwargs):
        path = kwargs.get("path", "./api_key.txt")
        key_file = os.path.join(config.gamedir, "api_key.txt")
        print(key_file)
        if os.path.exists(key_file):
            try:
                with open(key_file, 'r') as f:
                    print("ping")
                    return f.read()
            except Exception as e:
                print("Error: could not extract key file at: " + key_file + "Exception: " + e)        
        return os.environ.get("GEMINI_API_KEY")

    def call_gemini(prompt, **kwargs):

        model = kwargs.get('model', 'gemini-flash')
        temperature = kwargs.get('temperature', 0.7)
        max_tokens = kwargs.get('max_tokens', 1000)
        system_message = kwargs.get('system_message', None)
        
        api_key = load_api_key()
        print(api_key)

        url = str(model_endpoints.get(model, "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key="))
        url = url + api_key

        data = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }]
        }
        
        try:
            # Create SSL context that doesn't verify certificates - We're not writing Secure Software *wink*
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            
            req = urllib.request.Request(
                url,
                data=json.dumps(data).encode('utf-8'),
                headers={'Content-Type': 'application/json'}
            )
            
            with urllib.request.urlopen(req, context=ssl_context) as response:
                result = json.loads(response.read().decode('utf-8'))
                return result['candidates'][0]['content']['parts'][0]['text']
                
        except Exception as e:
            renpy.notify(f"AI Error: {str(e)}")
            return f"AI unavailable: {str(e)}"
    
    def custom_function():
        return call_gemini("Explain how AI works in a few words")