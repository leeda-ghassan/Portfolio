from flask import Flask, render_template, request
from src.gpt_services.gpt import GPT2FlaskApp

gpt_service = GPT2FlaskApp()
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    if request.method == "POST":
        first_name = request.form.get("first_name", "Osama")
        last_name = request.form.get("last_name", "Yousef")
        job_title = request.form.get("job_title", "Backend")

        # Generate CV summary
        data = gpt_service.generate_cv_entry(
            name=f"{first_name} {last_name}",
            age=25,
            location="Jordan",
            skills="Python, PostgreSQL, NodeJS",
            job_title=job_title
        )

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
