code = """import json, re

fp = var_call_pHP5hzDbhcmGTCFpwYdO8dFq
with open(fp, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

reviews = var_call_SLne7bzhPAWEMfT9QKRGLF52

biz_map = {}
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    cats = None
    if 'categories' in b and b.get('categories'):
        cats = b.get('categories')
        if isinstance(cats, str):
            cats = [c.strip() for c in cats.split(',') if c.strip()]
    if not cats:
        cats = []
        if isinstance(desc, str) and desc.strip():
            m = re.search(r"category of ['\"]([^'\"]+)['\"]", desc, flags=re.IGNORECASE)
            if m:
                text = m.group(1)
            else:
                m2 = re.search(r"\bin\b\s*(.+?)(?:\.|$)", desc, flags=re.IGNORECASE)
                if m2:
                    text = m2.group(1)
                else:
                    text = desc
            parts = [p.strip() for p in text.split(',') if p.strip()]
            final_parts = []
            for p in parts:
                low = p.lower()
                if ' and ' in low:
                    subparts = [sp.strip() for sp in low.split(' and ') if sp.strip()]
                    # keep original casing by mapping back to original substrings
                    # simple approach: split original p by ' and ' ignoring case is complex; use lower-case entries
                    final_parts.extend(subparts)
                else:
                    final_parts.append(p.strip())
            cleaned = []
            for p in final_parts:
                p = re.sub(r"^this (facility|establishment) offers .*? in \s*", '', p, flags=re.IGNORECASE)
                p = re.sub(r"^offers a range of services in \s*", '', p, flags=re.IGNORECASE)
                p = re.sub(r"^including \s*", '', p, flags=re.IGNORECASE)
                p = p.strip(" .'\"")
                if p:
                    cleaned.append(p)
            cats = cleaned
    biz_map[bid] = cats

from collections import defaultdict
cat_totals = defaultdict(int)
for r in reviews:
    bref = r.get('business_ref')
    cnt = int(r.get('review_count', 0))
    bid = None
    if isinstance(bref, str) and bref.startswith('businessref_'):
        bid = 'businessid_' + bref.split('_',1)[1]
    else:
        bid = bref
    cats = biz_map.get(bid)
    if not cats:
        continue
    for c in cats:
        cat_totals[c] += cnt

sorted_cats = sorted(cat_totals.items(), key=lambda x: x[1], reverse=True)
top5 = [{'category': c, 'total_reviews': v} for c, v in sorted_cats[:5]]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_lNBTQuzbbyOWzgqvMWBSkSmA': ['checkin', 'business'], 'var_call_jLFzbSKqv30tvPuTxKWItU2E': ['review', 'tip', 'user'], 'var_call_pHP5hzDbhcmGTCFpwYdO8dFq': 'file_storage/call_pHP5hzDbhcmGTCFpwYdO8dFq.json', 'var_call_6mXpNcvG29SAgrDNKZbTKIYx': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_call_SLne7bzhPAWEMfT9QKRGLF52': [{'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}]}

exec(code, env_args)
