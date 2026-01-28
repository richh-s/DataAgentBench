code = """import json
from collections import defaultdict

businesses = json.load(open(var_call_4gD7RcgzO0LTD6TtHVlV0ELM, 'r'))
review_aggs = var_call_VdiePHeCmvkzPqtOE7ClQitB

rev_map = {}
for r in review_aggs:
    br = r.get('business_ref')
    try:
        avg = float(r.get('avg_rating'))
    except:
        avg = None
    try:
        cnt = int(r.get('review_count'))
    except:
        cnt = 0
    rev_map[br] = (avg, cnt)

def accepts_credit(attributes):
    if not attributes:
        return False
    s = str(attributes).lower()
    return ('businessacceptscreditcards' in s) and ('true' in s)

def extract_categories(description):
    if not description:
        return []
    desc = description
    lower = desc.lower()
    tail = None
    idx = lower.rfind(' in ')
    if idx != -1:
        tail = desc[idx+4:]
    else:
        idx2 = lower.find('including')
        if idx2 != -1:
            tail = desc[idx2+9:]
        else:
            tail = desc
    if '.' in tail:
        tail = tail.split('.')[0]
    tail = tail.replace('&', ',')
    tail = tail.replace(' and ', ',')
    parts = [p.strip() for p in tail.split(',') if p.strip()]
    filtered = []
    for p in parts:
        lp = p.lower()
        if any(x in lp for x in ['located', 'offers', 'making', 'perfect spot', 'meet all', 'this location', 'to meet']):
            continue
        words = lp.split()
        if len(words) == 0 or len(words) > 6:
            continue
        filtered.append(lp)
    return filtered

cat_counts = defaultdict(int)
cat_businesses = defaultdict(list)
for b in businesses:
    bid = b.get('business_id')
    attrs = b.get('attributes')
    desc = b.get('description')
    if accepts_credit(attrs):
        cats = extract_categories(desc)
        if not cats:
            continue
        for c in cats:
            cat_counts[c] += 1
            cat_businesses[c].append(bid)

if not cat_counts:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    max_cat = max(cat_counts.items(), key=lambda x: (x[1], x[0]))[0]
    max_count = cat_counts[max_cat]
    bids = cat_businesses[max_cat]
    total_reviews = 0
    weighted_sum = 0.0
    avg_list = []
    for bid in bids:
        bref = bid.replace('businessid_', 'businessref_')
        if bref in rev_map:
            avg, cnt = rev_map[bref]
            if avg is not None and cnt > 0:
                weighted_sum += avg * cnt
                total_reviews += cnt
                avg_list.append(avg)
    if total_reviews > 0:
        final_avg = weighted_sum / total_reviews
    elif avg_list:
        final_avg = sum(avg_list) / len(avg_list)
    else:
        final_avg = None
    result = {'category': max_cat, 'business_count': max_count, 'average_rating': (None if final_avg is None else float(final_avg))}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_pqmOa5GDYmKeM7FE5KQotrUJ': ['business', 'checkin'], 'var_call_eD5ngFQrvZyF4GSwBdOkKeJv': ['review', 'tip', 'user'], 'var_call_4gD7RcgzO0LTD6TtHVlV0ELM': 'file_storage/call_4gD7RcgzO0LTD6TtHVlV0ELM.json', 'var_call_VdiePHeCmvkzPqtOE7ClQitB': [{'business_ref': 'businessref_79', 'avg_rating': '4.627906976744186', 'review_count': '43'}, {'business_ref': 'businessref_44', 'avg_rating': '2.9285714285714284', 'review_count': '42'}, {'business_ref': 'businessref_13', 'avg_rating': '3.9166666666666665', 'review_count': '12'}, {'business_ref': 'businessref_87', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'business_ref': 'businessref_47', 'avg_rating': '3.9047619047619047', 'review_count': '42'}, {'business_ref': 'businessref_16', 'avg_rating': '3.024390243902439', 'review_count': '41'}, {'business_ref': 'businessref_46', 'avg_rating': '4.181818181818182', 'review_count': '44'}, {'business_ref': 'businessref_91', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'business_ref': 'businessref_1', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'business_ref': 'businessref_55', 'avg_rating': '4.918918918918919', 'review_count': '37'}, {'business_ref': 'businessref_73', 'avg_rating': '5.0', 'review_count': '5'}, {'business_ref': 'businessref_6', 'avg_rating': '4.0', 'review_count': '37'}, {'business_ref': 'businessref_71', 'avg_rating': '3.268292682926829', 'review_count': '41'}, {'business_ref': 'businessref_38', 'avg_rating': '3.1176470588235294', 'review_count': '17'}, {'business_ref': 'businessref_32', 'avg_rating': '3.4285714285714284', 'review_count': '7'}, {'business_ref': 'businessref_30', 'avg_rating': '3.6', 'review_count': '5'}, {'business_ref': 'businessref_59', 'avg_rating': '4.6', 'review_count': '30'}, {'business_ref': 'businessref_5', 'avg_rating': '1.6', 'review_count': '5'}, {'business_ref': 'businessref_29', 'avg_rating': '3.9047619047619047', 'review_count': '21'}, {'business_ref': 'businessref_58', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'business_ref': 'businessref_39', 'avg_rating': '4.125', 'review_count': '8'}, {'business_ref': 'businessref_100', 'avg_rating': '4.0', 'review_count': '4'}, {'business_ref': 'businessref_81', 'avg_rating': '3.6666666666666665', 'review_count': '6'}, {'business_ref': 'businessref_93', 'avg_rating': '2.857142857142857', 'review_count': '7'}, {'business_ref': 'businessref_67', 'avg_rating': '3.3260869565217392', 'review_count': '46'}, {'business_ref': 'businessref_15', 'avg_rating': '3.5294117647058822', 'review_count': '17'}, {'business_ref': 'businessref_54', 'avg_rating': '3.5', 'review_count': '10'}, {'business_ref': 'businessref_33', 'avg_rating': '3.5217391304347827', 'review_count': '23'}, {'business_ref': 'businessref_89', 'avg_rating': '3.04', 'review_count': '25'}, {'business_ref': 'businessref_24', 'avg_rating': '3.289473684210526', 'review_count': '38'}, {'business_ref': 'businessref_36', 'avg_rating': '4.090909090909091', 'review_count': '44'}, {'business_ref': 'businessref_12', 'avg_rating': '3.730769230769231', 'review_count': '26'}, {'business_ref': 'businessref_60', 'avg_rating': '2.0', 'review_count': '32'}, {'business_ref': 'businessref_52', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'business_ref': 'businessref_43', 'avg_rating': '3.0476190476190474', 'review_count': '21'}, {'business_ref': 'businessref_48', 'avg_rating': '3.3846153846153846', 'review_count': '13'}, {'business_ref': 'businessref_17', 'avg_rating': '3.9', 'review_count': '10'}, {'business_ref': 'businessref_66', 'avg_rating': '2.1818181818181817', 'review_count': '44'}, {'business_ref': 'businessref_9', 'avg_rating': '4.435897435897436', 'review_count': '39'}, {'business_ref': 'businessref_25', 'avg_rating': '4.444444444444445', 'review_count': '36'}, {'business_ref': 'businessref_2', 'avg_rating': '4.769230769230769', 'review_count': '13'}, {'business_ref': 'businessref_74', 'avg_rating': '2.8333333333333335', 'review_count': '6'}, {'business_ref': 'businessref_51', 'avg_rating': '3.9714285714285715', 'review_count': '35'}, {'business_ref': 'businessref_53', 'avg_rating': '3.7142857142857144', 'review_count': '7'}, {'business_ref': 'businessref_80', 'avg_rating': '1.8888888888888888', 'review_count': '9'}, {'business_ref': 'businessref_19', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'business_ref': 'businessref_57', 'avg_rating': '1.9047619047619047', 'review_count': '42'}, {'business_ref': 'businessref_85', 'avg_rating': '3.3863636363636362', 'review_count': '44'}, {'business_ref': 'businessref_86', 'avg_rating': '3.739130434782609', 'review_count': '46'}, {'business_ref': 'businessref_37', 'avg_rating': '3.2083333333333335', 'review_count': '24'}, {'business_ref': 'businessref_42', 'avg_rating': '4.083333333333333', 'review_count': '12'}, {'business_ref': 'businessref_97', 'avg_rating': '4.294117647058823', 'review_count': '17'}, {'business_ref': 'businessref_8', 'avg_rating': '2.8222222222222224', 'review_count': '45'}, {'business_ref': 'businessref_90', 'avg_rating': '1.0', 'review_count': '3'}, {'business_ref': 'businessref_72', 'avg_rating': '4.6', 'review_count': '5'}, {'business_ref': 'businessref_56', 'avg_rating': '2.3333333333333335', 'review_count': '6'}, {'business_ref': 'businessref_62', 'avg_rating': '3.0', 'review_count': '7'}, {'business_ref': 'businessref_34', 'avg_rating': '3.3333333333333335', 'review_count': '9'}, {'business_ref': 'businessref_21', 'avg_rating': '2.0285714285714285', 'review_count': '35'}, {'business_ref': 'businessref_26', 'avg_rating': '1.7083333333333333', 'review_count': '24'}, {'business_ref': 'businessref_68', 'avg_rating': '1.7619047619047619', 'review_count': '21'}, {'business_ref': 'businessref_88', 'avg_rating': '3.212121212121212', 'review_count': '33'}, {'business_ref': 'businessref_65', 'avg_rating': '3.8333333333333335', 'review_count': '18'}, {'business_ref': 'businessref_4', 'avg_rating': '5.0', 'review_count': '7'}, {'business_ref': 'businessref_64', 'avg_rating': '3.7142857142857144', 'review_count': '7'}, {'business_ref': 'businessref_10', 'avg_rating': '4.1875', 'review_count': '16'}, {'business_ref': 'businessref_23', 'avg_rating': '3.4444444444444446', 'review_count': '9'}, {'business_ref': 'businessref_49', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'business_ref': 'businessref_84', 'avg_rating': '5.0', 'review_count': '4'}, {'business_ref': 'businessref_11', 'avg_rating': '4.2', 'review_count': '10'}, {'business_ref': 'businessref_41', 'avg_rating': '4.0', 'review_count': '4'}, {'business_ref': 'businessref_82', 'avg_rating': '4.309523809523809', 'review_count': '42'}, {'business_ref': 'businessref_35', 'avg_rating': '4.125', 'review_count': '8'}, {'business_ref': 'businessref_45', 'avg_rating': '3.3863636363636362', 'review_count': '44'}, {'business_ref': 'businessref_95', 'avg_rating': '2.1666666666666665', 'review_count': '6'}, {'business_ref': 'businessref_40', 'avg_rating': '4.476190476190476', 'review_count': '21'}, {'business_ref': 'businessref_61', 'avg_rating': '2.4705882352941178', 'review_count': '17'}, {'business_ref': 'businessref_92', 'avg_rating': '4.575757575757576', 'review_count': '33'}, {'business_ref': 'businessref_94', 'avg_rating': '4.066666666666666', 'review_count': '30'}, {'business_ref': 'businessref_7', 'avg_rating': '3.75', 'review_count': '16'}, {'business_ref': 'businessref_63', 'avg_rating': '2.8333333333333335', 'review_count': '6'}, {'business_ref': 'businessref_83', 'avg_rating': '4.833333333333333', 'review_count': '6'}, {'business_ref': 'businessref_77', 'avg_rating': '2.5476190476190474', 'review_count': '42'}, {'business_ref': 'businessref_27', 'avg_rating': '3.3214285714285716', 'review_count': '28'}, {'business_ref': 'businessref_50', 'avg_rating': '2.4285714285714284', 'review_count': '7'}, {'business_ref': 'businessref_76', 'avg_rating': '3.5555555555555554', 'review_count': '9'}, {'business_ref': 'businessref_75', 'avg_rating': '4.0', 'review_count': '5'}, {'business_ref': 'businessref_96', 'avg_rating': '3.8863636363636362', 'review_count': '44'}, {'business_ref': 'businessref_22', 'avg_rating': '2.8181818181818183', 'review_count': '11'}, {'business_ref': 'businessref_20', 'avg_rating': '3.2142857142857144', 'review_count': '42'}, {'business_ref': 'businessref_18', 'avg_rating': '1.8181818181818181', 'review_count': '11'}, {'business_ref': 'businessref_14', 'avg_rating': '3.4', 'review_count': '25'}, {'business_ref': 'businessref_3', 'avg_rating': '2.0', 'review_count': '4'}, {'business_ref': 'businessref_69', 'avg_rating': '4.222222222222222', 'review_count': '9'}, {'business_ref': 'businessref_98', 'avg_rating': '1.2', 'review_count': '5'}, {'business_ref': 'businessref_28', 'avg_rating': '4.055555555555555', 'review_count': '18'}, {'business_ref': 'businessref_70', 'avg_rating': '4.777777777777778', 'review_count': '9'}, {'business_ref': 'businessref_31', 'avg_rating': '1.5', 'review_count': '14'}, {'business_ref': 'businessref_78', 'avg_rating': '5.0', 'review_count': '6'}, {'business_ref': 'businessref_99', 'avg_rating': '3.2', 'review_count': '5'}]}

exec(code, env_args)
