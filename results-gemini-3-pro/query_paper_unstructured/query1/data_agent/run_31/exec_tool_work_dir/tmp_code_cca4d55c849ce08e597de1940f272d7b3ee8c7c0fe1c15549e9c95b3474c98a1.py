code = """import json

papers_path = locals()['var_function-call-5874155478376628757']
with open(papers_path, 'r') as f:
    papers = json.load(f)

print("__RESULT__:")
debug_list = []
for p in papers[:5]:
    text = p['text']
    # find keywords
    idx = text.lower().find('keywords')
    snippet = text[idx:idx+200] if idx != -1 else "NOT FOUND"
    debug_list.append({"filename": p['filename'], "keyword_snippet": snippet})

print(json.dumps(debug_list))"""

env_args = {'var_function-call-853909438841445340': 'file_storage/function-call-853909438841445340.json', 'var_function-call-1978902813264061650': 'file_storage/function-call-1978902813264061650.json', 'var_function-call-99245770254800995': 'file_storage/function-call-99245770254800995.json', 'var_function-call-5874155478376628757': 'file_storage/function-call-5874155478376628757.json', 'var_function-call-1098255190598746852': {'total_citations': 0, 'food_papers': []}}

exec(code, env_args)
