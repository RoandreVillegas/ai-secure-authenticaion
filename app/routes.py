import face_recognition
from flask import Flask, request, jsonify, Blueprint

auth = Blueprint('auth', __name__)

try:        
    known_image = face_recognition.load_image_file("app/database/test.jpg")
    known_encodings = face_recognition.face_encodings(known_image)[0]
    if len(known_encodings) == 0:
        raise ValueError("No face found in the known image.")
    known_encoding = known_encodings[0]
except Exception as e:
    print(f"Error loading known image: {e}")
    exit(1)

@auth.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    try:
        uploaded_image = face_recognition.load_image_file(file)
        uploaded_encoding = face_recognition.face_encodings(uploaded_image)
        
        if len(uploaded_encoding) == 0:
            return jsonify({"error": "No face detected"}), 400
        
        match = face_recognition.compare_faces([known_encoding], uploaded_encoding[0])
        
        if match[0]:
            return jsonify({"message": "Access Granted"}), 200 # Match found
        else:
            return jsonify({"message": "Access Denied"}), 403 # No match
    except Exception as e:
        return jsonify({"error": f"Failed to process image:{e}"}), 500