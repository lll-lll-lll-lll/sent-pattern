import spacy
from spacy.tokens import Doc
from sent_pattern import tags
from sent_pattern.core.elements import make_custom_elements, make_root_elements
from sent_pattern.core.elements.elements import RootElements
import argparse

nlp = spacy.load("en_core_web_sm")

def custom_elements(doc: Doc):
    dep_list = tags.create_dep_list(doc)
    custom_elements = make_custom_elements(doc, dep_list)
    return custom_elements
    

def make_elements(doc: Doc):
    dep_list = tags.create_dep_list(doc)
    elements = make_root_elements(dep_list)
    return elements


def make_sentpattern(elements: RootElements) -> RootElements:
    return tags.create_sent_pattern(elements=elements)
 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                prog='main', 
                usage='Demonstration of argparser', 
                description='description', 
                epilog='end',
                add_help=True,
                )
    parser.add_argument('-e', choices=['prep', 'relcl', 'all'])
    args = parser.parse_args()
    text = input()
    doc = nlp(text)
    if args.e == "all":
        elements = custom_elements(doc)
    elif args.e == "relcl":
        elements = custom_elements(doc)
        print(elements.relcl.relcl_section)
    elif args.e == "prep":
        elements = custom_elements(doc)
        print(elements.prep.prep_phrase)
    else:
        elements = make_elements(doc)
        print(elements)