import spacy
import sent_pattern

nlp = spacy.load("en_core_web_md")
nlp.add_pipe("span_noun")
nlp.add_pipe("sent_pattern")


def test_sent_pattern():
    text = "I give you something"
    doc = nlp(text)
    pattern = doc._.sentpattern
    assert pattern.__class__.__name__ == "FourthSentencePattern"
    assert pattern.subject.root.text == "I"
    assert pattern.abbreviation == "SVOO"
