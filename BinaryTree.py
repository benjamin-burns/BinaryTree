from __future__ import annotations
from typing import TypeVar, Generic

T = TypeVar('T')

class BinaryTree(Generic[T]):
    """
    Simple BinaryTree component implemented 'bare-handed.'
    BinaryTree[T] is a recursively defined structure that is parameterized by type T.

    DOCUMENTATION DEFINITIONS:
        SIZE(x):
            the number of root elements contained in x, excluding roots with value None
        
        HEIGHT(x):
            the number of nodes along the longest path from the root to a leaf in x
    """

    def __init__(self):
        """
        Default constructor.

        Preconditions: none

        Postconditions:
            {self.root} = None,
            {self.leftTree} = None,
            {self.rightTree} = None,
            {self.size} = 0
        """
        self.root: T = None
        self.leftTree: BinaryTree[T] = None
        self.rightTree: BinaryTree[T] = None
        self.size: int = 0
    
    def assemble(self, root: T, leftTree: BinaryTree, rightTree: BinaryTree) -> None:
        """
        Builds a binary tree, setting the root to {root}, and the left and right subtrees to {leftTree} and {rightTree}, respectively.

        Preconditions:
            {root} /= None,
            {leftTree} /= None,
            {rightTree} /= None

        Postconditions:
            {self} = compose({root}, {leftTree}, {rightTree}),
            {size} = 1 + SIZE({leftTree}) + SIZE({rightTree})

        Aliases:
        {leftTree} -> {self.leftTree}
        {rightTree} -> {self.rightTree}
        """
        self.root = root
        self.leftTree = leftTree
        self.rightTree = rightTree
        self.size = 1 + leftTree.getSize() + rightTree.getSize()

    def disassemble(self) -> tuple[T, BinaryTree, BinaryTree]:
        """
        Deconstructs a binary tree, returning the root, left subtree, and right subtree in that order.

        Preconditions:
            SIZE({self}) > 0

        Postconditions:
            disassemble = <self.root, self.leftTree, self.rightTree>

        Aliases:
            {self.root} -> [client variable]
            {self.leftTree} -> [client variable]
            {self.rightTree} -> [client variable]
        """
        return self.root, self.leftTree, self.rightTree

    def getSize(self) -> int:
        """
        Reports the size of a binary tree.

        Preconditions: none.

        Postconditions:
            getSize = SIZE({self})
        """
        return self.size

    def height(self) -> int:
        """
        Reports the height of a binary tree.

        Preconditions: none.

        Postconditons:
            height = HEIGHT({self})
        """
        maxHeight: int = 0
        if self.size > 0:
            tempRoot, tempLeft, tempRight = self.disassemble()
            leftHeight = tempLeft.height()
            rightHeight = tempRight.height()
            maxHeight = 1 + max(leftHeight, rightHeight)
        return maxHeight

    def __str__(self) -> str:
        """
        Outputs the string representation of a binary tree.

        Preconditions: none.

        Postconditions:
            __str__ = "({self.root}, ({self.leftTree}), ({self.rightTree}))"
        """
        output: str = "()"
        if self.size > 0:
            output = "(" + self.root + ", " + self.leftTree.__str__() + ", " + self.rightTree.__str__() + ")"
        return output