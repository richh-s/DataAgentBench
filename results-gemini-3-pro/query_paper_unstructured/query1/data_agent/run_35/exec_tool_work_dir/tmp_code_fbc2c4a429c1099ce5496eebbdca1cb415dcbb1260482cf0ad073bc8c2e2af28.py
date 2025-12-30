code = """import json

citations_path = locals()['var_function-call-14555610858560358239']
papers_path = locals()['var_function-call-11640274332636556525']

with open(citations_path, 'r') as f:
    citations = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

debug_info = []
food_titles = []
extracted_kw_samples = []

for i, p in enumerate(papers):
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    text_lower = text.lower()
    
    kw_header = 'author keywords'
    kw_start = text_lower.find(kw_header)
    offset = len(kw_header)
    
    if kw_start == -1:
        kw_header = 'keywords'
        kw_start = text_lower.find(kw_header)
        offset = len(kw_header)
    
    extracted_keywords = ""
    if kw_start != -1:
        start_idx = kw_start + offset
        chunk = text_lower[start_idx:start_idx+1000]
        # Split by double newline
        parts = chunk.split(chr(10) + chr(10))
        extracted_keywords = parts[0]
    
    if i < 5:
        extracted_kw_samples.append({'title': title, 'kw': extracted_keywords})
        
    is_food = False
    if 'food' in title.lower():
        is_food = True
        food_titles.append(title)
    
    if 'food' in extracted_keywords:
        is_food = True
        if title not in food_titles:
            food_titles.append(title)

# Check full text for 'food' just to see
full_text_food_count = 0
for p in papers:
    if 'food' in p.get('text', '').lower():
        full_text_food_count += 1

print("__RESULT__:")
print(json.dumps({
    "food_titles": food_titles,
    "sample_keywords": extracted_kw_samples,
    "full_text_food_count": full_text_food_count
}))"""

env_args = {'var_function-call-13801611410000855703': 'file_storage/function-call-13801611410000855703.json', 'var_function-call-13801611410000858480': ['Citations', 'sqlite_sequence'], 'var_function-call-14555610858560358239': 'file_storage/function-call-14555610858560358239.json', 'var_function-call-11640274332636556525': 'file_storage/function-call-11640274332636556525.json', 'var_function-call-9036090035766421574': 0}

exec(code, env_args)
