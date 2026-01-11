from flask import Flask, render_template, request
from db_config import create_connection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/membership")
def membership():
    return render_template("membership.html")

@app.route("/submit_membership", methods=["POST"])
def submit_membership():
    full_name = request.form["full_name"]
    email = request.form["email"]
    membership_type = request.form["membership_type"]
    start_date = request.form["start_date"]

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO gym_members
        (full_name, email, membership_type, start_date)
        VALUES (%s, %s, %s, %s)
    """, (full_name, email, membership_type, start_date))

    conn.commit()
    cursor.close()
    conn.close()

    return render_template("confirmation.html", full_name=full_name)

if __name__ == "__main__":
    app.run(debug=True)