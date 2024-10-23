from transformers import pipeline
import json

"""
This class is designed to classify a given news summary using zero-shot classification 
with the XLM-RoBERTa model. It assigns a label to the news content based on a predefined 
list of categories loaded from a JSON file.

Key Features:
- Uses a zero-shot classification model to label news content without requiring explicit 
  training on the predefined categories.
- Loads the candidate labels from a JSON file, allowing for easy updates or modifications 
  to the classification categories.
- Identifies the most relevant label for the given news summary based on the model's confidence scores.

Attributes:
- `labels_file_path`: The file path to the JSON file that contains the list of candidate labels.
- `summary`: The news summary that will be classified.
- `classifier`: Uses the `joeddav/xlm-roberta-large-xnli` model, a multilingual model for 
  zero-shot classification tasks.

Methods:
- `load_labels_from_json(file_path)`: Reads the JSON file and extracts the list of candidate 
  labels. If no labels are found, it returns an empty list.
- `run()`: Loads the zero-shot classification pipeline, applies it to the provided news 
  summary, and selects the most relevant label based on the highest confidence score.

Usage:
- To use this class, instantiate it with the path to the labels JSON file and the news summary 
  you wish to classify. Then call the `run()` method to get the label with the highest confidence.

Model Information:
- XLM-RoBERTa (`joeddav/xlm-roberta-large-xnli`) is a multilingual model that supports various 
  languages, making it well-suited for classifying text in different languages without requiring 
  task-specific training.
- The model is available through the following Hugging Face link: https://huggingface.co/joeddav/xlm-roberta-large-xnli  

Example:
    news_classifier = NewsLabelClassifier("labels.json", "Le groupe annonce une acquisition.")
    label = news_classifier.run()
    print(f"The predicted label is: {label}")

Dependencies:
- Requires the `transformers` library to load the XLM-RoBERTa model.
"""

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
    