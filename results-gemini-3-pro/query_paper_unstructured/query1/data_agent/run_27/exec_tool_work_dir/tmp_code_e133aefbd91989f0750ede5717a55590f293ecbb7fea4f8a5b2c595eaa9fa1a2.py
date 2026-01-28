code = """import json
import re

# Load papers
try:
    with open('var_function-call-16923378931810091090.json', 'r') as f:
        papers = json.load(f)
except:
    papers = []

# Load citations
try:
    with open('var_function-call-10009206756418749160.json', 'r') as f:
        citations = json.load(f)
except:
    citations = []

food_papers = []

for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p.get('text', '')
    
    # Check Keywords
    # Regex: Keywords followed by content.
    # We avoid using \n literal.
    # match anything after "Keywords:" or "Keywords "
    match = re.search(r'(?:Author\s+)?Keywords[:\s](.{0,500})', text, re.IGNORECASE | re.DOTALL)
    
    is_food = False
    
    if match:
        raw = match.group(1)
        # Check for stop words
        # "INTRODUCTION", "ABSTRACT", "ACM Classification"
        stop_words = ["INTRODUCTION", "ABSTRACT", "ACM CLASSIFICATION"]
        
        # Upper case for checking
        raw_upper = raw.upper()
        
        end_pos = len(raw)
        for w in stop_words:
            idx = raw_upper.find(w)
            if idx != -1 and idx < end_pos:
                end_pos = idx
        
        keywords = raw[:end_pos].lower()
        
        if 'food' in keywords:
            is_food = True
            
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

env_args = {'var_function-call-4428152146119552339': 'file_storage/function-call-4428152146119552339.json', 'var_function-call-1279721563085973081': 'file_storage/function-call-1279721563085973081.json', 'var_function-call-10463220630905116945': 'file_storage/function-call-10463220630905116945.json', 'var_function-call-6853165914555926720': {'food_papers': [], 'total_citations': 0}, 'var_function-call-4486819615144744261': 'file_storage/function-call-4486819615144744261.json', 'var_function-call-16923378931810091090': 'file_storage/function-call-16923378931810091090.json', 'var_function-call-10009206756418749160': 'file_storage/function-call-10009206756418749160.json'}

exec(code, env_args)
