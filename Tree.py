class TreeNode:
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

# Пример: файловая система
root = TreeNode('root', is_file=False)
folder1 = TreeNode('folder1', is_file=False)
folder2 = TreeNode('folder2', is_file=False)
file1 = TreeNode('file1.txt', is_file=True)
file2 = TreeNode('file2.txt', is_file=True)

root.add_child(folder1)
root.add_child(folder2)
folder1.add_child(file1)
folder2.add_child(file2)

# Функция для отображения структуры файловой системы
def display_tree(node, level=0):
    indent = ' ' * (level * 2)
    print(f"{indent}{node.name} {'(File)' if node.is_file else '(Folder)'}")
    for child in node.children:
        display_tree(child, level + 1)

display_tree(root)
# Вывод:
# root (Folder)
#   folder1 (Folder)
#     file1.txt (File)
#   folder2 (Folder)
#     file2.txt (File)
