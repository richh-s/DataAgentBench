code = """import pandas as pd
import json

with open(locals()['var_function-call-7743465443656875948'], 'r') as f:
    package_releases = json.load(f)

df = pd.DataFrame(package_releases)

def parse_version_info(version_info_str):
    try:
        info = json.loads(version_info_str)
        return info.get('IsRelease', False), info.get('Ordinal', -1)
    except json.JSONDecodeError:
        return False, -1

df[['IsRelease', 'Ordinal']] = df['VersionInfo'].apply(lambda x: pd.Series(parse_version_info(x)))

latest_releases = df[df['IsRelease'] == True].loc[df.groupby('Name')['Ordinal'].idxmax()]

print("__RESULT__:")
print(latest_releases.to_json(orient='records'))"""

env_args = {'var_function-call-7743465443656875948': 'file_storage/function-call-7743465443656875948.json'}

exec(code, env_args)
