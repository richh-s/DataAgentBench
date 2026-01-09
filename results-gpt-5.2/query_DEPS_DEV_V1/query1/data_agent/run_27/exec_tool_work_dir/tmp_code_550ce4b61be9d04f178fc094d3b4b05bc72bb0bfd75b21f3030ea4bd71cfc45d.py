code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_lsAnOvZvNdkvbgGUBvyPwnYR)
ppv = load_records(var_call_tCywGkYeZ4X71gVWwshF9IFT)
pi = load_records(var_call_NLyRLQSbpKKP31ds5Y0ZWSIA)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

# latest release per package: VersionInfo.IsRelease == true, max Ordinal then tie by UpstreamPublishedAt

def parse_isrelease(s):
    try:
        obj = json.loads(s)
        return bool(obj.get('IsRelease', False)), obj.get('Ordinal', None)
    except Exception:
        return False, None

ir_ord = pkg_df['VersionInfo'].apply(parse_isrelease)
pkg_df['IsRelease'] = ir_ord.apply(lambda x: x[0])
pkg_df['Ordinal'] = ir_ord.apply(lambda x: x[1] if x[1] is not None else -1)
pkg_df['UpstreamPublishedAt_num'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')

rel = pkg_df[pkg_df['IsRelease'] == True].copy()
rel['Ordinal'] = pd.to_numeric(rel['Ordinal'], errors='coerce').fillna(-1)

rel = rel.sort_values(['Name','Ordinal','UpstreamPublishedAt_num','Version'], ascending=[True, False, False, False])
latest = rel.drop_duplicates(subset=['Name'], keep='first')[['System','Name','Version']]

# Map to github projects
m = latest.merge(ppv_df, on=['System','Name','Version'], how='inner')
# if multiple repos per package+version, keep all; later take max stars

# parse stars from Project_Information
star_re = re.compile(r"(\\d[\\d,]*)\\s+stars")
proj_re = re.compile(r"project\s+([^\s]+/[^\s]+)")

def parse_pi(text):
    if not isinstance(text, str):
        return None, None
    pr = proj_re.search(text)
    project = pr.group(1).strip('.,') if pr else None
    sr = star_re.search(text)
    stars = int(sr.group(1).replace(',','')) if sr else None
    return project, stars

parsed = pi_df['Project_Information'].apply(parse_pi)
pi_df['ProjectName'] = parsed.apply(lambda x: x[0])
pi_df['Stars'] = parsed.apply(lambda x: x[1])
pi_df = pi_df.dropna(subset=['ProjectName'])[['ProjectName','Stars']]

m2 = m.merge(pi_df, on='ProjectName', how='left')

# Aggregate: for each package pick max stars across its repos
agg = (m2.groupby(['Name','Version'], as_index=False)
         .agg(Stars=('Stars','max')))
agg = agg.dropna(subset=['Stars'])
agg = agg.sort_values(['Stars','Name'], ascending=[False, True]).head(5)

result = agg.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_lsAnOvZvNdkvbgGUBvyPwnYR': 'file_storage/call_lsAnOvZvNdkvbgGUBvyPwnYR.json', 'var_call_tCywGkYeZ4X71gVWwshF9IFT': 'file_storage/call_tCywGkYeZ4X71gVWwshF9IFT.json', 'var_call_NLyRLQSbpKKP31ds5Y0ZWSIA': 'file_storage/call_NLyRLQSbpKKP31ds5Y0ZWSIA.json'}

exec(code, env_args)
