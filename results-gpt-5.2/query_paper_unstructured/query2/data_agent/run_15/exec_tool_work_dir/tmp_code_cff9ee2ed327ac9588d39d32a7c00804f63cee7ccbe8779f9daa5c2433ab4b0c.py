code = """import json, re
import pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

cit2018 = load_json_maybe(var_call_jk1Bx4UjiA3YO3Z16RkgZ9Dr)
papers = load_json_maybe(var_call_ErqyZHtOZWIF7BbqI1ePMN6Q)

def title_from_filename(fn):
    return re.sub(r'\.txt$', '', fn)

def is_acm_paper(text):
    if not text:
        return False
    t = text.lower()
    return ('copyright' in t and 'acm' in t) or ('acm ' in t) or ('association for computing machinery' in t)

acm_titles = set()
for d in papers:
    fn = d.get('filename','')
    title = title_from_filename(fn)
    if is_acm_paper(d.get('text','')):
        acm_titles.add(title)

# join with citations 2018
rows=[]
for r in cit2018:
    title=r.get('title')
    if title in acm_titles:
        try:
            cc=int(r.get('citation_count'))
        except Exception:
            continue
        rows.append({'title': title, 'citation_count': cc})

df=pd.DataFrame(rows)
result={'avg_citation_count_2018_acm': (None if df.empty else float(df['citation_count'].mean())),
        'acm_papers_with_2018_citations': int(df.shape[0])}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_alRQxrdn7NYo74vXOh9BYORz': [{'avg_citations_2018': 'None'}], 'var_call_jk1Bx4UjiA3YO3Z16RkgZ9Dr': 'file_storage/call_jk1Bx4UjiA3YO3Z16RkgZ9Dr.json', 'var_call_ErqyZHtOZWIF7BbqI1ePMN6Q': 'file_storage/call_ErqyZHtOZWIF7BbqI1ePMN6Q.json'}

exec(code, env_args)
