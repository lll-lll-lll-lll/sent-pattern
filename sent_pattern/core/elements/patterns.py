from ..interface.Ipattern import (FirstSentencePatternInterface, FifthSentencePatternInterface, FourthSentencePatternInterface,
                                  SecondSentencePatternInterface, ThirdSentencePatternInterface)
from ..interface.Ielement import SubjectInterface, VerbInterface, AdjectiveInterface, ObjectInterface
from typing import Union, List, Dict,Optional
from spacy.tokens import Token


class FirstSentencePattern(FirstSentencePatternInterface):
    def __init__(self, subject: SubjectInterface, verb: VerbInterface):
        self._subject = subject
        self._verb = verb

    @property
    def subject(self) -> "SubjectInterface":
        return self._subject

    @property
    def verb(self) -> "VerbInterface":
        return self._verb
    
    @property
    def spans(self) -> Dict[str, Union[List[Token], Token]]:
        span_dict = dict()
        span_dict["S"] = self._subject.span
        span_dict["V"] = self._verb.root
        return span_dict


class SecondSentencePattern(SecondSentencePatternInterface):
    def __init__(self, subject: SubjectInterface, verb: VerbInterface, adjective: AdjectiveInterface):
        self._subject = subject
        self._verb = verb
        self._adjective = adjective

    @property
    def subject(self) -> "SubjectInterface":
        return self._subject

    @property
    def verb(self) -> "VerbInterface":
        return self._verb

    @property
    def adjective(self) -> "AdjectiveInterface":
        return self._adjective
    
    @property
    def spans(self) -> Dict[str, List[Optional[Token]]]:
        span_dict = dict()
        span_dict["S"] = self._subject.span
        span_dict["V"] = self._verb.root
        span_dict["C"] = self._adjective.span
        return span_dict


class ThirdSentencePattern(ThirdSentencePatternInterface):
    def __init__(self, subject: SubjectInterface, verb: VerbInterface, object: ObjectInterface):
        self._subject = subject
        self._verb = verb
        self._object = object

    @property
    def subject(self) -> "SubjectInterface":
        return self._subject

    @property
    def verb(self) -> "VerbInterface":
        return self._verb

    @property
    def object(self) -> "ObjectInterface":
        return self._object
    
    @property
    def spans(self) -> Dict[str, List[Optional[Token]]]:
        span_dict = dict()
        span_dict["S"] = self._subject.span
        span_dict["V"] = self._verb.root
        span_dict["O"] = self._object.span
        return span_dict


class FourthSentencePattern(FourthSentencePatternInterface):
    def __init__(self, subject: SubjectInterface, verb: VerbInterface, object: ObjectInterface):
        self._subject = subject
        self._verb = verb
        self._object = object

    @property
    def subject(self) -> "SubjectInterface":
        return self._subject

    @property
    def verb(self) -> "VerbInterface":
        return self._verb

    @property
    def object(self) -> "ObjectInterface":
        return self._object
    
    @property
    def spans(self) -> Dict[str, List[Optional[Token]]]:
        span_dict = dict()
        span_dict["S"] = self._subject.span
        span_dict["V"] = self._verb.root
        span_dict["O1"] = self._object.span[0]
        span_dict["O2"] = self._object.span[1]
        return span_dict


class FifthSentencePattern(FifthSentencePatternInterface):
    def __init__(self,
                 subject: SubjectInterface,
                 verb: VerbInterface,
                 object: ObjectInterface,
                 adjective: AdjectiveInterface):

        self._subject = subject
        self._verb = verb
        self._object = object
        self._adjective = adjective

    @property
    def subject(self) -> "SubjectInterface":
        return self._subject

    @property
    def verb(self) -> "VerbInterface":
        return self._verb

    @property
    def object(self) -> "ObjectInterface":
        return self._object

    @property
    def adjective(self) -> "AdjectiveInterface":
        return self._adjective
    
    @property
    def spans(self) -> Dict[str, List[Optional[Token]]]:
        span_dict = dict()
        span_dict["S"] = self._subject.span
        span_dict["V"] = self._verb.root
        span_dict["O"] = self._object.span
        span_dict["C"] = self.adjective.span
        return span_dict
