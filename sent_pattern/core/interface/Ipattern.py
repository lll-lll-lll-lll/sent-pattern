from abc import ABCMeta, abstractclassmethod, abstractmethod
from .Ielements import SubjectInterface, VerbInterface, AdjectiveInterface, ObjectInterface, ElementsFactoryInterface


class BaseSentencePatternInterface(metaclass=ABCMeta):
    """ All FifthSentencePattern Base Interface
    """
    pass


class FirstSentencePatternInterface(BaseSentencePatternInterface):
    """ This interface means SV
    """
    @property
    @abstractmethod
    def subject(self) -> "SubjectInterface":
        raise NotImplementedError()

    @property
    @abstractmethod
    def verb(self) -> "VerbInterface":
        raise NotImplementedError()

    @property
    def abbreviation(self) -> str:
        return "SV"


class SecondSentencePatternInterface(BaseSentencePatternInterface):
    """ This interface means SVC
    """

    @property
    @abstractmethod
    def subject(self) -> "SubjectInterface":
        raise NotImplementedError()

    @property
    @abstractmethod
    def verb(self) -> "VerbInterface":
        raise NotImplementedError()

    @property
    @abstractmethod
    def adjective(self) -> "AdjectiveInterface":
        raise NotImplementedError()

    @property
    def abbreviation(self) -> str:
        return "SVC"


class ThirdSentencePatternInterface(BaseSentencePatternInterface):
    """ This interface means "SVO"
    """

    @property
    @abstractmethod
    def subject(self) -> "SubjectInterface":
        raise NotImplementedError()

    @property
    @abstractmethod
    def verb(self) -> "VerbInterface":
        raise NotImplementedError()

    @property
    @abstractmethod
    def object(self) -> "ObjectInterface":
        raise NotImplementedError()

    @property
    def abbreviation(self) -> str:
        return "SVO"


class FourthSentencePatternInterface(BaseSentencePatternInterface):
    """ This interface means SVOO
    """

    def __init__(self):
        raise NotImplementedError()

    @property
    @abstractmethod
    def subject(self) -> "SubjectInterface":
        raise NotImplementedError()

    @property
    @abstractmethod
    def verb(self) -> "VerbInterface":
        raise NotImplementedError()

    @property
    @abstractmethod
    def object(self) -> "ObjectInterface":
        raise NotImplementedError()

    @property
    def abbreviation(self) -> str:
        return "SVOO"


class FifthSentencePatternInterface(BaseSentencePatternInterface):
    """ This interface means SVOC
    """

    def __init__(self):
        raise NotImplementedError()

    @property
    @abstractmethod
    def subject(self) -> "SubjectInterface":
        raise NotImplementedError()

    @property
    @abstractmethod
    def verb(self) -> "VerbInterface":
        raise NotImplementedError()

    @property
    @abstractmethod
    def object(self) -> "ObjectInterface":
        raise NotImplementedError()

    @property
    @abstractmethod
    def adjective(self) -> "AdjectiveInterface":
        raise NotImplementedError()

    @property
    def abbreviation(self) -> str:
        return "SVOC"


class PatternFactoryInterface(metaclass=ABCMeta):
    elements: ElementsFactoryInterface

    @property
    @abstractclassmethod
    def pattern_type(self) -> BaseSentencePatternInterface:
        """
        Return an instance of one of the fifth sentence type classes
        """
        raise NotImplementedError()

    @abstractclassmethod
    def _classify_to_pattern_type(self):
        """
        classify sentence pattern.
        """
        raise NotImplementedError()
