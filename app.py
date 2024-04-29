from flask import Flask, render_template
from controllers.questionController import question_bp  
from controllers.highscoreController import highscore_bp  
from models import db, Question, Highscore, QuestionSeries

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Specificeer het pad naar het databasebestand
DB_FILE = 'music_quiz.db'
db.init(DB_FILE)

def create_tables():
    with db:
        db.create_tables([Question, Highscore,QuestionSeries])

# Registreer de Blueprint-objecten in de Flask-applicatie
app.register_blueprint(question_bp)
app.register_blueprint(highscore_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    print("__name__ is:", __name__)
    # Voer de create_tables functie uit als het script direct wordt uitgevoerd
    create_tables()
    app.run(debug=True)