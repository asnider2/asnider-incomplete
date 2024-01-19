import pytest
from docs import *

def test_initialization():
    """tests the initialization of docs"""
    norah = User("norah")
    doc= norah.create_document(None,None)
    assert doc.creator_id== "norah"
    assert doc.name== None
    assert doc.contents == None

def test_create_document():
    """tests the create_document function"""
    norah = User("norah")
    doctor= norah.create_document("Norah","dance")
    assert doctor.name == "Norah"
    assert doctor.contents == "dance"

def test_can_access():
    """tests the can_access function"""
    norah = User("norah")
    drake =User("drake")
    doc1= norah.create_document("Norah", "is")
    doc2 =norah.create_document("k", "lovely")
    assert norah.can_access(doc1)
    assert norah.can_access(doc2)
    assert not drake.can_access(doc2)


def test_get_document():
    """tests the get_document function"""
    norah = User("norah")
    norah.create_document("Norah", "is")
    norah.create_document("k", "lovely")

    I_am = norah.get_document(0)
    assert I_am.contents =="is"
    assert I_am.name == "Norah"

    we_are = norah.get_document(1)
    assert we_are.contents =="lovely"
    assert we_are.name == "k"
    with pytest.raises(Exception):
        we_are.get_document("situationship")

