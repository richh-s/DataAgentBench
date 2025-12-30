code = """import json

filepath = locals()['var_function-call-3288691391173490611']
with open(filepath, 'r') as f:
    papers = json.load(f)

debug_info = []
for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.rsplit('.', 1)[0]
    
    header = text[:200].replace('\n', ' ')
    has_2016 = "2016" in text[:3000]
    has_pa = "physical activity" in text.lower()
    
    debug_info.append({
        "title": title,
        "header_preview": header,
        "has_2016": has_2016,
        "has_pa": has_pa
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-18071913863727802806': ['paper_docs'], 'var_function-call-18071913863727800731': ['Citations', 'sqlite_sequence'], 'var_function-call-4878043967039962062': 'file_storage/function-call-4878043967039962062.json', 'var_function-call-16507150589347793699': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-9855888285311973797': 5, 'var_function-call-3288691391173490611': 'file_storage/function-call-3288691391173490611.json', 'var_function-call-9675587272762560169': []}

exec(code, env_args)
