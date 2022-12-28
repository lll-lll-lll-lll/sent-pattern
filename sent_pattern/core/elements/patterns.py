from ..interface.Ipattern import (FirstSentencePatternInterface, FifthSentencePatternInterface, FourthSentencePatternInterface,
                                  SecondSentencePatternInterface, ThirdSentencePatternInterface)
from ..interface.Ielement import SubjectInterface, VerbInterface, AdjectiveInterface, ObjectInterface
from typing import TypeAlias, Union, List, Dict,Optional
from spacy.tokens import Token

FirstSpanDictType: TypeAlias = Dict[str, Union[Token, List[Token]]]
FirstSpanDictTypeStr: TypeAlias = Dict[str, Optional[str]]
class FirstSentencePattern(FirstSentencePatternInterface):
    span_dict: FirstSpanDictType = dict()
    span_dict_str: FirstSpanDictTypeStr = dict()
    def __init__(self, subject: SubjectInterface, verb: VerbInterface):
        self._subject = subject
        self._verb = verb

    @property
    def subject(self) -> "SubjectInterface": return self._subject
    @property
    def verb(self) -> "VerbInterface": return self._verb
    
    @property
    def spans(self) -> FirstSpanDictType:
        if self._is_element_in_span_dict(self.span_dict):
            return self.span_dict
        self.span_dict["S"] = self._subject.span(self._subject.root)
        self.span_dict["V"] = self._verb.root
        return self.span_dict
    
    @property
    def spans_to_str(self) -> FirstSpanDictTypeStr:
        if self._is_element_in_span_dict(self.span_dict_str):
            return self.span_dict_str
        subject_span = self._subject.span(self._subject.root)
        self.span_dict_str["S"] = self._subject.span_str(subject_span)
        self.span_dict_str["V"] = self._verb.root.text
        return self.span_dict_str
    
    def _is_element_in_span_dict(self, dic: Union[FirstSpanDictType,FirstSpanDictTypeStr]) -> bool:
        if len(dic) == 0:
            return False
        return True

SecondSpanDictType: TypeAlias = Dict[str, List[Optional[Union[Token, str, List[Token]]]]]
SecondSpanDictTypeStr: TypeAlias = Dict[str, Optional[str]]
class SecondSentencePattern(SecondSentencePatternInterface):
    span_dict:SecondSpanDictType = dict()
    span_dict_str:SecondSpanDictTypeStr = dict()
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
    def spans(self) -> SecondSpanDictType:
        if self._is_element_in_span_dict(self.span_dict):
            return self.span_dict
        self.span_dict["S"] = self._subject.span(self._subject_root)
        self.span_dict["V"] = self._verb_root
        self.span_dict["C"] = self._adjective.span(self._adjective_root)
        return self.span_dict
    
    @property
    def spans_to_str(self) -> SecondSpanDictTypeStr:
        if self._is_element_in_span_dict(self.span_dict_str):
            return self.span_dict_str
        subject_span = self._subject.span(self._subject.root)
        adjective_span = self._adjective.span(self._adjective_root)
        self.span_dict_str["S"] = self._subject.span_str(subject_span)
        self.span_dict_str["V"] = self._verb.root.text
        self.span_dict_str["C"] = self._adjective.span_str(adjective_span)
        return self.span_dict_str
    
    def _is_element_in_span_dict(self, dic:Union[SecondSpanDictType,SecondSpanDictTypeStr]) -> bool:
        if len(dic) == 0:
            return False
        return True


