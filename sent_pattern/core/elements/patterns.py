from sent_pattern.core.elements import Subject, Verb, RootObject, Adjective
from sent_pattern.core.type import FifthSpanDictType, FifthSpanDictTypeStr, FirstSpanDictType, FirstSpanDictTypeStr, FourthSpanDictType, FourthSpanDictTypeStr, SecondSpanDictType, SecondSpanDictTypeStr, ThirdSpanDictType, ThirdSpanDictTypeStr
from ..interface.Ipattern import IBaseSentencePattern
from typing import  Union
from spacy.symbols import ADJ,nsubj
from typing import TypeAlias
from sent_pattern.core.elements import Adjective,RootObject, RootElements



class FirstSentencePattern(IBaseSentencePattern):
    def __init__(self, subject: Subject, verb: Verb):
        self._subject = subject
        self._verb = verb
        self._span_dict:FirstSpanDictType = dict()
        self._span_dict_str:FirstSpanDictTypeStr =dict()

    @property
    def subject(self) -> "Subject": return self._subject
    @property
    def verb(self) -> "Verb": return self._verb
    
    @property
    def spans(self) -> FirstSpanDictType:
        if self._is_element_in_span_dict(self._span_dict):
            return self._span_dict
        self._span_dict["S"] = self._subject.span(self._subject.root)
        self._span_dict["V"] = self._verb.root
        return self._span_dict
    
    @property
    def spans_str(self) -> FirstSpanDictTypeStr:
        if self._is_element_in_span_dict(self._span_dict_str):
            return self._span_dict_str
        subject_span = self._subject.span(self._subject.root)
        self._span_dict_str["S"] = self._subject.span_str(subject_span)
        self._span_dict_str["V"] = self._verb.root.text
        return self._span_dict_str
    
    def _is_element_in_span_dict(self, dic: Union[FirstSpanDictType,FirstSpanDictTypeStr]) -> bool:
        if len(dic) == 0:
            return False
        return True
    
    @property
    def abbreviation(self) -> str:
        return "SV"


class SecondSentencePattern(IBaseSentencePattern):
    def __init__(self, subject: Subject, verb: Verb, adjective: Adjective):
        self._subject = subject
        self._verb = verb
        self._adjective = adjective
        self._adjective_root = adjective.root
        self._subject_root = subject.root
        self._verb_root = verb.root
        self._span_dict:SecondSpanDictType = dict()
        self._span_dict_str:SecondSpanDictTypeStr = dict()

    @property
    def subject(self) -> "Subject": return self._subject
    @property
    def verb(self) -> "Verb": return self._verb
    @property
    def adjective(self) -> "Adjective": return self._adjective
    
    @property
    def spans(self) -> SecondSpanDictType:
        if self._is_element_in_span_dict(self._span_dict):
            return self._span_dict
        self._span_dict["S"] = self._subject.span(self._subject_root)
        self._span_dict["V"] = self._verb_root
        self._span_dict["C"] = self._adjective.span(self._adjective_root)
        return self._span_dict
    
    @property
    def spans_str(self) -> SecondSpanDictTypeStr:
        if self._is_element_in_span_dict(self._span_dict_str):
            return self._span_dict_str
        subject_span = self._subject.span(self._subject.root)
        adjective_span = self._adjective.span(self._adjective_root)
        self._span_dict_str["S"] = self._subject.span_str(subject_span)
        self._span_dict_str["V"] = self._verb.root.text
        self._span_dict_str["C"] = self._adjective.span_str(adjective_span)
        return self._span_dict_str
    
    def _is_element_in_span_dict(self, dic:Union[SecondSpanDictType,SecondSpanDictTypeStr]) -> bool:
        if len(dic) == 0:
            return False
        return True
    
    @property
    def abbreviation(self) -> str:
        return "SVC"



class ThirdSentencePattern(IBaseSentencePattern):
    def __init__(self, subject: Subject, verb: Verb, object: RootObject):
        self._subject = subject
        self._verb = verb
        self._object = object
        self._object_root = object.root
        self._subject_root = subject.root
        self._verb_root = verb.root
        self._span_dict:ThirdSpanDictType = dict()
        self._span_dict_str:ThirdSpanDictTypeStr = dict()

    @property
    def subject(self) -> "Subject": return self._subject
    @property
    def verb(self) -> "Verb": return self._verb
    @property
    def object(self) -> "RootObject": return self._object

    @property
    def spans(self) -> ThirdSpanDictType:
        if self._is_element_in_span_dict(self._span_dict):
            return self._span_dict
        self._span_dict["S"] = self._subject.span(self._subject_root)
        self._span_dict["V"] = self._verb_root
        self._span_dict["O"] = self._object.span(self._object_root)
        return self._span_dict
    
    @property
    def spans_str(self) -> ThirdSpanDictTypeStr:
        if self._is_element_in_span_dict(self._span_dict_str):
            return self._span_dict_str
        subject_span = self._subject.span(self._subject.root)
        object_span = self._object.span(self._object_root)
        self._span_dict_str["S"] = self._subject.span_str(subject_span)
        self._span_dict_str["V"] = self._verb_root.text
        self._span_dict_str["O"] = self._object.span_str(object_span)
        return self._span_dict_str
    
    def _is_element_in_span_dict(self, dic:Union[ThirdSpanDictType,ThirdSpanDictTypeStr]) -> bool:
        if len(dic) == 0:
            return False
        return True
    
    @property
    def abbreviation(self) -> str:
        return "SVO"


