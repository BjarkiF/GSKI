class Error(Exception):
    pass

class NotFoundException(Error):
    pass

class ItemExistsException(Error):
    pass