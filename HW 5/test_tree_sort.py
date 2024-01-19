from tree_sort import *
def test_tree_sort():
  my_list_none = []
  tree_sort(my_list_none)

  #test empty list
  assert my_list_none == []

  #single item in list
  my_list_one = [5]
  assert my_list_one == [5]

  #duplicates
  my_list_duplicate =[5,4,3,3,2,3,1,5]
  new_duplicate= tree_sort(my_list_duplicate)
  assert new_duplicate == [1, 2, 3, 3, 3, 4,5,5]

  #big list
  big_list=list(range(100, 0, -1))
  new_big_list= tree_sort(big_list)
  assert new_big_list == list(range(1, 101))

  #negative numbers
  negative_list = [-2, -1, -2, -3, -4, -5]
  new_neg = tree_sort(negative_list)
  assert new_neg == [-5, -4, -3, -2, -2, -1]

  #negative and pos
  neg_pos = [-2, 1, -2, -3, -4, 5]
  new_npos = tree_sort(neg_pos)
  assert new_npos == [-4, -3,-2, -2, 1, 5]


  def test_tree_sort_randomly():
    MAX_LENGTH = 100
    MIN_VALUE = -100000
    MAX_VALUE =  100000
    NUM_TRIALS = 100
    def test_mergesort_random():
        for i in range(NUM_TRIALS):
            test_list = random_list(MAX_LENGTH, MIN_VALUE, MAX_VALUE)
        assert test_mergesort_random(test_list) == tree_sort(test_list)