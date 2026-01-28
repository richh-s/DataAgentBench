code = """import json

# Load papers
with open(locals()['var_function-call-4358244583942540599'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-5959858908206975424'], 'r') as f:
    citations = json.load(f)

food_papers_titles = []

for p in papers:
    text = p['text']
    filename = p['filename']
    title = filename.replace('.txt', '')
    
    # Extract Author Keywords via simple string manipulation
    lower_text = text.lower()
    start_marker = "author keywords"
    start_idx = lower_text.find(start_marker)
    
    keywords_text = ""
    if start_idx != -1:
        # Take the next 1000 chars as a snippet for keywords
        snippet = lower_text[start_idx:start_idx+1000]
        keywords_text = snippet
    
    # Check for 'food' in title or keywords
    is_food = False
    if 'food' in title.lower():
        is_food = True
    elif 'food' in keywords_text:
        is_food = True
    
    if is_food:
        food_papers_titles.append(title)

# Filter citations
total_citations = 0

food_titles_set = set(food_papers_titles)

for c in citations:
    c_title = c.get('title')
    try:
        count = int(c.get('citation_count', 0))
    except:
        count = 0
        
    if c_title in food_titles_set:
        total_citations += count

result = {
    "food_papers_found": food_papers_titles,
    "total_citations": total_citations
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4625483642172775665': 'file_storage/function-call-4625483642172775665.json', 'var_function-call-4600237865366959545': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-5959858908206975424': 'file_storage/function-call-5959858908206975424.json', 'var_function-call-4358244583942540599': 'file_storage/function-call-4358244583942540599.json'}

exec(code, env_args)
