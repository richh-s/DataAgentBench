code = """import json, re
import pandas as pd

def load_tool_result(var):
    # var can be list (already loaded) or a path string
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

cit2020 = load_tool_result(var_call_k4U5ymJT7ZSf107TIzEljqeu)
papers = load_tool_result(var_call_TKoxGY9wVyVQvI5QgGsIXGCc)

# Build CHI title set from papers by parsing venue from text
chi_titles = set()
for doc in papers:
    fn = doc.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = doc.get('text','') or ''
    # Heuristic: look for venue tokens in header lines
    head = text[:4000].upper()
    if 'CHI' in head:
        # avoid matching e.g., 'CHINA' by requiring word boundary
        if re.search(r'\bCHI\b', head):
            chi_titles.add(title)

# Sum citations in 2020 for CHI papers
rows=[]
for r in cit2020:
    t=r.get('title')
    if t in chi_titles:
        try:
            cc=int(r.get('citation_count'))
        except Exception:
            cc=0
        rows.append((t,cc))

df=pd.DataFrame(rows, columns=['title','citation_count'])

total=int(df['citation_count'].sum()) if not df.empty else 0
out={'total_citation_count_2020_for_CHI_papers': total, 'num_CHI_papers_cited_in_2020': int(df['title'].nunique()), 'per_paper': df.sort_values('citation_count', ascending=False).to_dict(orient='records')}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_k4U5ymJT7ZSf107TIzEljqeu': 'file_storage/call_k4U5ymJT7ZSf107TIzEljqeu.json', 'var_call_TKoxGY9wVyVQvI5QgGsIXGCc': 'file_storage/call_TKoxGY9wVyVQvI5QgGsIXGCc.json'}

exec(code, env_args)
