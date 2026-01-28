code = """import json
import re

# Load papers
with open(locals()['var_function-call-15588531730774958369'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-359120652311004600'], 'r') as f:
    citations = json.load(f)

# Build citation map: title -> total_count
citation_map = {}
for c in citations:
    t = c['title'].strip().lower()
    count = int(c['citation_count'])
    citation_map[t] = citation_map.get(t, 0) + count

food_papers = []
total_food_citations = 0

for p in papers:
    text = p['text']
    filename = p['filename']
    title = filename.replace('.txt', '').strip()
    title_lower = title.lower()
    
    # Check title
    if 'food' in title_lower:
        food_papers.append(title)
        total_food_citations += citation_map.get(title_lower, 0)
        continue

    # Extract Author Keywords
    # Heuristic: Look for "Author Keywords" and take next 500 chars or until "ACM" or "Introduction"
    keywords_match = re.search(r'Author Keywords(.*?)(?:ACM Classification|INTRODUCTION|General Terms)', text, re.IGNORECASE | re.DOTALL)
    if keywords_match:
        keywords = keywords_match.group(1).lower()
        if 'food' in keywords:
            food_papers.append(title)
            total_food_citations += citation_map.get(title_lower, 0)
            continue
            
    # Fallback: Check Abstract?
    # Heuristic: Abstract is usually early in the text.
    # abstract_match = re.search(r'ABSTRACT(.*?)(?:Author Keywords|INTRODUCTION)', text, re.IGNORECASE | re.DOTALL)
    # if abstract_match:
    #     abstract = abstract_match.group(1).lower()
    #     if 'food' in abstract:
    #         # Food in abstract might be common.
    #         pass

print("__RESULT__:")
print(json.dumps({"food_papers": food_papers, "total_citations": total_food_citations}))"""

env_args = {'var_function-call-11112741078827704414': 'file_storage/function-call-11112741078827704414.json', 'var_function-call-15588531730774958369': 'file_storage/function-call-15588531730774958369.json', 'var_function-call-359120652311004600': 'file_storage/function-call-359120652311004600.json'}

exec(code, env_args)
