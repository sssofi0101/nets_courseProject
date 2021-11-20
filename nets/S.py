from Neuron import Neuron


class S(Neuron):
    def __init__(self,entries=None, weights=None,current_value=None):
        """Constructor"""
        super().__init__(entries,weights,current_value)
        self.entries=None

    def getValue(self):
        return self.current_value
