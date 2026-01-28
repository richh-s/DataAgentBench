code = """import json
import pandas as pd

# Variables from storage:
# var_call_Vk4VyxLAc8EPrTa7kgCfyPRl -> path to large business JSON file
# var_call_DTk1oC6BV5ts3meFkBy6QZdi -> SQL query result list

business_file = var_call_Vk4VyxLAc8EPrTa7kgCfyPRl
sql_results = var_call_DTk1oC6BV5ts3meFkBy6QZdi

# Load business documents from the JSON file
with open(business_file, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# Index businesses by business_id for quick lookup
biz_by_id = {b.get('business_id'): b for b in businesses}

# Helper to extract categories from a business doc
import re

def extract_categories(biz):
    # Try explicit 'categories' field first
    cats = biz.get('categories') if isinstance(biz, dict) else None
    if cats:
        if isinstance(cats, list):
            return [c.strip() for c in cats if c]
        if isinstance(cats, str):
            return [c.strip() for c in cats.split(',') if c.strip()]
    # Fallback to description parsing
    desc = biz.get('description') if isinstance(biz, dict) else None
    if not desc or not isinstance(desc, str):
        return []
    s = desc
    # Try several regex patterns to capture the category list
    patterns = [r'offers? a range of services in (.+)',
                r'offers? a wide range of services, including (.+)',
                r'offers? a wide range of services in (.+)',
                r'offers? .* in (.+)',
                r'in the category of (.+)',
                r'categories?: (.+)']
    match = None
    for p in patterns:
        m = re.search(p, s, flags=re.IGNORECASE)
        if m:
            match = m.group(1)
            break
    if not match:
        # try to find the first occurrence of capitalized list after location
        # split on 'this ' and take remainder
        parts = re.split(r'Located at .*?\,?\s*this\s+', s, flags=re.IGNORECASE)
        if len(parts) > 1:
            match = parts[1]
        else:
            # last resort: use full description
            match = s
    # Clean match: stop at first sentence end
    match = match.split('.')[0]
    # Replace 'and' with commas for splitting, also '/'
    match = re.sub(r'\band\b', ',', match, flags=re.IGNORECASE)
    match = match.replace('/', ',')
    # Split by commas
    parts = [p.strip() for p in match.split(',') if p.strip()]
    # Further clean parts by removing trailing phrases like 'to meet all your travel and transportation needs' etc.
    cleaned = []
    for p in parts:
        # remove leading verbs/phrases
        p = re.sub(r"offers? a range of services in", "", p, flags=re.IGNORECASE)
        p = re.sub(r"making it.*", "", p, flags=re.IGNORECASE)
        p = p.strip(' .')
        if p:
            cleaned.append(p)
    return cleaned

# Aggregate review counts per category
from collections import defaultdict
cat_counts = defaultdict(int)

for row in sql_results:
    bid = row.get('business_id')
    try:
        cnt = int(row.get('reviews_from_2016_users_since_2016') or 0)
    except:
        cnt = 0
    biz = biz_by_id.get(bid)
    if not biz:
        continue
    cats = extract_categories(biz)
    if not cats:
        # if no categories found, attribute to 'Unknown'
        cat_counts['Unknown'] += cnt
    else:
        for c in cats:
            cat_counts[c] += cnt

# Prepare sorted top 5
sorted_cats = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
top5 = sorted_cats[:5]

# Convert to list of dicts
result = [{"category": c, "review_count": v} for c, v in top5]

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YrE2sVNNDkDY1ESOY1Ir6u5r': ['checkin', 'business'], 'var_call_V3UgJROpNL7NVgzFzHvThUg7': ['review', 'tip', 'user'], 'var_call_Vk4VyxLAc8EPrTa7kgCfyPRl': 'file_storage/call_Vk4VyxLAc8EPrTa7kgCfyPRl.json', 'var_call_DTk1oC6BV5ts3meFkBy6QZdi': [{'business_id': 'businessid_45', 'reviews_from_2016_users_since_2016': '3'}, {'business_id': 'businessid_60', 'reviews_from_2016_users_since_2016': '2'}, {'business_id': 'businessid_96', 'reviews_from_2016_users_since_2016': '2'}, {'business_id': 'businessid_74', 'reviews_from_2016_users_since_2016': '2'}, {'business_id': 'businessid_66', 'reviews_from_2016_users_since_2016': '2'}, {'business_id': 'businessid_33', 'reviews_from_2016_users_since_2016': '2'}, {'business_id': 'businessid_92', 'reviews_from_2016_users_since_2016': '2'}, {'business_id': 'businessid_57', 'reviews_from_2016_users_since_2016': '2'}, {'business_id': 'businessid_36', 'reviews_from_2016_users_since_2016': '2'}, {'business_id': 'businessid_26', 'reviews_from_2016_users_since_2016': '1'}, {'business_id': 'businessid_62', 'reviews_from_2016_users_since_2016': '1'}, {'business_id': 'businessid_20', 'reviews_from_2016_users_since_2016': '1'}, {'business_id': 'businessid_79', 'reviews_from_2016_users_since_2016': '1'}, {'business_id': 'businessid_14', 'reviews_from_2016_users_since_2016': '1'}, {'business_id': 'businessid_31', 'reviews_from_2016_users_since_2016': '1'}, {'business_id': 'businessid_13', 'reviews_from_2016_users_since_2016': '1'}, {'business_id': 'businessid_86', 'reviews_from_2016_users_since_2016': '1'}, {'business_id': 'businessid_37', 'reviews_from_2016_users_since_2016': '1'}, {'business_id': 'businessid_53', 'reviews_from_2016_users_since_2016': '1'}, {'business_id': 'businessid_98', 'reviews_from_2016_users_since_2016': '1'}, {'business_id': 'businessid_15', 'reviews_from_2016_users_since_2016': '1'}, {'business_id': 'businessid_10', 'reviews_from_2016_users_since_2016': '1'}, {'business_id': 'businessid_68', 'reviews_from_2016_users_since_2016': '1'}, {'business_id': 'businessid_12', 'reviews_from_2016_users_since_2016': '1'}, {'business_id': 'businessid_6', 'reviews_from_2016_users_since_2016': '1'}, {'business_id': 'businessid_41', 'reviews_from_2016_users_since_2016': '1'}]}

exec(code, env_args)
