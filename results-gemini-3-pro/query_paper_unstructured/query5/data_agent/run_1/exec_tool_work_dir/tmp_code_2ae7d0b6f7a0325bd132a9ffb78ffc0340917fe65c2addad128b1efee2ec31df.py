code = """import json
import re

# Load paper docs
with open(locals()['var_function-call-17247428670658995703'], 'r') as f:
    paper_docs = json.load(f)

headers = []
for doc in paper_docs[:3]:
    headers.append({"title": doc['filename'], "header": doc['text'][:200]})

chi_matches = []
for doc in paper_docs:
    # Check for CHI pattern
    if re.search(r"CHI\s*[']?\d{2}", doc['text'][:1000]) or "Human Factors in Computing Systems" in doc['text'][:1000]:
        chi_matches.append(doc['filename'])

result = {
    "headers": headers,
    "num_chi_matches": len(chi_matches),
    "sample_matches": chi_matches[:5]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-12437250052302532993': 'file_storage/function-call-12437250052302532993.json', 'var_function-call-17247428670658995703': 'file_storage/function-call-17247428670658995703.json', 'var_function-call-767057999987748063': 16, 'var_function-call-17271081787061420733': 16, 'var_function-call-10439916293815859342': {'total_citations': 0, 'count': 0, 'titles': []}, 'var_function-call-8934908314266514909': 'Done'}

exec(code, env_args)
