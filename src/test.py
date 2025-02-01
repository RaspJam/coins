# At some point a bunch of automatic tests will be written here

import spacy

# BUG: This code does not work for some reason, even with a trained model
# Likely some incosistency between the training data and the model
nlp = spacy.load('COINS')
doc = nlp("set a timer for 15 minutes")
print('Entities', [(ent.text, ent.label_) for ent in doc.ents])
