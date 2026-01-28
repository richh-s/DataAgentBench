code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

pkg = load_records(var_call_3m97wNj3g9Tlg0iI8J6uh9Sj)
ppv = load_records(var_call_RrHlFOGiwW9wQ211KgUC4uao)
pi = load_records(var_call_ShNXjAyIbgDoMMm5y2fYcdJF)

df_pkg = pd.DataFrame(pkg)[['System','Name','Version']].drop_duplicates()
df_ppv = pd.DataFrame(ppv)[['System','Name','Version','ProjectName']].drop_duplicates()

j = df_pkg.merge(df_ppv, on=['System','Name','Version'], how='inner')
projects = set(j['ProjectName'].dropna().unique().tolist())

pat = re.compile(r"project\s+(?:is hosted on GitHub under the name\s+|named\s+|)\s*([^\s]+/[^\s,]+).*?(\d[\d,]*)\s+forks", re.IGNORECASE)

rows=[]
for rec in pi:
    txt = rec.get('Project_Information') or ''
    m = pat.search(txt)
    if not m:
        continue
    pname = m.group(1).strip().rstrip('.').rstrip(',')
    if pname not in projects:
        continue
    forks = int(m.group(2).replace(',',''))
    rows.append({'ProjectName': pname, 'Forks': forks})

df = pd.DataFrame(rows)
if df.empty:
    out=[]
else:
    df = df.groupby('ProjectName', as_index=False)['Forks'].max()
    df = df.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)
    out = df.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_3m97wNj3g9Tlg0iI8J6uh9Sj': 'file_storage/call_3m97wNj3g9Tlg0iI8J6uh9Sj.json', 'var_call_RrHlFOGiwW9wQ211KgUC4uao': 'file_storage/call_RrHlFOGiwW9wQ211KgUC4uao.json', 'var_call_ShNXjAyIbgDoMMm5y2fYcdJF': 'file_storage/call_ShNXjAyIbgDoMMm5y2fYcdJF.json', 'var_call_uTnLTPDiVgzOQ1DxYMwd9kTe': [], 'var_call_OvsypVOveoC8TUVJwWVT8HMm': {'ppv_projects': 8059, 'matched': 488, 'sample_matches': [['lberrocal/npm-packages-template', 0], ['leaflet/leaflet', 5782], ['leaflet/leaflet.fullscreen', 118], ['leandrowd/react-responsive-carousel', 636], ['ledgerproject/keypairoom', 0], ['leebyron/jasmine-check', 3], ['leecade/react-native-swiper', 2392], ['lekoarts/gatsby-themes', 568], ['lenconda/dollie', 3], ['leo-ran/easy-node-reflect', 0], ['leofelix077/bunchofnothing', 0], ['leoilab/react-native-analytics-segment-io', 36], ['leoroese/template-cli', 13], ['levelkdev/dxswap-sdk', 11], ['leviticusmb/divine-amd-loader', 0], ['leviticusmb/divine-synchronization', 0], ['leviticusmb/esxx-2', 0], ['libertydsnp/activity-content', 0], ['libertydsnp/parquetjs', 13], ['libertydsnp/sdk-ts', 2]]}}

exec(code, env_args)
