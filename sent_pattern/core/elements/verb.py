from typing import Any, List, Optional
from spacy.tokens import Token
from sent_pattern.core.interface.Ielement import IRootElement


class Verb:
    def __init__(self, dep_list):
        self._dep_list = dep_list
        self._verb_root = self._get_root_verb()

    @property
    def root(self) -> Token:
        return self._verb_root

    @property
    def root_verb_children(self)-> List[Any]:
        child = [child for child in self._dep_list["ROOT"][0].children]
        return child

    def _get_root_verb(self) -> Optional[Token]:
        root = self._dep_list["ROOT"][0]
        if not root:
            return
        return root
