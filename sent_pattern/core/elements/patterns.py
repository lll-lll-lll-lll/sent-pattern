from ..interface.Ipattern import (FirstSentencePatternInterface, FifthSentencePatternInterface, FourthSentencePatternInterface,
                                  SecondSentencePatternInterface, ThirdSentencePatternInterface)
from ..interface.Ielement import SubjectInterface, VerbInterface, AdjectiveInterface, ObjectInterface
from typing import Union, List, Dict,Optional
from spacy.tokens import Token


class FirstSentencePattern(FirstSentencePatternInterface):
    span_dict = dict()
    span_dict_str = dict()
    def __init__(self, subject: SubjectInterface, verb: VerbInterface):
        self._subject = subject
        self._verb = verb

    @property
    def subject(self) -> "SubjectInterface": return self._subject
    @property
    def verb(self) -> "VerbInterface": return self._verb
    
    @property
    def spans(self) -> Dict[str, Union[List[Token], Token]]:
        if self._is_element_in_span_dict(self.span_dict):
            return self.span_dict
        self.span_dict["S"] = self._subject.span(self._subject.root)
        self.span_dict["V"] = self._verb.root
        return self.span_dict
    
    @property
    def span_str(self) -> Dict[str, Optional[str]]:
        if self._is_element_in_span_dict(self.span_dict_str):
            return self.span_dict_str
        self.span_dict_str["S"] = self._subject.span_str(self._subject.root)
        self.span_dict_str["V"] = self._verb.root.text
        return self.span_dict_str
    
    def _is_element_in_span_dict(self, dic:dict) -> bool:
        if len(dic) == 0:
            return False
        return True


class SecondSentencePattern(SecondSentencePatternInterface):
    span_dict = dict()
    span_dict_str = dict()
    def __init__(self, subject: SubjectInterface, verb: VerbInterface, adjective: AdjectiveInterface):
        self._subject = subject
        self._verb = verb
        self._adjective = adjective
        self._adjective_root = adjective.root
        self._subject_root = subject.root
        self._verb_root = verb.root

    @property
    def subject(self) -> "SubjectInterface": return self._subject
    @property
    def verb(self) -> "VerbInterface": return self._verb
    @property
    def adjective(self) -> "AdjectiveInterface": return self._adjective
    
    @property
    def spans(self) -> Dict[str, List[Optional[Token]]]:
        if self._is_element_in_span_dict(self.span_dict):
            return self.span_dict
        self.span_dict["S"] = self._subject.span(self._subject_root)
        self.span_dict["V"] = self._verb_root.text
        self.span_dict["C"] = self._adjective.span(self._adjective_root)
        return self.span_dict
    
    @property
    def span_str(self) -> Dict[str, Optional[str]]:
        if self._is_element_in_span_dict(self.span_dict_str):
            return self.span_dict_str
        adjective_span = self._adjective.span(self._adjective_root)
        self.span_dict_str["S"] = self._subject.span_str(self._subject_root)
        self.span_dict_str["V"] = self._verb.root.text
        self.span_dict_str["C"] = self._adjective.span_str(adjective_span)
        return self.span_dict_str
    
    def _is_element_in_span_dict(self, dic:dict) -> bool:
        if len(dic) == 0:
            return False
        return True


class ThirdSentencePattern(ThirdSentencePatternInterface):
    span_dict = dict()
    span_dict_str = dict()
    def __init__(self, subject: SubjectInterface, verb: VerbInterface, object: ObjectInterface):
        self._subject = subject
        self._verb = verb
        self._object = object
        self._object_root = object.root
        self._subject_root = subject.root
        self._verb_root = verb.root

    @property
    def subject(self) -> "SubjectInterface": return self._subject
    @property
    def verb(self) -> "VerbInterface": return self._verb
    @property
    def object(self) -> "ObjectInterface": return self._object

    @property
    def spans(self) -> Dict[str, List[Optional[Token]]]:
        if self._is_element_in_span_dict(self.span_dict):
            return self.span_dict
        self.span_dict["S"] = self._subject.span(self._subject_root)
        self.span_dict["V"] = self._verb_root.text
        self.span_dict["O"] = self._object.span(self._object_root)
        return self.span_dict
    
    @property
    def span_str(self) -> Dict[str, Optional[str]]:
        if self._is_element_in_span_dict(self.span_dict_str):
            return self.span_dict_str
        self.span_dict_str["S"] = self._subject.span_str(self._subject_root)
        self.span_dict_str["V"] = self._verb_root.text
        self.span_dict_str["O"] = self._object.spans_str(self._object_root)
        return self.span_dict_str
    
    def _is_element_in_span_dict(self, dic:dict) -> bool:
        if len(dic) == 0:
            return False
        return True


