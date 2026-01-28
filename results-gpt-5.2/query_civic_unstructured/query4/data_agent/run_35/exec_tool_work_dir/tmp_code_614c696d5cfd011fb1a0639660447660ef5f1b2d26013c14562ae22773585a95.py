code = """import json, re

civic_src = var_call_2t22R3UaX4Znxt0xz8fGYIAP
if isinstance(civic_src, str):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

fn = 'malibucity_agenda__03232022-1869.txt'
text = next(d['text'] for d in civic_docs if d['filename']==fn)
# show snippets around Spring 2022 occurrences
snips=[]
for m in re.finditer(r"Spring\s*,?\s*2022", text, flags=re.IGNORECASE):
    snips.append(text[max(0,m.start()-200): m.start()+200])

print('__RESULT__:')
print(json.dumps({"filename": fn, "snippets": snips[:10]}))"""

env_args = {'var_call_KGer4GH8D7ZnCWgfNaReubzl': ['Funding'], 'var_call_2t22R3UaX4Znxt0xz8fGYIAP': 'file_storage/call_2t22R3UaX4Znxt0xz8fGYIAP.json', 'var_call_CAVbt0EfwT8uPhTQKJt2uLzX': 'file_storage/call_CAVbt0EfwT8uPhTQKJt2uLzX.json', 'var_call_gqCYwIbXiadWD03lxJ9pO1c8': {'projects_started_spring_2022_count': 0, 'projects_started_spring_2022_total_funding': 0, 'projects': []}, 'var_call_hsVw4mCiG6dQp2xLIQfz2jeb': {'docs_with_spring_2022': ['malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt', 'malibucity_agenda__03242021-1665.txt', 'malibucity_agenda__04282021-1687.txt', 'malibucity_agenda__05262021-1701.txt', 'malibucity_agenda__06222022-1919.txt', 'malibucity_agenda__06232021-1714.txt', 'malibucity_agenda__07272022-1939.txt', 'malibucity_agenda__07282021-1732.txt', 'malibucity_agenda__08252021-1746.txt', 'malibucity_agenda__09222021-1765.txt', 'malibucity_agenda__10272021-1779.txt', 'malibucity_agenda__11102022-1995.txt', 'malibucity_agenda__12142021-1808.txt'], 'count': 16}}

exec(code, env_args)
