from collections import defaultdict
from spacy.tokens import Doc
from sent_pattern.core.factory.elements import ElementsFactory
from sent_pattern.core.interface.Ipattern import IBaseSentencePattern
from sent_pattern.core.factory.pattern import SentencePattern
from sent_pattern.core.type import DepLemmaListType


def create_dep_list(doc: Doc) -> DepLemmaListType:
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


def create_lemma_list(doc: Doc) -> DepLemmaListType:
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


def create_elements(dep_list: DepLemmaListType, lemma_list: DepLemmaListType) -> ElementsFactory:
    """
    Parameters
    ----------
    dep_list : DepLemmaListType
        Put into dict for each dep of Token

    lemma_list: Dict[str, Optional[Token]]
        Put into dict for each lemma of Token

    Returns
    -------
    elements: ElementsInterface
        classes have subject, verb, adjective, and object
    """
    elements = ElementsFactory.make_root_elements(
        dep_list=dep_list, lemma_list=lemma_list)
    return elements


def create_sent_pattern(elements: ElementsFactory) -> IBaseSentencePattern:
    """
    Parameters
    ----------
    elements : ElementsInterface
        classes have subject, verb, adjective, and object

    Returns
    -------
    pattern : BaseSentencePatternInterface
    """
    pattern = SentencePattern(elements)
    return pattern.pattern_type
