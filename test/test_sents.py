import spacy
import sent_pattern
from typing import List, Tuple
import pytest

nlp = spacy.load("en_core_web_lg")
nlp.add_pipe("span_noun")
nlp.add_pipe("sent_pattern")

test_data = {
    "texts": [
        "The firm obtained that information without users' consent from a researcher who had been allowed by Facebook to deploy an app on the platform which harvested data from millions of its users. She makes me happy.",
        "I like you"
        ],
    "pattern": ["SVO SVOC", "SVO"],
}

def make_test_data(texts: List[str], answers: List[str])-> List[Tuple[str,str]]:
    data = []
    for text, ans in zip(texts, answers):
        data.append((text, ans))
    return data

pattern_test_data = make_test_data(test_data["texts"], test_data["pattern"])
@pytest.mark.parametrize(('text', 'pattern'), pattern_test_data)
def test_pattern(text:str, pattern:str):
    doc = nlp(text)
    ps = pattern.split()
    patterns = doc._.sentpattern
    if len(list(doc.sents)) == 1:
        assert patterns.abbreviation == ps[0]
        return
    for s, p in zip(ps, patterns):
        assert p.abbreviation == s