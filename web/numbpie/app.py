from __future__ import division, print_function
import sys
import os
import glob
import re
import shutil
import numpy as np

sys.path.append("/home/doggie/camp/deploy/code/")

from Searcher import *

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = 'models/your_model.h5'

searcher = Searcher(Config())

# Load trained model
# model = load_model(MODEL_PATH)
# model._make_predict_function()          # Necessary
# print('Model loaded. Start serving...')

# Pretrained model from Keras: https://keras.io/applications/
# from keras.applications.resnet50 import ResNet50
# model = ResNet50(weights='imagenet')
print('Model loaded. Check http://127.0.0.1:4321/')


# def model_predict(img_path, model):
#     img = image.load_img(img_path, target_size=(224, 224))
#
#     # Preprocess the image
#     x = image.img_to_array(img)
#     # x = np.true_divide(x, 255)
#     x = np.expand_dims(x, axis=0)
#
#     x = preprocess_input(x, mode='caffe')
#
#     preds = model.predict(x)
#     return preds


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the image from post request
        f = request.files['file']

        current_path = os.path.abspath(__file__)

        # Empty ./uploads
        for file in os.listdir('./uploads'):
            file_path = os.path.join('./uploads', file)
            try:
                if (os.path.isfile(file_path)):
                    os.unlink(file_path)
            except Exception as e:
                print(e)

        # Save the image to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename("1324.png"))
        f.save(file_path)

        searcher.run_once()

        # # Make prediction
        # preds = model_predict(file_path, model)
        #
        # # Process result for human
        # # pred_class = preds.argmax(axis=-1)
        # pred_class = decode_predictions(preds, top=1)   # ImageNet Decode
        # result = str(pred_class[0][0][1])               # Convert to string
        # return result
        return ""
    return None

@app.route('/writetxt', methods=['GET', 'POST'])
def write_txt():
    if request.method == 'POST':
        f = open('static/gan/' + request.form.get('file') + '.txt','w')
        f.write(request.form.get('value'))
        f.close()
        return "Success!"
    return None


if __name__ == '__main__':
    # Serve the app with gevent
    http_server = WSGIServer(('', 4321), app)
    http_server.serve_forever()
