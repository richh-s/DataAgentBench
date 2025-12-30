code = """import json
import re

# Load Paper Docs Candidates
with open(locals()['var_function-call-4190209602007516202'], 'r') as f:
    papers = json.load(f)

debug_info = {}
debug_info["num_papers"] = len(papers)

# Get headers
headers = []
for p in papers[:3]:
    headers.append({"title": p['filename'], "header": p['text'][:300]})
debug_info["headers"] = headers

# Check title matches
with open(locals()['var_function-call-10263286268720561281'], 'r') as f:
    citations_data = json.load(f)
citation_titles = set(c['title'] for c in citations_data)

matches = 0
examples_matched = []
for p in papers:
    t = p['filename'].replace('.txt', '')
    if t in citation_titles:
        matches += 1
        if len(examples_matched) < 3:
            examples_matched.append(t)

debug_info["matches"] = matches
debug_info["examples_matched"] = examples_matched

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-4042789943322229169': ['paper_docs'], 'var_function-call-4042789943322227422': ['Citations', 'sqlite_sequence'], 'var_function-call-12606358993077835147': 'file_storage/function-call-12606358993077835147.json', 'var_function-call-9821348660880975822': 'file_storage/function-call-9821348660880975822.json', 'var_function-call-10263286268720561281': 'file_storage/function-call-10263286268720561281.json', 'var_function-call-4190209602007516202': 'file_storage/function-call-4190209602007516202.json', 'var_function-call-14190727982573706246': []}

exec(code, env_args)
