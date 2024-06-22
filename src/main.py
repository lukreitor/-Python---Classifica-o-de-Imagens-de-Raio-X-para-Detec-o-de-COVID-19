import os
import sys
import numpy as np
# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.feature_extraction import extract_wavelet_features, load_images_from_folder
from src.classifier import train_and_evaluate
from src.utils import save_results
from classifier import train_and_evaluate
from utils import save_results

if __name__ == "__main__":
    data_folder = 'data'
    
    images, labels = load_images_from_folder(data_folder)
    features = np.array([extract_wavelet_features(img) for img in images])
    
    labels = np.array([1 if label == 'covid' else 0 for label in labels])
    
    accuracy, conf_matrix = train_and_evaluate(features, labels)
    
    save_results(accuracy, conf_matrix)
