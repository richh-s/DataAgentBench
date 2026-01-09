code = """import json, re
import pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

cit2020 = load_json_maybe(var_call_dP5gwIAcnz43wEUobhY4eaes)
docs = load_json_maybe(var_call_tLhcxOEE3W9goaq6763lsvZz)

def title_from_filename(fn):
    return re.sub(r'\.txt$', '', fn).strip()

# Identify CHI papers via presence of 'CHI' token in header strings like "CHI '15" or "Proceedings of the SIGCHI".
chi_titles = set()
chi_re = re.compile(r"\bCHI\b\s*['’]?\s*\d{2}\b|SIGCHI|Conference on Human Factors in Computing Systems", re.IGNORECASE)

for d in docs:
    txt = d.get('text','') or ''
    if chi_re.search(txt):
        chi_titles.add(title_from_filename(d.get('filename','')))

# Sum citations in 2020 for CHI titles
sum_cit = 0
for r in cit2020:
    t = (r.get('title') or '').strip()
    if t in chi_titles:
        sum_cit += int(r.get('citation_count') or 0)

out = {"total_citation_count_2020_for_CHI_papers": sum_cit}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_kc1D6EeHE1G66ydFvPOfKfBx': [{'total_citations_2020': '9576'}], 'var_call_dP5gwIAcnz43wEUobhY4eaes': 'file_storage/call_dP5gwIAcnz43wEUobhY4eaes.json', 'var_call_3clCorJ13afLC52oyGMgpghY': 'file_storage/call_3clCorJ13afLC52oyGMgpghY.json', 'var_call_tLhcxOEE3W9goaq6763lsvZz': 'file_storage/call_tLhcxOEE3W9goaq6763lsvZz.json'}

exec(code, env_args)
