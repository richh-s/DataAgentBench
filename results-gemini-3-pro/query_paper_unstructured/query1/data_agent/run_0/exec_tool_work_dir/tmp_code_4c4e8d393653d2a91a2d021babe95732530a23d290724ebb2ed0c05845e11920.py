code = """import json

# Load data
# Use locals() to access the file paths stored in variables
path_papers = locals()['var_function-call-4153567193002089374']
path_citations = locals()['var_function-call-9689341387854822982']

with open(path_papers, 'r') as f:
    papers = json.load(f)
with open(path_citations, 'r') as f:
    citations = json.load(f)

food_papers = []

for p in papers:
    filename = p.get('filename', '')
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
        snippet = text_lower[idx:idx+1000] # Take enough text
        # Truncate at next section headers
        end1 = snippet.find('acm classification')
        if end1 == -1: end1 = 1000
        end2 = snippet.find('introduction') 
        if end2 == -1: end2 = 1000
        
        end = min(end1, end2)
        keywords_block = snippet[:end]
        
        if 'food' in keywords_block:
            is_food = True
            
    if is_food:
        food_papers.append(title)

# Filter citations
total = 0
for c in citations:
    ct = c.get('title', '').strip()
    if ct in food_papers:
        try:
            total += int(c.get('citation_count', 0))
        except:
            pass

print('__RESULT__:')
print(json.dumps({'total_citations': total, 'titles': food_papers}))"""

env_args = {'var_function-call-12415105760214265050': 'file_storage/function-call-12415105760214265050.json', 'var_function-call-4971801496876042457': 'file_storage/function-call-4971801496876042457.json', 'var_function-call-9689341387854822982': 'file_storage/function-call-9689341387854822982.json', 'var_function-call-4153567193002089374': 'file_storage/function-call-4153567193002089374.json'}

exec(code, env_args)
