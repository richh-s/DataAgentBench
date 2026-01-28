code = """import json
from collections import defaultdict

# Load data from storage file paths provided by previous tool calls
with open(var_call_7oXHbp7Wt1huh37rUPVR1WE5, 'r') as f:
    businesses = json.load(f)
with open(var_call_kAnS6MmOjvKHyymYKR3mmpXQ, 'r') as f:
    reviews = json.load(f)

# Helper to determine if a business accepts credit cards
def accepts_credit(attrs):
    if attrs is None:
        return False
    # sometimes stored as dict
    if isinstance(attrs, dict):
        val = attrs.get('BusinessAcceptsCreditCards')
        if isinstance(val, bool):
            return val
        if isinstance(val, str):
            return val.lower() == 'true'
        return False
    # sometimes stored as string representation
    if isinstance(attrs, str):
        s = attrs.lower()
        # look for patterns indicating acceptance
        if "businessacceptscreditcards" in s and "true" in s:
            return True
        return False
    return False

# Build mapping of business_id -> set(categories)
biz_categories = {}
for b in businesses:
    bid = b.get('business_id')
    cats = b.get('categories')
    if cats is None:
        # maybe categories field missing; set empty
        biz_categories[bid] = set()
        continue
    # categories may be a string of comma-separated values
    if isinstance(cats, list):
        cat_list = cats
    else:
        # split by comma
        cat_list = [c.strip() for c in str(cats).split(',') if c.strip()]
    biz_categories[bid] = set(cat_list)

# Determine businesses that accept credit cards
accepting_biz_ids = set()
for b in businesses:
    bid = b.get('business_id')
    attrs = b.get('attributes')
    if accepts_credit(attrs):
        accepting_biz_ids.add(bid)

# Count businesses per category (count unique business ids)
cat_to_biz = defaultdict(set)
for bid in accepting_biz_ids:
    cats = biz_categories.get(bid, set())
    for c in cats:
        cat_to_biz[c].add(bid)

# Remove empty category key if present
if '' in cat_to_biz:
    del cat_to_biz['']

# Find top category by number of businesses
top_category = None
top_count = 0
for c, bizs in cat_to_biz.items():
    cnt = len(bizs)
    if cnt > top_count or (cnt == top_count and (top_category is None or c < top_category)):
        top_category = c
        top_count = cnt

# Compute average rating for reviews of businesses in top_category
avg_rating = None
if top_category is not None and top_count > 0:
    target_biz_ids = cat_to_biz[top_category]
    # Map reviews business_ref to business_id format
    ratings = []
    for r in reviews:
        bref = r.get('business_ref')
        if not bref:
            continue
        # convert businessref_# to businessid_#
        bid = bref.replace('businessref_', 'businessid_')
        if bid in target_biz_ids:
            try:
                ratings.append(float(r.get('rating')))
            except:
                pass
    if ratings:
        avg_rating = sum(ratings)/len(ratings)
        avg_rating = round(avg_rating, 2)

result = {
    'category': top_category,
    'business_count': top_count,
    'average_rating': avg_rating
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_tQod4WpsZZ0iGs8eN9r24z3L': ['business', 'checkin'], 'var_call_HXyX9Uhr94AH0xmlZr2p5i88': ['review', 'tip', 'user'], 'var_call_7oXHbp7Wt1huh37rUPVR1WE5': 'file_storage/call_7oXHbp7Wt1huh37rUPVR1WE5.json', 'var_call_kAnS6MmOjvKHyymYKR3mmpXQ': 'file_storage/call_kAnS6MmOjvKHyymYKR3mmpXQ.json'}

exec(code, env_args)
