init -1 python:
    import requests
    import json
    import threading
    from store import *

    def load_api_key (**kwargs):
        path = kwargs.get("path", "api_key.txt")
        key_file = os.path.join(config.gamedir, "api_key.txt")
        print(key_file)
        if os.path.exists(key_file):
            try:
                with open(key_file, 'r') as f:
                    return f.read()
            except Exception as e:
                print("Error: could not extract key file at: " + key_file + "Exception: " + e)        
        return os.environ.get("GEMINI_API_KEY")

    class GeminiAPI:
        def __init__(self, api_key, model_name):
            self.base_url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent"
            self.api_key = api_key
            self.pending_requests = {}
            self.completed_requests = {}
        
        def generate_content_async(self, prompt, request_id):
            """Generate content asynchronously"""
            def make_request():
                try:
                    headers = {
                        'Content-Type': 'application/json',
                    }
                    
                    data = {
                        "contents": [
                            {
                                "parts": [
                                    {"text": prompt}
                                ]
                            }
                        ]
                    }
                    
                    url = f"{self.base_url}?key={self.api_key}"
                    response = requests.post(url, headers=headers, json=data, timeout=30)
                    
                    if response.status_code == 200:
                        result = response.json()
                        content = result['candidates'][0]['content']['parts'][0]['text']
                        self.completed_requests[request_id] = {
                            'status': 'success',
                            'content': content,
                            'error': None
                        }
                    else:
                        self.completed_requests[request_id] = {
                            'status': 'error',
                            'content': None,
                            'error': f"API Error: {response.status_code}"
                        }
                        
                except Exception as e:
                    self.completed_requests[request_id] = {
                        'status': 'error',
                        'content': None,
                        'error': str(e)
                    }
                finally:
                    if request_id in self.pending_requests:
                        del self.pending_requests[request_id]
            
            # Start the request in a separate thread
            thread = threading.Thread(target=make_request)
            thread.daemon = True
            self.pending_requests[request_id] = thread
            thread.start()
        
        def is_request_complete(self, request_id):
            """Check if a request is complete"""
            return request_id in self.completed_requests
        
        def get_result(self, request_id):
            """Get the result of a completed request"""
            return self.completed_requests.get(request_id)
        
        def cleanup_request(self, request_id):
            """Clean up completed request data"""
            if request_id in self.completed_requests:
                del self.completed_requests[request_id]

    # Initialize the API client
    # Replace with your actual Gemini API key
    gemini_client = GeminiAPI(load_api_key(), "gemini-2.5-flash")