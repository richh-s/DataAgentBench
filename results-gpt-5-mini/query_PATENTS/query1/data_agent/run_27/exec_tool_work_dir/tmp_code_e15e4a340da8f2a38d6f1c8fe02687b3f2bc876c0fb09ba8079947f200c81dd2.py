code = """import json
print("__RESULT__:")
print(json.dumps({'a': var_call_hhze6RW5Hrd7TvkcPLkzfc5S, 'b': var_call_OgklCS1GfZ5AQf9iW6lgvq6w}))"""

env_args = {'var_call_hhze6RW5Hrd7TvkcPLkzfc5S': 'file_storage/call_hhze6RW5Hrd7TvkcPLkzfc5S.json', 'var_call_OgklCS1GfZ5AQf9iW6lgvq6w': 'file_storage/call_OgklCS1GfZ5AQf9iW6lgvq6w.json'}

exec(code, env_args)
