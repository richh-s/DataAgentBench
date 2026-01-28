code = """import json, re, os

# Load full Mongo results
path_docs = var_call_tysKXaN4r0cwUJRLZGNCj91J
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Load full citations results
path_cit = var_call_vILwXyPwHNW0s5fY341CV2pk
with open(path_cit, 'r') as f:
    cits = json.load(f)

# Identify paper titles in the 'food' domain by simple heuristic:
# assume domain info is mentioned in text like 'Domain: food' or similar, or use keyword 'food' in a domain/context list.
food_titles = set()
for d in docs:
    filename = d.get('filename','')
    title = re.sub(r"\.txt$", "", filename)
    text = d.get('text','').lower()
    # Heuristic: treat as food domain if ' food ' appears or 'diet' or 'nutrition'
    if ' food ' in text or 'diet ' in text or ' nutrition' in text:
        food_titles.add(title)

# Sum citation counts for those titles
total_citations = 0
for row in cits:
    title = row.get('title','')
    if title in food_titles:
        try:
            total_citations += int(row.get('citation_count',0))
        except ValueError:
            pass

result = {"total_food_domain_citations": total_citations, "food_titles": sorted(list(food_titles))}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_tysKXaN4r0cwUJRLZGNCj91J': 'file_storage/call_tysKXaN4r0cwUJRLZGNCj91J.json', 'var_call_vILwXyPwHNW0s5fY341CV2pk': 'file_storage/call_vILwXyPwHNW0s5fY341CV2pk.json'}

exec(code, env_args)
