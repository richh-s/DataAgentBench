code = """import json
import pandas as pd

with open(locals()['var_function-call-3657157287295125768'], 'r') as f:
    data = json.load(f)

ids = sorted(data['ids'])
df = pd.DataFrame({'id': ids})
df['diff'] = df['id'].diff()

print("__RESULT__:")
print(df['diff'].describe().to_json())"""

env_args = {'var_function-call-16230520417025150586': 'file_storage/function-call-16230520417025150586.json', 'var_function-call-3657157287295125768': 'file_storage/function-call-3657157287295125768.json', 'var_function-call-11380327074732110447': {'min': 13, 'max': 127570, 'count': 6696}, 'var_function-call-7239028984248077893': [{'COUNT(*)': '127600'}]}

exec(code, env_args)
