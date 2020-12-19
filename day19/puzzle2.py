from typing import Tuple, Union, List, Set
import sys
from itertools import product

def parse_raw_rule(rule: str) -> Tuple[int, Union[str, List[List[int]]]]:
    num, d = map(lambda s: s.strip(), rule.split(':'))
    num = int(num)
    if '"' in d:
        d = d[1]
    else:
        d = list(map(lambda a: list(map(int, a.strip().split(' '))), d.split('|')))
    return num, d


with open('input.txt', 'r') as f:
    rules, messages = map(lambda p: p.split("\n"), f.read().split("\n\n"))
    RAW_RULES = dict(map(parse_raw_rule, rules))
    RESOLVED_RULES = {num: set([d]) for num, d in RAW_RULES.items() if isinstance(d, str)}
    

def resolve_rule(num) -> Set[str]:
    if num not in RESOLVED_RULES:
        RESOLVED_RULES[num] = set("".join(c) for rule in RAW_RULES[num] for c in product(*map(resolve_rule, rule)))
    return RESOLVED_RULES[num]
    

rule_42 = resolve_rule(42)
rule_31 = resolve_rule(31)

assert len(set(map(len, rule_42))) == 1
assert len(set(map(len, rule_31))) == 1

step_42 = next(map(len, rule_42))
step_31 = next(map(len, rule_31))

def is_valid(message):
    i = 0
    while sub_message := message[i*step_42:(i+1)*step_42]:
        if sub_message not in rule_42:
            break
        i += 1
        
    j = i 
    while sub_message := message[j*step_31:(j+1)*step_31]:
        if sub_message not in rule_31:
            return False
        j += 1
        
    # We need at least one sub message to match rule 31
    if i == j:
        return False
    
    # We can have any number of matches to rule 42, as long as there are at most 1 fewer rule 31 matches.
    if i > j - i:
        return True
    
    return False


print(sum(map(is_valid, messages)))
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        