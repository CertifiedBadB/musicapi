from peewee import Model, SqliteDatabase, CharField, IntegerField, ForeignKeyField, BooleanField

# Definieer de database
db = SqliteDatabase('music_quiz.db')

# Initialisatie en verbinding met de database
db.connect()

class QuestionSeries(Model):
    text = CharField()

    class Meta:
        database = db


class Question(Model):
    text = CharField()
    answer = CharField()
    sound = CharField()
    submitted = BooleanField()
    country = CharField()
    series = ForeignKeyField(QuestionSeries, backref='questions')

    class Meta:
        database = db

class Highscore(Model):
    name = CharField()
    points = IntegerField()

    class Meta:
        database = db