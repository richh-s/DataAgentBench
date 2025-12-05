code = """import json, re, pandas as pd
from pathlib import Path

pkg_path = Path(var_call_jMcjHKzmPR90vtIjSCduMF9j)
proj_pkg_path = Path(var_call_0JT6wu7QGcR2COsoEXpyjn87)
proj_info_path = Path(var_call_qdw4fdUOuaEEyIRTxdfHOM1Z)

packageinfo = json.loads(pkg_path.read_text())
project_packageversion = json.loads(proj_pkg_path.read_text())
project_info = json.loads(proj_info_path.read_text())

pkg_df = pd.DataFrame(packageinfo)[['System','Name','Version']]
proj_pkg_df = pd.DataFrame(project_packageversion)
proj_info_df = pd.DataFrame(project_info)

pkg_df = pkg_df[pkg_df['System']=='NPM']
proj_pkg_df = proj_pkg_df[proj_pkg_df['System']=='NPM']

# Determine latest version per (System, Name) in proj_pkg_df directly (since those are the ones that map to projects)
latest = proj_pkg_df.sort_values('Version').groupby(['System','Name'], as_index=False).tail(1)

# Extract stars and project names from project_info
import numpy as np

def extract_stars(text):
    if not isinstance(text, str):
        return np.nan
    m = re.search(r'(?:has|with).*?(\d[\d,]*) stars', text)
    if not m:
        m = re.search(r'stars count of (\d[\d,]*)', text)
    if not m:
        return np.nan
    return int(m.group(1).replace(',',''))

proj_info_df['Stars'] = proj_info_df['Project_Information'].apply(extract_stars)


def extract_project_name(text):
    if not isinstance(text, str):
        return None
    m = re.search(r'project ([^\s,]+/[^\s,]+)', text)
    if m:
        return m.group(1)
    m = re.search(r'named ([^\s,]+/[^\s,]+)', text)
    if m:
        return m.group(1)
    return None

proj_info_df['ProjectName'] = proj_info_df['Project_Information'].apply(extract_project_name)

# Join latest with proj_info via ProjectName
full = latest.merge(proj_info_df[['ProjectName','Stars']], on='ProjectName', how='left')

agg = full.groupby(['System','Name','Version'], as_index=False)['Stars'].max()

agg = agg[agg['Stars'].notnull()].sort_values('Stars', ascending=False).head(5)

result = agg.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jMcjHKzmPR90vtIjSCduMF9j': 'file_storage/call_jMcjHKzmPR90vtIjSCduMF9j.json', 'var_call_0JT6wu7QGcR2COsoEXpyjn87': 'file_storage/call_0JT6wu7QGcR2COsoEXpyjn87.json', 'var_call_qdw4fdUOuaEEyIRTxdfHOM1Z': 'file_storage/call_qdw4fdUOuaEEyIRTxdfHOM1Z.json', 'var_call_A0LOq6kHInIcilqFXNLMWQQ8': {'proj_pkg_cols': ['System', 'Name', 'Version', 'ProjectType', 'ProjectName', 'RelationProvenance', 'RelationType']}, 'var_call_ICWPWab07ccSnRY6gIwmZoTd': {'sample': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectType': 'GITHUB', 'ProjectName': 'dataminingsupply/dms-io', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectType': 'GITHUB', 'ProjectName': 'isacvale/fc', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.16', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}, {'System': 'NPM', 'Name': '@djie/ws', 'Version': '1.0.8', 'ProjectType': 'GITHUB', 'ProjectName': 'laihaojie/jie', 'RelationProvenance': 'UNVERIFIED_METADATA', 'RelationType': 'SOURCE_REPO_TYPE'}], 'columns': ['System', 'Name', 'Version', 'ProjectType', 'ProjectName', 'RelationProvenance', 'RelationType']}}

exec(code, env_args)
