code = """import json
import re

# Load papers
with open(locals()['var_function-call-1190130121296070935'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-1190130121296070370'], 'r') as f:
    citations = json.load(f)

food_titles = set()

# Helper to check keywords
def has_food_keyword(text):
    text_lower = text.lower()
    # Find start
    start_match = re.search(r'(author keywords|keywords|index terms)', text_lower)
    if not start_match:
        return False
    
    start_idx = start_match.end()
    
    # Heuristic: Take next 2000 chars 
    chunk = text_lower[start_idx:start_idx+2000]
    
    # Truncate at common next sections
    stop_words = ['introduction', 'acm classification', 'categories and subject descriptors', 'general terms', 'reference']
    min_stop_idx = len(chunk)
    for sw in stop_words:
        idx = chunk.find(sw)
        if idx != -1 and idx < min_stop_idx:
            min_stop_idx = idx
            
    keywords_section = chunk[:min_stop_idx]
    
    return 'food' in keywords_section

for p in papers:
    filename = p.get('filename', '')
    title = filename.replace('.txt', '').strip()
    text = p.get('text', '')
    
    # Check title
    if 'food' in title.lower():
        food_titles.add(title)
        continue
        
    # Check keywords
    if has_food_keyword(text):
        food_titles.add(title)

# Filter citations and sum
total_citations = 0
matched_citations_count = 0
matched_papers = set()

for c in citations:
    c_title = c.get('title', '').strip()
    if c_title in food_titles:
        try:
            count = int(c.get('citation_count', 0))
            total_citations += count
            matched_papers.add(c_title)
            matched_citations_count += 1
        except ValueError:
            pass

print("__RESULT__:")
print(json.dumps({
    "total_citations": total_citations,
    "food_paper_count": len(food_titles),
    "matched_citations_records": matched_citations_count,
    "matched_papers_in_citations": len(matched_papers)
}))"""

env_args = {'var_function-call-14800347907700836141': 'file_storage/function-call-14800347907700836141.json', 'var_function-call-1190130121296070370': 'file_storage/function-call-1190130121296070370.json', 'var_function-call-1190130121296070935': 'file_storage/function-call-1190130121296070935.json'}

exec(code, env_args)
