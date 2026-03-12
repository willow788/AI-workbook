#implementing exact inference for bayesian networks using enumeration


class BayesNode:
    def __init__(self, var, parents, cpt):
        self.var = var
        self.parents = parents
        self.cpt = cpt

    def p(self, value, event):
        if not self.parents:
            return self.cpt[value] # No parents, so CPT is just a simple probability distribution.
        
        # Get the values of the parent variables from the event to index into the CPT.
        parent_values = tuple(event[p] for p in self.parents)
        # Accept both tuple keys (True,) and scalar keys True for single-parent CPTs.
        if parent_values in self.cpt:
            return self.cpt[parent_values][value]
        if len(parent_values) == 1 and parent_values[0] in self.cpt:
            return self.cpt[parent_values[0]][value]
        raise KeyError(f"Missing CPT entry for parents {self.parents}={parent_values}")
    

#contanier:
class BayesNet:
    def __init__(self):
        self.nodes = {}
        self.variables = []

    def add_node(self, node):
        self.nodes[node.var] = node
        self.variables.append(node.var)

    def get_node(self, var):
        return self.nodes.get(var)
            

#enumeration query:

def enumeration_Ask(X, evidence, bn):
    Q = {}
    for xi in [True, False]:
        extended_evidence = dict(evidence)
        extended_evidence[X] = xi

        Q[xi] = enumerate_all(bn.variables, extended_evidence, bn)

    return normalize(Q)


def enumerate_all(variables, evidence, bn):
     if not variables:
        return 1.0
     
     Y = variables[0]
     node = bn.get_node(Y) #first variable in the list
     rest = variables[1:]

     if Y in evidence:
         return node.p(evidence[Y], evidence) * enumerate_all(rest, evidence, bn)
     else:
            total = 0
            for yi in [True, False]:
                extended_evidence = dict(evidence)
                extended_evidence[Y] = yi
    
                total += node.p(yi, evidence) * enumerate_all(rest, extended_evidence, bn)
    
            return total
     

def normalize(Q):
    total = sum(Q.values())
    return {k: v / total for k, v in Q.items()}

#burglary network example:
bn = BayesNet()
bn.add_node(BayesNode('Burglary', 
                      [], 
                      {True: 0.001, False: 0.999
                       }))
bn.add_node(BayesNode('Earthquake', 
                      [],
                        {True: 0.002, False: 0.998
                         }))
bn.add_node(BayesNode('Alarm', 
                      ['Burglary', 'Earthquake'],
                        {(True, True): {True: 0.95, False: 0.05},
                         (True, False): {True: 0.94, False: 0.06},
                         (False, True): {True: 0.29, False: 0.71},
                         (False, False): {True: 0.001, False: 0.999}
                         }))
bn.add_node(BayesNode('JohnCalls',
                        ['Alarm'],
                            {True: {True: 0.90, False: 0.10},
                             False: {True: 0.05, False: 0.95}
                             }))
bn.add_node(BayesNode('MaryCalls',
                        ['Alarm'],
                            {True: {True: 0.70, False: 0.30},
                             False: {True: 0.01, False: 0.99}
                             }))





#querying
print("probability that there was a burglary given that the alarm went off: ")
result = enumeration_Ask('Burglary',
                         {'Alarm': True, 'JohnCalls': True, 'MaryCalls': True},
                         
                         bn)
for k, v in result.items():
    print(f"{k}: {v * 100:.2f}%")




    
