code = """import json, re

civic = var_call_dg5JVhfch06pxm1wQfiyAf8c
if isinstance(civic, str):
    with open(civic, 'r', encoding='utf-8') as f:
        civic = json.load(f)

# find first doc with design section and print extracted candidate lines count and sample
section_re = re.compile(r'\bCapital Improvement Projects\s*\(Design\)\b', re.IGNORECASE)
end_re = re.compile(r'\bCapital Improvement Projects\s*\((?:Construction|Not Started)\)\b|\bDisaster Recovery Projects\b', re.IGNORECASE)

for doc in civic:
    text = doc.get('text','') or ''
    m = section_re.search(text)
    if not m:
        continue
    sub = text[m.end():]
    m2 = end_re.search(sub)
    if m2:
        sub = sub[:m2.start()]
    lines = [ln.strip() for ln in sub.splitlines() if ln.strip()]
    # take first 60 lines
    sample = lines[:80]
    print('__RESULT__:')
    print(json.dumps({'filename': doc.get('filename'), 'sample_lines': sample[:60]}))
    break
else:
    print('__RESULT__:')
    print(json.dumps({'error':'no design section found'}))"""

env_args = {'var_call_8YSPtlxKUqAdVgtYrYZYfHTz': [{'cnt': '276'}], 'var_call_dg5JVhfch06pxm1wQfiyAf8c': 'file_storage/call_dg5JVhfch06pxm1wQfiyAf8c.json', 'var_call_ogMj4TmRt3AwmHHdNOMCPFls': ['Funding'], 'var_call_6HF3oFNFRkfp4Hk7ogXyDhPA': 'file_storage/call_6HF3oFNFRkfp4Hk7ogXyDhPA.json', 'var_call_bEOBsEXekaG6C5xSepof4VCl': {'count': 0, 'projects': []}}

exec(code, env_args)
