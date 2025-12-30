code = """import json

# Use the exact key string provided in the previous turn
filepath = locals()['var_function-call-3288691391173490611']
with open(filepath, 'r') as f:
    papers = json.load(f)

matching_titles = []
for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.rsplit('.', 1)[0]
    
    # Check year 2016
    header_text = text[:3000]
    is_2016 = "2016" in header_text
    
    # Check domain "physical activity"
    is_physical_activity = "physical activity" in text.lower()
    
    if is_2016 and is_physical_activity:
        matching_titles.append(title)

print("__RESULT__:")
print(json.dumps(matching_titles))"""

env_args = {'var_function-call-18071913863727802806': ['paper_docs'], 'var_function-call-18071913863727800731': ['Citations', 'sqlite_sequence'], 'var_function-call-4878043967039962062': 'file_storage/function-call-4878043967039962062.json', 'var_function-call-16507150589347793699': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-9855888285311973797': 5, 'var_function-call-3288691391173490611': 'file_storage/function-call-3288691391173490611.json'}

exec(code, env_args)
