code = """import json

citations_path = locals()['var_function-call-99245770254800995']
papers_path = locals()['var_function-call-5874155478376628757']

with open(citations_path, 'r') as f:
    citations = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

food_papers = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Simple extraction
    start_idx = text.find('Author Keywords')
    if start_idx == -1:
        start_idx = text.find('Index Terms')
    
    if start_idx != -1:
        # found keywords section
        # Look for end of section
        # commonly ends with 'ACM Classification' or 'INTRODUCTION'
        end_idx = text.find('ACM Classification', start_idx)
        if end_idx == -1:
            end_idx = text.find('INTRODUCTION', start_idx)
        if end_idx == -1:
            end_idx = start_idx + 500 # fallback
            
        keywords_text = text[start_idx:end_idx].lower()
        
        if 'food' in keywords_text:
            food_papers.append(title)
    else:
        # No keywords found, maybe check abstract or full text if domain is very prominent?
        # But instructions say "Fields like domain...". Implies it's a specific field.
        # Let's assume papers have keywords.
        pass

total_citations = 0
for cit in citations:
    if cit['title'] in food_papers:
        c = cit['citation_count']
        if isinstance(c, str):
            c = int(c) if c.strip() else 0
        total_citations += c

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "food_papers": food_papers}))"""

env_args = {'var_function-call-853909438841445340': 'file_storage/function-call-853909438841445340.json', 'var_function-call-1978902813264061650': 'file_storage/function-call-1978902813264061650.json', 'var_function-call-99245770254800995': 'file_storage/function-call-99245770254800995.json', 'var_function-call-5874155478376628757': 'file_storage/function-call-5874155478376628757.json'}

exec(code, env_args)
