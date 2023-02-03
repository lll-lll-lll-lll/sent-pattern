from typing import Any, List
from spacy.tokens import Token
from sent_pattern.core.interface.Ielement import IRootElement


class RootVerb(IRootElement):
    def __init__(self, verb: Token):
        self.__root = verb
        if not verb:
            raise AttributeError.message("root verb doesn't exist.")

    @property
    def root(self) -> Token:
        return self.__root

    def __str__(self) -> str:
        return self.root.text


class Verb(IRootElement):
    DEP = []

    def __init__(self, dep_list, lemma_list):
        self._dep_list = dep_list
        self._lemma_list = lemma_list
        self._verb_root = self._get_root_verb()

    @property
    def root(self) -> Token:
        return self._verb_root

    @property
    def root_verb_children(self)-> List[Any]:
        child = [child for child in self._dep_list["ROOT"][0].children]
        return child

    def _get_root_verb(self) -> Token:
        root = RootVerb(self._dep_list["ROOT"][0]).root
        return root
