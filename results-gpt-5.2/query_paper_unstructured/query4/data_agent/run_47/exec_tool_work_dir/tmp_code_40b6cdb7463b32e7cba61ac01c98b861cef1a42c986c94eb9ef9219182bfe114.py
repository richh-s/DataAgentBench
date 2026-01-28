code = """import json, re
import pandas as pd

path_docs = var_call_EdI5tfxdG7NthR2A0PqHgMLO
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# broaden year extraction: take minimum plausible year in header if copyright missing

def extract_year2(text):
    head = text[:4000]
    # prefer patterns like "2016" near conference line
    years = [int(y) for y in re.findall(r'\b(19\d{2}|20\d{2})\b', head)]
    years = [y for y in years if 1980 <= y <= 2030]
    if not years:
        return None
    # heuristic: publication year is often the first year mentioned in header
    return years[0]

rows=[]
for d in docs:
    title=d['filename'][:-4]
    year=extract_year2(d.get('text','') or '')
    is_pa=bool(re.search(r'physical\s+activity', d.get('text','') or '', re.IGNORECASE))
    rows.append({'title':title,'year':year,'is_pa':is_pa})

df=pd.DataFrame(rows)
# get candidate list for 2016 PA
cand=df[(df.year==2016) & (df.is_pa)]
# if empty, check distribution of years for PA papers
pa=df[df.is_pa]
counts=pa.year.value_counts(dropna=False).head(20).to_dict()

print('__RESULT__:')
print(json.dumps({'cand_count':int(len(cand)),'year_counts_top20':counts,'sample_pa_titles':pa.head(20).title.tolist()}))"""

env_args = {'var_call_EdI5tfxdG7NthR2A0PqHgMLO': 'file_storage/call_EdI5tfxdG7NthR2A0PqHgMLO.json', 'var_call_saVRj1ZwzmtyAiRdfptdqatS': 'file_storage/call_saVRj1ZwzmtyAiRdfptdqatS.json', 'var_call_pXsj2WWCsxISUEttDET8u11L': []}

exec(code, env_args)
