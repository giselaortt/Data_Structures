from copy import deepcopy
from multipledispatch import dispatch
import collections
from array import array
from typing import Type
import sys
sys.path.insert(0, '../map_skip_list/')
sys.path.insert(0, '../skip_list/')
from map_skip_list import MapSkipList
from skip_list import SkipList


class NodeBTree():
    precision = 0.00001
    max_len = 20


    def __init__( self, parent:'NodeBTree' = None ):
        self.keys = MapSkipList()
        self.parent = parent


    '''
    @dispatch(object)
    def __init__( self, keys:MapSkipList = None ):

        raise NotImplementedError
    '''


    def isLeaf( self ) -> bool:

        return self.keys[0][1] is None


    def __repr__( self ):

        return str(self.keys)


    def __len__( self ):

        return len(self.keys)


    def hasExceded( self ):

        print( len(self.keys) )
        return ( len(self.keys) > self.max_len )


    @dispatch( (int,float) )
    def __contains__( self, value:int ):

        return ( value in self.keys )


    @dispatch(int)
    def insert( self, key:int ) -> None:
       self.keys.insert(key)
       if( self.hasExceded() ):
           self.split()


    def _get_child( self, index:int ):

        raise NotImplementedError


    def _promoteChild( self, child:'None' )->None:

        raise NotImplementedError


    def _split( self ):
        pointer = self.keys
        middle = len(self.keys)/2
        self.keys = self.keys[middle]
        left = pointer[0:middle-1]
        right = pointer[middle+1:]
        #how to link 2 children if i have only one key ?


class BTree():

    def __init__( self ):
        self.root = None


    def __contains__( self, key:int ) -> bool:

        return ( self.search( key ) is not None )


    def __repr__( self ):
        if( self.root is None ):
            return "< >"
        ans = "<" + " ".join([str(self.pre_order())]) + ">"

        return ans


    def insert( self, key:int ) -> None:
        if( self.root is None ):
            self.root = NodeBTree( key )
            return
        node = self._findNodeToInsert( key )
        node.insert(key)
        self.bubbleUp(node)


    def _findNodeToInsert( self, key:int ) -> 'NodeBTree':
        node = BTree._search( key, self.root )
        if( key in node ):
            raise Exception("Operation not allowed.")
        return node


    def bubbleUp( self, node:'NodeBTree' ) -> None:
        while(node.hasExceded()):
            node.split()
            if(node.parent is not None):
                node.parent.removeChild( node )
                node.parent.insert( node )
                node = node.parent


    def search( self, key:int ) -> 'NodeBTree':
        if( self.isEmpty() ):
            return None
        node = BTree._search( key, self.root )
        if(key in node):
            return node
        return None


    @staticmethod
    def _search( key:int, node:'NodeBTree' ) -> 'NodeBTree':
        if( type(node) is not NodeBTree ):
            raise TypeError('expected type NodeBTree')
        if( key in node or node.isLeaf() ):
            return node
        raise NotImplementedError
        if( key < node.keys[0] ):
            return BTree._search( key, node.children[0] )
        if( node.isThreeNodeBTree() and key > node.keys[1] ):
            return BTree._search( key, node.children[2] )
        return BTree._search( key, node.children[1] )


    def pre_order( self ) -> list:
        if(self.root is None):
            return []
        answer = []
        BTree._pre_order(self.root, answer)

        return answer


    @staticmethod
    def _pre_order( node:'NodeBTree', answer:list ) -> list:

        raise NotImplementedError


    def isEmpty( self ):

        return ( self.root is None )


    def remove( self, key ):
        pass



    def _merge(self, node, other):
        pass


