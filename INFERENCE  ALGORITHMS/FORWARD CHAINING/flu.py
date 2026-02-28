#now we are going to make a flue or pneumonia detecting ai

#facts
facts = {
    "fever": 0.9,
    "cough": 0.8,
    "body_ache": 0.7,
    "fatigue": 0.6,
    "chest_pain": 0.4,
    "breathlessness": 0.5,
}

rules = [
    {"if": ["fever", "cough"], "then": "flu", "w": 0.9},
    {"if": ["body_ache", "fatigue"], "then": "flu", "w": 0.8},
    {"if": ["cough", "chest_pain"], "then": "pneumonia", "w": 0.85},
    {"if": ["fever", "breathlessness"], "then": "pneumonia", "w": 0.75},
    {"if": ["flu", "breathlessness"], "then": "pneumonia", "w": 0.6},
]

EPSILON = 0.01

def forward_chaining_uncertainity(facts, rules, epsilon= 0.01):
    inferred = dict(facts)
    while True:
        max_change = 0.0

        for rule in rules:
            premises = rule['if']
            conclusion = rule['then']
            weight = rule['w']

            #skipping rule if it is not in the premises yet
            if any(p not in inferred for p in premises):
                continue
            
            rule_conf = min(inferred[p] for p in premises)*weight
            old_conf = inferred.get(conclusion, 0.0)
            new_conf = max(rule_conf, old_conf)

            change = abs(new_conf - old_conf)
            if change>0 :
                inferred[conclusion] = new_conf
                max_change = max(max_change, change)

        if max_change < epsilon:
            break

    return inferred

final_inferences = forward_chaining_uncertainity(facts, rules, EPSILON)
print("Final inferences:")
for fact, conf in sorted(final_inferences.items(), key=lambda x: x[1], reverse=True):
    print("\n target conclusion:")
    print(f"flu      = {final_inferences.get('flu', 0.0):.2f}")
    print(f"pneumonia = {final_inferences.get('pneumonia', 0.0):.2f}")
          



