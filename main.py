from src.file import annotation_to_data, SUPPORTED_LABELS
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

nlp.add_pipe('ner', last=True)
ner = nlp.get_pipe('ner')

for label in SUPPORTED_LABELS:
    ner.add_label(label)

other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
with nlp.disable_pipes(*other_pipes):  # only train NER
    optimizer = nlp.begin_training()
    for itn in range(NUM_OF_ITERATIONS):
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in tqdm(TRAIN_DATA):
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            nlp.update([example], losses=losses, drop=0.3, sgd=optimizer)
        print(losses)


if OUTPUT_DIRECTORY is not None:
    if not OUTPUT_DIRECTORY.exists():
        OUTPUT_DIRECTORY.mkdir()
    nlp.to_disk(OUTPUT_DIRECTORY)
    print("Saved model to", OUTPUT_DIRECTORY)

# TODO: run some tests
