code = """import json

# Load data
with open(locals()['var_function-call-17235522576117083875'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-17235522576117081446'], 'r') as f:
    citations = json.load(f)

food_titles = set()

for p in papers:
    title = p.get('filename', '').replace('.txt', '')
    text = p.get('text', '')
    text_lower = text.lower()
    
    # Check title
    if 'food' in title.lower():
        food_titles.add(title)
        continue
        
    # Check Author Keywords
    # The block usually follows "Author Keywords"
    # and ends before "ACM Classification Keywords" or "INTRODUCTION" or another section.
    # We can take a slice.
    
    kwd_start = text_lower.find('author keywords')
    if kwd_start != -1:
        # Look for the next likely section header to end the block
        # Common headers in ACM papers: "ACM Classification Keywords", "INTRODUCTION", "General Terms"
        
        candidates = []
        for marker in ['acm classification', 'introduction', 'general terms', 'abstract']:
            idx = text_lower.find(marker, kwd_start + 15) # +15 to skip "author keywords" itself
            if idx != -1:
                candidates.append(idx)
        
        if candidates:
            kwd_end = min(candidates)
        else:
            kwd_end = kwd_start + 500 # fallback
            
        keywords_block = text_lower[kwd_start:kwd_end]
        
        # Check if 'food' is in this block
        if 'food' in keywords_block:
            food_titles.add(title)

# Filter citations
total_citations = 0
matched_citations_count = 0
for c in citations:
    if c['title'] in food_titles:
        try:
            total_citations += int(c['citation_count'])
            matched_citations_count += 1
        except ValueError:
            pass

print("__RESULT__:")
print(json.dumps({
    "food_paper_count": len(food_titles),
    "total_citations": total_citations,
    "matched_citation_records": matched_citations_count,
    "sample_food_titles": list(food_titles)[:5]
}))"""

env_args = {'var_function-call-5786904885440834537': 'file_storage/function-call-5786904885440834537.json', 'var_function-call-5786904885440834028': ['Citations', 'sqlite_sequence'], 'var_function-call-17235522576117083875': 'file_storage/function-call-17235522576117083875.json', 'var_function-call-17235522576117081446': 'file_storage/function-call-17235522576117081446.json'}

exec(code, env_args)
