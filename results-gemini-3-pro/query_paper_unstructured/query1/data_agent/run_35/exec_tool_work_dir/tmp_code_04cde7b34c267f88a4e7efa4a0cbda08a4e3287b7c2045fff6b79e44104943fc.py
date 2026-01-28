code = """import json

# Get file paths
citations_path = locals()['var_function-call-14555610858560358239']
papers_path = locals()['var_function-call-11640274332636556525']

with open(citations_path, 'r') as f:
    citations = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

food_papers = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Simple extraction without complex regex
    text_lower = text.lower()
    
    # Try to find keywords section
    keywords_start = text_lower.find('author keywords')
    if keywords_start == -1:
        keywords_start = text_lower.find('keywords')
    
    extracted_keywords = ""
    if keywords_start != -1:
        # Start searching after the label
        start_idx = keywords_start + 15 # approx len of "author keywords"
        # Find next double newline or "acm classification" or "introduction"
        # We'll just take the next 500 chars and split by newlines
        chunk = text_lower[start_idx:start_idx+500]
        # Usually keywords are until the next section which starts with a capitalized header or blank lines
        # Let's split by double newline
        parts = chunk.split('\n\n')
        extracted_keywords = parts[0]
        
    # Check if 'food' is in keywords or title
    is_food = False
    
    # Check title
    if 'food' in title.lower():
        is_food = True
    
    # Check keywords
    if not is_food and 'food' in extracted_keywords:
        is_food = True
        
    if is_food:
        food_papers.append(title)

total_citations = 0
for c in citations:
    if c.get('title') in food_papers:
        try:
            total_citations += int(c.get('citation_count', 0))
        except:
            pass

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-13801611410000855703': 'file_storage/function-call-13801611410000855703.json', 'var_function-call-13801611410000858480': ['Citations', 'sqlite_sequence'], 'var_function-call-14555610858560358239': 'file_storage/function-call-14555610858560358239.json', 'var_function-call-11640274332636556525': 'file_storage/function-call-11640274332636556525.json'}

exec(code, env_args)
