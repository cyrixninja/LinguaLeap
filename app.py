from flask import Flask, request, jsonify, render_template
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
groq = ChatGroq(
    api_key=os.getenv('groq_api_key'),
    model_name="mixtral-8x7b-32768"
)

# Store accumulated text for each session
session_texts = {}
user_preferences = {}
CHAR_THRESHOLD = 150

def count_words(text):
    return len(text.split())

def vocab_enhance(text):
    prompt = PromptTemplate.from_template("""
    Analyze the following text and provide:
    1. Vocabulary enhancement (sophisticated alternatives) by taking the given text and providing a more sophisticated alternative for each word.
    2. Give me output in the format: original_word -> sophisticated_word
    3. All the improvements should be in one single line and maximum 150 characters. Don't exceed that
    4. Strictly just give the output and nothing else. No Comments to the user. 
    5. Response Example - Enhanced vocabulary : good -> delightful , smart -> intelligent , bad -> malevolent . Strictly follow this format.STRICTLY Don't include original text in reponse. Don't exceed 150 characters.
    6. Don't include the words if no sophisticated alternative is available.                  
    Input Text: {text}
    """)
    response = groq.invoke(prompt.format(text=text))
    return response.content

def grammer_corrections(text):
    prompt = PromptTemplate.from_template("""
    Analyze the following text and provide:
    1. Grammar corrections if needed
    2. Style improvements
    2. All the improvements should be in one single line and maximum 150 characters. Don't exceed that
    3. Strictly just give the output and nothing else. No Comments to the user. STRICTLY Don't include original text in reponse.                                 
    Text: {text}
    """)
    response = groq.invoke(prompt.format(text=text))
    return response.content

def simplify_sentence(text):
    prompt = PromptTemplate.from_template("""
    Simplify the following text while maintaining its core meaning. 
    - Maximum response length: 150 characters
    - Return only the simplified text
    - No explanations or additional text
    
    Input text: {text}
    """)
    response = groq.invoke(prompt.format(text=text))
    return response.content

def check_cultural_sensitivity(text):
    prompt = PromptTemplate.from_template("""
    Review the text below for culturally insensitive or inappropriate phrases. Return flagged phrases and suggestions for improvement.
    Give a small response if no sensitive phrases are found.

    Rules:
    - Maximum response length: 150 characters
    - Return only the flagged phrases and suggestions
                                          
    Input text: {text}
    """)
    response = groq.invoke(prompt.format(text=text))
    return response.content

def tone_adjust_friendly(text, target_tone="friendly"):
    prompt = PromptTemplate.from_template("""
    Rewrite the text below in a {tone} tone. 
    
    Rules:
    - Maintain core meaning and key information
    - Adapt language to match requested tone
    - Keep approximately same length
    - Maximum response length: 150 characters
    - Return only the modified text
    - No explanations or additional text
    
    Input text: {text}
    """)
    response = groq.invoke(prompt.format(text=text, tone=target_tone))
    return response.content

def tone_adjust_casual(text, target_tone="casual"):
    prompt = PromptTemplate.from_template("""
    Rewrite the text below in a {tone} tone. 
    
    Rules:
    - Maintain core meaning and key information
    - Adapt language to match requested tone
    - Keep approximately same length
    - Maximum response length: 150 characters
    - Return only the modified text
    - No explanations or additional text
    
    Input text: {text}
    """)
    response = groq.invoke(prompt.format(text=text, tone=target_tone))
    return response.content

def tone_adjust_professional(text, target_tone="professional"):
    prompt = PromptTemplate.from_template("""
    Rewrite the text below in a {tone} tone. 
    
    Rules:
    - Maintain core meaning and key information
    - Adapt language to match requested tone
    - Keep approximately same length
    - Maximum response length: 150 characters
    - Return only the modified text
    - No explanations or additional text
    
    Input text: {text}
    """)
    response = groq.invoke(prompt.format(text=text, tone=target_tone))
    return response.content

@app.route('/login', methods=['GET', 'POST'])
def login():
    uid = request.args.get('uid')
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            preferred_function = request.form.get('preferred_function')
            
            if preferred_function not in ['vocab_enhance', 'grammer_corrections', 'simplify_sentence', 'check_cultural_sensitivity', 'tone_adjust_friendly', 'tone_adjust_casual', 'tone_adjust_professional']:
                return jsonify({'error': 'Invalid function choice'}), 400
            
            user_preferences[uid] = {
                'name': name,
                'preferred_function': preferred_function
            }
            
            return jsonify({'message': 'Login successful'}), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return render_template('login.html')

@app.route('/setup_status', methods=['GET'])
def setup_status():
    uid = request.args.get('uid')
    if uid in user_preferences:
        return jsonify({'is_setup_completed': True})
    else:
        return jsonify({'is_setup_completed': False})
    
@app.route('/transcript', methods=['POST'])
def receive_json():
    try:
        uid = request.args.get('uid')
        if uid not in user_preferences:
            return jsonify({'error': 'Unauthorized'}), 401
        
        data = request.get_json()
        session_id = data.get('session_id')
        
        # Extract new text from segments
        new_text = " ".join([segment['text'] for segment in data['segments'] if segment['text']])
        
        # Initialize or append to session text
        if session_id not in session_texts:
            session_texts[session_id] = ""
        session_texts[session_id] += " " + new_text
        
        current_text = session_texts[session_id].strip()
        char_length = len(current_text)
        
        if char_length >= CHAR_THRESHOLD:
            # Analyze the accumulated text based on user preference
            preferred_function = user_preferences[uid]['preferred_function']
            if preferred_function == 'vocab_enhance':
                analysis = vocab_enhance(current_text)
            elif preferred_function == 'grammer_corrections':
                analysis = grammer_corrections(current_text)
            elif preferred_function == 'simplify_sentence':
                analysis = simplify_sentence(current_text)
            elif preferred_function == 'check_cultural_sensitivity':
                analysis = check_cultural_sensitivity(current_text)
            elif preferred_function == 'tone_adjust_friendly':
                analysis = tone_adjust_friendly(current_text)
            elif preferred_function == 'tone_adjust_casual':
                analysis = tone_adjust_casual(current_text)
            elif preferred_function == 'tone_adjust_professional':
                analysis = tone_adjust_professional(current_text)
            
            # Clear the accumulated text
            session_texts[session_id] = ""
            return jsonify({
                'message': analysis,
            })

        # Simple 200 response while accumulating
        return jsonify({}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)