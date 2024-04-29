from models import Question, QuestionSeries
from flask import Blueprint, request, jsonify

question_bp = Blueprint('question', __name__)

def create_question(text, answer, series, country):
    question = Question.create(text=text, answer=answer, series=series, submitted=False, country=country)
    return question

@question_bp.route('/question', methods=['POST'])
def create_question_with_series():
    data = request.json
    text = data.get('text')
    answer = data.get('answer')
    series = data.get('series')
    country = data.get('country')
    series, _ = QuestionSeries.get_or_create(name=series)
    question = create_question(text, answer, series, country)
    return jsonify({'message': 'Question created successfully', 'question_id': question.id}), 201

@question_bp.route('/questionSubmit', methods=['PUT'])
def submitQuestion():
    data = request.json
    id = data.get('id')
    question = Question.get_or_none(id=id)
    if question:
        question.submitted = True
        question.save()
        return jsonify({'message': 'Question submitted successfully', 'question_id': question.id})
    else:
        return jsonify({'error': 'Question not found'}), 404

@question_bp.route('/question', methods=['GET'])
def get_question_by_id():
    data = request.json
    id = data.get('id')
    question = Question.get_or_none(id=id)
    if question:
        return jsonify(question.serialize())
    else:
        return jsonify({'error': 'Question not found'}), 404

@question_bp.route('/question', methods=['DELETE'])
def delete_question():
    data = request.json
    id = data.get('id')
    question = Question.get_or_none(id=id)
    if question:
        question.delete_instance()
        return jsonify({'message': 'Question deleted successfully'})
    else:
        return jsonify({'error': 'Question not found'}), 404