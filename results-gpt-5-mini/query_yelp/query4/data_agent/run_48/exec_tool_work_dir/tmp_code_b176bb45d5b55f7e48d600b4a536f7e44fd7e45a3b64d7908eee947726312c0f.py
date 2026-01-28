code = """import json

path = var_call_A9JencJUo1qHNPTfBWZ42ph7
with open(path, 'r') as f:
    data = json.load(f)

# collect business_id and description samples
samples = []
for doc in data:
    samples.append({'business_id': doc.get('business_id'), 'description': doc.get('description')})

print('__RESULT__:')
print(json.dumps(samples))"""

env_args = {'var_call_NeumhbNtYh7RIqIMjxGLdY3e': ['checkin', 'business'], 'var_call_yJeK0J3aYKtbIkDeETPJZWaP': ['review', 'tip', 'user'], 'var_call_5kJVrgXIvN0Edazsc7HFYBgI': 'file_storage/call_5kJVrgXIvN0Edazsc7HFYBgI.json', 'var_call_QYZaFbgIPmrqZ0Z5w0n7PI7g': 'file_storage/call_QYZaFbgIPmrqZ0Z5w0n7PI7g.json', 'var_call_YjJC0VopQuMgq5f2rYcJ7a7n': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_5lJRX3ne1c6ql1kvUOPQTGXF': [], 'var_call_A9JencJUo1qHNPTfBWZ42ph7': 'file_storage/call_A9JencJUo1qHNPTfBWZ42ph7.json', 'var_call_uxwhrrGVHMrvMk4un5Qes1Eh': {'category': None, 'business_count': 0, 'average_rating': None}}

exec(code, env_args)
