from spacy.tokens import Token
from ..interface.Ielements import VerbInterface


class RootVerb(VerbInterface):
    def __init__(self, verb: Token):
        self.__root = verb
        if not verb:
            raise AttributeError.message("root verb doesn't exist.")

    @property
    def root(self):
        return self.__root

    def __str__(self) -> str:
        return self.root.text


class Verb(VerbInterface):
    DEP = []

    def __init__(self, dep_list, lemma_list):
        self._dep_list = dep_list
        self._lemma_list = lemma_list

    @property
    def root(self) -> RootVerb:
        return self._get_root_verb()

    @property
    def beVerb(self):
        return self._getBeVerb()

    @property
    def root_verb_children(self):
        child = [child for child in self._dep_list["ROOT"][0].children]
        return child

    def _get_root_verb(self):
        root = RootVerb(self._dep_list["ROOT"][0]).root
        return root
