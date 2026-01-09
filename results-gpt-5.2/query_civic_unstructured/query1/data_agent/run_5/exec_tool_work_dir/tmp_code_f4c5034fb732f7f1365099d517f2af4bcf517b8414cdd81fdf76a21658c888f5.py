code = """import json, re
civic = var_call_dg5JVhfch06pxm1wQfiyAf8c
if isinstance(civic, str):
    with open(civic, 'r', encoding='utf-8') as f:
        civic = json.load(f)

# search for 'Capital Improvement Projects (Design)' literal and report matches count
pat = re.compile(r'Capital Improvement Projects \(Design\)', re.IGNORECASE)
found=[]
for doc in civic:
    if pat.search(doc.get('text','') or ''):
        found.append(doc.get('filename'))

print('__RESULT__:')
print(json.dumps({'matches': len(found), 'filenames': found[:20]}))"""

env_args = {'var_call_8YSPtlxKUqAdVgtYrYZYfHTz': [{'cnt': '276'}], 'var_call_dg5JVhfch06pxm1wQfiyAf8c': 'file_storage/call_dg5JVhfch06pxm1wQfiyAf8c.json', 'var_call_ogMj4TmRt3AwmHHdNOMCPFls': ['Funding'], 'var_call_6HF3oFNFRkfp4Hk7ogXyDhPA': 'file_storage/call_6HF3oFNFRkfp4Hk7ogXyDhPA.json', 'var_call_bEOBsEXekaG6C5xSepof4VCl': {'count': 0, 'projects': []}, 'var_call_3uR50DXJHVsaFxUXxvjrG6L2': {'error': 'no design section found'}}

exec(code, env_args)
