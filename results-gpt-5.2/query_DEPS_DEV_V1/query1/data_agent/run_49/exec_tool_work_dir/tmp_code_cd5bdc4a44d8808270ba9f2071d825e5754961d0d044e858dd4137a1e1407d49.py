code = """import json, re, pandas as pd
from pathlib import Path

def load_records(v):
    if isinstance(v, str) and v.endswith('.json') and Path(v).exists():
        return json.load(open(v, 'r', encoding='utf-8'))
    return v

pkg = load_records(var_call_DghBgWcCDhre1hoV1p49KMjK)
ppv = load_records(var_call_s41evPq6WIqyzFlKKtlRYKnm)
pi = load_records(var_call_HabFRHm0pS4Fl7y7LiFkNeiw)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# latest release versions per package based on VersionInfo.IsRelease == true and max UpstreamPublishedAt

def is_release(vinfo):
    try:
        obj = json.loads(vinfo)
        return bool(obj.get('IsRelease'))
    except Exception:
        return False

pkg_df['IsRelease'] = pkg_df['VersionInfo'].map(is_release)
# UpstreamPublishedAt seems microseconds; keep numeric
pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')

rel_df = pkg_df[pkg_df['IsRelease'] & pkg_df['UpstreamPublishedAt'].notna()].copy()
# choose latest per Name
rel_df.sort_values(['Name','UpstreamPublishedAt','Version'], ascending=[True, False, False], inplace=True)
latest_rel = rel_df.drop_duplicates(subset=['Name'], keep='first')[['Name','Version']]
latest_rel['System'] = 'NPM'

# join to github project mapping (exact version match)
merged = latest_rel.merge(ppv_df, on=['System','Name','Version'], how='inner')
# extract stars from Project_Information and also ProjectName

def parse_project_info(text):
    if not isinstance(text, str):
        return None, None
    m = re.search(r'project\s+([^\s]+/[^\s]+)', text)
    project = m.group(1).strip('.,') if m else None
    ms = re.search(r'(?:has garnered|has received|currently has|has)\s+(?:an?\s+open issues count of\s+\d+,\s+)?(?:a\s+total\s+of\s+)?(\d{1,3}(?:,\d{3})*)\s+stars', text)
    # alternative phrasing: "with ... 2,534 stars" etc
    if not ms:
        ms = re.search(r'\b(\d{1,3}(?:,\d{3})*)\s+stars\b', text)
    stars = int(ms.group(1).replace(',','')) if ms else None
    return project, stars

pi_df[['ProjectName','Stars']] = pi_df['Project_Information'].apply(lambda t: pd.Series(parse_project_info(t)))
pi_df = pi_df[pi_df['ProjectName'].notna()]
pi_df = pi_df.drop_duplicates(subset=['ProjectName'], keep='first')

merged2 = merged.merge(pi_df[['ProjectName','Stars']], on='ProjectName', how='left')
merged2 = merged2[merged2['Stars'].notna()].copy()

# Some packages may map to multiple repos; take max stars
agg = merged2.groupby(['Name','Version'], as_index=False)['Stars'].max()
agg.sort_values(['Stars','Name'], ascending=[False, True], inplace=True)

top5 = agg.head(5)
result = top5.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_DghBgWcCDhre1hoV1p49KMjK': 'file_storage/call_DghBgWcCDhre1hoV1p49KMjK.json', 'var_call_s41evPq6WIqyzFlKKtlRYKnm': 'file_storage/call_s41evPq6WIqyzFlKKtlRYKnm.json', 'var_call_HabFRHm0pS4Fl7y7LiFkNeiw': 'file_storage/call_HabFRHm0pS4Fl7y7LiFkNeiw.json'}

exec(code, env_args)
