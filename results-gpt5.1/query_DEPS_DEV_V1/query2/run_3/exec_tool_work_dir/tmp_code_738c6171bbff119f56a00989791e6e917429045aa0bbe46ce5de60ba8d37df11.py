code = """import json, pandas as pd

pkg_file = var_call_tuzyC6ONetjDYkHIjZO2yZHO
map_file = var_call_F3hisBLmADJa3yIxKYKztLkt
info_file = var_call_dMvO3SNTezyLaOK8UqS6wCz5

pkg_df = pd.read_json(pkg_file)
map_df = pd.read_json(map_file)
info_df = pd.read_json(info_file)

merged = pkg_df.merge(map_df, on=['System','Name','Version'], how='inner')

project_names = set(merged['ProjectName'].unique())

rows = []
for _, row in info_df.iterrows():
    text = row['Project_Information']
    if 'The project ' in text and ' on GitHub' in text:
        try:
            middle = text.split('The project ')[1].split(' on GitHub')[0]
            project = middle.strip()
        except Exception:
            continue
    elif 'The project is hosted on GitHub under the name ' in text:
        middle = text.split('The project is hosted on GitHub under the name ')[1].split(',')[0]
        project = middle.strip()
    elif 'The project is a GitHub repository named ' in text:
        middle = text.split('The project is a GitHub repository named ')[1].split(',')[0]
        project = middle.strip()
    elif 'The GitHub project ' in text and ' currently has' in text:
        middle = text.split('The GitHub project ')[1].split(' currently has')[0]
        project = middle.strip()
    elif 'The GitHub project named ' in text and ' currently has' in text:
        middle = text.split('The GitHub project named ')[1].split(' currently has')[0]
        project = middle.strip()
    elif 'The project is hosted on GITHUB and' in text and 'currently has' in text:
        middle = text.split('The project ')[1].split(' is hosted')[0]
        project = middle.strip()
    else:
        continue

    if project not in project_names:
        continue

    forks = None
    if 'forks count of ' in text:
        try:
            forks_part = text.split('forks count of ')[1].split('.')[0]
            forks = int(forks_part.replace(',','').strip())
        except Exception:
            pass
    if forks is None and ' and ' in text and ' forks' in text:
        try:
            before = text.split(' forks')[0]
            num = before.split(' and ')[-1]
            forks = int(num.replace(',','').strip())
        except Exception:
            pass
    if forks is None:
        continue

    rows.append({'ProjectName': project, 'Forks': forks})

if not rows:
    result = []
else:
    df = pd.DataFrame(rows).drop_duplicates(subset=['ProjectName'])
    df = df.sort_values('Forks', ascending=False).head(5)
    result = df.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_tuzyC6ONetjDYkHIjZO2yZHO': 'file_storage/call_tuzyC6ONetjDYkHIjZO2yZHO.json', 'var_call_F3hisBLmADJa3yIxKYKztLkt': 'file_storage/call_F3hisBLmADJa3yIxKYKztLkt.json', 'var_call_dMvO3SNTezyLaOK8UqS6wCz5': 'file_storage/call_dMvO3SNTezyLaOK8UqS6wCz5.json'}

exec(code, env_args)
