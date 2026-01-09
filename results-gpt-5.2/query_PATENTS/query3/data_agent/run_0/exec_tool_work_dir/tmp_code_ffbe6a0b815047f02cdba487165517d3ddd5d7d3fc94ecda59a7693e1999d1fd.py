code = """import json, re, pandas as pd
from pathlib import Path

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json') and Path(maybe_path).exists():
        return json.loads(Path(maybe_path).read_text())
    return maybe_path

recs = load_records(var_call_LLUMGJgH1Ae4i7xDhL2BBZjU)

def parse_assignee(pi):
    if not pi:
        return None
    m = re.search(r'(?:owned by|assigned to)\s+([^\.]+?)\s+and has', pi)
    if m:
        return m.group(1).strip()
    m = re.search(r'^\s*([^,]+?)\s+holds\b', pi)
    if m:
        return m.group(1).strip()
    m = re.search(r'\bis (?:owned by|assigned to)\s+([^\.]+?)(?:\.|,)', pi)
    if m:
        return m.group(1).strip()
    return None

def get_pub_number(pi):
    if not pi:
        return None
    m = re.search(r'pub\. number\s+([^\.]+)\.', pi)
    if m:
        return m.group(1).strip()
    m = re.search(r'publication number\s+([^\.]+)\.', pi)
    if m:
        return m.group(1).strip()
    return None

rows = []
for r in recs:
    pi = r.get('Patents_info','')
    assignee = parse_assignee(pi)
    pub = get_pub_number(pi)
    if assignee and 'UNIV CALIFORNIA' in assignee and pub:
        try:
            cpcs = json.loads(r.get('cpc') or '[]')
        except Exception:
            cpcs = []
        primary = [c.get('code') for c in cpcs if c.get('first') is True and c.get('code')]
        rows.append({'uc_pub': pub, 'primary_cpc': sorted(set(primary))})

uc_df = pd.DataFrame(rows)
uc_pubs = sorted(set(uc_df['uc_pub'].dropna().tolist()))

conds = []
for p in uc_pubs:
    conds.append("citation LIKE '%\\\"publication_number\\\": \\\"" + p + "\\\"%'")

out = {
    'uc_pubs': uc_pubs,
    'like_conds': conds,
    'uc_primary_map': uc_df.to_dict(orient='records')
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zc5HgAxzGMRhjjDkMxCFFf7e': ['publicationinfo'], 'var_call_8pOE0QFIbOJR0Dr8EUeOedwr': ['cpc_definition'], 'var_call_LLUMGJgH1Ae4i7xDhL2BBZjU': 'file_storage/call_LLUMGJgH1Ae4i7xDhL2BBZjU.json'}

exec(code, env_args)
