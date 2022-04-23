from flask import Flask,request,render_template,jsonify
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img,img_to_array
import numpy as np
import tensorflow as tf

app = Flask(__name__)
def pre():
    model = tf.keras.models.load_model('allchess')
    img = load_img('static/images/image.jpg',color_mode = 'rgb',target_size = (224,224))
    x =img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    features = model.predict(x)
    classes = ['bishop','queen','knight','king','rook','pawn']
    return classes[np.argmax(features)]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/pred',methods = ['POST'])
def predict():
    try:
        if 'file' not in request.files:
            return jsonify({'data' : 'nofile'})
        file = request.files['file']
        file.save("static/images/image.jpg")
        return jsonify({'data':pre()})
    except:
        return jsonify({'error':'Unexpected error (check the file, only jpg allowed)'})

if __name__ == "__main__":
    app.run(debug=True)