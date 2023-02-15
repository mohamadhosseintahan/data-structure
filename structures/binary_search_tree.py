class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None


    def display(self):
        lines, *_ = self._display_aux(self.root)
        for line in lines:
            print(line)

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # Node is None.
        if node is None:
            line = 'None'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # No child.
        if node.right is None and node.left is None:
            line = '%s' % node.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = '%s' % node.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = '%s' % node.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = '%s' % node.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    



    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True

        temp = self.root

        while True:
            if value == temp.value:
                return False
            if temp.value > value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            
            elif temp.value < value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contain(self, value):
        temp = self.root

        while temp:
            if temp.value < value:
                temp = temp.right
            
            elif temp.value > value:
                temp = temp.left
            else:
                return True

        return False


tree = BinarySearchTree()

# this code fill the tree in perfect way if second argument be in this order
# 2**n - 1, and n is an positive integer
def fill_tree(root_value, num_nodes):
    if num_nodes == 0:
        return None
    if num_nodes == 1:
        return Node(root_value)
    else:
        root = Node(root_value)
        left_size = (num_nodes - 1) // 2
        right_size = num_nodes - left_size - 1
        root.left = fill_tree(root_value - left_size - 1, left_size)
        root.right = fill_tree(root_value + right_size + 1, right_size)
        return root

tree.root = fill_tree(30,31)
print(tree.contain(100))

tree.display()



# some tree definition

#Full
# if there isn't any node that has just a child, the tree will be full

    #     5
    #    / \
    #   4   6
    #  / \
    # 1   3



#Perfect
# if all nodes, has two children and all leaves, has None in their left and right
# so we have (2**n - 1) item in our tree and this tree is perfect

    #     5
    #    / \
    #   4   6

# complete
# if tree will be filled from left to right, its is complete
#
#       5
#      / \
#     3   4
#    /
#   2
