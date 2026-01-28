code = """import json
from collections import Counter
import re

# Load review records
reviews = var_call_r3P9cgEuBb9eWLa0xEnKNCHg

# Load business records from provided file path
business_file_path = var_call_IQySmn2CewEFe5cHygwvyT30
with open(business_file_path, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# Build mapping
biz_map = {}
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    cats_field = b.get('categories') if 'categories' in b else None
    biz_map[bid] = {'description': desc, 'categories_field': cats_field}

# Simple category extractor
def extract_categories(desc, cats_field):
    if cats_field:
        if isinstance(cats_field, str):
            parts = re.split(',|;|\||\/', cats_field)
            parts = [p.strip() for p in parts if p.strip()]
            if parts:
                return parts
        if isinstance(cats_field, list):
            parts = [str(p).strip() for p in cats_field if str(p).strip()]
            if parts:
                return parts
    low = desc.lower()
    keywords = [
        'offers a diverse range of services in',
        'offers a range of services in',
        'offers a range of services including',
        'offers a diverse range of options ranging from',
        'in the category of',
        'categories of',
        'in the category',
        'in the categories',
        'in the category of',
        'in the category',
        'in the categories of',
        "in the category's",
        'in the category',
        'in the category',
        'in the category of',
        'in ',
        'including '
    ]
    for kw in keywords:
        idx = low.find(kw)
        if idx != -1:
            start = idx + len(kw)
            tail = desc[start:]
            # cut at sentence end
            tail = re.split(r'\.| to meet| to suit| making it| perfect for| to ', tail, maxsplit=1)[0]
            parts = re.split(',|;| and | & |/|\\|\n', tail)
            parts = [p.strip().strip('.') for p in parts if p and p.strip()]
            # filter tokens with digits or addresses
            parts = [p for p in parts if not re.search(r'\d', p) and len(p) <= 80]
            if parts:
                return parts
    # fallback: split by commas and filter
    parts = [p.strip().strip('.') for p in desc.split(',') if p.strip()]
    parts = [p for p in parts if not re.search(r'\d', p) and len(p) <= 80]
    return parts[:8]

# Precompute categories
biz_categories = {}
for bid, info in biz_map.items():
    cats = extract_categories(info['description'], info['categories_field'])
    # normalize
    cats_norm = []
    for c in cats:
        c2 = re.sub('\s+', ' ', c).strip()
        if c2:
            # remove leading articles
            if c2.lower().startswith('the '):
                c2 = c2[4:]
            cats_norm.append(c2)
    biz_categories[bid] = cats_norm

# Count reviews per category
counter = Counter()
for r in reviews:
    bref = r.get('business_ref')
    if not bref:
        continue
    bid = bref.replace('businessref_', 'businessid_')
    cats = biz_categories.get(bid, [])
    if not cats:
        continue
    for c in cats:
        counter[c] += 1

# Top 5
top5 = counter.most_common(5)
result = [{'category': c, 'count': n} for c, n in top5]

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_0K7y9JPekg11nekvROTu3R81': ['checkin', 'business'], 'var_call_IsgcxMvIn2EOFHgXpOCmENca': ['review', 'tip', 'user'], 'var_call_IQySmn2CewEFe5cHygwvyT30': 'file_storage/call_IQySmn2CewEFe5cHygwvyT30.json', 'var_call_r3P9cgEuBb9eWLa0xEnKNCHg': [{'business_ref': 'businessref_74', 'date': '2021-07-16 17:24:00'}, {'business_ref': 'businessref_57', 'date': 'September 04, 2017 at 08:57 PM'}, {'business_ref': 'businessref_96', 'date': 'August 06, 2016 at 02:19 AM'}, {'business_ref': 'businessref_45', 'date': 'August 10, 2016 at 04:36 AM'}, {'business_ref': 'businessref_74', 'date': 'April 17, 2016 at 12:00 AM'}, {'business_ref': 'businessref_53', 'date': '25 Nov 2016, 20:04'}, {'business_ref': 'businessref_41', 'date': 'December 12, 2017 at 02:27 AM'}, {'business_ref': 'businessref_96', 'date': '2017-01-06 11:15:06'}, {'business_ref': 'businessref_10', 'date': '2021-11-28 23:56:00'}, {'business_ref': 'businessref_66', 'date': 'November 10, 2021 at 06:40 AM'}, {'business_ref': 'businessref_31', 'date': '24 Jan 2017, 19:28'}, {'business_ref': 'businessref_92', 'date': '2019-11-14 17:06:00'}, {'business_ref': 'businessref_26', 'date': '2018-07-23 06:45:43'}, {'business_ref': 'businessref_98', 'date': '2017-11-17 16:06:00'}, {'business_ref': 'businessref_45', 'date': 'February 06, 2018 at 07:29 PM'}, {'business_ref': 'businessref_45', 'date': 'October 28, 2016 at 03:54 PM'}, {'business_ref': 'businessref_36', 'date': '2018-05-21 17:51:00'}, {'business_ref': 'businessref_14', 'date': 'May 04, 2017 at 11:25 PM'}, {'business_ref': 'businessref_86', 'date': '2019-04-14 23:08:41'}, {'business_ref': 'businessref_57', 'date': 'October 30, 2018 at 01:06 PM'}, {'business_ref': 'businessref_13', 'date': 'August 22, 2021 at 12:11 AM'}, {'business_ref': 'businessref_68', 'date': 'October 14, 2018 at 04:06 PM'}, {'business_ref': 'businessref_36', 'date': '2016-12-02 00:06:00'}, {'business_ref': 'businessref_60', 'date': '2017-03-24 23:59:00'}, {'business_ref': 'businessref_20', 'date': '27 May 2017, 00:50'}, {'business_ref': 'businessref_15', 'date': 'June 20, 2018 at 02:12 PM'}, {'business_ref': 'businessref_62', 'date': '2018-04-01 10:52:37'}, {'business_ref': 'businessref_33', 'date': 'August 18, 2016 at 11:57 AM'}, {'business_ref': 'businessref_37', 'date': '2016-07-24 20:27:00'}, {'business_ref': 'businessref_92', 'date': '30 Dec 2018, 18:49'}, {'business_ref': 'businessref_66', 'date': 'June 21, 2020 at 07:59 PM'}, {'business_ref': 'businessref_33', 'date': 'August 30, 2019 at 06:15 PM'}, {'business_ref': 'businessref_6', 'date': '30 Jun 2017, 04:44'}, {'business_ref': 'businessref_12', 'date': 'October 26, 2017 at 11:10 PM'}, {'business_ref': 'businessref_79', 'date': '30 Oct 2017, 01:27'}, {'business_ref': 'businessref_60', 'date': '2019-05-29 19:46:00'}]}

exec(code, env_args)
