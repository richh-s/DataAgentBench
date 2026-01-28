code = """import json
import re

with open('var_function-call-4486819615144744261.json', 'r') as f:
    papers = json.load(f)

with open('var_function-call-10463220630905116945.json', 'r') as f:
    citations = json.load(f)

strong_food_papers = []
weak_food_papers = []

for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p.get('text', '')
    
    # 1. Check Title
    if 'food' in title.lower():
        strong_food_papers.append(title)
        continue

    # 2. Check Keywords
    # Regex using \s instead of \n
    match = re.search(r'(?:Author\s+)?Keywords[:\s](.*?)(?:INTRODUCTION|ABSTRACT|ACM Classification|General Terms)', text, re.DOTALL | re.IGNORECASE)
    if match:
        kws = match.group(1).lower()
        if 'food' in kws:
            strong_food_papers.append(title)
            continue
    
    # 3. Check Text Frequency
    # Simple count
    count = text.lower().count('food')
    if count > 0:
        weak_food_papers.append({"title": title, "count": count})

# Calculate citations
strong_citations = 0
for c in citations:
    if c['title'] in strong_food_papers:
        strong_citations += int(c['citation_count'])

weak_citations = 0
for c in citations:
    if any(wp['title'] == c['title'] for wp in weak_food_papers):
        weak_citations += int(c['citation_count'])

print("__RESULT__:")
print(json.dumps({
    "strong_matches": strong_food_papers,
    "strong_citations": strong_citations,
    "weak_matches": weak_food_papers,
    "weak_citations": weak_citations
}))"""

env_args = {'var_function-call-4428152146119552339': 'file_storage/function-call-4428152146119552339.json', 'var_function-call-1279721563085973081': 'file_storage/function-call-1279721563085973081.json', 'var_function-call-10463220630905116945': 'file_storage/function-call-10463220630905116945.json', 'var_function-call-6853165914555926720': {'food_papers': [], 'total_citations': 0}, 'var_function-call-4486819615144744261': 'file_storage/function-call-4486819615144744261.json'}

exec(code, env_args)