class FourthSentencePattern(FourthSentencePatternInterface):
    span_dict = dict()
    span_dict_str = dict()
    def __init__(self, subject: SubjectInterface, verb: VerbInterface, object: ObjectInterface):
        self._subject = subject
        self._verb = verb
        self._object = object
        self._object_root = object.root
        self._subject_root = subject.root
        self._verb_root = verb.root

    @property
    def subject(self) -> "SubjectInterface": return self._subject
    @property
    def verb(self) -> "VerbInterface": return self._verb
    @property
    def object(self) -> "ObjectInterface": return self._object
    
    @property
    def spans(self) -> Dict[str, List[Optional[Token]]]:
        if self._is_element_in_span_dict(self.span_dict):
            return self.span_dict
        self.span_dict["S"] = self._subject.span(self._subject_root)
        self.span_dict["V"] = self._verb.root
        self.span_dict["O1"] = self._object.span(self._object_root)[0]
        self.span_dict["O2"] = self._object.span(self._object_root)[1]
        return self.span_dict
    
    @property
    def span_str(self) -> Dict[str, Optional[str]]:
        if self._is_element_in_span_dict(self.span_dict_str):
            return self.span_dict_str
        self.span_dict_str["S"] = self._subject.span_str(self._subject_root)
        self.span_dict_str["V"] = self._verb.root.text
        self.span_dict_str["O1"] = self._object.spans_str(self._object_root)[0]
        self.span_dict_str["O2"] = self._object.spans_str(self._object_root)[1]
        return self.span_dict_str
    
    def _is_element_in_span_dict(self, dic:dict) -> bool:
        if len(dic) == 0:
            return False
        return True


class FifthSentencePattern(FifthSentencePatternInterface):
    span_dict = dict()
    span_dict_str = dict()
    def __init__(self,
                 subject: SubjectInterface,
                 verb: VerbInterface,
                 object: ObjectInterface,
                 adjective: AdjectiveInterface):

        self._subject = subject
        self._verb = verb
        self._object = object
        self._adjective = adjective
        self._object_root = object.root
        self._subject_root = subject.root
        self._verb_root = verb.root
        self._adjective_root = adjective.root

    @property
    def subject(self) -> "SubjectInterface": return self._subject
    @property
    def verb(self) -> "VerbInterface": return self._verb
    @property
    def object(self) -> "ObjectInterface": return self._object
    @property
    def adjective(self) -> "AdjectiveInterface": return self._adjective
    
    @property
    def spans(self) -> Dict[str, List[Optional[Token]]]:
        if self._is_element_in_span_dict(self.span_dict):
            return self.span_dict
        self.span_dict["S"] = self._subject.span(self._subject_root)
        self.span_dict["V"] = self._verb.root.text
        self.span_dict["O"] = self._object.span(self._object_root)
        self.span_dict["C"] = self._adjective.span(self._adjective_root)
        return self.span_dict
    
    @property
    def span_str(self) -> Dict[str, Optional[str]]:
        if self._is_element_in_span_dict(self.span_dict_str):
            return self.span_dict_str
        adjective_span = self._adjective.span(self._adjective_root)
        self.span_dict_str["S"] = self._subject.span_str(self._subject_root)
        self.span_dict_str["V"] = self._verb.root.text
        self.span_dict_str["O"] = self._object.spans_str(self._object_root)
        self.span_dict_str["C"] = self._adjective.span_str(adjective_span)
        return self.span_dict_str

    def _is_element_in_span_dict(self, dic:dict) -> bool:
        if len(dic) == 0:
            return False
        return True