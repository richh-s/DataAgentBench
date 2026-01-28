code = """import json, re
import pandas as pd

# load records
src = var_call_QtSufoFOi6RQJdWNZm6rLZoQ
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        recs = json.load(f)
else:
    recs = src

# helper to parse assignee from Patents_info
assignee_re = re.compile(r"owned by ([^.,]+)|assigned to ([^.,]+)|holds the [A-Z]{2} patent filing .*?owned by ([^.,]+)", re.IGNORECASE)

def get_assignee(text):
    m = assignee_re.search(text or '')
    if not m:
        # fallback: look for 'is owned by X' or 'is assigned to X'
        m2 = re.search(r"(?:owned by|assigned to) ([^.,]+)", text or '', re.IGNORECASE)
        return (m2.group(1).strip() if m2 else None)
    for g in m.groups():
        if g:
            return g.strip()
    return None

# build map: cited_pub -> UC primary CPC subclass code (4-char subgroup like F25B)
rows = []
for r in recs:
    cited = []
    try:
        cited = json.loads(r.get('citation') or '[]')
    except Exception:
        cited = []
    # primary CPC: where first==true; if none, skip
    try:
        cpcs = json.loads(r.get('cpc') or '[]')
    except Exception:
        cpcs = []
    primary_codes = [c.get('code') for c in cpcs if isinstance(c, dict) and c.get('first') is True and c.get('code')]
    # convert to subclass (first 4 chars, strip spaces)
    primary_subclasses = sorted(set([pc.replace(' ', '')[:4] for pc in primary_codes if len(pc.replace(' ', ''))>=4]))
    for c in cited:
        pn = c.get('publication_number')
        if pn:
            for sc in primary_subclasses:
                rows.append({'uc_cited_pub': pn, 'uc_primary_subclass': sc})

uc_cited_df = pd.DataFrame(rows).drop_duplicates()
# output distinct subclasses to look up titles
subclasses = sorted(uc_cited_df['uc_primary_subclass'].dropna().unique().tolist())
print('__RESULT__:')
print(json.dumps({'n_uc_patents': len(recs), 'n_cited_pubs': int(uc_cited_df['uc_cited_pub'].nunique()) if not uc_cited_df.empty else 0, 'subclasses': subclasses}))"""

env_args = {'var_call_vUJMPfY6dnH3TNkgowJsOtGq': ['publicationinfo'], 'var_call_x8ZBV1E4gydbt2vDZIO64V0x': ['cpc_definition'], 'var_call_QtSufoFOi6RQJdWNZm6rLZoQ': 'file_storage/call_QtSufoFOi6RQJdWNZm6rLZoQ.json'}

exec(code, env_args)
