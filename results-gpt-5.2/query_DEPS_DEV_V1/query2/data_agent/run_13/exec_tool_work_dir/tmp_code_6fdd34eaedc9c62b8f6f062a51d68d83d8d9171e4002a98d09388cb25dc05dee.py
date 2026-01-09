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
    s = str(lic)
    return 'MIT' in s

def is_release(vi):
    if vi is None:
        return False
    try:
        o = json.loads(vi)
        return bool(o.get('IsRelease'))
    except Exception:
        return '"IsRelease"' in str(vi) and 'true' in str(vi).lower()

f_pkg = df_pkg[df_pkg['Licenses'].apply(is_mit) & df_pkg['VersionInfo'].apply(is_release)].copy()

# join on System,Name,Version
m = f_pkg.merge(df_proj, on=['System','Name','Version'], how='inner')

# extract forks from Project_Information
fork_re = re.compile(r"forks?\s+count\s+of\s+(\d+)|(?:and\s+)(\d+)\s+forks?\b|has\s+(\d+)\s+forks?\b", re.IGNORECASE)

def extract_forks(text):
    if text is None:
        return None
    t = str(text)
    # common pattern: '..., X stars, and Y forks.'
    m = re.search(r"\b(\d+)\s+forks\b", t, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    m2 = re.search(r"forks?\s+count\s+of\s+(\d+)", t, flags=re.IGNORECASE)
    if m2:
        return int(m2.group(1))
    return None

m['Forks'] = m['Project_Information'].apply(extract_forks)
m = m.dropna(subset=['Forks'])
m['Forks'] = m['Forks'].astype(int)

# For each project, take max forks (same) and also retain a representative package name
agg = (m.groupby('ProjectName', as_index=False)
         .agg(Forks=('Forks','max'), Packages=('Name', lambda x: sorted(set(x))[:5])))

agg = agg.sort_values(['Forks','ProjectName'], ascending=[False, True]).head(5)

lines = []
for i, r in enumerate(agg.itertuples(index=False), start=1):
    lines.append(f"{i}. {r.ProjectName} — {r.Forks} forks")

result = "\n".join(lines)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_BUWzNJIwMofeHnGKv2tTN7q8': 'file_storage/call_BUWzNJIwMofeHnGKv2tTN7q8.json', 'var_call_6g24M9KPCWqY1mkGxJUVFMXz': 'file_storage/call_6g24M9KPCWqY1mkGxJUVFMXz.json'}

exec(code, env_args)
