import os

from matplotlib import pyplot as plt
import seaborn as sns

def save_results(accuracy, conf_matrix, results_dir='results'):
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    
    with open(os.path.join(results_dir, 'accuracy.txt'), 'w') as f:
        f.write(f'Accuracy: {accuracy}\n')
    
    plt.figure(figsize=(6,6))
    sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.title('Confusion Matrix')
    plt.savefig(os.path.join(results_dir, 'confusion_matrix.png'))
