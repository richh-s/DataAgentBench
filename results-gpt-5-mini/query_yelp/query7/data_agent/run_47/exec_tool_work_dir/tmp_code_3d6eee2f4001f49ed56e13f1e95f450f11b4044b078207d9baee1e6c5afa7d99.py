code = """import json, re
# var_call_25Q5yWaPNMHMV4WiMMiIFZ9a is the file path to the full business query result
businesses = json.load(open(var_call_25Q5yWaPNMHMV4WiMMiIFZ9a, 'r'))
reviews = var_call_4dA3LWOTd46Mu4L1FXPSqm1W

# Build mapping from businessid (businessid_X) to review count (int)
business_review_counts = {}
for r in reviews:
    br = r.get('business_ref')
    rc = int(r.get('review_count') or 0)
    if not br:
        continue
    bid = br.replace('businessref_', 'businessid_')
    business_review_counts[bid] = business_review_counts.get(bid, 0) + rc

# Build mapping from businessid to categories list
biz_categories = {}
for b in businesses:
    bid = b.get('business_id')
    if not bid:
        continue
    cats = []
    if 'categories' in b and b.get('categories'):
        c = b.get('categories')
        if isinstance(c, list):
            cats = [str(x).strip() for x in c if x]
        else:
            # assume comma-separated string
            cats = [x.strip() for x in str(c).split(',') if x.strip()]
    elif 'description' in b and b.get('description'):
        desc = b.get('description')
        # try to find a categories substring using patterns
        m = re.search(r"(?:services in|range of services in|category of|in the category of|in the category of|in the category|in the category of the|in the categories of|offers a range of services in|offers a range of options in|category:|categories:|in)\s*(.+)$", desc, flags=re.I)
        cat_str = None
        if m:
            cat_str = m.group(1)
        else:
            # fallback: try after the last comma
            parts = re.split(r"[,\.]", desc)
            if len(parts) > 1:
                cat_str = parts[-1]
            else:
                cat_str = desc
        if cat_str:
            # remove location-like patterns (addresses) if present
            # remove phrases like 'making it a must-visit for anyone seeking' etc
            cat_str = re.sub(r"making it a must-visit for anyone.*$", "", cat_str, flags=re.I)
            cat_str = re.sub(r"for all your.*$", "", cat_str, flags=re.I)
            # split by commas and ' and '
            temp = re.split(r",| and | & |/|-", cat_str)
            cleaned = []
            for t in temp:
                t = t.strip()
                # remove leading words like 'this', 'the', 'offers', 'offering'
                t = re.sub(r"^(this|the|offers|offering|providing|a range of services in|a range of services|offering a range of services in)\s+", "", t, flags=re.I)
                # strip trailing punctuation
                t = t.strip(' .')
                if t:
                    cleaned.append(t)
            cats = cleaned
    # final cleanup: remove empties and lower/strip
    cats = [c for c in cats if c]
    biz_categories[bid] = cats

# Aggregate review counts per category
category_totals = {}
for bid, cnt in business_review_counts.items():
    cats = biz_categories.get(bid)
    if not cats:
        # try to find business in businesses list by id and see if any other field
        cats = ['Unknown']
    for c in cats:
        category_totals[c] = category_totals.get(c, 0) + cnt

# Sort categories by total desc and take top 5
sorted_cats = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
top5 = sorted_cats[:5]

# Prepare output
out = []
for cat, total in top5:
    out.append({"category": cat, "total_reviews": total})

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_95pTBq66UeLiRerWSCzT6JGb': ['business', 'checkin'], 'var_call_03SEwA6SVMA6NZaET9HW9Zy2': ['review', 'tip', 'user'], 'var_call_25Q5yWaPNMHMV4WiMMiIFZ9a': 'file_storage/call_25Q5yWaPNMHMV4WiMMiIFZ9a.json', 'var_call_JfwPetpfZyBecrtf0XAhtedK': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_call_4dA3LWOTd46Mu4L1FXPSqm1W': [{'business_ref': 'businessref_13', 'review_count': '1'}, {'business_ref': 'businessref_79', 'review_count': '1'}, {'business_ref': 'businessref_6', 'review_count': '1'}, {'business_ref': 'businessref_74', 'review_count': '2'}, {'business_ref': 'businessref_66', 'review_count': '2'}, {'business_ref': 'businessref_15', 'review_count': '1'}, {'business_ref': 'businessref_33', 'review_count': '2'}, {'business_ref': 'businessref_36', 'review_count': '2'}, {'business_ref': 'businessref_60', 'review_count': '2'}, {'business_ref': 'businessref_12', 'review_count': '1'}, {'business_ref': 'businessref_31', 'review_count': '1'}, {'business_ref': 'businessref_53', 'review_count': '1'}, {'business_ref': 'businessref_92', 'review_count': '2'}, {'business_ref': 'businessref_26', 'review_count': '1'}, {'business_ref': 'businessref_68', 'review_count': '1'}, {'business_ref': 'businessref_41', 'review_count': '1'}, {'business_ref': 'businessref_10', 'review_count': '1'}, {'business_ref': 'businessref_45', 'review_count': '3'}, {'business_ref': 'businessref_57', 'review_count': '2'}, {'business_ref': 'businessref_86', 'review_count': '1'}, {'business_ref': 'businessref_62', 'review_count': '1'}, {'business_ref': 'businessref_37', 'review_count': '1'}, {'business_ref': 'businessref_96', 'review_count': '2'}, {'business_ref': 'businessref_98', 'review_count': '1'}, {'business_ref': 'businessref_14', 'review_count': '1'}, {'business_ref': 'businessref_20', 'review_count': '1'}]}

exec(code, env_args)
