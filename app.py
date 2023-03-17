from flask import Flask, request, jsonify
from deepface import DeepFace
import os

app = Flask(__name__)

UPLOAD_FOLDER = './UPLOAD'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/verify", methods=["POST"])
def verify():
    try:
        file = request.files['image']
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        dfs = DeepFace.find(img_path=file_path,db_path="DB",model_name="Facenet512",distance_metric="euclidean_l2")
        if dfs.empty:
            return jsonify({'verified':'false'})
        else:
            return jsonify({'verified':'true'})
    except Exception as e:
        print(e)
        return jsonify({"msg":"An error has occured"})