class Document:
    """represents a document in a cloud-based document editing and sharing system"""

    def __init__(self, creator_id: int, name: str, contents: str):
        self.name = name
        self.contents = contents
        self.creator_id = creator_id
        self.shared_user_ids = set()

    def share_with_user(self, user_id: int):
        """adds a user to the set of users with document access"""
        self.shared_user_ids.add(user_id)

    def unshare_with_user(self, user_id: int):
        """removes a user from the set of users with document access"""
        self.shared_user_ids.remove(user_id)

    def user_ids_with_access(self) -> set:
        """returns a set of all users with document access """
        return {self.creator_id} | self.shared_user_ids


class NoDocumentError(Exception):
    pass

class User:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.documents = []

    def create_document(self, name: str, contents: str):
       """takes in the name and contents of a document and creates a new document"""
       user_doc= Document(self.user_id, name, contents)
       self.documents.append(user_doc)
       return user_doc

    def can_access(self, doc: Document)-> bool:
        """takes in a Document and returns a boolean checking whether the user’s ID is in the set of users who can
        access the documen"""
        return self.user_id in doc.user_ids_with_access()

    def get_document(self, index: int) -> Document:
        """ takes in the index of a document and returns that document"""
        if index >= len(self.documents):
            raise NoDocumentError("not there")
        return self.documents[index]

    class AdminUser:
        def can_access(self, document: Document)-> bool:
            """gives access to any document for AdminUser"""
            return True