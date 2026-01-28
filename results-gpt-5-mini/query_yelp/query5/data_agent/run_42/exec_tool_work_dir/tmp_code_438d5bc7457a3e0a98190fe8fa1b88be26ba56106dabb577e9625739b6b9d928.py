code = """import json
r = var_call_PS57I3jmpPoGhQZFKymDxqFB
avg = None
if r and isinstance(r, list) and 'avg_rating' in r[0]:
    try:
        avg = float(r[0]['avg_rating'])
    except:
        avg = None
result = {"state": "PA", "business_count": 8, "average_rating": round(avg, 4) if avg is not None else None}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_XOSA9iI13kq2EaWHXmzBEWGB': 'file_storage/call_XOSA9iI13kq2EaWHXmzBEWGB.json', 'var_call_58SQ1aCDoYUKxXyStY325R9R': {'top_state': 'PA', 'business_count': 8, 'business_refs': ['businessref_89', 'businessref_97', 'businessref_67', 'businessref_77', 'businessref_86', 'businessref_40', 'businessref_44', 'businessref_82']}, 'var_call_PS57I3jmpPoGhQZFKymDxqFB': [{'avg_rating': '3.4839857651245554'}]}

exec(code, env_args)
