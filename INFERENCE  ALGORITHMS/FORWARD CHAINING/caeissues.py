#here we are goining to implement the forward chainnig method
#inintial facts
facts = set(["engine_wont_start", "battery_dead", "headlights_dim"])

#rules
rules = [
    ({'battery_dead','headlights_dim'}, 'weak_battery'),
    ({'weak_battery', 'engine_wont_start'}, 'car_needs_jumpstart'),
    ({'engine_wont_start', 'fuel_empty'}, 'out_of_fuel'),
    ({'car_needs_jumpstart'}, 'call_roadside_assistance')
    
]

def forward_Chaining(initial_facts, inference_rules):
    kb = set(initial_facts)
    #here we set changed to true to start the loop
    changed = True
    while changed:
        #here change is set to false beacuse will check if any new fct added or not
        #if added then it is true
        #else false and we will exit the loop
        changed = False
        for premise_Set, conclusion in inference_rules:
            if premise_Set.issubset(kb):
                if conclusion not in kb:
                    kb.add(conclusion)
                    changed = True
                    print(f"inferred new fact: {conclusion}"
                          f" from premises: {premise_Set}")
    return kb

#printing the final fact
print(f"final facts: {forward_Chaining(facts, rules)}")


            