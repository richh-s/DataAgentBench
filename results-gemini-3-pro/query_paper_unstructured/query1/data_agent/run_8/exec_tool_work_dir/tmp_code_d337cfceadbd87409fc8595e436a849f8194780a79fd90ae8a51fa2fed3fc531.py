code = """import json

# Load papers
with open(locals()['var_function-call-1518864463960469704'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-16808733530214175810'], 'r') as f:
    citations = json.load(f)

food_papers = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # 1. Check Title
    if 'food' in title.lower():
        food_papers.append(title)
        continue

    # 2. Check Keywords
    # Find "Author Keywords" or "Keywords"
    text_lower = text.lower()
    start_idx = -1
    
    # Try different headers for keywords
    for header in ["author keywords", "index terms", "keywords"]:
        idx = text_lower.find(header)
        if idx != -1:
            start_idx = idx + len(header)
            break
    
    if start_idx != -1:
        # Extract a chunk of text after the header
        # We look for the start of the next section, which usually looks like "INTRODUCTION" or "ACM CLASSIFICATION"
        # or just take the next few lines.
        snippet = text_lower[start_idx:start_idx+1000]
        
        # Heuristic to stop: find next major header or double newline sequence that looks like a break
        # Common headers in these papers
        stop_markers = ["introduction", "acm classification", "general terms", "abstract"] 
        # Note: Abstract usually comes before keywords, but sometimes after.
        
        min_stop = len(snippet)
        for marker in stop_markers:
            s_idx = snippet.find(marker)
            if s_idx != -1 and s_idx < min_stop:
                min_stop = s_idx
        
        keywords_content = snippet[:min_stop]
        
        if 'food' in keywords_content:
            food_papers.append(title)

# Deduplicate in case logic adds same paper twice (though 'continue' handles it)
food_papers_set = set(food_papers)

# Calculate total citations
total_citations = 0
found_titles = set()

for c in citations:
    c_title = c.get('title')
    count = c.get('citation_count')
    if c_title in food_papers_set:
        total_citations += int(count)
        found_titles.add(c_title)

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "paper_count": len(food_papers_set), "matched_titles": list(found_titles)}))"""

env_args = {'var_function-call-13263841084100216715': ['paper_docs'], 'var_function-call-2979229897755399322': 'file_storage/function-call-2979229897755399322.json', 'var_function-call-1518864463960469704': 'file_storage/function-call-1518864463960469704.json', 'var_function-call-16808733530214175810': 'file_storage/function-call-16808733530214175810.json'}

exec(code, env_args)
