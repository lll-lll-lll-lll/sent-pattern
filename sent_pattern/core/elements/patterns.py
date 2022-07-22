from ..interface.Ipattern import (FirstSentencePatternInterface, FifthSentencePatternInterface, FourthSentencePatternInterface,
                                  SecondSentencePatternInterface, ThirdSentencePatternInterface)
from ..interface.Ielement import SubjectInterface, VerbInterface, AdjectiveInterface, ObjectInterface


class FirstSentencePattern(FirstSentencePatternInterface):
    def __init__(self, subject: SubjectInterface, verb: VerbInterface):
        self._subject = subject
        self._verb = verb

    @property
    def subject(self) -> "SubjectInterface":
        return self._subject

    @property
    def verb(self) -> "VerbInterface":
        return self._verb


class SecondSentencePattern(SecondSentencePatternInterface):
    def __init__(self, subject: SubjectInterface, verb: VerbInterface, adjective: AdjectiveInterface):
        self._subject = subject
        self._verb = verb
        self._adjective = adjective

    @property
    def subject(self) -> "SubjectInterface":
        return self._subject

    @property
    def verb(self) -> "VerbInterface":
        return self._verb

    @property
    def adjective(self) -> "AdjectiveInterface":
        return self._adjective


class ThirdSentencePattern(ThirdSentencePatternInterface):
    def __init__(self, subject: SubjectInterface, verb: VerbInterface, object: ObjectInterface):
        self._subject = subject
        self._verb = verb
        self._object = object

    @property
    def subject(self) -> "SubjectInterface":
        return self._subject

    @property
    def verb(self) -> "VerbInterface":
        return self._verb

    @property
    def object(self) -> "ObjectInterface":
        return self._object


class FourthSentencePattern(FourthSentencePatternInterface):
    def __init__(self, subject: SubjectInterface, verb: VerbInterface, object: ObjectInterface):
        self._subject = subject
        self._verb = verb
        self._object = object

    @property
    def subject(self) -> "SubjectInterface":
        return self._subject

    @property
    def verb(self) -> "VerbInterface":
        return self._verb

    @property
    def object(self) -> "ObjectInterface":
        return self._object


class FifthSentencePattern(FifthSentencePatternInterface):
    def __init__(self,
                 subject: SubjectInterface,
                 verb: VerbInterface,
                 object: ObjectInterface,
                 adjective: AdjectiveInterface):

        self._subject = subject
        self._verb = verb
        self._object = object
        self._adjective = adjective

    @property
    def subject(self) -> "SubjectInterface":
        return self._subject

    @property
    def verb(self) -> "VerbInterface":
        return self._verb

    @property
    def object(self) -> "ObjectInterface":
        return self._object

    @property
    def adjective(self) -> "AdjectiveInterface":
        return self._adjective
