from abc import abstractmethod, ABCMeta
from spacy.tokens import Token
from typing import List, Union,Optional
from typing import TypeAlias

class RootElementInterface(metaclass=ABCMeta):
    @property
    @abstractmethod
    def root(self) -> Union[Token, str]:
        raise NotImplementedError()

AdjectiveSpanType: TypeAlias = Optional[List[Token]]
AdjectiveSpanStrType: TypeAlias = Optional[str]
AdjectiveRootType: TypeAlias = Union[Token, str]
class AdjectiveInterface(RootElementInterface):
    @property
    @abstractmethod
    def root(self) -> AdjectiveRootType:
        """
        Return Adjective (C)

        Returns:
            - Adjective(Token) | ""(str)
        """
        raise NotImplementedError()
    
    @abstractmethod
    def span(self,root:AdjectiveRootType) -> AdjectiveSpanType:
        """
        Span summarizing subtrees of elements
        """
        raise NotImplementedError()
    
    @abstractmethod
    def span_str(self,spans:AdjectiveSpanType) -> AdjectiveSpanStrType:
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


SubjectSpanType: TypeAlias = List[Token]
SubjectRootType: TypeAlias = Token
class SubjectInterface(RootElementInterface):
    @property
    @abstractmethod
    def root(self) -> SubjectRootType:
        """
        return subject
        Params:

        Returns:
            - _get_root(self): (SubjectRootType)
        """
        raise NotImplementedError()
    
    @abstractmethod
    def span(self,root:SubjectRootType) -> SubjectSpanType:
        """
        Span summarizing subtrees of elements
        """
        raise NotImplementedError()

    @abstractmethod
    def span_str(self,span:SubjectSpanType) -> str:
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

ObjectRootType: TypeAlias = List[Optional[Token]]
ObjectSpanType: TypeAlias = Optional[List[Union[List[Token], Token]]]
class ObjectInterface(RootElementInterface):

    @property
    @abstractmethod
    def root(self) -> ObjectRootType:
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
    def span(self,root:ObjectRootType) -> ObjectSpanType:
        """
        Span summarizing subtrees of elements
        """
        raise NotImplementedError()
    
    @abstractmethod
    def span_str(self,spans: ObjectSpanType) -> Optional[Union[List[str],str]]:
        """
        span property str
        """
        raise NotImplementedError()
