from abc import abstractmethod, ABCMeta
from spacy.tokens import Token
from typing import List, Union


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
    def root(self) -> Token:
        """
        return subject
        Params:

        Returns:
            - _get_root(self): (Token)
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
    def root(self) -> List[str]:
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
