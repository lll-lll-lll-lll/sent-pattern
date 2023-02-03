import spacy
import sent_pattern
from typing import List, Tuple
import pytest

nlp = spacy.load("en_core_web_lg")
nlp.add_pipe("span_noun")
nlp.add_pipe("sent_pattern")


test_data = {
    "texts": [
        "The firm obtained that information without users' consent from a researcher who had been allowed by Facebook to deploy an app on the platform which harvested data from millions of its users.",
        "She makes me happy.",
        "I am hero",
        "I give you something",
        "The Eureka client handles all aspects of service instance registration and deregistration",
        "She goes to school"
        ],
    "pattern": ["SVO"],
    "spans": [
        {"SVO":["The firm", "obtained", "that information"]},
        {"SVOC":["She", "makes", "me", "happy"]},
        {"SVC": ["I", "am", "hero"]},
        {"SVOO": ["I", "give", "you", "something"]},
        {"SVO": ["The Eureka client", "handles", "all aspects of service instance registration and deregistration"]},
        {"SV": ["She", "goes", ]}
        ]
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
    p = doc._.sentpattern
    assert p.abbreviation == pattern


pattern_test_data = make_test_data(test_data["texts"], test_data["spans"])
@pytest.mark.parametrize(('text', 'spans'), pattern_test_data)
def test_pattern_span(text:str, spans:str):
    doc = nlp(text)
    p = doc._.sentpattern
    if spans.get("SV") != None:
        data = spans.get("SV")
        s = data[0]
        v = data[1]
        assert s == p.spans_str["S"]
        assert v == p.spans_str["V"]
    elif spans.get("SVC") != None:
        data = spans.get("SVC")
        s = data[0]
        v = data[1]
        c = data[2]
        assert s == p.spans_str["S"]
        assert v == p.spans_str["V"]
        assert c == p.spans_str["C"]
    elif spans.get("SVO") != None:
        data = spans.get("SVO")
        s = data[0]
        v = data[1]
        o = data[2]
        assert s == p.spans_str["S"]
        assert v == p.spans_str["V"]
        assert o == p.spans_str["O"]
    elif spans.get("SVOO") != None:
        data = spans.get("SVOO")
        s = data[0]
        v = data[1]
        o1 = data[2]
        o = data[3]
        assert s == p.spans_str["S"]
        assert v == p.spans_str["V"]
        assert o1 == p.spans_str["O1"]
        assert o == p.spans_str["O2"]
    elif spans.get("SVOC") != None:
        data = spans.get("SVOC")
        s = data[0]
        v = data[1]
        o = data[2]
        c = data[3]
        print(p)
        assert s == p.spans_str["S"]
        assert v == p.spans_str["V"]
        assert o == p.spans_str["O"]
        assert c == p.spans_str["C"]


        
        