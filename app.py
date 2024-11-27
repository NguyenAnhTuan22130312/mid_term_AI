from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import pickle

with open('spam_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('count_vectorizer.pkl', 'rb') as file:
    cv = pickle.load(file)

app = Flask(__name__)
CORS(app)  # Cấu hình CORS cho toàn bộ ứng dụng Flask

@app.route('/check_spam', methods=['POST'])
def check_spam():
    msg = request.json.get('message')
    vect = cv.transform([msg]).toarray()
    result = model.predict(vect)
    return jsonify({'result': 'Spam' if result[0] == 1 else 'Ham'})

if __name__ == '__main__':
    app.run(debug=True)
