from abc import ABCMeta, abstractmethod
from typing import List,Dict
from spacy.tokens import Token

class IBaseSentencePattern(metaclass=ABCMeta):
    """ All FifthSentencePattern Base Interface
    """
    @property
    @abstractmethod
    def spans(self) -> Dict[str, List[Token]]:
        raise NotImplementedError()
    
    @property
    @abstractmethod
    def spans_to_str(self) -> Dict[str, List[str]]:
        """
        span property str
        """
        raise NotImplementedError()

    @property
    @abstractmethod
    def abbreviation(self) -> str:
        raise NotImplementedError()