from transformers import BartForConditionalGeneration, BartTokenizer
import textwrap
import re


class Summarizer:
    def __init__(self, model_name="philschmid/bart-large-cnn-samsum"):
        # Load tokenizer and model
        self.tokenizer = BartTokenizer.from_pretrained(model_name)
        self.model = BartForConditionalGeneration.from_pretrained(model_name)
    #must use preprocesser to clean data before using this class

    #extact only texts that contain the company name or 'Actualités' or 'news'
    def preprocess_data(self, text, company_name, min_words=10):
        # Convert both text and company name to lowercase for case-insensitive matching
        text = text.lower()
        company_name = company_name.lower()

        # Compile regex patterns for efficiency to match company name, "actualités", and "news"
        pattern = re.compile(rf'\b{re.escape(company_name)}', re.IGNORECASE)

        # Split text into lines
        lines = text.splitlines()

        # Use list comprehension to filter relevant lines
        relevant_lines = [
            line for line in lines
            if pattern.search(line) and len(line.split()) >= min_words
        ]

        # Remove empty lines and join relevant lines
        return "\n".join(line for line in relevant_lines if line.strip())


    def summarize_text(self, text):
        # Extract events first
        if text:
            # Join events into a single string to summarize
            inputs = self.tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
            summary_ids = self.model.generate(inputs,
                                               max_length=3000,
                                                 min_length=300,
                                                   length_penalty=0.05,
                                                     num_beams=4,
                                                       early_stopping=True)
            
            summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            formatted_summary = "\n".join(textwrap.wrap(summary, width=80))
            return formatted_summary
        else:
            return "No relevant events found."
        



'''
import spacy
class EventExtractor:
    def __init__(self):
        # Load the small French model
        self.nlp = spacy.load('fr_core_news_sm')

    def extract_events(self, text):
        # Process the text using the spaCy pipeline
        doc = self.nlp(text)
        events = []
        
        # Extracting events based on named entities and verbs
        for ent in doc.ents:
            if ent.label_ in ['MISC', 'LOC', 'ORG', 'PER', 'DATE']:  # Common labels for events
                events.append(ent.text)
        
        # Extracting verbs that might indicate actions or events
        for token in doc:
            if token.pos_ == 'VERB':
                events.append(token.lemma_)

        return events

'''