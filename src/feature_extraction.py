import cv2
import pywt
import numpy as np
import os

def extract_wavelet_features(image, wavelet='db1', level=3, feature_length=1024):
    coeffs = pywt.wavedec2(image, wavelet, level=level)
    features = []
    for coeff in coeffs:
        for arr in coeff:
            features.extend(arr.flatten())
    # Padronizar o tamanho das features
    features = features[:feature_length] if len(features) >= feature_length else features + [0] * (feature_length - len(features))
    return np.array(features)

def load_images_from_folder(folder):
    images = []
    labels = []
    for label in ['covid', 'normal']:
        path = os.path.join(folder, label)
        for filename in os.listdir(path):
            img = cv2.imread(os.path.join(path, filename), cv2.IMREAD_GRAYSCALE)
            if img is not None:
                images.append(img)
                labels.append(label)
    return images, labels
