import spacy
from sent_pattern import tags

nlp = spacy.load("en_core_web_lg")
nlp.add_pipe("span_noun")
nlp.add_pipe("sent_pattern")


def test_pipe_added_to_nlp():
    assert nlp.pipe_names[-1] == "sent_pattern"
