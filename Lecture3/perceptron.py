# import numpy as np

class Perceptron:
    """ A perceptron model.
    >>> p = Perceptron(3, [1,2,3], 4)
    >>> p.input([0,1,0])
    0
    >>> p.input([1,0,1])
    0
    >>> p.input([0,1,1])
    1
    """
    def __init__(self, num_inputs, weights, threshold):
        if num_inputs != len(weights):
            raise ValueError('Input number and weight mismatch')
        self.ninputs = num_inputs
        self.weights = weights
        self.threshold = threshold
    def input(self, input_list):
        if self.ninputs != len(input_list):
            raise ValueError('The input list length should match the number of inputs')
        weighted_sum = 0
        for i in range(len(self.weights)):
            weighted_sum+= self.weights[i] * input_list[i]
        # weighted_sum = np.dot(self.weights, input_list)
        if weighted_sum > self.threshold:
            return 1
        else:
            return 0
class Decision(Perceptron):
    """ Models a binary decision that someone would want to make.
    """
    def __init__(self, decision, num_factors, weights, factors=[], threshold=None):
        if not threshold:
            threshold = sum(weights)/2
        Perceptron.__init__(self, num_factors, weights, threshold)
        self.decision = decision
        self.factors = factors
    def eval_factors(self):
        print("Answer Y or N for the following questions")
        factor_input = []
        for i in range(self.ninputs):
            valid_inp = False
            while not valid_inp:
                val = input(self.factors[i]+" ").upper()
                if val == "Y":
                    valid_inp = True
                    factor_input.append(1)
                elif val == "N":
                    valid_inp = True
                    factor_input.append(0)
                else:
                    print("Invalid Input")
        self.test_factors(factor_input)

    def test_factors(self, factor_input):
        value = Perceptron.input(self, factor_input)
        if value:
            print("You should", self.decision)
        else:
            print("You should not", self.decision)
    def new_decision(evaluate=True):
        """ Starts a command line prompt that evaluates a new decision
        Args:
        evaliate (boolean): whether or not we should evaluate the new decision or
        just return it
        Returns:
        A decision that has been set up by the series of user prompts
        """
        decision = input('What would you like to decide today? ')
        num_factors = int(input('How many factors does this depend on? '))
        factors = []
        weights = []
        for i in range(1, num_factors+1):

            factor = input('Factor {0}: '.format(i))
            weight = int(input('How much does {0} matter to you (0-10)? '.format(factor)))
            while weight > 10 or weight < 0:
                weight = int(input("{0} isn't a valid value, enter a number 0 - 10: ".format(weight)))
            factors.append(factor)
            weights.append(weight)
        d = Decision(decision, num_factors, weights, factors)
        print('Decision Created!')
        keep_deciding = evaluate
        while keep_deciding:
            command = input("Type 'q' to quit or 'f' to try new factors ")
            if command == 'q':
                keep_deciding = False
            elif command == 'f':
                d.eval_factors()
            else:
                print("Invalid command")
        return d
class PerceptronNetwork:
    def __init__(self, sizes):
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
    def feedforward(self,a):
        for b, w in zip(self.biases, self.weights):
            a = np.dot(w, a)+b
        return a
    def adjust_weight(self, j, k, l, val):
        '''
        Sets the weight w^l_{jk} that connects the kth node in the (l-1) layer
        to the jth node in the lth layer
        j, k, and l are all indexed starting at 1. All of teh
        '''
        # Normalization to zero-based indexing
        self.weights[(l-2)][(j-1)][(k-1)] = val
