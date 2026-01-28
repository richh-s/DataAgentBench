code = """import json
import re

with open(locals()['var_function-call-4672195044827894195'], 'r') as f:
    papers = json.load(f)

food_papers = []
debug_info = []

for p in papers:
    text = p.get('text', '')
    title = p.get('filename', '').replace('.txt', '')
    
    # Strategy 1: Title contains food
    if 'food' in title.lower():
        food_papers.append(title)
        debug_info.append(f"Found by title: {title}")
        continue
        
    # Strategy 2: Keywords
    # Look for "Author Keywords" and extract text until next section
    # Regex to find Author Keywords block
    # It might span multiple lines.
    # Usually followed by "ACM Classification" or "INTRODUCTION" or "General Terms"
    match = re.search(r'Author Keywords\s*(.*?)\s*(?:ACM Classification|INTRODUCTION|General Terms)', text, re.IGNORECASE | re.DOTALL)
    if match:
        keywords = match.group(1).lower()
        if 'food' in keywords:
            food_papers.append(title)
            debug_info.append(f"Found by keywords: {title}")
            continue
    
    # Fallback or check if missed
    # If not in title or keywords, but 'food' is frequent in text?
    # Maybe count occurrences?
    # For now, let's stick to Title + Keywords as primary indicators.
    
print("__RESULT__:")
print(json.dumps({"count": len(food_papers), "titles": food_papers}))"""

env_args = {'var_function-call-13370766090165900916': 'file_storage/function-call-13370766090165900916.json', 'var_function-call-9130405135784485262': 'file_storage/function-call-9130405135784485262.json', 'var_function-call-9265765399726123142': 'file_storage/function-call-9265765399726123142.json', 'var_function-call-4672195044827894195': 'file_storage/function-call-4672195044827894195.json', 'var_function-call-6440888066773927974': 876}

exec(code, env_args)
