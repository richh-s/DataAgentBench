code = """import json

file_path = locals()['var_function-call-16827222845140739924']
with open(file_path, 'r') as f:
    papers = json.load(f)

debug_info = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    header_snippet = text[:200]
    has_2016 = '2016' in text[:1000]
    has_physical_activity = 'physical activity' in text.lower()
    
    debug_info.append({
        'title': title,
        'has_2016': has_2016,
        'has_physical_activity': has_physical_activity,
        'header_snippet': header_snippet
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-6317052684018889130': 'file_storage/function-call-6317052684018889130.json', 'var_function-call-1880334969290671800': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-16827222845140739924': 'file_storage/function-call-16827222845140739924.json', 'var_function-call-14106871442231885979': []}

exec(code, env_args)
