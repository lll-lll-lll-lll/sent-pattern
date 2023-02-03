from sent_pattern.core.elements import Subject, Verb, Adjective, RootObject

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