class FourthSentencePattern(IBaseSentencePattern):
    def __init__(self, subject: Subject, verb: Verb, object: RootObject):
        self._subject = subject
        self._verb = verb
        self._object = object
        self._object_root = object.root
        self._subject_root = subject.root
        self._verb_root = verb.root
        self._span_dict:FourthSpanDictType = dict()
        self._span_dict_str:FourthSpanDictTypeStr = dict()

    @property
    def subject(self) -> "Subject": return self._subject
    @property
    def verb(self) -> "Verb": return self._verb
    @property
    def object(self) -> "RootObject": return self._object
    
    @property
    def spans(self) -> FourthSpanDictType:
        if self._is_element_in_span_dict(self._span_dict):
            return self._span_dict
        self._span_dict["S"] = self._subject.span(self._subject_root)
        self._span_dict["V"] = self._verb.root
        self._span_dict["O1"] = self._object.span(self._object_root)[0]
        self._span_dict["O2"] = self._object.span(self._object_root)[1]
        return self._span_dict
    
    @property
    def spans_str(self) -> FourthSpanDictTypeStr:
        if self._is_element_in_span_dict(self._span_dict_str):
            return self._span_dict_str
        subject_span = self._subject.span(self._subject.root)
        object_spans = self._object.span(self._object_root)
        self._span_dict_str["S"] = self._subject.span_str(subject_span)
        self._span_dict_str["V"] = self._verb.root.text
        self._span_dict_str["O1"] = self._object.span_str(object_spans)[0]
        self._span_dict_str["O2"] = self._object.span_str(object_spans)[1]
        return self._span_dict_str
    
    def _is_element_in_span_dict(self, dic:Union[FourthSpanDictType,FourthSpanDictTypeStr]) -> bool:
        if len(dic) == 0:
            return False
        return True
    
    @property
    def abbreviation(self) -> str:
        return "SVOO"


class FifthSentencePattern(IBaseSentencePattern):
    def __init__(self,
                 subject: Subject,
                 verb: Verb,
                 object: RootObject,
                 adjective: Adjective):

        self._subject = subject
        self._verb = verb
        self._object = object
        self._adjective = adjective
        self._object_root = object.root
        self._subject_root = subject.root
        self._verb_root = verb.root
        self._adjective_root = adjective.root
        self._span_dict = dict()
        self._span_dict_str = dict()

    @property
    def subject(self) -> "Subject": return self._subject
    @property
    def verb(self) -> "Verb": return self._verb
    @property
    def object(self) -> "RootObject": return self._object
    @property
    def adjective(self) -> "Adjective": return self._adjective
    
    @property
    def spans(self) -> FifthSpanDictType:
        if self._is_element_in_span_dict(self._span_dict):
            return self._span_dict
        self._span_dict["S"] = self._subject.span(self._subject_root)
        self._span_dict["V"] = self._verb.root
        self._span_dict["O"] = self._object.span(self._object_root)
        self._span_dict["C"] = self._adjective.span(self._adjective_root)
        return self._span_dict
    
    @property
    def spans_str(self) -> FifthSpanDictTypeStr:
        if self._is_element_in_span_dict(self._span_dict_str):
            return self._span_dict_str
        subject_span = self._subject.span(self._subject.root)
        object_spans = self._object.span(self._object_root)
        adjective_span = self._adjective.span(self._adjective_root)
        self._span_dict_str["S"] = self._subject.span_str(subject_span)
        self._span_dict_str["V"] = self._verb.root.text
        self._span_dict_str["O"] = self._object.span_str(object_spans)
        self._span_dict_str["C"] = self._adjective.span_str(adjective_span)
        return self._span_dict_str

    def _is_element_in_span_dict(self, dic:Union[FifthSpanDictType, FifthSpanDictTypeStr]) -> bool:
        if len(dic) == 0:
            return False
        return True
    
    @property
    def abbreviation(self) -> str:
        return "SVOC"

    

SentencePatternType: TypeAlias = FirstSentencePattern | SecondSentencePattern | ThirdSentencePattern | FourthSentencePattern | FifthSentencePattern

class SentencePatternDoc:
    def __init__(self, elements: RootElements):
        self.elements = elements

    @property
    def type(self) -> SentencePatternType: return self._classify_pattern_type()

    def _classify_pattern_type(self) -> SentencePatternType:
        """
        classify as one of the fifth sentence types

        Returns
        -------
        pattern: BaseSentencePatternInterface
        """

        subject = self.elements.subject
        verb = self.elements.verb
        adjective = self.elements.adjective
        rootobject = self.elements.rootobject
        
        if self.is_fifth_sentence(adjective=adjective, object=rootobject):
            return FifthSentencePattern(subject=subject, verb=verb, object=rootobject, adjective=adjective)

        if adjective.have_root:
            if rootobject.object_num == 1:
                pattern = FifthSentencePattern(subject=subject, verb=verb, object=rootobject, adjective=adjective)
            else:
                pattern = SecondSentencePattern(subject=subject, verb=verb, adjective=adjective)

        elif rootobject.object_num == 2:
            pattern = FourthSentencePattern(subject=subject, verb=verb, object=rootobject)
        elif rootobject.object_num == 1:
            pattern = ThirdSentencePattern(subject=subject, verb=verb, object=rootobject)
        else:
            pattern = FirstSentencePattern(subject=subject, verb=verb)
        return pattern

    def is_fifth_sentence(self, adjective: Adjective, object: RootObject) -> bool:
        if adjective.have_root == False:
            return False
        if adjective.root.pos == ADJ:
            for token in adjective.root.children:
                if token.dep == nsubj:
                    object.root.append(token)
                    return True
        return False