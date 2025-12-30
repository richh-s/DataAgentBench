code = """import json

# Load data
with open('var_function-call-4153567193002089374.json', 'r') as f:
    papers = json.load(f)
with open('var_function-call-9689341387854822982.json', 'r') as f:
    citations = json.load(f)

food_papers = []

for p in papers:
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    text = p.get('text', '')
    
    is_food = False
    
    # Check title
    if 'food' in title.lower():
        is_food = True
    
    # Check Keywords
    # Find "Author Keywords"
    idx = text.lower().find("author keywords")
    if idx != -1:
        # Start reading after "Author Keywords"
        start_idx = idx + len("Author Keywords")
        # Find end: "ACM Classification" or "\n\n"
        subtext = text[start_idx:]
        end_idx_1 = subtext.lower().find("acm classification")
        if end_idx_1 == -1:
            end_idx_1 = len(subtext)
            
        # Also look for double newline, but be careful (maybe just 500 chars limit)
        # keywords usually are short
        end_idx = end_idx_1
        
        keywords = subtext[:end_idx].lower()
        if 'food' in keywords:
            is_food = True
            
    if is_food:
        food_papers.append(title)

# Filter citations
total_citations = 0
matched_citation_titles = set()

for c in citations:
    c_title = c.get('title', '').strip()
    try:
        c_count = int(c.get('citation_count', 0))
    except:
        c_count = 0
    
    # Check exact match
    if c_title in food_papers:
        total_citations += c_count
        matched_citation_titles.add(c_title)

print("__RESULT__:")
print(json.dumps({"food_papers": food_papers, "total_citations": total_citations, "matched_count": len(matched_citation_titles)}))"""

env_args = {'var_function-call-12415105760214265050': 'file_storage/function-call-12415105760214265050.json', 'var_function-call-4971801496876042457': 'file_storage/function-call-4971801496876042457.json', 'var_function-call-9689341387854822982': 'file_storage/function-call-9689341387854822982.json', 'var_function-call-4153567193002089374': 'file_storage/function-call-4153567193002089374.json'}

exec(code, env_args)
