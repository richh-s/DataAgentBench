code = """import json
import re

# Load the papers
with open(locals()['var_function-call-10170891781232486104'], 'r') as f:
    papers = json.load(f)

titles_2016 = []

for p in papers:
    text = p['text']
    filename = p['filename']
    title = filename.replace('.txt', '')
    
    # Check for Year 2016
    # Look for 2016 in the header or copyright
    # Heuristic: 2016 within the first 1000 characters
    header_text = text[:1000]
    if '2016' in header_text:
        # Check if it is likely the publication year
        # e.g. "Copyright 2016", "CHI 2016", "September 2016"
        # Avoid "Copyright 2015 ... 2016" (unlikely in header for 2015 paper?)
        # Let's assume presence in header implies publication year for now.
        
        # Check for domain 'physical activity'
        # The query ensured it is in the text.
        # Let's check if it is in the abstract/keywords (first 3000 chars) to be safer?
        # Or just trust the query? The prompt says "domain... physical activity", implying it's a topic.
        # I'll stick to the query result but maybe ensure it's not just a reference.
        if 'physical activity' in text.lower():
            titles_2016.append(title)

print("__RESULT__:")
print(json.dumps(titles_2016))"""

env_args = {'var_function-call-3386748849417591379': 'file_storage/function-call-3386748849417591379.json', 'var_function-call-10170891781232486104': 'file_storage/function-call-10170891781232486104.json'}

exec(code, env_args)
