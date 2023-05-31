from keras.preprocessing import image
import numpy as np
from PIL import Image
from flask import Flask, jsonify, request
import tensorflow as tf
import keras
from classes import classes


def load_models():
    model_path = '.\\models\\bird.h5'
    model= keras.models.load_model(model_path, custom_objects={'F1_score':'F1_score'})
    return model


def predict_result(model,img):
    img = Image.open(img).convert('RGB')
    img = img.resize((300, 300 * img.size[1] // img.size[0]), Image.ANTIALIAS)
    inp_numpy = np.array(img)[None]
    inp = tf.constant(inp_numpy, dtype='float32')
    class_scores = model(inp)[0].numpy()
    return classes[class_scores.argmax()]


app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def infer_image():
    img = '..\\test\\test_images\\black_swan.jpeg' 
    model = load_models()
    result = predict_result(model,img)
    return jsonify(prediction=result)
    

@app.route('/', methods=['GET'])
def index():
    return 'Bird Species Classifier'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
