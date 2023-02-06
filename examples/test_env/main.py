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
                prog='main', # プログラム名
                usage='Demonstration of argparser', # プログラムの利用方法
                description='description', # 引数のヘルプの前に表示
                epilog='end', # 引数のヘルプの後で表示
                add_help=True, # -h/–help オプションの追加
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