ThirdSpanDictType: TypeAlias = Dict[str, List[Optional[Union[Token, str, List[Token]]]]]
ThirdSpanDictTypeStr: TypeAlias = Dict[str, Optional[str]]
class ThirdSentencePattern(ThirdSentencePatternInterface):
    span_dict:ThirdSpanDictType = dict()
    span_dict_str:ThirdSpanDictTypeStr = dict()
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
    def spans(self) -> ThirdSpanDictType:
        if self._is_element_in_span_dict(self.span_dict):
            return self.span_dict
        self.span_dict["S"] = self._subject.span(self._subject_root)
        self.span_dict["V"] = self._verb_root
        self.span_dict["O"] = self._object.span(self._object_root)
        return self.span_dict
    
    @property
    def spans_to_str(self) -> ThirdSpanDictTypeStr:
        if self._is_element_in_span_dict(self.span_dict_str):
            return self.span_dict_str
        subject_span = self._subject.span(self._subject.root)
        object_span = self._object.span(self._object_root)
        self.span_dict_str["S"] = self._subject.span_str(subject_span)
        self.span_dict_str["V"] = self._verb_root.text
        self.span_dict_str["O"] = self._object.span_str(object_span)
        return self.span_dict_str
    
    def _is_element_in_span_dict(self, dic:Union[ThirdSpanDictType,ThirdSpanDictTypeStr]) -> bool:
        if len(dic) == 0:
            return False
        return True

FourthSpanDictType: TypeAlias = Dict[str, Optional[List[Union[List[Token], Token]]]]
FourthSpanDictTypeStr: TypeAlias = Dict[str, Optional[str]]
class FourthSentencePattern(FourthSentencePatternInterface):
    span_dict:FourthSpanDictType = dict()
    span_dict_str:FourthSpanDictTypeStr = dict()
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
    def spans(self) -> FourthSpanDictType:
        if self._is_element_in_span_dict(self.span_dict):
            return self.span_dict
        self.span_dict["S"] = self._subject.span(self._subject_root)
        self.span_dict["V"] = self._verb.root
        self.span_dict["O1"] = self._object.span(self._object_root)[0]
        self.span_dict["O2"] = self._object.span(self._object_root)[1]
        return self.span_dict
    
    @property
    def spans_to_str(self) -> FourthSpanDictTypeStr:
        if self._is_element_in_span_dict(self.span_dict_str):
            return self.span_dict_str
        subject_span = self._subject.span(self._subject.root)
        object_spans = self._object.span(self._object_root)
        self.span_dict_str["S"] = self._subject.span_str(subject_span)
        self.span_dict_str["V"] = self._verb.root.text
        self.span_dict_str["O1"] = self._object.span_str(object_spans)[0]
        self.span_dict_str["O2"] = self._object.span_str(object_spans)[1]
        return self.span_dict_str
    
    def _is_element_in_span_dict(self, dic:Union[FourthSpanDictType,FourthSpanDictTypeStr]) -> bool:
        if len(dic) == 0:
            return False
        return True

FifthSpanDictType: TypeAlias = Dict[str, Optional[List[Union[List[Token], Token]]]]
FifthSpanDictTypeStr: TypeAlias = Dict[str, Optional[str]]
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
    def spans(self) -> FifthSpanDictType:
        if self._is_element_in_span_dict(self.span_dict):
            return self.span_dict
        self.span_dict["S"] = self._subject.span(self._subject_root)
        self.span_dict["V"] = self._verb.root
        self.span_dict["O"] = self._object.span(self._object_root)
        self.span_dict["C"] = self._adjective.span(self._adjective_root)
        return self.span_dict
    
    @property
    def spans_to_str(self) -> FifthSpanDictTypeStr:
        if self._is_element_in_span_dict(self.span_dict_str):
            return self.span_dict_str
        subject_span = self._subject.span(self._subject.root)
        object_spans = self._object.span(self._object_root)
        adjective_span = self._adjective.span(self._adjective_root)
        self.span_dict_str["S"] = self._subject.span_str(subject_span)
        self.span_dict_str["V"] = self._verb.root.text
        self.span_dict_str["O"] = self._object.span_str(object_spans)
        self.span_dict_str["C"] = self._adjective.span_str(adjective_span)
        return self.span_dict_str

    def _is_element_in_span_dict(self, dic:Union[FifthSpanDictType, FifthSpanDictTypeStr]) -> bool:
        if len(dic) == 0:
            return False
        return True