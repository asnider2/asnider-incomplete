import pytest
from linkedlist import *

#### STUDENTS
# We have provided you with a very BASIC example of testing for linkedlist.
# Please expand this testing along with testing for your own methods.
####
def test_init():
    """
    Test the initialization of the LinkedList class.
    """
    ## testing correctt initialization of a LinkedList object
    l = LinkedList()
    assert not l.first


def test_append():
    """
    Test the 'append' method of the LinkedList class. This method should add new nodes to
    the end of the list, updating the 'next' attributes of the nodes accordingly.
    """
    ## testing append method works on a new LinkedList object
    m = LinkedList()
    m.append("hello")
    assert m.first.data =="hello"
    m.append("Norah")
    assert m.first.data == "hello"



def test_length():
    """
    Test the 'length' method of the LinkedList class. This method calculates the number of
    elements/nodes in the list.
    """
    ## testing the length of a new LinkedList object is 0
    a = LinkedList()
    assert a.length() == 0

    a.append("Norah")== 1
    a.append("Norah") == 2
    a.append(2) == 3

    a.remove(2)
    assert a.length() == 1


def test_nth():
    """
    Test the 'nth' method of the LinkedList class. The 'nth' method retrieves the nth element.
    """
    ## tests retrieval of nth element when linkedlist object is new (empty)
    o = LinkedList()
    with pytest.raises(Exception):
        o.nth(0)


def test_remove():
    """tests the remove function"""
    #empty
    l = LinkedList()
    with pytest.raises(Exception):
       l.length(0)

    l.append("Rhianna")
    l.append("Beyonce")
    l.append("Drake")
    l.remove("Drake")
    assert l.length() ==2
    assert l.first.data == "Rhianna"
    l.remove("Rhianna")
    assert l.first.data == "Beyonce"
    with pytest.raises(Exception):
        l.remove("Drake")
    with pytest.raises(Exception):
        l.remove(9)

def test_remove_from():
    """tests the remove_from function"""
    norah = LinkedList()
    norah.append("amazing'")
    norah.append("gorgeous")
    norah.append("love")

    with pytest.raises(Exception):
        norah.remove("situationship")


