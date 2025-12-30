code = """import json
import re

with open(locals()['var_function-call-15588531730774958369'], 'r') as f:
    papers = json.load(f)

matches = []
for p in papers:
    text = p['text'].lower()
    if 'food' in text:
        count = text.count('food')
        # Snippet
        idx = text.find('food')
        snippet = text[max(0, idx-50):min(len(text), idx+50)].replace('\n', ' ')
        
        # Keywords check
        kw = "Not Found"
        m = re.search(r'author keywords(.*?)(?:acm classification|introduction)', text, re.DOTALL)
        if m:
            kw = m.group(1).strip()[:100] # First 100 chars of keywords
        
        matches.append({
            "filename": p['filename'],
            "count": count,
            "snippet": snippet,
            "keywords_found": kw
        })

print("__RESULT__:")
print(json.dumps(matches[:10])) # Print first 10 matches"""

env_args = {'var_function-call-11112741078827704414': 'file_storage/function-call-11112741078827704414.json', 'var_function-call-15588531730774958369': 'file_storage/function-call-15588531730774958369.json', 'var_function-call-359120652311004600': 'file_storage/function-call-359120652311004600.json', 'var_function-call-240713878677989138': {'food_papers': [], 'total_citations': 0}}

exec(code, env_args)
