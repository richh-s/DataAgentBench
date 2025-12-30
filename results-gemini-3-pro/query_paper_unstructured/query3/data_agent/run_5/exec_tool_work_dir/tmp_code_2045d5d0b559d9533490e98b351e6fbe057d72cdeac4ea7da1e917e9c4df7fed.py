code = """import json
import re

with open(locals()['var_function-call-12792815428648479832'], 'r') as f:
    paper_docs = json.load(f)

diagnostics = []
for doc in paper_docs[:10]:
    text = doc['text']
    filename = doc['filename']
    header_text = text[:1000]
    years = re.findall(r'\b(20\d{2})\b', header_text)
    has_empirical = "empirical" in text.lower()
    diagnostics.append({
        "filename": filename,
        "years": years,
        "has_empirical": has_empirical,
        "snippet": header_text[:100].replace('\n', ' ')
    })

print("__RESULT__:")
print(json.dumps(diagnostics))"""

env_args = {'var_function-call-9689432006532158130': 'file_storage/function-call-9689432006532158130.json', 'var_function-call-7106794807816664619': 'file_storage/function-call-7106794807816664619.json', 'var_function-call-12792815428648479832': 'file_storage/function-call-12792815428648479832.json', 'var_function-call-15343514597715386657': 'file_storage/function-call-15343514597715386657.json', 'var_function-call-16410926222375514887': []}

exec(code, env_args)
