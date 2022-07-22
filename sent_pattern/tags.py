from collections import defaultdict
from spacy.tokens import Doc
from spacy.tokens import Token
from typing import List, Dict, Optional
from sent_pattern.core.elements.rootelements import RootElements
from sent_pattern.core.interface.Ielements import RootElementsInterface
from sent_pattern.core.interface.Ipattern import BaseSentencePatternInterface
from sent_pattern.core.patternfactory import PatternFactory


def create_dep_list(doc: Doc) -> Dict[str, List[Optional[Token]]]:
    """
    Put into dict for each dep of Token
    Parameters
    ----------
    doc: spacy.tokens.Doc
        doc after nlp initialization

    Returns
    -------
    dep_list: Dict[str, Optional[Token]]
    """
    dep_list = defaultdict(list)
    for token in doc:
        dep_list[token.dep_].append(token)
    return dict(dep_list)


def create_lemma_list(doc: Doc) -> Dict[str, List[Optional[Token]]]:
    """
    Put into dict for each lemma of Token
    Parameters
    ----------
    doc: spacy.tokens.Doc
        doc after nlp initialization

    Returns
    -------
    lemma_list: Dict[str, Optional[Token]]
    """
    lemma_list = defaultdict(list)
    for token in doc:
        lemma_list[token.lemma_].append(token)
    return dict(lemma_list)


def create_elements(dep_list: Dict[str, List[Optional[Token]]], lemma_list: Dict[str, List[Optional[Token]]]) -> RootElementsInterface:
    """
    Parameters
    ----------
    dep_list : Dict[str, List[Optional[Token]]]
        Put into dict for each dep of Token

    lemma_list: Dict[str, Optional[Token]]
        Put into dict for each lemma of Token

    Returns
    -------
    elements: ElementsInterface
        classes have subject, verb, adjective, and object
    """
    elements = RootElements.make_self(
        dep_list=dep_list, lemma_list=lemma_list)
    return elements


def create_sent_pattern(elements: RootElementsInterface) -> BaseSentencePatternInterface:
    """
    Parameters
    ----------
    elements : ElementsInterface
        classes have subject, verb, adjective, and object

    Returns
    -------
    pattern : BaseSentencePatternInterface
    """
    pattern = PatternFactory(elements)
    return pattern.pattern_type
