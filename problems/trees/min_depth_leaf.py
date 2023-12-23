from tree import Tree



def min_depth_leaf(tree):
    """
    Computes the minimum depth of a leaf in the tree (length of shortest
    path from the root to a leaf).
    Input:
        tree: a Tree instance.
    
    Returns: (integer) the minimum depth of of a leaf in the tree.
    """
    if not tree.children:
        return 0
    return min(min_depth_leaf(child) for child in tree.children) + 1
    
def min_depth_leaf_custom(tree, custom_depth=0):
    """
    Finds the custom minimum depth of a leaf in the tree. By default,
    it finds the absolute minimum depth.
    
    Inputs:
    tree (Tree): The tree to find the minimum depth in.
    Custom_depth (int, optional): The custom depth to start from. Defaults to 0.
    
    Returns (int): The custom minimum depth of a leaf in the tree.
    """
    def lst_of_depth(tree, depth=0):
        """
        Recursively finds the depths of all leaves in the tree and returns
        them in a sorted list.
        
        Parameters:
        tree (Tree): The tree to find the depths in.
        depth (int, optional): The current depth. Defaults to 0.
        
        Returns:
        list: A sorted list of the depths of all leaves in the tree.
        """
        if not tree.children:
            return [depth]
        return sorted(new_depth for child in tree.children for new_depth \
            in lst_of_depth(child, depth + 1))
    tree_lst_of_depth = lst_of_depth(tree)
    if len(tree_lst_of_depth) > custom_depth:
        return tree_lst_of_depth[custom_depth]
    else:
        return tree_lst_of_depth[-1]


import sys
import pytest
import util

sys.path.append('../')

import test_utils as utils
import tree_test_utils as tree_utils

def do_test_min_depth_leaf(trees_and_original_trees, tree_name, expected):
    trees, original_trees = trees_and_original_trees
    recreate_msg = tree_utils.gen_recreate_msg_with_trees('min_depth_leaf', tree_name)
    actual = min_depth_leaf(trees[tree_name])
    utils.check_none(actual, recreate_msg)
    utils.check_type(actual, expected, recreate_msg)
    utils.check_equals(actual, expected, recreate_msg)
    tree_utils.check_tree_unmodified(trees[tree_name], original_trees[tree_name], 
                                recreate_msg)


def test_min_depth_leaf_1(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_1", 1)

def test_min_depth_leaf_2(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_2", 1)

def test_min_depth_leaf_3(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_3", 5)

def test_min_depth_leaf_4(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_4", 4)

def test_min_depth_leaf_5(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_5", 3)

def test_min_depth_leaf_6(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_6", 2)

def test_min_depth_leaf_7(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_7", 2)

def test_min_depth_leaf_8(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_8", 2)

def test_min_depth_leaf_9(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_9", 49)

def test_min_depth_leaf_10(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_10", 2)

def test_min_depth_leaf_11(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_11", 6)

def test_min_depth_leaf_12(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_12", 2)

def test_min_depth_leaf_13(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_13", 4)

def test_min_depth_leaf_14(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_14", 4)

def test_min_depth_leaf_15(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_15", 3)

def test_min_depth_leaf_16(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_16", 4)

def test_min_depth_leaf_17(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_17", 2)

def test_min_depth_leaf_18(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_18", 6)

def test_min_depth_leaf_19(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_19", 3)

def test_min_depth_leaf_20(trees_min_depth_leaf):
    do_test_min_depth_leaf(trees_min_depth_leaf, "tree_20", 2)

@pytest.fixture(scope="session")
def trees_min_depth_leaf():
    """
    Fixture for loading the trees for min_depth_leaf
    """
    return get_trees()

def get_trees():
    trees = util.load_trees("sample_trees.json")
    original_trees = util.load_trees("sample_trees.json")
    return trees, original_trees