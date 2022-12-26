from abc import abstractmethod, ABCMeta
from spacy.tokens import Token, Span
from typing import List, Union,Optional


class RootElementInterface(metaclass=ABCMeta):
    @property
    @abstractmethod
    def root(self) -> Union[Token, str]:
        raise NotImplementedError()


class AdjectiveInterface(RootElementInterface):
    @property
    @abstractmethod
    def root(self) -> Union[Token, str]:
        """
        Return Adjective (C)

        Returns:
            - Adjective(Token) | ""(str)
        """
        raise NotImplementedError()
    
    @abstractmethod
    def span(self,root_adjective:Union[str, Token]) -> Optional[List[Token]]:
        """
        Span summarizing subtrees of elements
        """
        raise NotImplementedError()
    
    @abstractmethod
    def span_str(self,spans:Optional[List[Token]]) -> str:
        """
        span property str
        """
        raise NotImplementedError()

    @property
    @abstractmethod
    def have_root(self) -> bool:
        """Whether or not have an adjective
        Params:

        Returns:
            - True: has adjective
            - False: not adjective
        """
        raise NotImplementedError()


class SubjectInterface(RootElementInterface):

    def __init__(self, dep_list):
        pass

    @property
    @abstractmethod
    def root(self) ->Token:
        """
        return subject
        Params:

        Returns:
            - _get_root(self): (Token)
        """
        raise NotImplementedError()
    
    @abstractmethod
    def span(self,root_subject_token:Token) -> List[Token]:
        """
        Span summarizing subtrees of elements
        """
        raise NotImplementedError()

    @abstractmethod
    def span_str(self,root_subject_token:Token) -> str:
        """
        span property str
        """
        raise NotImplementedError()


class VerbInterface(RootElementInterface):

    @property
    @abstractmethod
    def root(self) -> Token:
        """return verb of root
        Returns:
            root(Token)
        """
        return NotImplementedError()


class ObjectInterface(RootElementInterface):

    @property
    @abstractmethod
    def root(self) -> List[Optional[Token]]:
        """return list of objects
        Returns:
            objects: List
        """
        raise NotImplementedError()

    @property
    @abstractmethod
    def object_num(self) -> int:
        """num of objects
        """
        raise NotImplementedError()
    
    @abstractmethod
    def span(self,root_objects:List[Optional[Token]]) -> List[Optional[List[Token]]]:
        """
        Span summarizing subtrees of elements
        """
        raise NotImplementedError()
    
    @abstractmethod
    def spans_str(self,spans: Optional[List[Union[List[Token], Token]]]) -> Optional[Union[List[str],str]]:
        """
        span property str
        """
        raise NotImplementedError()
