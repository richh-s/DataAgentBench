code = """import json

with open(locals()['var_function-call-8026237664886157710'], 'r') as f:
    papers = json.load(f)

food_papers = []

for paper in papers:
    text = paper['text'].lower()
    
    start_idx = text.find("author keywords")
    if start_idx != -1:
        # Take substring
        sub = text[start_idx+15:]
        
        # Find nearest end marker
        end_idx = len(sub)
        for marker in ["acm classification", "introduction", "general terms", "abstract"]:
            idx = sub.find(marker)
            if idx != -1 and idx < end_idx:
                end_idx = idx
        
        keywords = sub[:end_idx]
        
        # Check if 'food' is in keywords
        if "food" in keywords:
            food_papers.append(paper['filename'])

print("__RESULT__:")
print(json.dumps(food_papers))"""

env_args = {'var_function-call-16660481108527722743': 'file_storage/function-call-16660481108527722743.json', 'var_function-call-16660481108527725918': ['Citations', 'sqlite_sequence'], 'var_function-call-8026237664886157710': 'file_storage/function-call-8026237664886157710.json', 'var_function-call-6945791491886797443': 'file_storage/function-call-6945791491886797443.json', 'var_function-call-12216116696517767484': {'total_citations': 0, 'food_papers_count': 0, 'food_titles': []}}

exec(code, env_args)
