from sent_pattern.core.interface.Ielement import IRootElement
from sent_pattern.core.type import DepLemmaListType
from typing import Optional
from sent_pattern.core.type import SubjectRootType, SubjectSpanType,  DepLemmaListType


class Subject(IRootElement):
    DEP = [
        "nsubj",
        "nsubjpass",
        "csubj",
        "csubjpass"
    ]

    def __init__(self, dep_list: DepLemmaListType):
        self._dep_list = dep_list
        self._subject_root = self._get_root()

    @property
    def root(self) -> SubjectRootType:
        """
        return subject
        Params:

        Returns:
            - _get_root(self): (SubjectRootType)
        """
        return self._subject_root

    def span(self,root:SubjectRootType) -> SubjectSpanType:
        """
        Span summarizing subtrees of elements
        """
        return self._get_span(root)
    
    def span_str(self, spans:SubjectSpanType) -> str:
        """
        span property str
        """
        return " ".join([token.text for token in spans])

    def _get_root(self) -> SubjectRootType:
        subj_type = self._get_subj_type()
        root_subject = self._dep_list[subj_type][0]
        return root_subject

    def _get_subj_type(self) -> Optional[str]:
        root_verb = self._dep_list["ROOT"][0]
        verb_child_dep = [
            child.dep_ for child in root_verb.children]
        for subj in Subject.DEP:
            if subj in verb_child_dep:
                return subj
    
    def _get_span(self, root:SubjectRootType) -> SubjectSpanType:
        return [token for token in root.subtree]
    
    
