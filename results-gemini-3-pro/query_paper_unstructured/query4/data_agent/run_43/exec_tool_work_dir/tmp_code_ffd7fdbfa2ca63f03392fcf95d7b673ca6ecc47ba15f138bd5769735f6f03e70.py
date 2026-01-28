code = """import json

file_path = locals()['var_function-call-16827222845140739924']
with open(file_path, 'r') as f:
    papers = json.load(f)

matching_titles = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check year 2016 in the first 1000 characters (header/copyright)
    # It might be in format "2016" or "'16". "2016" is safer.
    header_text = text[:1000]
    if '2016' in header_text:
        is_2016 = True
    else:
        is_2016 = False
        
    # Check domain "physical activity" in the whole text (case-insensitive)
    if 'physical activity' in text.lower():
        is_domain = True
    else:
        is_domain = False
        
    if is_2016 and is_domain:
        matching_titles.append(title)

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-6317052684018889130': 'file_storage/function-call-6317052684018889130.json', 'var_function-call-1880334969290671800': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-16827222845140739924': 'file_storage/function-call-16827222845140739924.json'}

exec(code, env_args)
