# Dans cet exemple, nous avons deux classes : Node et LinkedList.
# La classe Node représente un nœud dans la liste chaînée et contient une référence à la donnée qu'il stocke et une référence au nœud suivant dans la liste.
# La classe LinkedList représente la liste chaînée elle-même et contient une référence à la tête de la liste.
# La méthode append ajoute un nouveau nœud à la fin de la liste chaînée. Si la liste est vide, le nouveau nœud devient la tête de la liste. Sinon, nous parcourons la liste jusqu'à atteindre le dernier nœud et ajoutons le nouveau nœud à la fin.
# La méthode print_list parcourt la liste chaînée et affiche la donnée stockée dans chaque nœud.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
