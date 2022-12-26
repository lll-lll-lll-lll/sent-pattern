from typing import List, Dict, Optional
from spacy.tokens import Token
from sent_pattern.core.interface.Ielements import ObjectInterface


class RootObject(ObjectInterface):
    DEP = [
        "pobj",
        "obj",
        "dative",
        "dobj"
    ]

    def __init__(self, dep_list: Dict[str, List[Optional[Token]]]):
        self._dep_list = dep_list

    @property
    def dep_list(self):
        return self._dep_list

    @property
    def root(self) -> List:
        return self._get_root()

    def _get_root(self) -> List[Optional[Token]]:
        objects = []
        root_verb = self._dep_list["ROOT"][0]
        child = [child.dep_ for child in root_verb.children]
        for object_dep in RootObject.DEP:
            if object_dep in child:
                objects.append(self._dep_list[object_dep][0])

        return objects

    @property
    def object_num(self) -> int:
        return len(self.root)

    @property
    def span(self):
        return self._get_span()
    
    def _get_span(self) -> List[Optional[List[Token]]]:
        root_objects = self._get_root()
        if len(root_objects) > 0:
            if len(root_objects) == 1:
                return [token for token in root_objects[0].subtree]
            elif len(root_objects) == 2:
                return [[token for token in root_objects[0].subtree], [token for token in root_objects[1].subtree]]
        return