from flask import Flask, render_template, request

app = Flask(__name__)


movies = {

    "telugu": {
        "action": [
            "RRR",
            "Baahubali",
            "Pushpa",
            "Vikramarkudu"
        ],
        "comedy": [
            "Jathi Ratnalu",
            "F2",
            "Venkatadri Express",
            "Ala Modalaindi"
        ],
        "drama": [
            "Jersey",
            "Mahanati",
            "Sita Ramam",
            "Arjun Reddy"
        ]
    },


    "hindi": {
        "action": [
            "Jawan",
            "Pathaan",
            "War",
            "Dhoom 3"
        ],
        "comedy": [
            "Hera Pheri",
            "3 Idiots",
            "Golmaal",
            "Munna Bhai MBBS"
        ],
        "drama": [
            "Dangal",
            "Rockstar",
            "Barfi",
            "Taare Zameen Par"
        ]
    },


    "english": {
        "action": [
            "Avengers",
            "John Wick",
            "Mission Impossible",
            "The Dark Knight"
        ],
        "comedy": [
            "Home Alone",
            "The Hangover",
            "Free Guy",
            "Mr. Bean"
        ],
        "drama": [
            "Titanic",
            "Forrest Gump",
            "The Shawshank Redemption",
            "The Pursuit of Happyness"
        ]
    }

}


@app.route("/", methods=["GET","POST"])
def home():

    recommendations = []

    if request.method == "POST":

        language = request.form["language"]
        genre = request.form["genre"]

        recommendations = movies[language][genre]


    return render_template(
        "index.html",
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)