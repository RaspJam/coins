from annotation import annotation_to_data, SUPPORTED_LABELS
from pathlib import Path
import spacy
from spacy.training.example import Example
from tqdm import tqdm
import random

OUTPUT_DIRECTORY = Path("COINS")
TRAIN_DATA = annotation_to_data("annotations.txt")
NUM_OF_ITERATIONS = 100

# TODO: Ask the user if they'd like to train a new model or use an existing one
nlp = spacy.blank("en")

ner = nlp.create_pipe("ner")
nlp.add_pipe("ner", last=True)

for label in SUPPORTED_LABELS:
    ner.add_label(label)

optimizer = nlp.begin_training()
for itn in tqdm(range(NUM_OF_ITERATIONS)):
    random.shuffle(TRAIN_DATA)
    for text, annotations in TRAIN_DATA:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        nlp.update([example], drop=0.5, sgd=optimizer)


if OUTPUT_DIRECTORY is not None:
    if not OUTPUT_DIRECTORY.exists():
        OUTPUT_DIRECTORY.mkdir()
    nlp.to_disk(OUTPUT_DIRECTORY)
    print("Saved model to", OUTPUT_DIRECTORY)

# TODO: run some tests
