from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/messages', methods = ['GET', 'POST'])
def messages():
    if request.method == 'GET':
        messages_list = []
        for message in Message.query.all():
            messages_list.append(message.to_dict())

        response = make_response(jsonify(messages_list), 200)

    elif request.method == 'POST':
        data = request.get_json()
        new_message = Message(
            body=data['body'],
            username=data['username'],
            # updated_at = data['updated_at'],
            # created_at = data['created_at']
        )

        db.session.add(new_message)
        db.session.commit()

        response = make_response(jsonify(new_message.to_dict()), 201)

    return response
    return 'hi'

@app.route('/messages/<int:id>', methods = ['PATCH, DELETE'])
def messages_by_id(id):
    message = Message.query.filter(Message.id == id).first()
    if request.method == 'PATCH':
        for attr in request.form:
            setattr(message, attr, request.form.get(attr))

        db.session.add(message)
        db.session.commit()

        response = make_response(jsonify(message.to_dict()), 200)

    elif request.method == 'DELETE':
        db.session.delete(message)
        db.session.commit()

        response = make_response(jsonify({'deleted': True}), 200)

    # elif request.method == 'GET':
    #     response = make_response(message.to_dict(), 200)
        
    return response

if __name__ == '__main__':
    app.run(port=5555)
