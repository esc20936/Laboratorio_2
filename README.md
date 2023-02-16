
# Bayesian Network

This is a Python class that implements a Bayesian Network. It takes a probability dictionary as input, and provides methods for validating the dictionary, compacting it, and performing inference on the network.

# Install
```
pip install BayesianNetworksPablo
```


## Probability Dictionary

The probability dictionary is a dictionary that specifies the probability distribution for each variable in the network. The keys of the dictionary are the variable names, and the values are dictionaries with the following keys:

probs: A list of probabilities for the variable. The sum of these probabilities must be 1, and each probability must be between 0 and 1.

parents: A list of tuples, where each tuple contains the name of a parent variable and a value for that parent variable. For example, if variable A has two parent variables B and C, with values 0 and 1, respectively, then the parents entry for A would be [(B, '0'), (C, '1')].
## Methods

The class provides the following methods:

validate_prob_dict(): Validates the probability dictionary to ensure that it is properly formatted and does not contain circular dependencies.
compact_prob_dict(): Compacts the probability dictionary into a string that represents the network in a more concise form.
inference(query): Performs inference on the network given a query, which is a tuple containing a variable name and a set of observed values. Returns the probability of the query variable given the observed values.
get_compact_prob_dict(): Returns the compact form of the probability dictionary as a string.
## Example Usage

Here is an example of how to use the Bayesian Network class:

``` prob_dict = {
    'A': {
        'probs': [0.6, 0.4],
        'parents': []
    },
    'B': {
        'probs': [0.7, 0.3],
        'parents': []
    },
    'C': {
        'probs': [0.8, 0.2],
        'parents': [('A', '0'), ('B', '0')]
    },
    'D': {
        'probs': [0.9, 0.1],
        'parents': [('B', '1')]
    },
    'E': {
        'probs': [0.3, 0.7],
        'parents': [('C', '0'), ('D', '0')]
    }
}

# Create a BayesianNetwork object
bn = BayesianNetwork(prob_dict)

# Validate the probability dictionary
bn.validate_prob_dict()

# Get the compact form of the probability dictionary
print(bn.compact)

# Perform inference on the network
query = ('E', ('A', '0'))
result = bn.inference(query)
print(f"P({query[0]}|{query[1]}) = {result:.3f}") ```



```
Salida

P(A)P(B)P(C|AB)P(D|B)P(E|CD)

P(E|A=0) = 0.648
```

