# we will apply MCMC (Gibbs sampling) on a Bayesian network to estimate P(Query | Evidence)
import random
from collections import defaultdict

class BayesNet:
    def __init__(self, parents, cpt):
        self.parents = parents
        self.cpt = cpt


def gibbs_sampling(bn, query, evidence, num_samples):
    if num_samples <= 0:
        raise ValueError("num_samples must be > 0")

    nodes = list(bn.parents.keys())

    if query not in nodes:
        raise KeyError(f"Unknown query node: {query}")

    unknown_evidence = [n for n in evidence if n not in nodes]
    if unknown_evidence:
        raise KeyError(f"Unknown evidence nodes: {unknown_evidence}")

    # state initialization
    state = {}

    for n in nodes:
        if n in evidence:
            state[n] = bool(evidence[n])  # do not change evidence nodes
        else:
            state[n] = random.choice([True, False])

    counts = defaultdict(int)

    # non-evidence nodes are the only ones resampled
    non_evidence_nodes = [n for n in nodes if n not in evidence]

    for _ in range(num_samples):
        for node in non_evidence_nodes:
            p_True = conditional_probability(bn, node, state)
            state[node] = random.random() < p_True
        counts[state[query]] += 1

    # normalize counts to get probability distribution
    total = sum(counts.values())
    return {k: v / total for k, v in counts.items()}


def _local_probability(bn, node, value, state):
    parents = bn.parents[node]
    parent_values = tuple(state[p] for p in parents)
    return bn.cpt[(parent_values, node)][value]


def _markov_blanket_unnormalized(bn, node, value, state):
    temp_state = state.copy()
    temp_state[node] = value

    # P(node=value | Parents(node))
    prob = _local_probability(bn, node, value, temp_state)

    # Multiply by each child's conditional probability under the updated node value
    children = [n for n, p in bn.parents.items() if node in p]
    for child in children:
        child_value = temp_state[child]
        prob *= _local_probability(bn, child, child_value, temp_state)

    return prob


#here we are defnining confditional probability P(node=value | MarkovBlanket(node)) which is proportional to P(node=value | Parents(node)) * Π P(child | Parents(child))
# Note that the denominator P(MarkovBlanket(node)) is not needed for Gibbs sampling since we only need the relative probabilities of node being True vs False, and the denominator cancels out when we normalize.

def conditional_probability(bn, node, state):
    p_true_unnormalized = _markov_blanket_unnormalized(bn, node, True, state)
    p_false_unnormalized = _markov_blanket_unnormalized(bn, node, False, state)

    denom = p_true_unnormalized + p_false_unnormalized
    if denom == 0:
        return 0.5
    return p_true_unnormalized / denom


# convenience wrapper matching earlier naming
def gibbs_Ask(X, evidence, bn, num_samples):
    return gibbs_sampling(bn, X, evidence, num_samples)

#we will test the implementation using the student example from the book
if __name__ == "__main__":
    # Define the Bayesian network
    bn = BayesNet(
        parents={
            'Difficulty': [],
            'Intelligence': [],
            'Grade': ['Difficulty', 'Intelligence'],
            'Letter': ['Grade']
        },
        cpt={
            ((), 'Difficulty'): {True: 0.6, False: 0.4},
            ((), 'Intelligence'): {True: 0.7, False: 0.3},
            ((True, True), 'Grade'): {True: 0.9, False: 0.1},
            ((True, False), 'Grade'): {True: 0.8, False: 0.2},
            ((False, True), 'Grade'): {True: 0.7, False: 0.3},
            ((False, False), 'Grade'): {True: 0.1, False: 0.9},
            ((True,), 'Letter'): {True: 0.9, False: 0.1},
            ((False,), 'Letter'): {True: 0.2, False: 0.8}
        }
    )

    # Query probability of Grade given Difficulty=True and Intelligence=False
    evidence = {'Difficulty': True, 'Intelligence': True}
    query = 'Grade'
    num_samples = 10000

    result = gibbs_Ask(query, evidence, bn, num_samples)
    print(f"Estimated P(Grade | Difficulty=True, Intelligence=True) = {result}")
    print(f"P(Grade | Difficulty=True, Intelligence=False) = {result}")



