from transformers import pipeline


'''
analyzer = pipeline(
    task='text-classification',
    model="cmarkea/distilcamembert-base-sentiment",
    tokenizer="cmarkea/distilcamembert-base-sentiment"
)
result = analyzer(
    "J'aime me promener en forêt même si ça me donne mal aux pieds.",
    return_all_scores=True
)

print(result)

'''

text= "À Madagascar, AVSF (Agronomes et Vétérinaires Sans Frontières) accompagne la coopérative paysanne Fanohana dans la production de fruits et d’épices bio, commercialisant leur production sur les marchés du commerce équitable grâce à un partenariat avec ETHIQUABLE, qui vend ces produits en France sous forme de jus et de desserts. Par ailleurs, SIDI et ETHIQUABLE ont mis en place un fonds de roulement de 1,2M€ pour soutenir les petites coopératives engagées dans la bio et le commerce équitable. Cependant, face au risque de détricotage du règlement européen contre la déforestation, les acteurs du commerce équitable expriment des préoccupations concernant le report de l'entrée en application de ce règlement, qui pourrait fragiliser les initiatives existantes. Ils appellent à des relations commerciales plus équitables et à un renforcement des capacités des coopératives de producteurs, tout en soulignant l'importance de la traçabilité et de la durabilité des filières pour les petits producteurs de café et de cacao."


#not really good-make it optional 

# Load a French sentiment analysis model
#sentiment_pipeline = pipeline("sentiment-analysis", model="tblard/tf-allocine")

# Run sentiment analysis on the summary (in French)
#summary = result.get('summary', '')
#sentiment_result = sentiment_pipeline(summary)
#print(f"Sentiment: {sentiment_result}")

#https://huggingface.co/bardsai/finance-sentiment-fr-base

#nlp = pipeline("sentiment-analysis", model="bardsai/finance-sentiment-fr-base")





#result=nlp(text)
#print()
#print(result)



#https://huggingface.co/joeddav/xlm-roberta-large-xnli
# Load XLM-RoBERTa for zero-shot classification
classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")


# Define candidate labels
labels = [
    "acquisition", "juridique", "financier", "ressources humaines", 
    "développement durable", "recherche et développement", "stratégie", 
    "diversité", "communication", "événement", "produit", "technologie", 
    "marché", "concurrent", "partenariat", "client", "fournisseur", 
    "distributeur", "employé", "actionnaire", "gouvernance", "environnement", 
    "social", "économie", "société", "entreprise", "industrie", "secteur", 
    "bourse", "finance", "actualité", "information", "presse", "média", 
    "journalisme", "publicité", "marketing", "digital", "numérique", 
    "innovation", "startup", "entrepreneuriat", "investissement", "capital", 
    "fonds", "R&D", "logistique", "supply chain", "automation", "robotique", 
    "cloud", "cybersécurité", "blockchain", "intelligence artificielle", 
    "IoT", "big data", "analyse de données", "énergies renouvelables", 
    "biotechnologie", "santé", "pharmaceutique", "commerce électronique", 
    "retail", "distribution", "production", "services", "transformation digitale", 
    "mobilité", "transport", "logement", "urbanisme", "tourisme", "finance verte"
]


# Perform zero-shot classification
result2 = classifier(text, candidate_labels=labels)
#return max score
# Get the index of the max score
max_index = result2['scores'].index(max(result2['scores']))

# Print the corresponding label
max_label = result2['labels'][max_index]
print(f"Max label: {max_label}")