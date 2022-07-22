from typing import Dict, List, Optional
from . import Adjective
from . import RootObject
from . import Subject
from . import Verb
from spacy.tokens import Token
from ..interface.Ielements import RootElementsInterface
from ..interface.Ielements import SubjectInterface, VerbInterface, AdjectiveInterface, ObjectInterface


class RootElements(RootElementsInterface):
    """
    this class have subject, verb, adjective and object so on.
    """
    def __init__(self, subject: SubjectInterface, verb: VerbInterface, adjective: AdjectiveInterface, rootobject: ObjectInterface):
        self.subject = subject
        self.verb = verb
        self.adjective = adjective
        self.rootobject = rootobject

    @classmethod
    def make_self(cls, dep_list: Dict[str, List[Optional[Token]]], lemma_list: Dict[str, List[Optional[Token]]]) -> "RootElements":
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
        subject = Subject(dep_list)
        verb = Verb(dep_list, lemma_list)
        adjective = Adjective(dep_list)
        rootobject = RootObject(dep_list)

        return cls(**{"subject": subject, "verb": verb, "adjective": adjective, "rootobject": rootobject})
