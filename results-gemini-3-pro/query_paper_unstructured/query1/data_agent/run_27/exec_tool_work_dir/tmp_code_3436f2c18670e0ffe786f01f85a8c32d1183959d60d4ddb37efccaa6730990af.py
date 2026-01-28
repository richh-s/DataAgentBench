code = """import json
import re

# Access file paths from local variables
papers_path = locals()['var_function-call-13338059779918874712']
citations_path = locals()['var_function-call-1369991432828738488']

with open(papers_path, 'r') as f:
    papers = json.load(f)

with open(citations_path, 'r') as f:
    citations = json.load(f)

food_papers = []
debug_info = []

for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p.get('text', '')
    
    is_food = False
    
    # 1. Check Title
    if 'food' in title.lower():
        is_food = True
    
    # 2. Check Keywords
    # Find "Keywords" or "Author Keywords"
    # Take text until next double newline or "INTRODUCTION"
    match = re.search(r'(?:Author\s+)?Keywords[:\s](.*?)(?:INTRODUCTION|ABSTRACT|ACM Classification)', text, re.IGNORECASE | re.DOTALL)
    keywords_found = ""
    if match:
        keywords_found = match.group(1).lower()
        if 'food' in keywords_found:
            is_food = True
            
    # 3. Check for specific food-related terms if "food" domain is broader?
    # Hint says: "Common domains include: 'food', 'physical activity'..."
    # So "food" is the term.
    
    if is_food:
        food_papers.append(title)
        
    debug_info.append({
        "title": title,
        "is_food": is_food,
        "keywords_snippet": keywords_found[:100] if keywords_found else "None"
    })

total_citations = 0
for c in citations:
    if c['title'] in food_papers:
        total_citations += int(c['citation_count'])

print("__RESULT__:")
print(json.dumps({
    "food_papers": food_papers,
    "total_citations": total_citations,
    "debug_info": debug_info[:5]
}))"""

env_args = {'var_function-call-4428152146119552339': 'file_storage/function-call-4428152146119552339.json', 'var_function-call-1279721563085973081': 'file_storage/function-call-1279721563085973081.json', 'var_function-call-10463220630905116945': 'file_storage/function-call-10463220630905116945.json', 'var_function-call-6853165914555926720': {'food_papers': [], 'total_citations': 0}, 'var_function-call-4486819615144744261': 'file_storage/function-call-4486819615144744261.json', 'var_function-call-16923378931810091090': 'file_storage/function-call-16923378931810091090.json', 'var_function-call-10009206756418749160': 'file_storage/function-call-10009206756418749160.json', 'var_function-call-8154133366834530525': {'food_papers': [], 'total_citations': 0}, 'var_function-call-13338059779918874712': 'file_storage/function-call-13338059779918874712.json', 'var_function-call-1369991432828738488': 'file_storage/function-call-1369991432828738488.json'}

exec(code, env_args)
