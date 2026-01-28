code = """import json

with open(locals()['var_function-call-4358244583942540599'], 'r') as f:
    papers = json.load(f)

debug_info = []

for p in papers:
    text = p['text']
    title = p['filename'].replace('.txt', '')
    
    lower_text = text.lower()
    start_idx = lower_text.find("author keywords")
    
    extracted = ""
    if start_idx != -1:
        # extract next 500 chars
        raw_snippet = text[start_idx:start_idx+500]
        extracted = raw_snippet
    
    debug_info.append({"title": title, "snippet": extracted})

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-4625483642172775665': 'file_storage/function-call-4625483642172775665.json', 'var_function-call-4600237865366959545': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-5959858908206975424': 'file_storage/function-call-5959858908206975424.json', 'var_function-call-4358244583942540599': 'file_storage/function-call-4358244583942540599.json', 'var_function-call-1694766061137811147': {'food_papers_found': ['A Lived Informatics Model of Personal Informatics'], 'total_citations': 390}}

exec(code, env_args)
