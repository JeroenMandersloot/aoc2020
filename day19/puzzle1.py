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
    

VALID = resolve_rule(0)
print(len([message for message in messages if message in VALID]))
    