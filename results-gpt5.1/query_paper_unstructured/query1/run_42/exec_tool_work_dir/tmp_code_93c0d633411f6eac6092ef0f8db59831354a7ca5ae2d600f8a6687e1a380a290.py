code = """import json, re, pandas as pd

# Load full Mongo results
path_docs = var_call_TX37OpZfoDDNlMXAkS1V1Dwi
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Heuristic: treat papers as 'food' domain if their text mentions key food-tracking terms
food_keywords = [r'food tracking', r'food journal', r'food journaling', r'calorie tracking', r'dietary self-tracking', r'dietary self tracking', r'nutrition tracking', r'dietary self-monitoring', r'dietary self monitoring', r'nutrition app', r'healthy eating', r'dietary tracking']

food_titles = []
for d in docs:
    text = d.get('text','').lower()
    if any(re.search(k, text) for k in food_keywords):
        filename = d.get('filename','')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        food_titles.append(title)

# Deduplicate
food_titles = sorted(set(food_titles))

# Load citation aggregates
path_cit = var_call_CKCwH99eNxuJAHaTvbf3gz3L
with open(path_cit, 'r') as f:
    cit = json.load(f)

# Sum citations for titles that are in food_titles (case-sensitive match as in description)
food_set = set(food_titles)

total_citations_food = 0
for row in cit:
    title = row['title']
    if title in food_set:
        total_citations_food += int(row['total_citations'])

result = {
  'food_titles': food_titles,
  'total_citations_food': total_citations_food
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_TX37OpZfoDDNlMXAkS1V1Dwi': 'file_storage/call_TX37OpZfoDDNlMXAkS1V1Dwi.json', 'var_call_CKCwH99eNxuJAHaTvbf3gz3L': 'file_storage/call_CKCwH99eNxuJAHaTvbf3gz3L.json'}

exec(code, env_args)
