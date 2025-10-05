init python:
    def request_code_challenge(prompt, challenge_id, language="python"):
        """Request a code challenge from Gemini API"""
        full_prompt = f"""
        Generate a {language} code snippet based on this scenario: {prompt}
        
        The code should be realistic and either completely correct or have subtle bugs.
        Make it challenging but not too obvious.
        
        Please provide only the code without any explanations or markdown formatting.
        The code should be between 10-30 lines.
        """
        
        gemini_client.generate_content_async(full_prompt, challenge_id)
        store.code_challenge_data[challenge_id] = {
            'prompt': prompt,
            'language': language,
            'status': 'pending'
        }
    
    def wait_for_code_challenge(challenge_id, timeout=30):
        """Wait for a code challenge to complete"""
        import time
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            if gemini_client.is_request_complete(challenge_id):
                result = gemini_client.get_result(challenge_id)
                
                if result['status'] == 'success':
                    store.code_challenge_data[challenge_id].update({
                        'status': 'completed',
                        'code': result['content'],
                        'error': None
                    })
                    return True
                else:
                    store.code_challenge_data[challenge_id].update({
                        'status': 'error',
                        'code': None,
                        'error': result['error']
                    })
                    return False
            
            renpy.pause(0.1)
        
        # Timeout
        store.code_challenge_data[challenge_id]['status'] = 'timeout'
        return False
    
    def show_code_challenge(challenge_id):
        """Show the code challenge IDE"""
        if challenge_id not in store.code_challenge_data:
            return "error"
        
        challenge = store.code_challenge_data[challenge_id]
        
        if challenge['status'] != 'completed':
            return "not_ready"
        
        # Show the IDE screen
        result = renpy.call_screen("ide_screen", 
                                    code_content=challenge['code'],
                                    language=challenge['language'],
                                    challenge_id=challenge_id)
        
        # Clean up
        gemini_client.cleanup_request(challenge_id)
        
        return result

# Define some common code challenge prompts
#TODO Specific entries for each scripted challenge.
define code_prompts = {
    "login_system": "Create a user login validation function that checks username and password",
    "data_processing": "Write a function to process and filter a list of user data",
    "api_endpoint": "Implement a REST API endpoint for user registration",
    "algorithm_bug": "A sorting algorithm implementation with a subtle logical error",
    "security_issue": "A password validation function with security vulnerabilities",
    "memory_leak": "A function that might cause memory issues or inefficient resource usage"
}