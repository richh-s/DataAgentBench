code = """import json
import re
from collections import Counter

# Load review records from storage
reviews = var_call_r3P9cgEuBb9eWLa0xEnKNCHg

# Load business records from the JSON file path provided
business_file_path = var_call_IQySmn2CewEFe5cHygwvyT30
with open(business_file_path, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# Build a mapping from business_id to description and possible categories field
biz_map = {}
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    cats_field = b.get('categories') if 'categories' in b else None
    biz_map[bid] = {'description': desc, 'categories_field': cats_field}

# Helper to extract categories from a business document
def extract_categories(desc, cats_field):
    # If categories field exists and is a string, try to split it
    cats = []
    if cats_field:
        if isinstance(cats_field, str):
            cats = [c.strip() for c in re.split(r',|;|\|', cats_field) if c.strip()]
            if cats:
                return cats
        elif isinstance(cats_field, list):
            cats = [str(c).strip() for c in cats_field if str(c).strip()]
            if cats:
                return cats
    # Try regex patterns to capture categories portion
    patterns = [
        r'offers a diverse range of services (?:and products )?in (.*)$',
        r'offers a range of services (?:and products )?in (.*)$',
        r'offers a range of services including (.*)$',
        r'offers a diverse range of options (?:ranging from )?(.*)$',
        r'in the category(?:s)? of (.*)$',
        r'categories? of (.*)$',
        r'offers (?:a |the )?range of services (?:in|including) (.*)$',
        r'this .* offers (.*)$',
        r'offers (.*)$'
    ]
    desc_clean = desc.replace('\n', ' ').strip()
    for pat in patterns:
        m = re.search(pat, desc_clean, flags=re.IGNORECASE)
        if m:
            tail = m.group(1)
            # remove trailing location-like phrases after a dash or 'to meet' etc
            tail = re.split(r'(-|to meet|to suit|for all your|\.|$)', tail)[0]
            parts = re.split(r',|;| and | & |/|\|\band\b', tail)
            parts = [p.strip().strip('.') for p in parts if p and p.strip()]
            # filter out tokens that look like addresses or single locations (contain digits or 'Ste' or 'Ave')
            parts = [p for p in parts if not re.search(r'\d', p) and len(p) <= 60]
            if parts:
                return parts
    # Fallback: take last 6 comma-separated tokens from description
    parts = [p.strip().strip('.') for p in desc_clean.split(',') if p.strip()]
    # Filter out tokens that contain digits or look like addresses
    parts = [p for p in parts if not re.search(r'\d', p) and len(p) <= 60]
    # Heuristic: keep tokens that contain at least one space or are capitalized words
    filtered = []
    for p in parts:
        if len(p) <= 2:
            continue
        # remove leading location phrases
        if re.search(r'located at', p, flags=re.IGNORECASE):
            continue
        if p.lower().startswith(('located', 'this', 'offers', 'located at')):
            continue
        filtered.append(p)
    if filtered:
        return filtered
    return []

# Precompute categories for each business
biz_categories = {}
for bid, info in biz_map.items():
    cats = extract_categories(info['description'], info['categories_field'])
    # Normalize categories: title case and strip
    cats_norm = [re.sub(r'\s+', ' ', c).strip() for c in cats]
    biz_categories[bid] = cats_norm

# Count reviews per category
counter = Counter()
missed = 0
for r in reviews:
    bref = r.get('business_ref')
    if not bref:
        continue
    # convert businessref_ to businessid_
    bid = bref.replace('businessref_', 'businessid_')
    cats = biz_categories.get(bid)
    if not cats:
        missed += 1
        continue
    for c in cats:
        counter[c] += 1

# Get top 5 categories
top5 = counter.most_common(5)
result = []
for cat, cnt in top5:
    result.append({'category': cat, 'count': cnt})

# If fewer than 5 results, still return what's available
import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_0K7y9JPekg11nekvROTu3R81': ['checkin', 'business'], 'var_call_IsgcxMvIn2EOFHgXpOCmENca': ['review', 'tip', 'user'], 'var_call_IQySmn2CewEFe5cHygwvyT30': 'file_storage/call_IQySmn2CewEFe5cHygwvyT30.json', 'var_call_r3P9cgEuBb9eWLa0xEnKNCHg': [{'business_ref': 'businessref_74', 'date': '2021-07-16 17:24:00'}, {'business_ref': 'businessref_57', 'date': 'September 04, 2017 at 08:57 PM'}, {'business_ref': 'businessref_96', 'date': 'August 06, 2016 at 02:19 AM'}, {'business_ref': 'businessref_45', 'date': 'August 10, 2016 at 04:36 AM'}, {'business_ref': 'businessref_74', 'date': 'April 17, 2016 at 12:00 AM'}, {'business_ref': 'businessref_53', 'date': '25 Nov 2016, 20:04'}, {'business_ref': 'businessref_41', 'date': 'December 12, 2017 at 02:27 AM'}, {'business_ref': 'businessref_96', 'date': '2017-01-06 11:15:06'}, {'business_ref': 'businessref_10', 'date': '2021-11-28 23:56:00'}, {'business_ref': 'businessref_66', 'date': 'November 10, 2021 at 06:40 AM'}, {'business_ref': 'businessref_31', 'date': '24 Jan 2017, 19:28'}, {'business_ref': 'businessref_92', 'date': '2019-11-14 17:06:00'}, {'business_ref': 'businessref_26', 'date': '2018-07-23 06:45:43'}, {'business_ref': 'businessref_98', 'date': '2017-11-17 16:06:00'}, {'business_ref': 'businessref_45', 'date': 'February 06, 2018 at 07:29 PM'}, {'business_ref': 'businessref_45', 'date': 'October 28, 2016 at 03:54 PM'}, {'business_ref': 'businessref_36', 'date': '2018-05-21 17:51:00'}, {'business_ref': 'businessref_14', 'date': 'May 04, 2017 at 11:25 PM'}, {'business_ref': 'businessref_86', 'date': '2019-04-14 23:08:41'}, {'business_ref': 'businessref_57', 'date': 'October 30, 2018 at 01:06 PM'}, {'business_ref': 'businessref_13', 'date': 'August 22, 2021 at 12:11 AM'}, {'business_ref': 'businessref_68', 'date': 'October 14, 2018 at 04:06 PM'}, {'business_ref': 'businessref_36', 'date': '2016-12-02 00:06:00'}, {'business_ref': 'businessref_60', 'date': '2017-03-24 23:59:00'}, {'business_ref': 'businessref_20', 'date': '27 May 2017, 00:50'}, {'business_ref': 'businessref_15', 'date': 'June 20, 2018 at 02:12 PM'}, {'business_ref': 'businessref_62', 'date': '2018-04-01 10:52:37'}, {'business_ref': 'businessref_33', 'date': 'August 18, 2016 at 11:57 AM'}, {'business_ref': 'businessref_37', 'date': '2016-07-24 20:27:00'}, {'business_ref': 'businessref_92', 'date': '30 Dec 2018, 18:49'}, {'business_ref': 'businessref_66', 'date': 'June 21, 2020 at 07:59 PM'}, {'business_ref': 'businessref_33', 'date': 'August 30, 2019 at 06:15 PM'}, {'business_ref': 'businessref_6', 'date': '30 Jun 2017, 04:44'}, {'business_ref': 'businessref_12', 'date': 'October 26, 2017 at 11:10 PM'}, {'business_ref': 'businessref_79', 'date': '30 Oct 2017, 01:27'}, {'business_ref': 'businessref_60', 'date': '2019-05-29 19:46:00'}]}

exec(code, env_args)
