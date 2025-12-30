code = """import json

# Load data
with open('var_function-call-4153567193002089374.json', 'r') as f:
    papers = json.load(f)
with open('var_function-call-9689341387854822982.json', 'r') as f:
    citations = json.load(f)

food_papers = []

for p in papers:
    filename = p.get('filename', '')
    # Strip .txt extension
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
        
    text = p.get('text', '')
    
    is_food = False
    
    # Check title
    if 'food' in title.lower():
        is_food = True
    
    # Check Keywords
    text_lower = text.lower()
    idx = text_lower.find('author keywords')
    if idx != -1:
        # Check next 500 chars for 'food'
        # This is a heuristic. 
        # Usually keywords are close to the header.
        # We stop at 'acm classification' or 'introduction' or double newline.
        snippet = text_lower[idx:idx+500]
        # Check if 'food' is in snippet
        # But we must ensure it's in the keywords section.
        # Let's just assume if 'food' is near 'author keywords', it counts.
        # But wait, 'food' could be in 'acm classification' if that's included in snippet.
        # So we should truncate at 'acm classification'.
        end = snippet.find('acm classification')
        if end != -1:
            snippet = snippet[:end]
            
        if 'food' in snippet:
            is_food = True
            
    if is_food:
        food_papers.append(title)

# Filter citations
total = 0
for c in citations:
    ct = c.get('title', '').strip()
    # Handle possible casing mismatch? 
    # The prompt says they match, but let's be safe.
    # Actually, if I change case, I might mismatch.
    # Let's assume exact match first.
    if ct in food_papers:
        try:
            total += int(c.get('citation_count', 0))
        except:
            pass

print('__RESULT__:')
print(json.dumps({'total_citations': total, 'titles': food_papers}))"""

env_args = {'var_function-call-12415105760214265050': 'file_storage/function-call-12415105760214265050.json', 'var_function-call-4971801496876042457': 'file_storage/function-call-4971801496876042457.json', 'var_function-call-9689341387854822982': 'file_storage/function-call-9689341387854822982.json', 'var_function-call-4153567193002089374': 'file_storage/function-call-4153567193002089374.json'}

exec(code, env_args)
