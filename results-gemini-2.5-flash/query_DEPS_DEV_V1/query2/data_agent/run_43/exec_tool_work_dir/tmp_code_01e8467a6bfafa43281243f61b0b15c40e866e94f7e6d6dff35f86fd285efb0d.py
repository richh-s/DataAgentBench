code = """import json
import pandas as pd

packageinfo = pd.read_json(locals()['var_function-call-16763418198789656899'])

def check_license_and_release(row):
    try:
        licenses = json.loads(row["Licenses"])
        version_info = json.loads(row["VersionInfo"])
        is_release = version_info.get("IsRelease", False)
        return "MIT" in licenses and is_release
    except (json.JSONDecodeError, TypeError):
        return False

filtered_packages = packageinfo[packageinfo.apply(check_license_and_release, axis=1)]

print("__RESULT__:")
print(filtered_packages.to_json(orient='records'))"""

env_args = {'var_function-call-16763418198789656899': 'file_storage/function-call-16763418198789656899.json'}

exec(code, env_args)
