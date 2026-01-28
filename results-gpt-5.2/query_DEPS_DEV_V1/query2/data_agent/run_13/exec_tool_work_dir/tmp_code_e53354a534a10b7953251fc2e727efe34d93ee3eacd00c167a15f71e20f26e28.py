code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_6g24M9KPCWqY1mkGxJUVFMXz)
proj = load_records(var_call_BUWzNJIwMofeHnGKv2tTN7q8)

df_pkg = pd.DataFrame(pkg)
df_proj = pd.DataFrame(proj)

# filter package license contains MIT and VersionInfo IsRelease true

def is_mit(lic):
    if lic is None:
        return False
    return 'MIT' in str(lic)

def is_release(vi):
    if vi is None:
        return False
    try:
        o = json.loads(vi)
        return bool(o.get('IsRelease'))
    except Exception:
        return '"IsRelease"' in str(vi) and 'true' in str(vi).lower()

f_pkg = df_pkg[df_pkg['Licenses'].apply(is_mit) & df_pkg['VersionInfo'].apply(is_release)].copy()

m = f_pkg.merge(df_proj, on=['System','Name','Version'], how='inner')

def extract_forks(text):
    if text is None:
        return None
    t = str(text)
    m1 = re.search(r"\b(\d+)\s+forks\b", t, flags=re.IGNORECASE)
    if m1:
        return int(m1.group(1))
    m2 = re.search(r"forks?\s+count\s+of\s+(\d+)", t, flags=re.IGNORECASE)
    if m2:
        return int(m2.group(1))
    return None

m['Forks'] = m['Project_Information'].apply(extract_forks)
m = m.dropna(subset=['Forks']).copy()
m['Forks'] = m['Forks'].astype(int)

agg = (m.groupby('ProjectName', as_index=False)
         .agg(Forks=('Forks','max')))

agg = agg.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

lines = [f"{i}. {row.ProjectName} — {int(row.Forks)} forks" for i, row in enumerate(agg.itertuples(index=False), start=1)]
result = "\n".join(lines)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_BUWzNJIwMofeHnGKv2tTN7q8': 'file_storage/call_BUWzNJIwMofeHnGKv2tTN7q8.json', 'var_call_6g24M9KPCWqY1mkGxJUVFMXz': 'file_storage/call_6g24M9KPCWqY1mkGxJUVFMXz.json'}

exec(code, env_args)
