code = """import json

paper_docs_path = locals()['var_function-call-14925158578354177648']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

debug_info = []

for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    header_text = text[:1000]
    
    # Check years
    years_found = []
    for y in range(2010, 2020):
        if str(y) in header_text:
            years_found.append(y)
            
    has_pa = 'physical activity' in text.lower()
    
    debug_info.append({
        'title': title,
        'years_found': years_found,
        'has_physical_activity': has_pa
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-1637384971147103697': ['paper_docs'], 'var_function-call-1637384971147100208': ['Citations', 'sqlite_sequence'], 'var_function-call-12832305372190774842': 'file_storage/function-call-12832305372190774842.json', 'var_function-call-8891803198092466496': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-15218699156222790202': 5, 'var_function-call-14925158578354177648': 'file_storage/function-call-14925158578354177648.json', 'var_function-call-15838681542065948214': 'file_storage/function-call-15838681542065948214.json', 'var_function-call-1830984539435977228': []}

exec(code, env_args)
