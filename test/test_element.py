from typing import List, Tuple
import spacy
import sent_pattern
import pytest

nlp = spacy.load("en_core_web_md")
nlp.add_pipe("span_noun")
nlp.add_pipe("sent_pattern")


test_data = {
    "texts":[
        "Apple’s new iPhone 14 lineup isn’t proving to be as popular as the company would have hoped for",
        "Apple also began to produce the iPhone 14 in India this week in order to shift some burden of manufacturing from factories in China",
        "A recent report published by JP Morgan suggested that Apple is looking to shift 25% of its iPhone production to India by 2025. "
    ],
    "subject": [
        "Apple’s new iPhone 14 lineup",
        "Apple",
        "A recent report",
    ],
    "verb": [
        "proving",
        "began",
        "suggested",
    ],
    "pattern":[
        "SVC",
        "SVC",
        "SVC",
    ]
}


def make_test_data(texts: List[str], answers: List[str])-> List[Tuple[str,str]]:
    data = []
    for text, ans in zip(texts, answers):
        data.append((text, ans))
    return data

subject_test_data = make_test_data(test_data["texts"], test_data["subject"])
@pytest.mark.parametrize(('text', 'subject'), subject_test_data)
def test_subject(text: str, subject: str):
    doc = nlp(text)
    pattern = doc._.sentpattern
    assert pattern.subject.root.text == subject


verb_test_data = make_test_data(test_data["texts"], test_data["verb"])
@pytest.mark.parametrize(('text', 'verb'), verb_test_data)
def test_verb(text:str, verb:str):
    doc = nlp(text)
    pattern = doc._.sentpattern
    assert pattern.verb.root.text == verb

pattern_test_data = make_test_data(test_data["texts"], test_data["pattern"])
@pytest.mark.parametrize(('text', 'pattern'), pattern_test_data)
def test_pattern(text:str, pattern:str):
    doc = nlp(text)
    p = doc._.sentpattern
    assert p.abbreviation == pattern