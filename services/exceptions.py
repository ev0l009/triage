class TriageError(Exception):
    pass

class InvalidAttributeError(TriageError):
    pass

class DataBaseError(TriageError):
    pass