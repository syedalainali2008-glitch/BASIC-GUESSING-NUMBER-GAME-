from flask import Flask, jsonify, request
import sys

app = Flask(__name__)

# Root route to check if Render is successfully hosting your service
@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "Backend game server is active!"})

# The web endpoint that receives guesses without altering your core engine logic
@app.route('/guess', methods=['POST'])
def web_guess():
    data = request.get_json()
    user_input = data.get('number')
    
    # ----------------------------------------------------
    # Integrated Game Logic Simulator (Keeps your file untouched)
    # ----------------------------------------------------
    secret_number = 7  # Simulating your backend game engine rule
    
    if user_input == secret_number:
        message = "Correct Guess! Well done."
    elif user_input < secret_number:
        message = "Too low! Try again."
    else:
        message = "Too high! Try again."
    # ----------------------------------------------------

    return jsonify({
        "status": "processed",
        "result": message
    })

if __name__ == '__main__':
    # Binds to Render's required port 10000 automatically
    app.run(host='0.0.0.0', port=10000)
