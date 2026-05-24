from flask import Flask, render_template_string

app = Flask(__name__)

# এটি হলো ওয়েবসাইটের মূল পেজ (Home Route)
@app.route('/')
def home():
    # পাইথনের ভেতরেই আমরা HTML এবং জাভাস্ক্রিপ্ট কোডটি দিয়ে দিচ্ছি
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python Flask Website</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background-color: #1e272e;
                color: white;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                text-align: center;
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            }
            h1 { color: #00d2d3; margin-bottom: 10px; }
            button {
                background-color: #ff9f43;
                border: none;
                padding: 12px 24px;
                font-size: 1rem;
                font-weight: bold;
                color: white;
                border-radius: 8px;
                cursor: pointer;
                transition: 0.3s;
            }
            button:hover { background-color: #ee5253; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>HELLO TANVIR</h1>
            <p>This website is powered by Python & Flask!</p>
            <button onclick="speakGreeting()">Click Me</button>
        </div>

        <script>
            // বাটনে ক্লিক করলে ১ বার ভয়েস বলবে
            function speakGreeting() {
                window.speechSynthesis.cancel();
                let speech = new SpeechSynthesisUtterance("Welcome to your Python website Tanvir");
                window.speechSynthesis.speak(speech);
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    # সার্ভারটি লোকালহোস্টে রান হবে
    app.run(debug=True)
