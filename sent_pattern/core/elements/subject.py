from ..interface.Ielements import SubjectInterface
from typing import Dict, List, Optional
from spacy.tokens import Token


class Subject(SubjectInterface):
    DEP = [
        "nsubj",
        "nsubjpass",
        "csubj",
        "csubjpass"
    ]

    def __init__(self, dep_list: Dict[str, List[Optional[Token]]]):
        self._dep_list = dep_list
        self._subject_root = self._get_root()

    @property
    def root(self) -> Token:
        return self._subject_root

    @property
    def dep_list(self):
        return self._dep_list

    def _get_root(self) -> List[Token]:
        subj_type = self._get_subj_type()
        root_subject = self.dep_list[subj_type][0]
        return root_subject

    def _get_subj_type(self):
        root_verb = self.dep_list["ROOT"][0]
        verb_child_dep = [
            child.dep_ for child in root_verb.children]
        for subj in Subject.DEP:
            if subj in verb_child_dep:
                return subj
    
    def span(self,root_subject_token:Token):
        return self._get_span(root_subject_token)
    
    def _get_span(self, root_subject_token:Token) -> List[Token]:
        return [token for token in root_subject_token.subtree]
    
    def span_str(self, root_subject_token:Token) -> str:
        spans = self._get_span(root_subject_token)
        return " ".join([token.text for token in spans])
