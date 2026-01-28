code = """import json
p = var_call_KABRrtqNUlTcXdQMb8MB38mC
with open(p, 'r') as f:
    docs = json.load(f)
# inspect keys of first doc and count presence of 'categories' and 'description'
keys = set()
for d in docs[:10]:
    keys.update(d.keys())
count_with_categories = sum(1 for d in docs if 'categories' in d and d.get('categories'))
sample_categories = [d.get('categories') for d in docs if 'categories' in d and d.get('categories')][:10]
count_with_description = sum(1 for d in docs if 'description' in d and d.get('description'))
sample_descriptions = [d.get('description') for d in docs if 'description' in d and d.get('description')][:5]
res = {
    'first_keys': sorted(list(keys)),
    'count_with_categories': count_with_categories,
    'sample_categories': sample_categories,
    'count_with_description': count_with_description,
    'sample_descriptions': sample_descriptions,
    'total_docs': len(docs)
}
print('__RESULT__:')
import json
print(json.dumps(res))"""

env_args = {'var_call_7ZgO1JmiFzKIX0XDrSGqVpq3': ['checkin', 'business'], 'var_call_tn6yro8Bzk11NeQZGFUQjmNo': ['review', 'tip', 'user'], 'var_call_KABRrtqNUlTcXdQMb8MB38mC': 'file_storage/call_KABRrtqNUlTcXdQMb8MB38mC.json', 'var_call_ZcHJViISDWvVgJ1fdfMMnt95': {'top_category': None, 'top_count': 0, 'business_ids': [], 'business_refs': []}, 'var_call_UO8D11S4FDoOd36hCh8GDjr6': 'file_storage/call_UO8D11S4FDoOd36hCh8GDjr6.json', 'var_call_B4Q9naiPeGPBCP1R7GbTugi8': {'top_category': None, 'top_count': 0, 'business_ids': [], 'business_refs': []}, 'var_call_zwQw6gZD6zpdzHflOeRTPcxK': []}

exec(code, env_args)
