'''
Легковага – це структурний патерн проектування, який дозволяє вмістити більшу
кількість об'єктів у відведену оперативну пам'ять. Легковага заощаджує пам'ять,
розділяючи загальний стан об'єктів між собою, замість зберігання однакових даних
у кожному об'єкті.

Приклад: Розміщення дерев на карті в комп'ютерній грі
'''

class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x, y):
        print(f"Тип дерева: {self.name} Колір: {self.color} Текстура: {self.texture} Координати: ({x}, {y})")

class TreeFactory:
    _tree_types = {}

    @staticmethod
    def get_tree_type(name, color, texture):
        key = (name, color, texture)
        if key not in TreeFactory._tree_types:
            TreeFactory._tree_types[key] = TreeType(name, color, texture)
        return TreeFactory._tree_types[key]

class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def display(self):
        self.tree_type.draw(self.x, self.y)

# Використання
factory = TreeFactory()

# Створюємо багато дерев, багато з яких мають однаковий тип
trees = []

# Приклад розташування дерев
positions = [(10, 20), (15, 25), (20, 30), (25, 35), (17, 10), (33, 12), (28, 10)]
for pos in positions:
    tree_type = factory.get_tree_type("Ялинка", "Зелений", "Густа")
    tree = Tree(pos[0], pos[1], tree_type)
    trees.append(tree)

# Відображення дерев
for tree in trees:
    tree.display()