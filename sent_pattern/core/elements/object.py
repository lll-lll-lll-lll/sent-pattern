from typing import List,  Optional, Union
from sent_pattern.core.interface.Ielement import IRootElement
from sent_pattern.core.type import DepLemmaListType
from sent_pattern.core.type import ObjectSpanType, ObjectRootType,  DepLemmaListType


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
    
    def span(self,root:ObjectRootType) ->ObjectSpanType: 
        return self._get_span(root)
    
    def span_str(self, spans: ObjectSpanType) -> Optional[Union[List[str],str]]:
        """If the target word is included in the sentence, the tokens are concatenated into a string

        Args:
            spans (ObjectSpanType): tokens related to the target word token

        Returns:
            Optional[Union[List[str],str]]: argument spans converted to string
        """        
        if len(spans) == 0:
            return
        elif len(spans) == 1:
            return " ".join([token.text for token in spans[0]])
        elif len(spans) == 2:
            return [" ".join([token.text for token in spans[0]])," ".join([token.text for token in spans[1]])]
        return

    def _get_root(self) -> ObjectRootType:
        """If the child token's dep of the verb in the sentence is included in the DEP list, return a list of the tokens

        Returns:
            ObjectRootType: List of tokens matched to DEP list
        """        
        objects = []
        root_verb = self._dep_list["ROOT"][0]
        child = [child.dep_ for child in root_verb.children]
        for object_dep in RootObject.DEP:
            if object_dep in child:
                objects.append(self._dep_list[object_dep][0])
        return objects

    def _get_span(self, root:ObjectRootType) ->ObjectSpanType:
        """extract tokens related to the target word token

        Args:
            root (ObjectRootType): Token corresponding to sentence type "O" (ex. ThirdSentencePattern(SVO))

        Returns:
            ObjectSpanType: tokens related to the target word token
        """        
        if len(root) == 0:
            return
        if len(root) == 1:
            return [[token for token in root[0].subtree]]
        elif len(root) == 2:
            return [[token for token in root[0].subtree], [token for token in root[1].subtree]]
        return
    
    
        