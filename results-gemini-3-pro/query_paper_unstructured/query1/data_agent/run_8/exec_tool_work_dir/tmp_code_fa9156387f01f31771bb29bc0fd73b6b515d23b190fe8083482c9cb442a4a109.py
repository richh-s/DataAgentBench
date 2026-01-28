code = """import json

with open(locals()['var_function-call-1518864463960469704'], 'r') as f:
    papers = json.load(f)

debug_info = []

for i, p in enumerate(papers[:10]):
    text = p.get('text', '')
    filename = p.get('filename', '')
    
    # search for keywords
    text_lower = text.lower()
    idx = text_lower.find("keywords")
    snippet = ""
    if idx != -1:
        start = max(0, idx - 20)
        end = min(len(text), idx + 200)
        snippet = text[start:end]
    
    debug_info.append({
        "filename": filename,
        "keywords_snippet": snippet
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-13263841084100216715': ['paper_docs'], 'var_function-call-2979229897755399322': 'file_storage/function-call-2979229897755399322.json', 'var_function-call-1518864463960469704': 'file_storage/function-call-1518864463960469704.json', 'var_function-call-16808733530214175810': 'file_storage/function-call-16808733530214175810.json', 'var_function-call-8705897625478698375': {'total_citations': 0, 'paper_count': 0, 'matched_titles': []}}

exec(code, env_args)
