code = """import json, re
civic = var_call_dg5JVhfch06pxm1wQfiyAf8c
if isinstance(civic, str):
    with open(civic, 'r', encoding='utf-8') as f:
        civic = json.load(f)

fname='malibucity_agenda_03222023-2060.txt'
doc = next(d for d in civic if d.get('filename')==fname)
text = doc.get('text','')
section_re = re.compile(r'Capital Improvement Projects \(Design\)', re.IGNORECASE)
end_re = re.compile(r'Capital Improvement Projects \((?:Construction|Not Started)\)|Disaster Recovery Projects', re.IGNORECASE)
m=section_re.search(text)
sub=text[m.end():]
m2=end_re.search(sub)
if m2:
    sub=sub[:m2.start()]
lines=[ln.strip() for ln in sub.splitlines() if ln.strip()]
print('__RESULT__:')
print(json.dumps({'n_lines': len(lines), 'first_50': lines[:50]}))"""

env_args = {'var_call_8YSPtlxKUqAdVgtYrYZYfHTz': [{'cnt': '276'}], 'var_call_dg5JVhfch06pxm1wQfiyAf8c': 'file_storage/call_dg5JVhfch06pxm1wQfiyAf8c.json', 'var_call_ogMj4TmRt3AwmHHdNOMCPFls': ['Funding'], 'var_call_6HF3oFNFRkfp4Hk7ogXyDhPA': 'file_storage/call_6HF3oFNFRkfp4Hk7ogXyDhPA.json', 'var_call_bEOBsEXekaG6C5xSepof4VCl': {'count': 0, 'projects': []}, 'var_call_3uR50DXJHVsaFxUXxvjrG6L2': {'error': 'no design section found'}, 'var_call_W7cColvqRHw80B0TmzgYyERS': {'matches': 5, 'filenames': ['malibucity_agenda_03222023-2060.txt', 'malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt']}}

exec(code, env_args)
