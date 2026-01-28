code = """import json
import re

# Load papers
try:
    with open('var_function-call-1279721563085973081.json', 'r') as f:
        papers = json.load(f)
except:
    papers = []

# Load citations
try:
    with open('var_function-call-10463220630905116945.json', 'r') as f:
        citations = json.load(f)
except:
    citations = []

food_papers = []

for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p.get('text', '')
    
    # regex for keywords
    # Matches "Keywords" followed by content until "Introduction" or "ACM Classification"
    match = re.search(r'(?:Author\s+)?Keywords[:\s]*(.*?)(?:INTRODUCTION|ACM Classification)', text, re.DOTALL | re.IGNORECASE)
    
    is_food = False
    if match:
        kws = match.group(1).lower()
        if 'food' in kws:
            is_food = True
    
    # Check title as well
    if 'food' in title.lower():
        is_food = True
        
    if is_food:
        food_papers.append(title)

total_citations = 0
for c in citations:
    if c['title'] in food_papers:
        total_citations += int(c['citation_count'])

print("__RESULT__:")
print(json.dumps({"food_papers": food_papers, "total_citations": total_citations}))"""

env_args = {'var_function-call-4428152146119552339': 'file_storage/function-call-4428152146119552339.json', 'var_function-call-1279721563085973081': 'file_storage/function-call-1279721563085973081.json', 'var_function-call-10463220630905116945': 'file_storage/function-call-10463220630905116945.json'}

exec(code, env_args)
