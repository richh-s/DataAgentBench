code = """import json, re
import pandas as pd

def load_tool_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

cites = load_tool_result(var_call_N8bqixKn8qN8zhquYyvbEjeZ)
pdocs = load_tool_result(var_call_apURVC91sbdE3Dm9jan8CQv6)

# Build title->venue using regex on text
venue_by_title = {}
venue_pat = re.compile(r"\bCHI\s*'?\d{2}\b|\bCHI\s+\d{4}\b", re.IGNORECASE)

for d in pdocs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    txt = d.get('text','') or ''
    is_chi = bool(venue_pat.search(txt))
    # also match 'Proceedings of the SIGCHI Conference' phrasing
    if not is_chi and re.search(r"SIGCHI\s+Conference|Conference\s+on\s+Human\s+Factors\s+in\s+Computing\s+Systems", txt, re.IGNORECASE):
        is_chi = True
    if is_chi:
        venue_by_title[title] = 'CHI'

# Filter citations to CHI titles and sum citation_count
chi_cites = []
for r in cites:
    t = r.get('title')
    if t in venue_by_title:
        try:
            cc = int(r.get('citation_count') or 0)
        except Exception:
            cc = 0
        chi_cites.append({'title': t, 'citation_count_2020': cc})

df = pd.DataFrame(chi_cites)
if df.empty:
    out = {'total_citation_count_2020_for_CHI_papers': 0, 'num_CHI_papers': 0}
else:
    out = {
        'total_citation_count_2020_for_CHI_papers': int(df['citation_count_2020'].sum()),
        'num_CHI_papers': int(df['title'].nunique())
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_N8bqixKn8qN8zhquYyvbEjeZ': 'file_storage/call_N8bqixKn8qN8zhquYyvbEjeZ.json', 'var_call_apURVC91sbdE3Dm9jan8CQv6': 'file_storage/call_apURVC91sbdE3Dm9jan8CQv6.json'}

exec(code, env_args)
