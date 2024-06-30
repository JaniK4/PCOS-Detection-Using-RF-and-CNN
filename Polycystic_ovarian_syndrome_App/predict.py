from tensorflow.keras.models import load_model
import os
from PIL import Image
import numpy as np
from tensorflow.keras.applications import Xception
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.xception import preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.layers import GlobalAveragePooling2D

def process():
    feature_folder = "Fea"
    base_model = Xception(weights='imagenet', include_top=False)
    x = GlobalAveragePooling2D()(base_model.output)
    feature_extraction_model = Model(inputs=base_model.input, outputs=x)


    def extract_features(img_path):
        img = image.load_img(img_path, target_size=(299, 299))  # Xception requires input size of (299, 299)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        features = feature_extraction_model.predict(x)
        return features


    dataset_features = np.load(os.path.join(feature_folder, "all_features.npy"))

    def compute_similarity(input_features, dataset_features):
        distances = np.linalg.norm(input_features - dataset_features, axis=1)
        return distances


    def match_features(input_features, dataset_features):
        distances = compute_similarity(input_features, dataset_features)
        min_distance = np.min(distances)
    
        print(min_distance)
        if min_distance <= 8.7:
            return min_distance
        else:
             return None


    cnn_model = load_model("trained_model_pcos.h5")


    def preprocess_image(image):
        target_size = (64, 64) 
        image = image.resize(target_size)
        image = np.expand_dims(image, axis=0)
        return image

    uploaded_file = r"C:\Project(final)\Polycystic_ovarian_syndrome\media\upload\input.png"

    if uploaded_file is not None:
        img = image.load_img(uploaded_file, target_size=(299, 299))  # Xception requires input size of (299, 299)
        input_features = extract_features(uploaded_file)
        min_distance = match_features(input_features, dataset_features)
        print(min_distance)

        if min_distance is not None:
            cnn_input = preprocess_image(img)
            cnn_pred = cnn_model.predict(cnn_input)
            print(cnn_pred)
            if cnn_pred[0][0] < 0.5:
                result="PCOS"
            else:
                result="Normal Ovary"
        else:
            result="Invalid Image"
        return result
   

    