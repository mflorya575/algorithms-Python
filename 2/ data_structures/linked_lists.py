class Node:
    def __init__(self, value=None, next_node=None):
        self.next_node = next_node
        self.value = value

    def __str__(self):
        return str(self.value)


class List:
    def __init__(self):
        # Ссылка на первый элемент.
        self.head = None

    def append(self, value):
        """
        Добавление нового элемента в конец связного списка.
        Время работы O(N).
        """

        # Если нет первого элемента, то создаем и завершаем работу.
        if self.head is None:
            self.head = Node(value)
            return

        # Перебираем по очереди все элементы, чтобы найти последний
        current = self.head
        while current.next_node is not None:
            current = current.next_node

        # Создаем ссылку для последнего элемента на новый
        current.next_node = Node(value)

    def __str__(self):
        """
        Возвращает все элементы связного списка в виде строки.
        """
        current = self.head
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"


lst = List()
lst.append(75)
lst.append(12)
lst.append(28)
lst.append(6)
print(lst)
