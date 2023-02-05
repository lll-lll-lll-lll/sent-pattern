from abc import abstractmethod, ABCMeta
from spacy.tokens import Token
from typing import Union

class IRootElement(metaclass=ABCMeta):
    @property
    @abstractmethod
    def root(self) -> Union[Token, str]:
        raise NotImplementedError()

    @abstractmethod
    def span(self):
        raise NotImplementedError()

    @abstractmethod
    def span_str(self):
        raise NotImplementedError()