from basics.Gate import Gate


class NOT_Gate_1x1(Gate):
    MAX_INPUTS = 1
    MAX_OUTPUTS = 1

    def __init__(self, inputs, outputs):
        super().__init__(inputs, outputs)

    def execute(self):
        self.outputs[0].value = not self.inputs[0].value
