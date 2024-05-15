from basics.Gate import Gate


class XOR_Gate_2x1(Gate):
    MAX_INPUTS = 2
    MAX_OUTPUTS = 1

    def __init__(self, inputs, outputs):
        super().__init__(inputs, outputs)

    def execute(self):
        self.outputs[0].value = self.inputs[0].value ^ self.inputs[1].value


class XOR_Gate_3x1(Gate):
    MAX_INPUTS = 3
    MAX_OUTPUTS = 1

    def __init__(self, inputs, outputs):
        super().__init__(inputs, outputs)

    def execute(self):
        self.outputs[0].value = (
            self.inputs[0].value ^ self.inputs[1].value ^ self.inputs[2].value
        )
