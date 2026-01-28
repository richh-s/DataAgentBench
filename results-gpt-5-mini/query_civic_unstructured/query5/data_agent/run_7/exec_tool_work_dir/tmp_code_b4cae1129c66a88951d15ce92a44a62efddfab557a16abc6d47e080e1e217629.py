code = """import json
try:
    # Check available variables
    vars_list = [k for k in globals().keys() if k.startswith('var_call_')]
    result = {'vars': vars_list}
except Exception as e:
    result = {'error': str(e)}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_xHNly7z1Fzv5N8jwdK3mtrAL': ['civic_docs'], 'var_call_jRI4KvDQihFoo9gBTqySXjRT': ['Funding'], 'var_call_q7R3xqp8WG9IOZBRlFr8pyIy': 'file_storage/call_q7R3xqp8WG9IOZBRlFr8pyIy.json', 'var_call_QzBZclHwTrrUNkhyo5VjgzV8': 'file_storage/call_QzBZclHwTrrUNkhyo5VjgzV8.json'}

exec(code, env_args)
