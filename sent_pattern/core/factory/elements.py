from sent_pattern.core.elements.elements import CustomElements, ElementOption, RootElements
from sent_pattern.core.elements.sub.phrase import PrepPhrase
from sent_pattern.core.type import DepLemmaListType
from ..elements import Adjective,Subject,RootObject,Verb

class ElementsFactory:

    @classmethod
    def make_root_elements(cls, dep_list: DepLemmaListType) -> "RootElements":
        """
        create instance of self
        Parameters
        ----------
        dep_list : type.DepLemmaListType

        Returns
        -------
        RootElements : self
        """
        subject = Subject(dep_list)
        verb = Verb(dep_list)
        adjective = Adjective(dep_list)
        rootobject = RootObject(dep_list)

        return RootElements(subject, verb, adjective, rootobject)
    
    @classmethod
    def make_custom_elements(cls, dep_list: DepLemmaListType,  opt:str = "all") -> "CustomElements":
        """_summary_

        Args:
            dep_list (DepLemmaListType): dict for each dep of Token
            doc (Doc): spacy.tokens.Doc
            option (str): _description_

        Returns:
            CustomElements: _description_
        """        
        subject = Subject(dep_list)
        verb = Verb(dep_list)
        adjective = Adjective(dep_list)
        rootobject = RootObject(dep_list)
        options = ElementOption(option=opt)
        custom_elements = CustomElements(subject, verb, adjective, rootobject, option=options)
        return custom_elements