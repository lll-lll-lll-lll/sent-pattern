from abc import ABCMeta
from typing import Dict, List, Optional
from spacy.tokens import Token
from .Ielement import SubjectInterface, VerbInterface, AdjectiveInterface, ObjectInterface


class RootElementsInterface(metaclass=ABCMeta):
    """
    classes have subject, verb, adjective, and object
    """
    subject: SubjectInterface
    verb: VerbInterface
    adjective: AdjectiveInterface
    rootobject: ObjectInterface

    @classmethod
    def make_self(cls, dep_list: Dict[str, List[Optional[Token]]], lemma_list: Dict[str, List[Optional[Token]]]) -> "RootElementsInterface":
        """
        create instance of self
        Parameters
        ----------
        dep_list : Dict[str, Optional[Token]
        lemma_list : Dict[str, Optional[Token]]

        Returns
        -------
        RootElements : self
        """
        raise NotImplementedError()
