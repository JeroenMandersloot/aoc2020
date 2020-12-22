def parse_line(line: str):
    ingredients, allergens = line.strip().split('(contains ')
    ingredients = ingredients.strip().split(' ')
    allergens = allergens.strip(')').split(', ')
    return (ingredients, allergens)
    

with open('input.txt', 'r') as f:
    inp = list(map(parse_line, f.readlines()))


candidates = dict()
all_allergens = set(a for _, b in inp for a in b)
for allergen in all_allergens:
    cs = None
    for ingredients, allergens in inp:
        if allergen in allergens:
            if cs is None:
                cs = set(ingredients)
            else:
                cs = cs.intersection(set(ingredients))
    candidates[allergen] = cs

locked = dict()
while candidates:
    for allergen, ingredients in candidates.items():
        if len(ingredients) == 1:
            ingredient = ingredients.pop()
            locked[allergen] = ingredient
            candidates.pop(allergen)
            for allergen, ingredients in candidates.items():
                if ingredient in ingredients:
                    ingredients.remove(ingredient)
            break
     

all_ingredients = set(i for b, _ in inp for i in b)
ingredients_without_allergens = all_ingredients.difference(set(locked.values()))
counts = dict()
for ingredient in ingredients_without_allergens:
    counts[ingredient] = 0
    for ing, _ in inp:
        if ingredient in ing:
            counts[ingredient] += 1

print(sum(counts.values()))
