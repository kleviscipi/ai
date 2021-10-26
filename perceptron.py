class Perceptron:

    node_inputs     = []
    node_weight     = []
    threshould      = 0

    def __init__(self,node_input,node_weight,threshould):

        self.node_inputs = node_input
        self.node_weight = node_weight

        self.threshould = threshould
   
    def activation(self):
        sum_i_w = 0
        for x in range(len(self.node_inputs)):
            sum_i_w += self.node_inputs[x] * self.node_weight[x]
        
        if sum_i_w > self.threshould:
            return True
        return False



perceptron = Perceptron([1, 0, 1, 0, 1],[0.7, 0.6, 0.5, 0.3, 0.4],1.5)

if perceptron.activation():
    print("Yes i will go to concert")
else:
    print("No i will not go to concert")
