code = """import json, re
import pandas as pd

# load citations 2020
cit_path = var_call_6CTBsVW3trjDkhwdECLFRHhz
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

# load paper docs
docs_path = var_call_2QnmXfSXpG1ucEmIigFZPc1S
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def guess_venue(text):
    # look for common venue tokens; prioritize CHI
    if re.search(r"\bCHI\b", text):
        return 'CHI'
    # other known venues (not needed but avoid false negatives?)
    venues = ['CSCW','UBICOMP','UbiComp','DIS','IUI','WWW','OzCHI','TEI','AH','PervasiveHealth']
    for v in venues:
        if re.search(r"\b"+re.escape(v)+r"\b", text):
            return 'Ubicomp' if v in ['UBICOMP','UbiComp'] else v
    return None

chi_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    venue = guess_venue(d.get('text',''))
    if venue == 'CHI':
        chi_titles.add(title)

# sum citations for chi titles

total = 0
for r in cit:
    if r.get('title') in chi_titles:
        try:
            total += int(r.get('citation_count') or 0)
        except Exception:
            pass

out = json.dumps({"total_citation_count_CHI_cited_in_2020": total})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_6CTBsVW3trjDkhwdECLFRHhz': 'file_storage/call_6CTBsVW3trjDkhwdECLFRHhz.json', 'var_call_2QnmXfSXpG1ucEmIigFZPc1S': 'file_storage/call_2QnmXfSXpG1ucEmIigFZPc1S.json'}

exec(code, env_args)
