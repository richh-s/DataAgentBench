code = """import json
from collections import defaultdict

business_file = var_call_KtKiT0Ihn7XbBKhltcRL89fC
with open(business_file, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

reviews_per_business = var_call_GVD5X3CHVSQoYi8Fb6SeyNGz

biz_cat = {}

def clean_cat(s):
    s = s.strip()
    s = s.rstrip('. ')
    return s

for b in businesses:
    bid = b.get('business_id')
    cats = []
    if 'categories' in b and b.get('categories'):
        c = b.get('categories')
        if isinstance(c, list):
            cats = [clean_cat(str(x)) for x in c]
        else:
            cats = [clean_cat(x) for x in str(c).split(',') if x.strip()]
    if not cats and 'description' in b and b.get('description'):
        desc = b.get('description').replace('\n', ' ')
        lo = desc.lower()
        idx = lo.find('offers')
        if idx != -1:
            candidate = desc[idx + len('offers'):]
        else:
            # try after the second comma
            parts = desc.split(',')
            if len(parts) > 2:
                candidate = ','.join(parts[2:])
            else:
                candidate = desc
        candidate = candidate.split('.')[0]
        candidate = candidate.replace(' and ', ',')
        # split by comma or slash
        raw = []
        for part in candidate.split(','):
            for sub in part.split('/'):
                raw.append(sub)
        cats = []
        for rc in raw:
            rc = rc.strip()
            if not rc:
                continue
            # remove leading phrases
            low = rc.lower()
            if low.startswith('a range of services in'):
                rc = rc[len('a range of services in'):]
            if low.startswith('including'):
                rc = rc[len('including'):]
            rc = clean_cat(rc)
            if rc:
                cats.append(rc)
    final = []
    for c in cats:
        # split on '&'
        parts = [clean_cat(x) for x in c.split('&') if x.strip()]
        final.extend(parts)
    seen = set()
    out = []
    for c in final:
        if c and c not in seen:
            seen.add(c)
            out.append(c)
    if out:
        biz_cat[bid] = out

cat_counts = defaultdict(int)
for rec in reviews_per_business:
    bref = rec.get('business_ref')
    try:
        rc = int(rec.get('review_count'))
    except:
        rc = 0
    bid = None
    if isinstance(bref, str) and bref.startswith('businessref_'):
        bid = 'businessid_' + bref.split('_', 1)[1]
    else:
        bid = bref
    cats = biz_cat.get(bid)
    if not cats:
        continue
    for c in cats:
        cat_counts[c] += rc

sorted_cats = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
top5 = [{'category': k, 'total_reviews_from_2016_users': v} for k, v in sorted_cats[:5]]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_P65b3Ebh5RGjST8CC3Qa8RlV': ['business', 'checkin'], 'var_call_s4IXnZ3il1F6TSw32HiFhRYB': ['review', 'tip', 'user'], 'var_call_KtKiT0Ihn7XbBKhltcRL89fC': 'file_storage/call_KtKiT0Ihn7XbBKhltcRL89fC.json', 'var_call_LqHtbfyUfFa1y7ZszRlV9kuj': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_call_GVD5X3CHVSQoYi8Fb6SeyNGz': [{'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}]}

exec(code, env_args)
