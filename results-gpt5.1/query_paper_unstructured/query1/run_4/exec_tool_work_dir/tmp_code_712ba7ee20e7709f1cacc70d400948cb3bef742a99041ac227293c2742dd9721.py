code = """import json, re, os

# Load full mongo results
path_docs = var_call_2dVasd8DRDTEfC5MszOd2QQE
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Identify food-domain papers via simple heuristics in text (domain labels are not explicit, so use keyword 'food').
# We'll assume papers substantially about food will mention 'food' or 'diet' multiple times.
food_titles = set()
for d in docs:
    text = d.get('text','').lower()
    # Count occurrences
    food_count = text.count(' food') + text.count('food ') + text.count('food,') + text.count('food.')
    diet_count = text.count(' diet') + text.count('diet ')
    if food_count + diet_count >= 5:  # heuristic threshold
        filename = d.get('filename','')
        title = re.sub(r"\.txt$","", filename)
        if title:
            food_titles.add(title)

# Load citations
path_cits = var_call_jUOUclpU5fw75PFSdAxUYgBI
with open(path_cits, 'r') as f:
    cits = json.load(f)

# Sum citation_count for titles in food_titles
total_citations = 0
for row in cits:
    title = row.get('title')
    if title in food_titles:
        try:
            total_citations += int(row.get('citation_count',0))
        except ValueError:
            pass

result = {"total_citation_count_food_domain": total_citations, "food_titles": sorted(list(food_titles))}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_2dVasd8DRDTEfC5MszOd2QQE': 'file_storage/call_2dVasd8DRDTEfC5MszOd2QQE.json', 'var_call_jUOUclpU5fw75PFSdAxUYgBI': 'file_storage/call_jUOUclpU5fw75PFSdAxUYgBI.json'}

exec(code, env_args)
