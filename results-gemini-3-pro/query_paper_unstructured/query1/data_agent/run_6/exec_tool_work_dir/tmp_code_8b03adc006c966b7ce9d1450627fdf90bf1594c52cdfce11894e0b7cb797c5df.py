code = """import json
import re

with open(locals()['var_function-call-8026237664886157710'], 'r') as f:
    papers = json.load(f)

all_keywords = set()
food_papers = []

for paper in papers:
    text = paper['text']
    # Normalize text
    lower_text = text.lower()
    
    # regex for Author Keywords
    # It seems to be "Author Keywords" followed by some text until "ACM Classification" or "Introduction"
    # Let's try to capture a chunk
    match = re.search(r'author keywords\s*(.*?)\s*(?:acm classification|introduction|general terms|abstract)', lower_text, re.DOTALL)
    
    if match:
        keywords_block = match.group(1)
        # Split by ; or , or \n
        kws = re.split(r'[;,\n]', keywords_block)
        for kw in kws:
            kw = kw.strip()
            if kw:
                all_keywords.add(kw)
                if "food" in kw:
                    food_papers.append(paper['filename'])

print("__RESULT__:")
print(json.dumps({"food_papers_matches": food_papers, "sample_keywords": list(all_keywords)[:50]}))"""

env_args = {'var_function-call-16660481108527722743': 'file_storage/function-call-16660481108527722743.json', 'var_function-call-16660481108527725918': ['Citations', 'sqlite_sequence'], 'var_function-call-8026237664886157710': 'file_storage/function-call-8026237664886157710.json', 'var_function-call-6945791491886797443': 'file_storage/function-call-6945791491886797443.json', 'var_function-call-12216116696517767484': {'total_citations': 0, 'food_papers_count': 0, 'food_titles': []}}

exec(code, env_args)
