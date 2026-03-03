import os
from flask import Flask, request, jsonify

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
    font-family:Arial;
    text-align:center;
}
.chat-box {
    width:90%;
    max-width:500px;
    margin:20px auto;
    background:#1e1e1e;
    padding:15px;
    border-radius:10px;
    height:350px;
    overflow-y:auto;
}
input {
    width:70%;
    padding:10px;
    border-radius:5px;
    border:none;
}
button {
    padding:10px 15px;
    border:none;
    border-radius:5px;
    background:#00ffcc;
    cursor:pointer;
}
.user { color:#00ffcc; }
.bot { color:#ffffff; }
</style>
</head>
<body>

<h2>🏠 Home Safety Chatbot</h2>

<div class="chat-box" id="chat"></div>

<input type="text" id="message" placeholder="Type your message...">
<button onclick="sendMessage()">Send</button>

<script>
function sendMessage(){
    let msg = document.getElementById("message").value;
    if(msg === "") return;

    let chat = document.getElementById("chat");
    chat.innerHTML += "<p class='user'><b>You:</b> " + msg + "</p>";

    fetch("/chat", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({message:msg})
    })
    .then(res => res.json())
    .then(data=>{
        chat.innerHTML += "<p class='bot'><b>Bot:</b> " + data.reply + "</p>";
        chat.scrollTop = chat.scrollHeight;
    });

    document.getElementById("message").value="";
}
</script>

</body>
</html>
"""

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    if "secure" in user_message:
        reply = "System Secure ✅ No threats detected."
    elif "alert" in user_message:
        reply = "Alert Mode Activated 🚨"
    elif "status" in user_message:
        reply = "All sensors working properly."
    else:
        reply = "I'm your Home Safety Bot. Ask about security or system status."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
