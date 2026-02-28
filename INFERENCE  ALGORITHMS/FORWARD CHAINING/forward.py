#we are going to implement froward chainnig method in python
#this is one of the inference algorithm

"""overview of the algorithm
1. start with an initial knowledge base and all rules
2. iterate through the rules if they are satisfired by the kb
3. if true then it is a new fact
4. repeat untill no new facts can be added
"""

facts = set(["has_hair","is_mammal", "eats_meat"])

rules = [
    ({"has_hair", "gives_milk"}, "is_mammal"),
    ({"is_mammal", "eats_meat"}, "is_carnivore"),
    ({"has_feathers", "flies"}, "is_bird"),
    ({"is_mammal", "has_hoofs"}, "is_ungulate"),
    ({"is_bird", "swims"}, "is_penguin")

]

def forward_chaining(initial_facts, inference_rules):
    knowledge_base = set(initial_facts)
    changed = True

    #iteratation
    while changed:
        changed = False
        for premise_set, conclusion in inference_rules:
            #if in the kb
            if premise_set.issubset(knowledge_base):
                #if not in kb add it
                if conclusion not in knowledge_base:
                    knowledge_base.add(conclusion)
                    changed = True
                    print(f"inferred new fact: {conclusion} from premises: {premise_set}")
    return knowledge_base

#runnig the forward chaining algorithm
final_facts = forward_chaining(facts, rules)

#test the algorithm 
print("Final facts:", final_facts)

