code = """import json
from collections import Counter
with open(var_call_7oXHbp7Wt1huh37rUPVR1WE5, 'r') as f:
    businesses = json.load(f)

def accepts_credit(attrs):
    if attrs is None:
        return False
    if isinstance(attrs, dict):
        val = attrs.get('BusinessAcceptsCreditCards')
        if isinstance(val, bool):
            return val
        if isinstance(val, str):
            return val.lower() == 'true'
        return False
    if isinstance(attrs, str):
        s = attrs.lower()
        if 'businessacceptscreditcards' in s and 'true' in s:
            return True
        return False
    return False

total = len(businesses)
count_accept = 0
count_categories = 0
cat_counter = Counter()
missing_cats_examples = []
for b in businesses:
    bid = b.get('business_id')
    attrs = b.get('attributes')
    cats = b.get('categories')
    if cats is not None and cats != 'None' and str(cats).strip()!='':
        count_categories += 1
    else:
        if len(missing_cats_examples) < 5:
            missing_cats_examples.append({'business_id': bid, 'name': b.get('name'), 'attributes': attrs})
    if accepts_credit(attrs):
        count_accept += 1
        # parse categories
        if cats is None or cats == 'None':
            continue
        if isinstance(cats, list):
            cat_list = cats
        else:
            cat_list = [c.strip() for c in str(cats).split(',') if c.strip()]
        for c in cat_list:
            cat_counter[c] += 1

most_common = cat_counter.most_common(10)
res = {
    'total_businesses': total,
    'businesses_accepting_credit_cards': count_accept,
    'businesses_with_categories_field': count_categories,
    'top_categories_among_credit_accepting': most_common,
    'examples_missing_categories': missing_cats_examples
}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_tQod4WpsZZ0iGs8eN9r24z3L': ['business', 'checkin'], 'var_call_HXyX9Uhr94AH0xmlZr2p5i88': ['review', 'tip', 'user'], 'var_call_7oXHbp7Wt1huh37rUPVR1WE5': 'file_storage/call_7oXHbp7Wt1huh37rUPVR1WE5.json', 'var_call_kAnS6MmOjvKHyymYKR3mmpXQ': 'file_storage/call_kAnS6MmOjvKHyymYKR3mmpXQ.json', 'var_call_XXnr7iNttN1XqWuaXcJOZkaW': {'category': None, 'business_count': 0, 'average_rating': None}}

exec(code, env_args)
