code = """print('Testing variable access')
print('Available keys:', list(locals().keys()))

# Try to access specific keys
target_keys = [k for k in locals().keys() if 'query_db' in str(k)]
print('Query DB keys:', target_keys)

# Show first few keys with their types
for k in list(locals().keys())[:5]:
    val = locals()[k]
    print(f"{k}: {type(val)} = {str(val)[:50]}...")

# Set a result for testing
result = {"status": "test_complete"}"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}]}

exec(code, env_args)
