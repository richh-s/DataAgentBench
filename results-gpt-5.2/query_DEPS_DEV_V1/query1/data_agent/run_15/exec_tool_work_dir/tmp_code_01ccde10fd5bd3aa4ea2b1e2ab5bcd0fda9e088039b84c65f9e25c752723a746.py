code = """import json, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = pd.DataFrame(load_records(var_call_gtaQo2P6ajdntw498a9RP2Di))
ppv = pd.DataFrame(load_records(var_call_RmOJzOIWztJVA9SbhMArfZXI))
pi = pd.DataFrame(load_records(var_call_yXTo0MRz99rYjTCpGq8QR0cV))

pkg['UpstreamPublishedAt'] = pd.to_numeric(pkg['UpstreamPublishedAt'], errors='coerce')
pkg = pkg.dropna(subset=['UpstreamPublishedAt'])

pkg_latest = pkg.sort_values(['Name','UpstreamPublishedAt']).groupby('Name', as_index=False).tail(1)

ppv = ppv[['System','Name','Version','ProjectName']].dropna()
latest_with_proj = pkg_latest.merge(ppv, on=['Name','Version'], how='inner')

info = pi.copy()
info['ProjectName'] = info['Project_Information'].str.extract(r'project\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)')
info['Stars'] = info['Project_Information'].str.extract(r'([0-9][0-9,]*)\s+stars')[0]
info['Stars'] = pd.to_numeric(info['Stars'].astype(str).str.replace(',', '', regex=False), errors='coerce')
info = info.dropna(subset=['ProjectName','Stars'])[['ProjectName','Stars']]

merged = latest_with_proj.merge(info, on='ProjectName', how='inner')
agg = merged.groupby(['Name','Version'], as_index=False).agg(Stars=('Stars','max'), ProjectName=('ProjectName','first'))

top5 = agg.sort_values(['Stars','Name'], ascending=[False, True]).head(5)

lines = []
for _, r in top5.iterrows():
    lines.append('{}@{} — {} stars (GitHub: {})'.format(r['Name'], r['Version'], int(r['Stars']), r['ProjectName']))

out = "\n".join(lines)
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_gtaQo2P6ajdntw498a9RP2Di': 'file_storage/call_gtaQo2P6ajdntw498a9RP2Di.json', 'var_call_RmOJzOIWztJVA9SbhMArfZXI': 'file_storage/call_RmOJzOIWztJVA9SbhMArfZXI.json', 'var_call_yXTo0MRz99rYjTCpGq8QR0cV': 'file_storage/call_yXTo0MRz99rYjTCpGq8QR0cV.json'}

exec(code, env_args)
