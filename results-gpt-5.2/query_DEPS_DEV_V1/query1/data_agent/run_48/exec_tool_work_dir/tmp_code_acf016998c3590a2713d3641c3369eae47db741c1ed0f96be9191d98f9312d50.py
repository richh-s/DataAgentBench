code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_xZfX8m7juBZAhDpie0ky2Ocv)
ppv = load_records(var_call_nxbRDxJPFe5Fwdy324k8CJAF)
pi = load_records(var_call_ueVh18dNNkRGfxRSZf46z22z)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
# latest release per package name
pkg_latest = (pkg_df.sort_values(['Name','UpstreamPublishedAt','Version'])
                .groupby('Name', as_index=False)
                .tail(1)[['Name','Version']])

# map to github projects for that exact version
ppv_df = ppv_df[['Name','Version','ProjectName']].dropna()
merged = pkg_latest.merge(ppv_df, on=['Name','Version'], how='inner')

# extract stars from Project_Information text
star_re = re.compile(r"([0-9][0-9,]*)\s+stars")
proj_re = re.compile(r"\b([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b")

def parse_info(s):
    if not isinstance(s, str):
        return None, None
    m_proj = proj_re.search(s)
    proj = m_proj.group(1) if m_proj else None
    m_star = star_re.search(s)
    stars = int(m_star.group(1).replace(',','')) if m_star else None
    return proj, stars

pi_df[['ProjectName','Stars']] = pi_df['Project_Information'].apply(lambda x: pd.Series(parse_info(x)))
pi_df = pi_df.dropna(subset=['ProjectName'])
pi_df['Stars'] = pd.to_numeric(pi_df['Stars'], errors='coerce')

merged2 = merged.merge(pi_df[['ProjectName','Stars']], on='ProjectName', how='left')
merged2 = merged2.dropna(subset=['Stars'])

# If multiple projects per package version, take max stars
agg = (merged2.groupby(['Name','Version'], as_index=False)
              .agg(Stars=('Stars','max')))

top5 = agg.sort_values(['Stars','Name'], ascending=[False, True]).head(5)
result_lines = [f"{row.Name} {row.Version} — {int(row.Stars)} stars" for row in top5.itertuples(index=False)]
answer = "\n".join(result_lines)
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_xZfX8m7juBZAhDpie0ky2Ocv': 'file_storage/call_xZfX8m7juBZAhDpie0ky2Ocv.json', 'var_call_nxbRDxJPFe5Fwdy324k8CJAF': 'file_storage/call_nxbRDxJPFe5Fwdy324k8CJAF.json', 'var_call_ueVh18dNNkRGfxRSZf46z22z': 'file_storage/call_ueVh18dNNkRGfxRSZf46z22z.json'}

exec(code, env_args)
