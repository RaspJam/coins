## Useful functions for reading, writing, and dealing with annotations
import re

SUPPORTED_LABELS = ("COMMAND", "OPTION", "INPUT", "NUMBER", "STRING")

def annotation_to_data(path: str) -> list[tuple[str, dict]]:
    """
    Extracts annotations from a text file, returning usable training data.
    """
    with open(path, "r") as f:
        annotations = f.readlines()

    # matches text within square brackets or parentheses
    #pattern = re.compile(r"\[(?P<entity>.*?)\]|\((?P<label>.*?)\)")
    pattern = re.compile(r"\[(?P<entity>.*?)\]\((?P<label>.*?)\)")

    data = []
    for line in annotations:
        raw_line = re.sub(pattern, r'\1', line).strip()

        entities = []
        for match in list(re.finditer(pattern, line)):
            entity, label = match.group("entity", "label")
            if not is_supported_label(label):
                raise ValueError(f'Unsupported label: "{label}"!')

            start = raw_line.find(match.group("entity"))
            end = start + len(match.group("entity"))

            entities.append((start, end, label))
        data.append((raw_line, {"entities": entities}))
    return data

def is_supported_label(label: str) -> bool:
    return label in SUPPORTED_LABELS

# TODO: Implement function for data cleaning
