code = """import json
from collections import Counter

with open(var_call_SAZGzLxLXbN199MGBjTmNm1v, 'r') as f:
    businesses = json.load(f)

# collect keys
keys = Counter()
sample_docs = []
for i, doc in enumerate(businesses[:20]):
    keys.update(doc.keys())
    sample_docs.append({k: doc.get(k) for k in doc.keys()})

# check how many have 'categories'
has_categories = sum(1 for doc in businesses if 'categories' in doc and doc.get('categories') not in (None, 'None', ''))
# check other possible fields: 'category', 'categories_parsed'
possible = ['categories', 'categoriesList', 'category', 'Category']
counts = {p: sum(1 for doc in businesses if p in doc and doc.get(p) not in (None, 'None', '')) for p in possible}

result = {
    'total_documents': len(businesses),
    'most_common_keys': keys.most_common(20),
    'has_categories_count': has_categories,
    'possible_fields_counts': counts,
    'sample_first_5': sample_docs[:5]
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_PfBFEnOqSxBmE3yZz4jDYeYE': ['business', 'checkin'], 'var_call_NjmNYE8FrhRYoKqDZPZ3zDE6': ['review', 'tip', 'user'], 'var_call_SAZGzLxLXbN199MGBjTmNm1v': 'file_storage/call_SAZGzLxLXbN199MGBjTmNm1v.json', 'var_call_y40HEuxeyQN0L9Kcca7Zn9Up': 'file_storage/call_y40HEuxeyQN0L9Kcca7Zn9Up.json', 'var_call_OYr07TAIM4tYqxzrmcLlah9K': {'category': None, 'business_count': 0, 'average_rating': None}}

exec(code, env_args)
