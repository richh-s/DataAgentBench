code = """import json
import pandas as pd

packageinfo = pd.read_json(locals()['var_function-call-16653849855473276997'])

def check_license_and_release(row):
    licenses = json.loads(row['Licenses'])
    version_info = json.loads(row['VersionInfo'])
    is_mit = False
    for license_item in licenses:
        if license_item == 'MIT':
            is_mit = True
            break
    is_release = version_info.get('IsRelease', False)
    return is_mit and is_release

filtered_packages = packageinfo[packageinfo.apply(check_license_and_release, axis=1)]

# Select relevant columns for the next join
result = filtered_packages[['System', 'Name', 'Version']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-16653849855473276997': 'file_storage/function-call-16653849855473276997.json'}

exec(code, env_args)
