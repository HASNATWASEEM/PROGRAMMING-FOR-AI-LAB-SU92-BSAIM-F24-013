from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

admission_data = [
    (["deadline", "application deadline", "when to apply", "last date"],
     "The application deadline for Fall 2025 is May 30, 2025. Late applications are accepted until June 15 with a late fee."),
    (["documents", "required documents", "transcript", "recommendation", "ielts", "toefl", "personal statement"],
     "You need: high school transcripts, personal statement, 2 recommendation letters, and IELTS/TOEFL scores (for international students)."),
    (["programs", "courses", "majors", "bsc", "computer science", "business", "psychology", "engineering"],
     "We offer B.Sc. in Computer Science, Business Administration, Electrical Engineering, and Psychology."),
    (["requirements", "admission requirements", "gpa", "sat", "ielts score", "toefl score"],
     "Minimum high school GPA of 3.0. SAT: 1200+ (optional). English proficiency: IELTS 6.5 or TOEFL 80+."),
    (["fees", "fee", "tuition", "cost", "price", "scholarship", "financial aid"],
     "Tuition for 2025/2026 is $18,000/year. Scholarships and financial aid are available."),
    (["contact", "email", "phone", "admissions office"],
     "Admissions Office: admissions@university.edu, Phone: +1 234 567 890"),
    (["visit", "campus tour", "tour", "open day"],
     "Schedule a campus tour by calling +1 234 567 890 or emailing visits@university.edu."),
    (["accommodation", "housing", "dorm", "residence", "on campus"],
     "On‑campus housing costs $6,500 per year. Apply via the student portal after admission."),
]

def find_best_response(user_input):
    user_input_lower = user_input.lower()
    for keywords, reply in admission_data:
        if any(keyword in user_input_lower for keyword in keywords):
            return reply
    return "I'm not sure about that. Try asking about deadlines, fees, requirements, programs, or contact details."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['message']
    bot_reply = find_best_response(user_message)
    return jsonify(reply=bot_reply)

if __name__ == '__main__':
    app.run(debug=True)