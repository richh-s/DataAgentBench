code = """import json

# Load the result from the previous query
file_path = locals()['var_function-call-1041647607165487633']

with open(file_path, 'r') as f:
    papers = json.load(f)

food_papers = []

for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    is_food = False
    
    # Check title
    if 'food' in title.lower():
        is_food = True
    
    # Check keywords (simple extraction)
    if not is_food:
        lower_text = text.lower()
        start_idx = lower_text.find('author keywords')
        if start_idx != -1:
            # Look at the next 500 characters
            snippet = lower_text[start_idx:start_idx+500]
            # Check if 'food' is in this snippet
            # To be more precise, stop at the next section usually "ACM Classification" or "Introduction"
            end_idx = snippet.find('acm classification')
            if end_idx == -1:
                end_idx = snippet.find('introduction')
            
            if end_idx != -1:
                keywords_section = snippet[:end_idx]
            else:
                keywords_section = snippet
            
            if 'food' in keywords_section:
                is_food = True

    if is_food:
        food_papers.append(title)

print("__RESULT__:")
print(json.dumps(food_papers))"""

env_args = {'var_function-call-17948406739355176464': 'file_storage/function-call-17948406739355176464.json', 'var_function-call-1041647607165485382': ['Citations', 'sqlite_sequence'], 'var_function-call-1041647607165487633': 'file_storage/function-call-1041647607165487633.json'}

exec(code, env_args)
