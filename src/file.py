## Useful functions for reading, writing, and dealing with annotations
import re

SUPPORTED_LABELS = ("COMMAND", "OPTION", "INPUT", "NUMBER", "STRING")

def annotation_to_data(path: str) -> list[tuple[str, dict]]:
    """
    Extracts annotations from a text file, returning usable training data.
    """
    with open(path, "r") as annotations:
        text = annotations.readlines()

    # matches text within square brackets or parentheses
    pattern = re.compile(r"\[(?P<entity>.*?)\]|\((?P<label>.*?)\)")

    data = []
    for line in text:
        line = line.strip('\n')

        matches = list(re.finditer(pattern, line))
        entities = []

        for entity, label in zip(matches[::2], matches[1::2]):
            label = label.group("label")
            if not is_supported_label(label):
                print(f'Unsupported label: "{label}". Ignoring...')
                continue

            # NOTE: The start and end indices are offset by 1 because the pattern includes the brackets
            entities.append((entity.start() + 1, entity.end() - 1, label))

        data.append((line, {"entities": entities}))
    return data

def is_supported_label(label: str) -> bool:
    return label in SUPPORTED_LABELS

# TODO: Implement function for data cleaning
