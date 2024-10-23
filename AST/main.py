class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        """
        :param node_type: String indicating the type of node ('operator' or 'operand')
        :param value: The condition value (used for operand nodes)
        :param left: Left child (used for operator nodes)
        :param right: Right child (used for operator nodes)
        """
        self.type = node_type
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value}, left={self.left}, right={self.right})"
