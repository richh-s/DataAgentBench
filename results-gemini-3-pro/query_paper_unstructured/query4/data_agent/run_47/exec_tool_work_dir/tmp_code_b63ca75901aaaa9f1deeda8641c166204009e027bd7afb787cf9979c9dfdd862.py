code = """import json

key_name = 'var_function-call-1660175416261696799'
file_path = locals()[key_name]

with open(file_path, 'r') as f:
    papers = json.load(f)

titles = []
for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    if not filename:
        continue
    
    # Check Year 2016 in header
    header = text[:500]
    if '2016' not in header:
        continue
        
    # Check Domain
    title = filename.replace('.txt', '')
    search_text = (title + ' ' + text[:3000]).lower()
    
    if 'physical activity' in search_text:
        titles.append(title)

print('__RESULT__:')
print(json.dumps(titles))"""

env_args = {'var_function-call-8186241074131223286': ['paper_docs'], 'var_function-call-8186241074131224069': ['Citations', 'sqlite_sequence'], 'var_function-call-11444584410328735250': 'file_storage/function-call-11444584410328735250.json', 'var_function-call-1660175416261696799': 'file_storage/function-call-1660175416261696799.json'}

exec(code, env_args)
