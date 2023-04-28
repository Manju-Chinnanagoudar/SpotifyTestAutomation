class DragAndDropException(Exception):

    """Exception for drag and drop
    """

    def __init__(self, value):
        self.value = value
    
    def __str__(self) -> str:
        return super().__str__()
    
class NavigationException(Exception):

    """Exception for navigation
    """

    def __init__(self, value):
        self.value = value
    
    def __str__(self) -> str:
        return super().__str__()

class ElementNotFoundException(Exception):
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self) -> str:
        return super().__str__()
    
class ElementActionException(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self) -> str:
        return super().__str__()
    
class ActionFailedException(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self) -> str:
        return super().__str__()
