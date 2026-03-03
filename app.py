import os
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Home Safety Chatbot</title>
<style>
body {
    background:#121212;
    color:white;
    font-family:Arial, sans-serif;
    text-align:center;
    margin:0;
    padding:0;
}

h2 {
    margin-top:20px;
    color:#00ffcc;
}

.chat-box {
    width:90%;
    max-width:500px;
    margin:20px auto;
    background:#1e1e1e;
    padding:15px;
    border-radius:10px;
    height:400px;
    overflow-y:auto;
    text-align:left;
}

.message {
    margin:8px 0;
}

.user {
    color:#00ffcc;
}

.bot {
    color:#ffffff;
}

.typing {
    color:#888;
    font-style:italic;
}

.input-area {
    margin-bottom:30px;
}

input {
    width:65%;
    padding:10px;
    border-radius:5px;
    border:none;
    outline:none;
}

button {
    padding:10px 15px;
    border:none;
    border-radius:5px;
    background:#00ffcc;
    cursor:pointer;
    font-weight:bold;
}

button:hover {
    background:#00ccaa;
}
</style>
</head>
<body>

<h2>🏠 Smart Home Safety Bot</h2>

<div class="chat-box" id="chat"></div>

<div class="input-area">
<input type="text" id="message" placeholder="Type your message..." onkeypress="if(event.key==='Enter') sendMessage()">
<button onclick="sendMessage()">Send</button>
</div>

<script>
function sendMessage(){
    let msg = document.getElementById("message").value;
    if(msg === "") return;

    let chat = document.getElementById("chat");

    // show user message
    chat.innerHTML += "<div class='message user'><b>You:</b> " + msg + "</div>";
    document.getElementById("message").value="";

    // add typing indicator
    chat.innerHTML += "<div class='message typing' id='typing'><b>Bot:</b> typing...</div>";
    chat.scrollTop = chat.scrollHeight;

    fetch("/chat", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({message:msg})
    })
    .then(res => res.json())
    .then(data=>{
        // remove typing
        let typeElem = document.getElementById("typing");
        if(typeElem) typeElem.remove();

        // bot response
        chat.innerHTML += "<div class='message bot'><b>Bot:</b> " + data.reply + "</div>";
        chat.scrollTop = chat.scrollHeight;
    });
}
</script>

</body>
</html>
"""

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    # Greetings
    if any(word in user_message for word in ["hi", "hello", "hey"]):
        reply = "Hello 👋 Welcome to your Smart Home Safety System!"

    # Security
    elif "secure" in user_message or "safety" in user_message:
        reply = "All security systems are active ✅ Your home is fully protected."

    # Alert mode
    elif "alert" in user_message:
        reply = "🚨 Alert Mode Activated! Monitoring all sensors closely."

    # Status
    elif "status" in user_message:
        reply = "System Status: 🟢 All sensors operational. No threats detected."

    # Camera
    elif "camera" in user_message:
        reply = "📷 Cameras are online and recording normally."

    # Time
    elif "time" in user_message:
        now = datetime.now().strftime("%H:%M:%S")
        reply = f"Current system time is {now}"

    # Help
    elif "help" in user_message:
        reply = "You can ask about: security, alert, status, camera, or time."

    else:
        reply = "I'm your Smart Home Safety Bot 🤖 Type 'help' to see available commands."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
