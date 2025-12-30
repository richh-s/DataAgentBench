code = """import json
import re

with open(locals()['var_function-call-8026237664886157710'], 'r') as f:
    papers = json.load(f)

all_keywords = set()
food_papers = []

for paper in papers:
    text = paper['text']
    lower_text = text.lower()
    
    # Regex to find Author Keywords section
    # Use explicit newline handling if needed, but . matches all with DOTALL
    # We look for "author keywords"
    start_idx = lower_text.find("author keywords")
    if start_idx != -1:
        # Extract a generous chunk
        chunk = lower_text[start_idx+15:start_idx+500] 
        # Find end
        end_idx = 500
        for marker in ["acm classification", "introduction", "general terms", "abstract"]:
            idx = chunk.find(marker)
            if idx != -1 and idx < end_idx:
                end_idx = idx
        
        keywords_str = chunk[:end_idx]
        
        # Split
        kws = keywords_str.replace('\n', ';').replace(',', ';').split(';')
        
        for kw in kws:
            kw = kw.strip()
            if kw:
                all_keywords.add(kw)
                if "food" in kw:
                    food_papers.append(paper['filename'])

print("__RESULT__:")
print(json.dumps({"food_papers_matches": food_papers, "sample_keywords": list(all_keywords)[:20]}))"""

env_args = {'var_function-call-16660481108527722743': 'file_storage/function-call-16660481108527722743.json', 'var_function-call-16660481108527725918': ['Citations', 'sqlite_sequence'], 'var_function-call-8026237664886157710': 'file_storage/function-call-8026237664886157710.json', 'var_function-call-6945791491886797443': 'file_storage/function-call-6945791491886797443.json', 'var_function-call-12216116696517767484': {'total_citations': 0, 'food_papers_count': 0, 'food_titles': []}}

exec(code, env_args)
