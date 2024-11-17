from flask import Flask, request, jsonify

app = Flask(__name__)

# Quiz questions for each level
quiz_questions_1 = [
    ("What is the capital of India?", "Delhi"),
    ("What is the highest placement of LPU?", "3 crore"),
    ("What is the largest private university in India?", "Lovely Professional University"),
    ("Who built Lovely Professional University?", "Dr. Rashmi Mittal"),
    ("What is the campus size of LPU?", "900acre"),
]

quiz_questions_2 = [
    ("What profession do you want to be in?", "IT guy"),
    ("What is this professional called?", "Software developer"),
    ("How many companies are there globally?", "200"),
    ("What is the motto of LPU?", "Transforming Education Transforming India"),
    ("In which state is LPU located?", "Punjab"),
]

quiz_questions_bca = [
    ("What does BCA stand for?", "Bachelor of Computer Applications"),
    ("What programming language is known as the 'language of the web'?", "JavaScript"),
    ("What is the full form of CPU?", "Central Processing Unit"),
    ("Which data structure uses FIFO (First In, First Out) principle?", "Queue"),
    ("What is the base of the binary number system?", "2"),
]

quiz_questions_btech = [
    ("What does B.Tech stand for?", "Bachelor of Technology"),
    ("What is Ohm's Law formula?", "V=IR"),
    ("Who is known as the father of computer science?", "Alan Turing"),
    ("What is the primary material used in semiconductors?", "Silicon"),
    ("What programming language is heavily used in engineering?", "C++"),
]

# Storing user progress and scores
user_progress = {}

# Helper function to check answers
def check_answers(questions, answers):
    score = 0
    for question, answer in zip(questions, answers):
        correct_answer = dict(questions).get(question)
        if answer.strip().lower() == correct_answer.lower():
            score += 1
    return score

@app.route('/start', methods=['GET'])
def start_quiz():
    user_id = request.args.get("user_id")
    user_progress[user_id] = {"level": 1, "total_score": 0}
    return jsonify({"message": "Quiz started", "questions": quiz_questions_1})

@app.route('/level1', methods=['POST'])
def level1():
    user_id = request.json.get("user_id")
    answers = request.json.get("answers")

    # Validate user
    if user_id not in user_progress:
        return jsonify({"error": "User not found. Start the quiz first."}), 404

    # Check answers for level 1
    score = check_answers(quiz_questions_1, answers)
    user_progress[user_id]["total_score"] += score

    if score >= 3:
        user_progress[user_id]["level"] = 2
        return jsonify({
            "message": "Congratulations! You have qualified for Level 2.",
            "score": score,
            "questions": quiz_questions_2
        })
    else:
        return jsonify({"message": "Sorry, you did not qualify for Level 2.", "score": score})

@app.route('/level2', methods=['POST'])
def level2():
    user_id = request.json.get("user_id")
    answers = request.json.get("answers")

    # Validate user and progress
    if user_id not in user_progress or user_progress[user_id]["level"] < 2:
        return jsonify({"error": "You haven't qualified for this level yet."}), 403

    # Check answers for level 2
    score = check_answers(quiz_questions_2, answers)
    user_progress[user_id]["total_score"] += score

    if score >= 3:
        user_progress[user_id]["level"] = 3
        return jsonify({
            "message": "Well done! Choose your path for Level 3.",
            "score": score,
            "options": ["BCA", "B.Tech"]
        })
    else:
        return jsonify({"message": "Sorry, you did not qualify to choose a path.", "score": score})

@app.route('/level3', methods=['POST'])
def level3():
    user_id = request.json.get("user_id")
    path = request.json.get("path")
    answers = request.json.get("answers")

    # Validate user and progress
    if user_id not in user_progress or user_progress[user_id]["level"] < 3:
        return jsonify({"error": "You haven't qualified for this level yet."}), 403

    # Check chosen path and questions
    if path.lower() == "bca":
        score = check_answers(quiz_questions_bca, answers)
        max_score = len(quiz_questions_1) + len(quiz_questions_2) + len(quiz_questions_bca)
    elif path.lower() == "b.tech":
        score = check_answers(quiz_questions_btech, answers)
        max_score = len(quiz_questions_1) + len(quiz_questions_2) + len(quiz_questions_btech)
    else:
        return jsonify({"error": "Invalid path choice"}), 400

    final_score = user_progress[user_id]["total_score"] + score

    return jsonify({
        "message": "Level 3 finished! Here is your final score.",
        "path": path,
        "final_score": final_score,
        "max_score": max_score
    })

if __name__ == "__main__":
    app.run(debug=True)
