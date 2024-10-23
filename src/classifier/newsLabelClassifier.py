from transformers import pipeline
import json

class NewsLabelClassifier:
    def __init__(self,labels_file_path, summary):
        self.labels_file_path = labels_file_path
        self.summary = summary

    def load_labels_from_json(self,file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data.get('labels', [])    

    def run(self):
        # Load XLM-RoBERTa for zero-shot classification
        classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

        # Load labels from the JSON file
        labels = self.load_labels_from_json(self.labels_file_path)
        
        # Perform zero-shot classification
        result = classifier(self.summary, candidate_labels=labels)

        # Get the index of the max score
        max_index = result['scores'].index(max(result['scores']))

        # Print the corresponding label
        max_label = result['labels'][max_index]
        return max_label