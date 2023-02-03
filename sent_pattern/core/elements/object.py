from typing import List,  Optional, Union
from sent_pattern.core.interface.Ielement import IRootElement, ObjectSpanType,ObjectRootType
from sent_pattern.core.type import DepLemmaListType

class RootObject(IRootElement):
    DEP = [
        "pobj",
        "obj",
        "dative",
        "dobj"
    ]

    def __init__(self, dep_list: DepLemmaListType):
        self._dep_list = dep_list
        self._object_root = self._get_root()

    @property
    def dep_list(self) -> DepLemmaListType:
        return self._dep_list

    @property
    def root(self) -> ObjectRootType:
        return self._object_root
    
    @property
    def object_num(self) -> int:
        return len(self.root)

    def _get_root(self) -> ObjectRootType:
        objects = []
        root_verb = self._dep_list["ROOT"][0]
        child = [child.dep_ for child in root_verb.children]
        for object_dep in RootObject.DEP:
            if object_dep in child:
                objects.append(self._dep_list[object_dep][0])
        return objects

    def span(self,root:ObjectRootType) ->ObjectSpanType:
        return self._get_span(root)
    
    def _get_span(self, root:ObjectRootType) ->ObjectSpanType:
        if len(root) == 0:
            return
        if len(root) == 1:
            return [[token for token in root[0].subtree]]
        elif len(root) == 2:
            return [[token for token in root[0].subtree], [token for token in root[1].subtree]]
        return
    
    def span_str(self, spans: ObjectSpanType) -> Optional[Union[List[str],str]]:
        if len(spans) == 0:
            return
        elif len(spans) == 1:
            return " ".join([token.text for token in spans[0]])
        elif len(spans) == 2:
            return [" ".join([token.text for token in spans[0]])," ".join([token.text for token in spans[1]])]
        return
        