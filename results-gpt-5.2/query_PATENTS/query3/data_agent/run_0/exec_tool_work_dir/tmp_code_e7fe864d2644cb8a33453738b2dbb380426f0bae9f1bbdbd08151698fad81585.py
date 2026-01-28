code = """import json, re, pandas as pd
from pathlib import Path

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json') and Path(maybe_path).exists():
        return json.loads(Path(maybe_path).read_text())
    return maybe_path

recs = load_records(var_call_LLUMGJgH1Ae4i7xDhL2BBZjU)

def parse_assignee(pi:str):
    if not pi:
        return None
    # common patterns: 'owned by X', 'assigned to X', 'holds the' ...
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

def get_pub_number(pi:str):
    m = re.search(r'pub\. number\s+([^\.]+)\.', pi)
    if m:
        return m.group(1).strip()
    m = re.search(r'publication number\s+([^\.]+)\.', pi)
    if m:
        return m.group(1).strip()
    return None

rows=[]
for r in recs:
    assignee = parse_assignee(r.get('Patents_info',''))
    pub = get_pub_number(r.get('Patents_info',''))
    if assignee and 'UNIV CALIFORNIA' in assignee:
        try:
            cpcs = json.loads(r.get('cpc') or '[]')
        except Exception:
            cpcs = []
        primary = [c.get('code') for c in cpcs if c.get('first') is True]
        primary = [p for p in primary if p]
        rows.append({'uc_pub': pub, 'primary_cpc': sorted(set(primary))})

uc_df = pd.DataFrame(rows).dropna(subset=['uc_pub'])
uc_pub_set = set(uc_df['uc_pub'])

# now query all publications whose citation list includes any UC pub
# SQLite LIKE scan on citation field per UC pub; chunked OR conditions
uc_pubs = sorted(list(uc_pub_set))

conds=[]
for p in uc_pubs:
    # citation is JSON-like with publication_number values containing e.g., "US-xxxx"
    conds.append(f"citation LIKE '%\"publication_number\": \\\"{p}\\\"%'")

# Return for downstream querying: list of conditions and uc_df mapping
out = {
    'uc_pubs': uc_pubs,
    'like_conds': conds,
    'uc_primary_map': uc_df.to_dict(orient='records')
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zc5HgAxzGMRhjjDkMxCFFf7e': ['publicationinfo'], 'var_call_8pOE0QFIbOJR0Dr8EUeOedwr': ['cpc_definition'], 'var_call_LLUMGJgH1Ae4i7xDhL2BBZjU': 'file_storage/call_LLUMGJgH1Ae4i7xDhL2BBZjU.json'}

exec(code, env_args)
