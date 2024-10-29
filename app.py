from flask import Flask, render_template, request

app = Flask(__name__)

# Function to check password strength
def check_password_strength(password):
    import re
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1

    # Check for uppercase, lowercase, digits, and special characters
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    # Determine password strength based on score
    if score == 5:
        return "Strong"
    elif 3 <= score < 5:
        return "Moderate"
    else:
        
        return "Weak"

# Route for the home page
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        password = request.form["password"]
        strength = check_password_strength(password)
        return render_template("index.html", strength=strength)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
