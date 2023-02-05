from sent_pattern.core.interface.Ielement import IRootElement
from sent_pattern.core.type import AdjectiveRootType, AdjectiveSpanStrType, AdjectiveSpanType, DepLemmaListType


class Adjective(IRootElement):
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

    def __init__(self, dep_list:DepLemmaListType):
        self._dep_list = dep_list
        self._adjective_root = self._get_root()
    
    @property
    def root(self) -> AdjectiveRootType:
        """
        Return Adjective (C)

        Returns:
            - Adjective(Token) | ""(str)
        """
        return self._adjective_root

    def span(self,root:AdjectiveRootType) -> AdjectiveSpanType: return self._get_span(root)
    
    def span_str(self, spans:AdjectiveSpanType) -> AdjectiveSpanStrType:
        if len(spans) == 0:
            return
        else:
            return " ".join([token.text for token in spans if token.dep_ != "nsubj"])
    
    @property
    def have_root(self) -> bool:
        """Whether or not have an adjective
        Params:

        Returns:
            - True: has adjective
            - False: not adjective
        """
        return bool(self.root)

    def _get_root(self) -> AdjectiveRootType:
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

    def _get_span(self, root:AdjectiveRootType)->AdjectiveSpanType:
        """method that returns a list of subtrees of the root of the argument

        Args:
            root (AdjectiveRootType): _description_

        Returns:
            AdjectiveSpanType:  Type[List[Token]] | Type[None]
        """        
        if type(root) == str:
            return
        adje_list = [token for token in root.subtree]
        return adje_list

    