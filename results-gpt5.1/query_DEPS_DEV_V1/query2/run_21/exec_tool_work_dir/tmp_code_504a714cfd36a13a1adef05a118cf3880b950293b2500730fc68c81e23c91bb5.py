code = """import json, re, pandas as pd

pkg_path = var_call_2G0LJAX4IXdksHvtje94SLDI
ppv_path = var_call_ybno4wsXGuIsG5p8ObNZkI2Q
pi_path = var_call_G9MuqwUjHEjlINa0aWIDrA0a

with open(pkg_path) as f:
    pkg = json.load(f)
with open(ppv_path) as f:
    ppv = json.load(f)
with open(pi_path) as f:
    pi = json.load(f)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

pkg_df = pkg_df[pkg_df['System']=='NPM']

pkg_df['IsRelease'] = pkg_df['VersionInfo'].apply(lambda x: json.loads(x).get('IsRelease') if pd.notna(x) else False)

pkg_df = pkg_df[pkg_df['IsRelease']]

pkg_df['HasMIT'] = pkg_df['Licenses'].apply(lambda x: 'MIT' in json.loads(x) if pd.notna(x) and x.strip() else False)

pkg_df = pkg_df[pkg_df['HasMIT']]

merged = pkg_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

text = pi_df['Project_Information'].fillna('')

def parse_info(s):
    m = re.search(r'The project (.+?) on GitHub', s)
    if not m:
        m = re.search(r'The project (.+?) is hosted on GitHub', s)
    if not m:
        m = re.search(r'The project is hosted on GitHub under the name ([^,]+)', s)
    if not m:
        m = re.search(r'The GitHub project(?: named)? ([^ ]+/[^ ]+) ', s)
    name = m.group(1) if m else None
    m2 = re.search(r'(?:and )?([0-9,]+) forks', s)
    forks = int(m2.group(1).replace(',','')) if m2 else None
    return pd.Series({'ProjectName': name, 'Forks': forks})

info_parsed = text.apply(parse_info)
pi_parsed = pd.concat([pi_df, info_parsed], axis=1)

final = merged.merge(pi_parsed[['ProjectName','Forks']], on='ProjectName', how='left')

final = final.dropna(subset=['Forks'])

agg = final.groupby('ProjectName', as_index=False)['Forks'].max()

agg = agg.sort_values('Forks', ascending=False).head(5)

result = agg.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_2G0LJAX4IXdksHvtje94SLDI': 'file_storage/call_2G0LJAX4IXdksHvtje94SLDI.json', 'var_call_ybno4wsXGuIsG5p8ObNZkI2Q': 'file_storage/call_ybno4wsXGuIsG5p8ObNZkI2Q.json', 'var_call_G9MuqwUjHEjlINa0aWIDrA0a': 'file_storage/call_G9MuqwUjHEjlINa0aWIDrA0a.json'}

exec(code, env_args)
