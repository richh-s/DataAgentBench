code = """import json

# Load paper docs
with open(locals()['var_function-call-11391268532651985749'], 'r') as f:
    paper_docs = json.load(f)

snippets = []
for doc in paper_docs[:10]:
    text = doc['text']
    lower_text = text.lower()
    start_idx = lower_text.find("author keywords")
    if start_idx == -1:
        start_idx = lower_text.find("keywords")
    
    if start_idx != -1:
        snippet = text[start_idx:start_idx+300] # Take 300 chars
        snippets.append(snippet)
    else:
        snippets.append("NO KEYWORDS FOUND")

print("__RESULT__:")
print(json.dumps(snippets))"""

env_args = {'var_function-call-2084014560423739449': 'file_storage/function-call-2084014560423739449.json', 'var_function-call-11352259319045470857': 'file_storage/function-call-11352259319045470857.json', 'var_function-call-9528525890526779817': 'file_storage/function-call-9528525890526779817.json', 'var_function-call-11391268532651985749': 'file_storage/function-call-11391268532651985749.json', 'var_function-call-4893813044392379918': {'food_papers_count': 0, 'total_citations': 0, 'sample_food_papers': []}}

exec(code, env_args)
