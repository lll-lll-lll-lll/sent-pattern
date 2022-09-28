import spacy
from sent_pattern import tags

nlp = spacy.load("en_core_web_md")
nlp.add_pipe("span_noun")
nlp.add_pipe("sent_pattern")


def test_pipe_added_to_nlp():
    assert nlp.pipe_names[-1] == "sent_pattern"


def test_dep_list_get_root_verb():
    text = "he gives me something"
    doc = nlp(text)
    dep_list = tags.create_dep_list(doc)
    root_verb = dep_list["ROOT"]
    assert root_verb[0].text == "gives"


def test_sent_pattern():
    text = "he gives me something"
    doc = nlp(text)
    dep_list = tags.create_dep_list(doc)
    lemma_list = tags.create_lemma_list(doc)
    elements = tags.create_elements(dep_list, lemma_list)
    pattern = tags.create_sent_pattern(elements)
    assert pattern.subject.root.text == "he"
