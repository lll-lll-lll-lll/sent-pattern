from typing import Any, Dict, List, Optional
from sent_pattern.core.elements.phrase import PrepPhrase
from sent_pattern.core.interface.Ielement import AdjectiveInterface, ObjectInterface, SubjectInterface, VerbInterface
from .elements import Adjective
from .elements import RootObject
from .elements import Subject
from .elements import Verb
from spacy.tokens import Token
from .interface.Ielements import ElementsFactoryInterface,ElementsInterface
from spacy.tokens import Doc

class RootElements(ElementsInterface):
    """
    this class have just subject, verb, adjective and object
    """
    def __init__(self, 
            subject: SubjectInterface, 
            verb: VerbInterface, 
            adjective: AdjectiveInterface, 
            rootobject: ObjectInterface):

        self.subject = subject
        self.verb = verb
        self.adjective = adjective
        self.rootobject = rootobject


class CustomElements(RootElements):
    def __init__(self,
            subject: SubjectInterface, 
            verb: VerbInterface, 
            adjective: AdjectiveInterface, 
            rootobject: ObjectInterface, 
            option: Any):

        super().__init__(subject, verb, adjective, rootobject)
        self._option = option
    
    @property
    def option(self):
        """
        option property is freely configurable properties
        """
        return self._option


class ElementsFactory(ElementsFactoryInterface):

    @classmethod
    def make_root_elements(cls, dep_list: Dict[str, List[Optional[Token]]], lemma_list: Dict[str, List[Optional[Token]]]) -> "ElementsInterface":
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

        return RootElements(subject, verb, adjective, rootobject)
    
    @classmethod
    def make_custom_elements(cls, dep_list: Dict[str, List[Optional[Token]]], lemma_list: Dict[str, List[Optional[Token]]], doc:Doc,  option:str) -> "CustomElements":
        subject = Subject(dep_list)
        verb = Verb(dep_list, lemma_list)
        adjective = Adjective(dep_list)
        rootobject = RootObject(dep_list)

        if option == "prep":
            prep = PrepPhrase()
            doc = prep.register_prep_phrase(doc)
            custom_elements = CustomElements(subject, verb, adjective, rootobject, option=prep)
        else:
            raise AttributeError("option is not included")
        return custom_elements