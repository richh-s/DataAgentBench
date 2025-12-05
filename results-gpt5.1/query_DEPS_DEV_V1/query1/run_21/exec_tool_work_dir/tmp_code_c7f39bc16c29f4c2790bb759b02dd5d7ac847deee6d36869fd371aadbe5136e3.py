code = """import json, pandas as pd

# load latest npm versions
with open(var_call_QEsbgcpKn2CCdjWCs828IMQO, 'r') as f:
    latest = json.load(f)

# load project_packageversion
with open(var_call_nWhvTYFpwcHiYioJgyJkMQ8z, 'r') as f:
    ppv = json.load(f)

# load project_info
with open(var_call_DpBXW2rASLOALH5RaT3lJ2ZY, 'r') as f:
    pinfo = json.load(f)

latest_df = pd.DataFrame(latest)
ppv_df = pd.DataFrame(ppv)
pinfo_df = pd.DataFrame(pinfo)

# join latest releases with project_packageversion on System, Name, Version
merged = latest_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

# extract repo name from Project_Information text using simple parsing
# assume format contains "The project <repo>" or "The project <repo> on GitHub"
import re

def extract_repo(text):
    m = re.search(r"The project ([^ ]+/[^ ]+)", text)
    if m:
        return m.group(1)
    m = re.search(r"named ([^ ]+/[^ ]+)", text)
    if m:
        return m.group(1)
    m = re.search(r"repository named ([^ ]+/[^ ]+)", text)
    if m:
        return m.group(1)
    return None

# also extract stars count
def extract_stars(text):
    m = re.search(r"(\d[\d,]*) stars", text)
    if m:
        return int(m.group(1).replace(',', ''))
    return None

pinfo_df['Repo'] = pinfo_df['Project_Information'].apply(extract_repo)
pinfo_df['Stars'] = pinfo_df['Project_Information'].apply(extract_stars)

# join merged with pinfo_df on repo name: ProjectName == Repo
final = merged.merge(pinfo_df[['Repo','Stars']], left_on='ProjectName', right_on='Repo', how='left')

# for each package name, pick max stars (some packages may map to multiple repos/versions etc.)
agg = final.groupby(['Name','Version'], as_index=False)['Stars'].max()

# get top 5 by stars
agg['Stars'] = agg['Stars'].fillna(0)
 top5 = agg.sort_values('Stars', ascending=False).head(5)

result = top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jjj8X2PBEdMvJqjdKtB1SLHz': 'file_storage/call_jjj8X2PBEdMvJqjdKtB1SLHz.json', 'var_call_fIlM10O9K2O4WChXcOhhBjv9': ['project_info', 'project_packageversion'], 'var_call_QEsbgcpKn2CCdjWCs828IMQO': 'file_storage/call_QEsbgcpKn2CCdjWCs828IMQO.json', 'var_call_nWhvTYFpwcHiYioJgyJkMQ8z': 'file_storage/call_nWhvTYFpwcHiYioJgyJkMQ8z.json', 'var_call_NNPkkxYdAzfrwDejybi4SB1N': ['project_info', 'project_packageversion'], 'var_call_m8wwFi5LPNp3ln8NYpnYH9on': [{'cid': '0', 'name': 'Project_Information', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'Licenses', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'Description', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'Homepage', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'OSSFuzz', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_call_DpBXW2rASLOALH5RaT3lJ2ZY': 'file_storage/call_DpBXW2rASLOALH5RaT3lJ2ZY.json'}

exec(code, env_args)
