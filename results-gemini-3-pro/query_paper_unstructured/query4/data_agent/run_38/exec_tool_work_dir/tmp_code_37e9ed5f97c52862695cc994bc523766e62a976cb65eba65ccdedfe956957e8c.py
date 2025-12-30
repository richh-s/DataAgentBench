code = """import json

with open(locals()['var_function-call-4534989108856043984'], 'r') as f:
    paper_docs = json.load(f)

debug_info = []

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    if 'physical activity' in text.lower():
        snippet = text[:300].replace('\n', ' ')
        debug_info.append({"filename": filename, "snippet": snippet})

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-8115990490355926110': 'file_storage/function-call-8115990490355926110.json', 'var_function-call-15132226113380290757': 'file_storage/function-call-15132226113380290757.json', 'var_function-call-4534989108856043984': 'file_storage/function-call-4534989108856043984.json', 'var_function-call-280795814972665149': 'file_storage/function-call-280795814972665149.json', 'var_function-call-6662066494306016302': []}

exec(code, env_args)
