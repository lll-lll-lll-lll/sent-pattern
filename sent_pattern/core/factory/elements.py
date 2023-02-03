from sent_pattern.core.elements.elements import RootElements
from sent_pattern.core.elements.sub.phrase import PrepPhrase
from sent_pattern.core.type import DepLemmaListType
from ..elements import Adjective,Subject,RootObject,Verb
from spacy.tokens import Doc
from enum import Enum

class ElementOption(Enum):
    Prep = "prep"
    Relcl = "relcl"

    @classmethod
    def has_option(cls, value: str) -> bool:
        return value in cls._value2member_map_

    @classmethod
    def str_list(cls) -> str:
        return ", ".join([e.value for e in ElementOption])

class CustomElements(RootElements):
    def __init__(self,
            subject: Subject, 
            verb: Verb, 
            adjective: Adjective, 
            rootobject: RootObject, 
            option: ElementOption):

        super().__init__(subject, verb, adjective, rootobject)
        self._option = self._is_valid_option(option)

    def _is_valid_option(self, option_str: str) -> str:
        try:
            if ElementOption.has_option(option_str):
                return option_str
            else:
                raise ValueError
        except ValueError:
            raise ValueError(f"invalid option. valid option: [{ElementOption.str_list()}]")
    
    @property
    def option(self) -> str:
        """
        option property is freely configurable properties
        """
        return self._option


class ElementsFactory:

    @classmethod
    def make_root_elements(cls, dep_list: DepLemmaListType, lemma_list: DepLemmaListType) -> "RootElements":
        """
        create instance of self
        Parameters
        ----------
        dep_list : type.DepLemmaListType
        lemma_list : type.DepLemmaListType

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
    def make_custom_elements(cls, dep_list: DepLemmaListType, lemma_list: DepLemmaListType, doc:Doc,  option:str) -> "CustomElements":
        subject = Subject(dep_list)
        verb = Verb(dep_list, lemma_list)
        adjective = Adjective(dep_list)
        rootobject = RootObject(dep_list)

        prep = PrepPhrase()
        doc = prep.register_prep_phrase(doc)
        custom_elements = CustomElements(subject, verb, adjective, rootobject, option=option)
        return custom_elements