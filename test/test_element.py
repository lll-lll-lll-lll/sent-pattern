from typing import List, Tuple
import spacy
import sent_pattern
import pytest


nlp = spacy.load("en_core_web_lg")
nlp.add_pipe("span_noun")
nlp.add_pipe("sent_pattern")


test_data = {
    "texts":[
        "Apple’s new iPhone 14 lineup isn’t proving to be as popular as the company would have hoped for",
        "Apple also began to produce the iPhone 14 in India this week in order to shift some burden of manufacturing from factories in China",
        "A recent report published by JP Morgan suggested that Apple is looking to shift 25% of its iPhone production to India by 2025. ",
        "Tech author James Ball told the BBC it was `not a surprise` that Meta has had to agree to a serious pay-out but that it was `not that much` money to the tech giant.",
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
        "told"
    ],
    "adjective":[
        "be",
        "produce",
        "looking"
    ],
    "pattern":[
        "SVC",
        "SV",
        "SVO",
        "SVOO",
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


pattern_test_data = make_test_data(test_data["texts"], test_data["adjective"])
@pytest.mark.parametrize(('text', 'adjective'), pattern_test_data)
def test_pattern(text:str, adjective:str):
    doc = nlp(text)
    pattern = doc._.sentpattern
    assert pattern.adjective.root.text == adjective



objects_data = {
    "texts": [
        "In this quickstart we’ll create a development shell with specific tools installed. ",
        ],
    "object":[
        "a development shell",
        ],
}
def make_test_object_data(texts: List[str], answers: List[str])-> List[Tuple[str,str]]:
    data = []
    for text, ans in zip(texts, answers):
        data.append((text, ans))
    return data
object_test_data = make_test_object_data(objects_data["texts"], objects_data["object"])
@pytest.mark.parametrize(('text', 'object'), object_test_data)
def test_object(text: str, object: str):
    doc = nlp(text)
    pattern = doc._.sentpattern
    if len(pattern.object.root) == 1:
        assert pattern.object.root[0].text == object
    else:
        assert pattern.object.root[0].text + " " + pattern.object.root[1].text == object
