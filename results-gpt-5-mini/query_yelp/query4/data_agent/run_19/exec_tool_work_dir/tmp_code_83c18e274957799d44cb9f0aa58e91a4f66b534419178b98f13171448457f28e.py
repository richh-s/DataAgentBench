code = """import json, os
bvar = var_call_q48RY1T7FvRnav9ZALijmUUy
if isinstance(bvar, str) and os.path.exists(bvar):
    with open(bvar, 'r', encoding='utf-8') as f:
        businesses = json.load(f)
else:
    businesses = bvar

# analyze
from collections import Counter
key_counter = Counter()
accepting_examples = []
accepting_with_categories = 0
total = len(businesses)
for b in businesses:
    for k in b.keys():
        key_counter[k]+=1
    attrs = b.get('attributes')
    accepts = False
    if isinstance(attrs, dict):
        v = attrs.get('BusinessAcceptsCreditCards')
        if v is True or (isinstance(v, str) and v.lower().strip()== 'true'):
            accepts = True
    if accepts:
        accepting_examples.append(b)
        if b.get('categories'):
            accepting_with_categories += 1

# collect distinct categories values among all businesses
cats_values = Counter()
for b in businesses:
    c = b.get('categories')
    if c is not None:
        cats_values[str(c)] += 1

out = {
    'total_business_docs': total,
    'keys_counts_sample': dict(key_counter.most_common(20)),
    'accepting_credit_cards_count': len(accepting_examples),
    'accepting_with_categories_count': accepting_with_categories,
    'distinct_categories_values_sample_count': len(cats_values),
    'categories_values_examples': list(dict(cats_values.most_common(10)).keys()),
    'first_accepting_business_examples': accepting_examples[:5]
}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_kO5syuL1LsUQnhXBy0rFpI3f': ['business', 'checkin'], 'var_call_jXQ5r6YvxcGSGqRI5ZzOM04h': ['review', 'tip', 'user'], 'var_call_q48RY1T7FvRnav9ZALijmUUy': 'file_storage/call_q48RY1T7FvRnav9ZALijmUUy.json', 'var_call_dzON48RfddMU1hmCaWPTf0kE': 'file_storage/call_dzON48RfddMU1hmCaWPTf0kE.json', 'var_call_SLdv0tyszDKAaXTSmGyc1oyf': {'category': None, 'business_count': 0, 'average_rating': None}}

exec(code, env_args)
