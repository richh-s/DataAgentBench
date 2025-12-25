code = """import json
path = var_call_3adUP0VsqHUvmn8L3fh5QuCd
with open(path, 'r') as f:
    union_query = json.load(f)
print("__RESULT__:")
print(json.dumps(union_query))"""

env_args = {'var_call_wqklihAasrBKRuoWyy8oUS7J': 'file_storage/call_wqklihAasrBKRuoWyy8oUS7J.json', 'var_call_OsjvFxMov1crpVghIc8litG0': 'file_storage/call_OsjvFxMov1crpVghIc8litG0.json', 'var_call_j9IsO58A2IOQawvk4SsZtfHH': 'file_storage/call_j9IsO58A2IOQawvk4SsZtfHH.json', 'var_call_2aeL0LJVfvfpaVKAGBUrgufy': 'file_storage/call_2aeL0LJVfvfpaVKAGBUrgufy.json', 'var_call_f0tZYwaaJXmBTZbZRBoXwb1q': 'file_storage/call_f0tZYwaaJXmBTZbZRBoXwb1q.json', 'var_call_3adUP0VsqHUvmn8L3fh5QuCd': 'file_storage/call_3adUP0VsqHUvmn8L3fh5QuCd.json'}

exec(code, env_args)
