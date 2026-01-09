code = """import json, re

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_maybe_path(var_call_z3zm8pDXu23IfNloY6fv3NfR)

patterns = [r'\bCopyright\s+\d{4}\s*\u00a9\s*ACM\b', r'\bCopyright\s+\d{4}\s*\(C\)\s*ACM\b', r'\bACM\s+Classification\s+Keywords\b', r'\bpermissions@acm\.org\b']

out=[]
for d in docs:
    text=d.get('text','') or ''
    is_acm=any(re.search(p, text, flags=re.IGNORECASE) for p in patterns)
    out.append({'filename': d.get('filename'), 'is_acm': is_acm})

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6rTeQEQAZgKGOBxvZpmROagG': 'file_storage/call_6rTeQEQAZgKGOBxvZpmROagG.json', 'var_call_RZlNS97SQlUlupjP0QBop1zH': 'file_storage/call_RZlNS97SQlUlupjP0QBop1zH.json', 'var_call_2xecwlxkbozOl7kUriT09oxo': {'average_citation_count_2018_acm': None, 'acm_papers_with_citations_2018_n': 0, 'total_papers_cited_2018_n': 158}, 'var_call_z3zm8pDXu23IfNloY6fv3NfR': 'file_storage/call_z3zm8pDXu23IfNloY6fv3NfR.json'}

exec(code, env_args)
