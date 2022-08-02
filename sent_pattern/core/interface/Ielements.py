from abc import ABCMeta, abstractmethod
from typing import Any, Dict, List, Optional
from spacy.tokens import Token
from .Ielement import SubjectInterface, VerbInterface, AdjectiveInterface, ObjectInterface

class ElementsInterface(metaclass=ABCMeta):
    """
    classes have subject, verb, adjective, and object
    """
    subject: SubjectInterface
    verb: VerbInterface
    adjective: AdjectiveInterface
    rootobject: ObjectInterface

class ElementsFactoryInterface(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
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
        raise NotImplementedError()


    @classmethod
    @abstractmethod
    def make_custom_elements(cls, dep_list: Dict[str, List[Optional[Token]]], lemma_list: Dict[str, List[Optional[Token]]], option: str) -> "ElementsInterface":
        """
        Customize generated elements by 'options'
        Parameters
        ----------
        dep_list : Dict[str, Optional[Token]
        lemma_list : Dict[str, Optional[Token]]
        option: Any. free option

        Returns
        -------
        CustomElements : CustomElements
        """
        raise NotImplementedError()