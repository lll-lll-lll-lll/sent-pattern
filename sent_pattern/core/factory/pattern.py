from sent_pattern.core.interface.Ielement import AdjectiveInterface,ObjectInterface
from ..interface.Ipattern import BaseSentencePatternInterface, SentencePatternInterface
from ..interface.Ielements import  ElementsInterface
from ..elements.patterns import FirstSentencePattern, SecondSentencePattern, ThirdSentencePattern, FourthSentencePattern, FifthSentencePattern
from spacy.symbols import ADJ,nsubj

class SentencePattern(SentencePatternInterface):
    def __init__(self, elements: ElementsInterface):
        self.elements = elements

    @property
    def pattern_name(self) -> str:
        """
        Returns
        -------
        name: str
            the class name string of one of the fifth sentence types
        """
        name = self.pattern_type.__class__.__name__
        return name

    @property
    def pattern_type(self) -> BaseSentencePatternInterface:
        return self._classify_pattern_type()

    def _classify_pattern_type(self) -> BaseSentencePatternInterface:
        """
        classify as one of the fifth sentence types

        Returns
        -------
        pattern: BaseSentencePatternInterface
        """

        subject = self.elements.subject
        verb = self.elements.verb
        adjective = self.elements.adjective
        rootobject = self.elements.rootobject
        
        if self.is_fifth_sentence(adjective=adjective, object=rootobject):
            return FifthSentencePattern(subject=subject, verb=verb, object=rootobject, adjective=adjective)

        if adjective.have_root:
            if rootobject.object_num == 1:
                pattern = FifthSentencePattern(subject=subject, verb=verb, object=rootobject, adjective=adjective)
            else:
                pattern = SecondSentencePattern(subject=subject, verb=verb, adjective=adjective)

        elif rootobject.object_num == 2:
            pattern = FourthSentencePattern(subject=subject, verb=verb, object=rootobject)
        elif rootobject.object_num == 1:
            pattern = ThirdSentencePattern(subject=subject, verb=verb, object=rootobject)
        else:
            pattern = FirstSentencePattern(subject=subject, verb=verb)
        return pattern

    def is_fifth_sentence(self, adjective: AdjectiveInterface, object: ObjectInterface)-> bool:
        if adjective.have_root == False:
            return False
        if adjective.root.pos == ADJ:
            for token in adjective.root.children:
                if token.dep == nsubj:
                    object.root.append(token)
                    return True
        return False