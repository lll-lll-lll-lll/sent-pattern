from typing import List, Dict, Optional, Union
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
        self._object_root = self._get_root()

    @property
    def dep_list(self):
        return self._dep_list

    @property
    def root(self) -> List[Optional[Token]]:
        return self._object_root

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

    def span(self,root_objects:List[Optional[Token]]):
        return self._get_span(root_objects)
    
    def _get_span(self, root_objects:List[Optional[Token]]) -> Optional[List[Union[List[Token], Token]]]:
        if len(root_objects) == 0:
            return
        if len(root_objects) == 1:
            return [token for token in root_objects[0].subtree]
        elif len(root_objects) == 2:
            return [[token for token in root_objects[0].subtree], [token for token in root_objects[1].subtree]]
        return
    
    def spans_str(self, spans: Optional[List[Union[List[Token], Token]]]) -> Optional[Union[List[str],str]]:
        if len(spans) == 0:
            return
        elif len(spans) == 1:
            return " ".join([token.text for token in spans])
        elif len(spans) == 2:
            return [" ".join([token.text for token in spans[0]])," ".join([token.text for token in spans[1]])]
        return
        