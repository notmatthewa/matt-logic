from uuid import uuid4


class Node:
    value: bool = False
    id: str = ""

    def __init__(self):
        self.id = str(uuid4())

    def set_value(self, value: bool):
        self.value = value


class ConnectionNode(Node):
    outgoing: list[Node] = []
    incoming: list[Node] = []

    def __init__(self):
        super().__init__()

    def add_outgoing(self, node: Node):
        self.outgoing.append(node)

    def add_incoming(self, node: Node):
        self.incoming.append(node)

    def remove_outgoing(self, node: Node):
        self.outgoing.remove(node)

    def remove_incoming(self, node: Node):
        self.incoming.remove(node)

    def __str__(self):
        return f"ConnectionNode({self.id})"
