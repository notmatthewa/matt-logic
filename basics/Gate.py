from basics.Node import ConnectionNode


class Gate:
    MAX_INPUTS = 0
    MAX_OUTPUTS = 0
    inputs: list[ConnectionNode] = []
    outputs: list[ConnectionNode] = []

    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs

        if len(inputs) > self.MAX_INPUTS:
            raise ValueError(f"Expected {self.MAX_INPUTS} inputs, got {len(inputs)}")

        if len(outputs) > self.MAX_OUTPUTS:
            raise ValueError(f"Expected {self.MAX_OUTPUTS} outputs, got {len(outputs)}")

        inputs = [ConnectionNode() for _ in range(self.MAX_INPUTS)]
        outputs = [ConnectionNode() for _ in range(self.MAX_OUTPUTS)]

    def execute(self):
        pass

    def __str__(self):
        return f"Gate({self.inputs}, {self.outputs})"
