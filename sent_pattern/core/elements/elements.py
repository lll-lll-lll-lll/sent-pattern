from typing import List, Optional, Union
from sent_pattern.core.elements import Subject, Verb, Adjective, RootObject
from enum import Enum
from spacy.tokens import Doc
from sent_pattern.core.elements.sub.phrase import PrepPhrase
from sent_pattern.core.elements.sub.relative import RelativeClause

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


class ElementOption(Enum):
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
        
        return option in cls._value2member_map_

    @classmethod
    def option_list(cls) -> str:
        """returns a list of what can be set as options

        Returns:
            str: list of options
        """
        return ",".join([e.value for e in ElementOption])

    def __str__(self) -> str:
        if type(self._option) is str:
            return self._option
        return ",".join([e for e in self._option])

class CustomElements(RootElements):
    def __init__(self,
            doc: Doc,
            subject: Subject, 
            verb: Verb, 
            adjective: Adjective, 
            rootobject: RootObject, 
            option: ElementOption = "all"):

        super().__init__(subject, verb, adjective, rootobject)
        self._option = self._is_valid_option(option)
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
            raise ValueError(f"invalid option. valid option: [{ElementOption.option_list()}]")
    
    @property
    def all(self):
        return list(self.relcl, self.prep)
    
    @property
    def relcl(self) -> Optional["RelativeClause"]:
        if self._option == "all" or self._option == ElementOption.Relcl.value:
            return self.__relcl
        return
    
    @property
    def prep(self) ->Optional["PrepPhrase"]:
        return self.__prep
    
    def _get_relcl(self) -> RelativeClause:
        relcl = RelativeClause(self._doc)
        return relcl
    
    def _get_prep(self) -> Optional["PrepPhrase"]:
        prep = PrepPhrase(self._doc)
        return prep