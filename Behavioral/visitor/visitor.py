#!/usr/bin/env python


class ExpressionTreeComponent(object):

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

    def accept(self, visitor):
        visitor.visit(self)


class ExpressionTreeComposite(ExpressionTreeComponent):

    def __init__(self, value):
        super().__init__(value)


class AddNode(ExpressionTreeComposite):

    def __init__(self, left_child, right_child):
        super().__init__('+')
        self.children.append(left_child)
        self.children.append(right_child)


class MultiplyNode(ExpressionTreeComposite):

    def __init__(self, left_child, right_child):
        super().__init__('x')
        self.children.append(left_child)
        self.children.append(right_child)


class ExpressionTreeLeaf(ExpressionTreeComponent):

    def __init__(self, value):
        super().__init__(value)


class NumberNode(ExpressionTreeLeaf):

    def __init__(self, value):
        super().__init__(value)


class DepthFirstTreeVisitor(object):

    def __init__(self):
        self.presistent_state = []

    def visit(self, tree_node):
        self.__dfs(tree_node)

    def __dfs(self, tree_node):
        if len(tree_node.children) == 0:
            self.presistent_state.append(tree_node.value)
        elif len(tree_node.children) == 2:
            for child in tree_node.children:
                child.accept(self)
            self.presistent_state.append(tree_node.value)


def main():
    add = AddNode(NumberNode(2), NumberNode(3))
    multi = MultiplyNode(add, NumberNode(7))
    visitor = DepthFirstTreeVisitor()
    multi.accept(visitor)
    print(visitor.presistent_state)
    # outputs: [2, 3, '+', 7, 'x']


if __name__ == '__main__':
    main()
