from typing import List, Optional, Union
from sent_pattern.core.elements import Subject, Verb, Adjective, RootObject
from spacy.tokens import Doc
from sent_pattern.core.elements.sub.phrase import PrepPhrase
from sent_pattern.core.elements.sub.relative import RelativeClause
from sent_pattern.core.type import DepLemmaListType

def make_root_elements(dep_list: DepLemmaListType) -> "RootElements":
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


def make_custom_elements(doc:Doc, dep_list: DepLemmaListType,  opt:str = "all") -> "CustomElements":
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
    custom_elements = CustomElements(doc, subject, verb, adjective, rootobject, option=options)
    return custom_elements


class RootElements:
    """
    this class have just subject, verb, adjective and object
    """
    def __init__(self, 
            subject: Subject, 
            verb: Verb, 
            adjective: Adjective, 
            rootobject: RootObject):

        self.subject = subject
        self.verb = verb
        self.adjective = adjective
        self.rootobject = rootobject


class ElementOption:
    _all = "all"
    Prep = "prep"
    Relcl = "relcl"
    
    def __init__(self, option: Union[List[str],str]) -> None:
        self._option = option

    @classmethod
    def has_option(cls, option: str) -> bool:
        """returns a bool indicating whether the option is configurable or not

        Args:
            option (str): option str (etc. prep, relcl)

        Returns:
            bool: whether the option is configurable or not
        """
        opt_list = cls.option_list()
        return option in opt_list

    @classmethod
    def option_list(cls) -> List[str]:
        """returns a list of what can be set as options

        Returns:
            str: list of options
        """
        return [cls.Prep, cls.Relcl, cls._all]

    def __str__(self) -> str:
        if type(self._option) is str:
            return self._option
        return " ".join([e for e in self._option])

class CustomElements(RootElements):
    def __init__(self,
            doc: Doc,
            subject: Subject, 
            verb: Verb, 
            adjective: Adjective, 
            rootobject: RootObject, 
            option: ElementOption):

        super().__init__(subject, verb, adjective, rootobject)
        self._option = self._is_valid_option(option.__str__())
        self._doc = doc
        self.__relcl = self._get_relcl()
        self.__prep = self._get_prep()

    def _is_valid_option(self, option: str) -> str:
        """determine if the argument option is a configurable option

        Args:
            option (str): _description_

        Raises:
            ValueError: _description_

        Returns:
            str: _description_
        """        
        try:
            if ElementOption.has_option(option):
                return option
            else:
                raise ValueError
        except ValueError:
            raise ValueError(f"invalid option. your option is {option} valid option: [{ElementOption.option_list()}]")
    
    @property
    def all(self):
        return [self.relcl, self.prep]
    
    @property
    def relcl(self) -> Optional["RelativeClause"]:
        if self._option == "all" or self._option == ElementOption.Relcl:
            return self.__relcl
        return
    
    @property
    def prep(self) ->Optional["PrepPhrase"]:
        return self.__prep
    
    def _get_relcl(self) -> Optional[RelativeClause]:
        relcl = RelativeClause(self._doc)
        if relcl.relcl_section:
            return relcl
        return 
    
    def _get_prep(self) -> Optional["PrepPhrase"]:
        prep = PrepPhrase(self._doc)
        if prep.prep_phrase:
            return prep
        return