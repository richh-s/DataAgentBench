code = """import json
from collections import Counter

# Load grouped review counts
counts = var_call_YDx9k0c7r4c4Q9TGlLW8nd07

# Load business documents from file
business_file = var_call_IQySmn2CewEFe5cHygwvyT30
with open(business_file, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# Build mapping from business_id to description
biz_desc = {}
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    biz_desc[bid] = desc

# Simple extractor without regex
def extract_categories(desc):
    if not desc:
        return []
    low = desc.lower()
    tail = desc
    if ' in the category' in low:
        idx = low.find(' in the category')
        tail = desc[idx+len(' in the category'):]
    elif 'categories of' in low:
        idx = low.find('categories of')
        tail = desc[idx+len('categories of'):]
    elif 'in the categories' in low:
        idx = low.find('in the categories')
        tail = desc[idx+len('in the categories'):]
    elif 'offers a range of services in' in low:
        idx = low.find('offers a range of services in')
        tail = desc[idx+len('offers a range of services in'):]
    elif 'offers a diverse range of services in' in low:
        idx = low.find('offers a diverse range of services in')
        tail = desc[idx+len('offers a diverse range of services in'):]
    elif 'offers a range of services including' in low:
        idx = low.find('offers a range of services including')
        tail = desc[idx+len('offers a range of services including'):]
    elif 'offers a diverse range of options' in low:
        idx = low.find('offers a diverse range of options')
        tail = desc[idx+len('offers a diverse range of options'):]
    elif 'offers a range of services' in low:
        idx = low.find('offers a range of services')
        tail = desc[idx+len('offers a range of services'):]
    elif 'offers a diverse range of options ranging from' in low:
        idx = low.find('offers a diverse range of options ranging from')
        tail = desc[idx+len('offers a diverse range of options ranging from'):]
    # split tail by commas and ' and '
    parts = []
    for part in tail.split(','):
        for sub in part.split(' and '):
            tok = sub.strip().strip('.')
            if not tok:
                continue
            # exclude if contains digits or looks like address
            if any(ch.isdigit() for ch in tok):
                continue
            lowtok = tok.lower()
            if any(addr in lowtok for addr in ['located', 'rd', 'ave', 'street', 'blvd', 'pkwy', 'suite', 'ste', 'unit', 'in ']):
                # skip likely address fragments
                continue
            parts.append(tok)
    # fallback: if parts empty, try splitting full desc by commas
    if not parts:
        for part in desc.split(','):
            tok = part.strip().strip('.')
            if not tok:
                continue
            if any(ch.isdigit() for ch in tok):
                continue
            lowtok = tok.lower()
            if any(addr in lowtok for addr in ['located', 'rd', 'ave', 'street', 'blvd', 'pkwy', 'suite', 'ste', 'unit']):
                continue
            parts.append(tok)
    # clean up and limit
    cleaned = []
    for p in parts:
        p2 = ' '.join(p.split())
        if len(p2) > 100:
            continue
        cleaned.append(p2)
    return cleaned[:6]

# Aggregate counts by category
counter = Counter()
for rec in counts:
    bref = rec.get('business_ref')
    if not bref:
        continue
    cnt = int(rec.get('cnt') or 0)
    bid = bref.replace('businessref_', 'businessid_')
    desc = biz_desc.get(bid, '')
    cats = extract_categories(desc)
    if not cats:
        # try to use name field by scanning businesses list for this id
        # but we didn't load names; skip
        continue
    for c in cats:
        counter[c] += cnt

# Prepare top 5
top5 = counter.most_common(5)
result = [{'category': c, 'count': n} for c, n in top5]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_0K7y9JPekg11nekvROTu3R81': ['checkin', 'business'], 'var_call_IsgcxMvIn2EOFHgXpOCmENca': ['review', 'tip', 'user'], 'var_call_IQySmn2CewEFe5cHygwvyT30': 'file_storage/call_IQySmn2CewEFe5cHygwvyT30.json', 'var_call_r3P9cgEuBb9eWLa0xEnKNCHg': [{'business_ref': 'businessref_74', 'date': '2021-07-16 17:24:00'}, {'business_ref': 'businessref_57', 'date': 'September 04, 2017 at 08:57 PM'}, {'business_ref': 'businessref_96', 'date': 'August 06, 2016 at 02:19 AM'}, {'business_ref': 'businessref_45', 'date': 'August 10, 2016 at 04:36 AM'}, {'business_ref': 'businessref_74', 'date': 'April 17, 2016 at 12:00 AM'}, {'business_ref': 'businessref_53', 'date': '25 Nov 2016, 20:04'}, {'business_ref': 'businessref_41', 'date': 'December 12, 2017 at 02:27 AM'}, {'business_ref': 'businessref_96', 'date': '2017-01-06 11:15:06'}, {'business_ref': 'businessref_10', 'date': '2021-11-28 23:56:00'}, {'business_ref': 'businessref_66', 'date': 'November 10, 2021 at 06:40 AM'}, {'business_ref': 'businessref_31', 'date': '24 Jan 2017, 19:28'}, {'business_ref': 'businessref_92', 'date': '2019-11-14 17:06:00'}, {'business_ref': 'businessref_26', 'date': '2018-07-23 06:45:43'}, {'business_ref': 'businessref_98', 'date': '2017-11-17 16:06:00'}, {'business_ref': 'businessref_45', 'date': 'February 06, 2018 at 07:29 PM'}, {'business_ref': 'businessref_45', 'date': 'October 28, 2016 at 03:54 PM'}, {'business_ref': 'businessref_36', 'date': '2018-05-21 17:51:00'}, {'business_ref': 'businessref_14', 'date': 'May 04, 2017 at 11:25 PM'}, {'business_ref': 'businessref_86', 'date': '2019-04-14 23:08:41'}, {'business_ref': 'businessref_57', 'date': 'October 30, 2018 at 01:06 PM'}, {'business_ref': 'businessref_13', 'date': 'August 22, 2021 at 12:11 AM'}, {'business_ref': 'businessref_68', 'date': 'October 14, 2018 at 04:06 PM'}, {'business_ref': 'businessref_36', 'date': '2016-12-02 00:06:00'}, {'business_ref': 'businessref_60', 'date': '2017-03-24 23:59:00'}, {'business_ref': 'businessref_20', 'date': '27 May 2017, 00:50'}, {'business_ref': 'businessref_15', 'date': 'June 20, 2018 at 02:12 PM'}, {'business_ref': 'businessref_62', 'date': '2018-04-01 10:52:37'}, {'business_ref': 'businessref_33', 'date': 'August 18, 2016 at 11:57 AM'}, {'business_ref': 'businessref_37', 'date': '2016-07-24 20:27:00'}, {'business_ref': 'businessref_92', 'date': '30 Dec 2018, 18:49'}, {'business_ref': 'businessref_66', 'date': 'June 21, 2020 at 07:59 PM'}, {'business_ref': 'businessref_33', 'date': 'August 30, 2019 at 06:15 PM'}, {'business_ref': 'businessref_6', 'date': '30 Jun 2017, 04:44'}, {'business_ref': 'businessref_12', 'date': 'October 26, 2017 at 11:10 PM'}, {'business_ref': 'businessref_79', 'date': '30 Oct 2017, 01:27'}, {'business_ref': 'businessref_60', 'date': '2019-05-29 19:46:00'}], 'var_call_YDx9k0c7r4c4Q9TGlLW8nd07': [{'business_ref': 'businessref_13', 'cnt': '1'}, {'business_ref': 'businessref_79', 'cnt': '1'}, {'business_ref': 'businessref_26', 'cnt': '1'}, {'business_ref': 'businessref_68', 'cnt': '1'}, {'business_ref': 'businessref_41', 'cnt': '1'}, {'business_ref': 'businessref_10', 'cnt': '1'}, {'business_ref': 'businessref_45', 'cnt': '3'}, {'business_ref': 'businessref_92', 'cnt': '2'}, {'business_ref': 'businessref_96', 'cnt': '2'}, {'business_ref': 'businessref_98', 'cnt': '1'}, {'business_ref': 'businessref_14', 'cnt': '1'}, {'business_ref': 'businessref_20', 'cnt': '1'}, {'business_ref': 'businessref_6', 'cnt': '1'}, {'business_ref': 'businessref_74', 'cnt': '2'}, {'business_ref': 'businessref_66', 'cnt': '2'}, {'business_ref': 'businessref_15', 'cnt': '1'}, {'business_ref': 'businessref_33', 'cnt': '2'}, {'business_ref': 'businessref_36', 'cnt': '2'}, {'business_ref': 'businessref_60', 'cnt': '2'}, {'business_ref': 'businessref_12', 'cnt': '1'}, {'business_ref': 'businessref_31', 'cnt': '1'}, {'business_ref': 'businessref_53', 'cnt': '1'}, {'business_ref': 'businessref_57', 'cnt': '2'}, {'business_ref': 'businessref_86', 'cnt': '1'}, {'business_ref': 'businessref_62', 'cnt': '1'}, {'business_ref': 'businessref_37', 'cnt': '1'}]}

exec(code, env_args)
