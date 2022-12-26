from typing import List, Dict, Optional, Union
from spacy.tokens import Token
from ..interface.Ielements import AdjectiveInterface


class Adjective(AdjectiveInterface):
    DEP = [
        "acomp",
        "ccomp",
        "complm",
        "pcomp",
        "xcomp",
        "attr",
        "oprd",
        "npadvmod"
    ]

    def __init__(self, dep_list: Dict[str, List[Optional[str]]]):
        self._dep_list = dep_list
    
    @property
    def dep_list(self):
        return self._dep_list

    @property
    def root(self):
        return self._get_root()

    def _get_root(self) -> Union[str, Token]:
        """
        get root adjective
        Return
                adjctive(Token) or empty string(string)
        """
        root_verb = self._dep_list["ROOT"][0]
        child = [child.dep_ for child in root_verb.children]

        for speech in self.DEP:
            if speech in child:
                adjective = self._dep_list[speech]
                return adjective[0]
        return ""

    @property
    def have_root(self) -> bool:
        return bool(self.root)
    
    @property
    def span(self):
        return self._get_span()
    
    def _get_span(self)->Optional[List[Token]]:
        root_adjective = self._get_root()
        if type(root_adjective) == str:
            return
        adje_list = [token for token in root_adjective.subtree]
        return adje_list
