code = """import json

# Load the result from the previous tool call
# The variable name is var_function-call-8395827407536305276
with open(locals()['var_function-call-8395827407536305276'], 'r') as f:
    papers = json.load(f)

food_papers = []
debug_info = []

for p in papers:
    text = p.get('text', '').lower()
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check Title
    if 'food' in title.lower():
        food_papers.append(title)
        debug_info.append(f"Found in TITLE: {title}")
        continue
        
    # Check Keywords (heuristic)
    # Look for "keywords" and check the next few lines
    lines = text.split('\n')
    found_in_keywords = False
    for i, line in enumerate(lines):
        if 'keywords' in line:
            # Check this line and next 3 lines
            context = ' '.join(lines[i:i+4])
            if 'food' in context:
                food_papers.append(title)
                debug_info.append(f"Found in KEYWORDS: {title}")
                found_in_keywords = True
                break
    
    if found_in_keywords:
        continue
        
    # Fallback: Check Abstract? 
    # The prompt says "Common domains include... food".
    # If it's not in keywords or title, maybe it's in the abstract.
    # But as we saw, abstract can mention other domains.
    # Let's start with Title + Keywords and see how many we get.

print("__RESULT__:")
print(json.dumps({"food_papers": food_papers, "debug": debug_info}))"""

env_args = {'var_function-call-3709648201764099351': 'file_storage/function-call-3709648201764099351.json', 'var_function-call-12009379333761153785': 'file_storage/function-call-12009379333761153785.json', 'var_function-call-8395827407536305276': 'file_storage/function-call-8395827407536305276.json'}

exec(code, env_args)
