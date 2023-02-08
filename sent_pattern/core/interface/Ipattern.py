from abc import ABCMeta, abstractmethod
from typing import Any, List,Dict
from spacy.tokens import Token
from sent_pattern.core.elements import Subject,Verb

class IBaseSentencePattern(metaclass=ABCMeta):
    """ All FifthSentencePattern Base Interface
    """
    @property
    @abstractmethod
    def subject(self) -> Subject:
        raise NotImplementedError()
    
    @property
    @abstractmethod
    def verb(self) -> Verb:
        raise NotImplementedError()
    
    @property
    @abstractmethod
    def spans(self) -> Dict[str, List[Any]]:
        """combine the tokens associated with each element token of a sentence type into a single element

        Returns:
            Dict[str, List[Any]]: key: (character representing element tokens for each sentence type) value: ()
        """        
        raise NotImplementedError()
    
    @property
    @abstractmethod
    def spans_str(self) -> Dict[str, List[str]]:
        """
        span property str
        """
        raise NotImplementedError()

    @property
    @abstractmethod
    def abbreviation(self) -> str:
        raise NotImplementedError()