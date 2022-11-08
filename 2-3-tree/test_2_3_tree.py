import pytest
from tree_2_3 import Node, Tree_2_3


class Test():

    def test_insert_key( self ):
        node = Node(1)
        node.insertKey(2)
        assert 2 in node


    @staticmethod
    def proove_all_keys( node ):
        if(node is None):
            return
        assert (type(node.keys) == list)
        assert (len(node.keys) >= 1 and len(node.keys)<=3 )
        for key in node.keys:
            assert (type(key) is int)
        if( node.children is None ):
            return
        for child in node.children:
            Test.proove_all_keys(child)


    @staticmethod
    def proove_all_children(node):
        if(node is None):
            return
        if( node.children is None ):
            return
        assert (type(node.children) is list)
        assert (len(node.children) >= 2 and len(node.children)<=3 )
        for child in node.children:
            assert (type(child) is Node)
            Test.proove_all_children(child)


    def test_has_exceded( self ):
        node = Node( 2 )
        node.keys = [2,3,4]
        assert node.hasExceded()


    def test_has_exceded_should_be_false( self ):
        node = Node( 2 )
        node.keys = [2,3]
        assert (not node.hasExceded())


    def test_insert_node_on_the_right( self ):
        pass


    def test_insert_node_on_the_left( self ):
        pass


    def test_insert_node_on_the_middle( self ):
        pass


    def test_split_on_leaf_node( self ):
        node = Node( 2 )
        node.keys = [2,3,4]
        node.split()
        assert  len(node.children)==2
        print( node.children )
        assert (node.children[0].parent is node and node.children[1].parent is node)
        assert (node.children[0].keys == [2] and node.children[1].keys == [4])


    def proove_nodes( self, tree ):
        node = tree.root
        Test.proove_all_keys(node)
        Test.proove_all_children(node)


    def test( self ):
        tree = Tree_2_3()
        tree.insert( 0 )
        tree.insert( 1 )
        tree.insert( 2 )
        tree.insert( 3 )
        tree.insert( 4 )
        tree.insert( 5 )
        tree.insert( 6 )
        tree.insert( 7 )
        tree.insert( 8 )
        tree.insert( 9 )
        tree.insert( 10 )
        tree.insert( 11 )
        tree.insert( 12 )
        tree.insert( 13 )
        self.proove_nodes(tree)


    def test_is_leaf_node( self ):
        node = Node( 2 )
        assert node.isLeaf() is True


    def test_is_leaf_when_not_leaf( self ):
        pass


    def test_create_node_with_key( self ):
        node = Node( 4 )
        assert node.keys == [4]


    def test_is_smaller_than( self ):
        node = Node( 2 )
        other_node = Node( 3 )
        assert node < other_node


    def test_is_equal( self ):
        node = Node(2)
        other = Node(2)
        assert node == other


    def test_is_greater_than( self ):
        node = Node(2)
        other = Node(4)
        assert other > node


    def test_greater_equal( self ):
        node = Node( 3 )
        other_node = Node( 3 )
        assert node >= other_node


    def test_greater_equal_with_diferent_values( self ):
        node = Node( 3 )
        other_node = Node( 2 )
        assert node >= other_node


    def test_add_key_greater( self ):
        node = Node( 3 )
        node.insertKey( 4 )
        assert node.keys[0] == 3 and node.keys[1] == 4


    def test_add_key_smaller( self ):
        node = Node( 3 )
        node.insertKey( 2 )
        assert node.keys[0] == 2 and node.keys[1] == 3


    def test_contain_on_empty_tree_returns_false( self ):
        tree = Tree_2_3()
        assert (0 in tree) is False


    def test_is_empty_when_false( self ):
        tree = Tree_2_3()
        tree.insert( 0 )
        assert tree.isEmpty() is False


    def test_is_two_node( self ):
        node = Node( 2 )
        assert  node.isTwoNode()


    def test_is_two_node_should_be_false( self ):
        node = Node(2)
        node.insertKey( 3 )
        assert (not node.isTwoNode())


    def test_is_three_node( self ):
        node = Node( 2 )
        node.insertKey( 3 )
        assert node.isThreeNode()


    def test_is_tree_node_false( self ):
        node = Node( 2 )
        assert  node.isThreeNode() is False


    def test_should_add_multiple_keys_in_tree( self ):
        tree = Tree_2_3()
        tree.insert( 0 )
        tree.insert( 2 )
        tree.insert( 3 )
        tree.insert( 5 )
        """
        tree.insert( 4 )
        tree.insert( 6 )
        tree.insert( 7 )
        tree.insert( 8 )
        """


