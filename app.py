from flask import Flask, request, jsonify, render_template
from recommender import get_recommendations, load_dataset

app = Flask(__name__)
df = load_dataset()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json(silent=True)
    if not data or "skills" not in data:
        return jsonify({"error": "Missing skills field", "status": 400}), 400

    skills = data["skills"]
    if not isinstance(skills, list) or len(skills) < 3:
        return jsonify({"error": "Minimum 3 skills required", "status": 400}), 400

    try:
        result = get_recommendations(skills)
    except ValueError:
        return jsonify({"error": "Minimum 3 skills required", "status": 400}), 400

    return jsonify(result)


@app.route("/jobs")
def jobs():
    return jsonify({"jobs": df["job_role"].tolist()})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
