code = """import json, re, pandas as pd
from pathlib import Path

# load merged latest-release packages with project names
file_merge = Path(var_call_jLwbd8HHHeGUnGyQxvR6gtWu)
merged = json.loads(file_merge.read_text())
df_merge = pd.DataFrame(merged)

# load all project_info rows
file_info = Path(var_call_53oZId9tM2Z5deue1airObyi)
info = json.loads(file_info.read_text())
df_info = pd.DataFrame(info)

# extract repo name and stars from Project_Information using regex
repo_re = re.compile(r"project ([^ ]+/[^ ]+)", re.IGNORECASE)
stars_re = re.compile(r"(\d+) stars")

def parse_info(text):
    repo = None
    m = repo_re.search(text)
    if m:
        repo = m.group(1)
    m2 = stars_re.search(text)
    stars = int(m2.group(1)) if m2 else None
    return repo, stars

parsed = df_info['Project_Information'].apply(parse_info)
df_info['ProjectName'] = parsed.apply(lambda x: x[0])
df_info['Stars'] = parsed.apply(lambda x: x[1])

# drop rows without repo or stars
df_info = df_info.dropna(subset=['ProjectName','Stars'])

# join on ProjectName
df = df_merge.merge(df_info[['ProjectName','Stars']], on='ProjectName', how='inner')

# for each package Name, keep one row (they should already be single latest version) and sort by Stars desc
# but there can be multiple projects per package; keep max stars
agg = df.groupby(['Name','Version'], as_index=False)['Stars'].max()

# top 5 by Stars
top5 = agg.sort_values('Stars', ascending=False).head(5)

result = top5.to_dict(orient='records')

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_4oyI9xuUANUktpGYGKXBOECD': 'file_storage/call_4oyI9xuUANUktpGYGKXBOECD.json', 'var_call_YJfHpRk4tzC33Fei8Tj15eFr': 'file_storage/call_YJfHpRk4tzC33Fei8Tj15eFr.json', 'var_call_jLwbd8HHHeGUnGyQxvR6gtWu': 'file_storage/call_jLwbd8HHHeGUnGyQxvR6gtWu.json', 'var_call_53oZId9tM2Z5deue1airObyi': 'file_storage/call_53oZId9tM2Z5deue1airObyi.json'}

exec(code, env_args)
