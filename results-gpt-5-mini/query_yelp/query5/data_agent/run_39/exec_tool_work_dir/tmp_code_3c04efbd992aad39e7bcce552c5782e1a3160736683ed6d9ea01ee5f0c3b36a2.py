code = """import json
import pandas as pd
import re

# Load business collection result from file path provided in var_call_JmH66U9NAea1QQWm75JdhDUC
with open(var_call_JmH66U9NAea1QQWm75JdhDUC, 'r') as f:
    businesses = json.load(f)

# Load review aggregation from var_call_D91O35CFQVckdTKnyoNa0pYY
reviews_agg = var_call_D91O35CFQVckdTKnyoNa0pYY

# Normalize businesses into DataFrame
biz_rows = []
for b in businesses:
    biz_id = b.get('business_id')
    attrs = b.get('attributes')
    desc = b.get('description') or ''
    wifi_val = None
    if isinstance(attrs, dict):
        wifi_val = attrs.get('WiFi') if 'WiFi' in attrs else None
    # Normalize wifi_val to clean string
    if wifi_val is None:
        wifi_norm = None
    else:
        # Some values are strings like "u'free'" or "'free'" or plain 'free'
        s = str(wifi_val)
        # remove leading u' and surrounding quotes
        s = s.strip()
        # remove leading u'
        s = re.sub(r"^u'", "'", s)
        # strip quotes
        s = s.strip("\"' ")
        wifi_norm = s.lower()
    # Extract state from description: look for ", XX," pattern
    state = None
    m = re.search(r",\s*([A-Z]{2})\s*,", desc)
    if not m:
        # try " in City, ST" pattern
        m = re.search(r"in [^,]+,\s*([A-Z]{2})", desc)
    if m:
        state = m.group(1)
    biz_rows.append({'business_id': biz_id, 'wifi': wifi_norm, 'state': state})

df_biz = pd.DataFrame(biz_rows)

# Define wifi offered if wifi not in negative values
negatives = set(['no','none','false','na','n'])

df_biz['wifi_offered'] = df_biz['wifi'].apply(lambda x: False if (x is None or x in negatives) else True)

# Count wifi-offering businesses per state (exclude None states)
state_counts = df_biz[df_biz['state'].notnull() & df_biz['wifi_offered']].groupby('state').size().reset_index(name='count')

if state_counts.empty:
    result = {'state': None, 'wifi_business_count': 0, 'average_rating': None}
else:
    # find state with max count
    top = state_counts.sort_values('count', ascending=False).iloc[0]
    top_state = top['state']
    top_count = int(top['count'])

    # Get business_ids in that state with wifi offered
    top_biz = df_biz[(df_biz['state']==top_state) & (df_biz['wifi_offered'])]['business_id'].tolist()

    # Map to business_ref by replacing prefix
    biz_to_ref = {b: b.replace('businessid_', 'businessref_') for b in top_biz}

    # Build review agg lookup
    rev_lookup = {r['business_ref']: {'avg_rating': float(r['avg_rating']), 'review_count': int(r['review_count'])} for r in reviews_agg}

    # For businesses in top state, collect review counts and avg ratings
    total_reviews = 0
    weighted_rating_sum = 0.0
    biz_with_reviews = 0
    for b,bref in biz_to_ref.items():
        if bref in rev_lookup:
            info = rev_lookup[bref]
            rc = info['review_count']
            ar = info['avg_rating']
            total_reviews += rc
            weighted_rating_sum += ar * rc
            biz_with_reviews += 1
    if total_reviews>0:
        overall_avg = weighted_rating_sum / total_reviews
    else:
        # fallback: average of business average ratings (unweighted) for those with any avg
        if biz_with_reviews>0:
            overall_avg = weighted_rating_sum / (1 if total_reviews==0 else total_reviews)
            # but this fallback makes no sense; set to None
            overall_avg = None
        else:
            overall_avg = None

    result = {'state': top_state, 'wifi_business_count': top_count, 'average_rating': (round(overall_avg,3) if overall_avg is not None else None)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_JmH66U9NAea1QQWm75JdhDUC': 'file_storage/call_JmH66U9NAea1QQWm75JdhDUC.json', 'var_call_D91O35CFQVckdTKnyoNa0pYY': [{'business_ref': 'businessref_57', 'avg_rating': '1.9047619047619047', 'review_count': '42'}, {'business_ref': 'businessref_85', 'avg_rating': '3.3863636363636362', 'review_count': '44'}, {'business_ref': 'businessref_86', 'avg_rating': '3.739130434782609', 'review_count': '46'}, {'business_ref': 'businessref_37', 'avg_rating': '3.2083333333333335', 'review_count': '24'}, {'business_ref': 'businessref_42', 'avg_rating': '4.083333333333333', 'review_count': '12'}, {'business_ref': 'businessref_97', 'avg_rating': '4.294117647058823', 'review_count': '17'}, {'business_ref': 'businessref_8', 'avg_rating': '2.8222222222222224', 'review_count': '45'}, {'business_ref': 'businessref_90', 'avg_rating': '1.0', 'review_count': '3'}, {'business_ref': 'businessref_72', 'avg_rating': '4.6', 'review_count': '5'}, {'business_ref': 'businessref_56', 'avg_rating': '2.3333333333333335', 'review_count': '6'}, {'business_ref': 'businessref_62', 'avg_rating': '3.0', 'review_count': '7'}, {'business_ref': 'businessref_34', 'avg_rating': '3.3333333333333335', 'review_count': '9'}, {'business_ref': 'businessref_21', 'avg_rating': '2.0285714285714285', 'review_count': '35'}, {'business_ref': 'businessref_26', 'avg_rating': '1.7083333333333333', 'review_count': '24'}, {'business_ref': 'businessref_68', 'avg_rating': '1.7619047619047619', 'review_count': '21'}, {'business_ref': 'businessref_88', 'avg_rating': '3.212121212121212', 'review_count': '33'}, {'business_ref': 'businessref_65', 'avg_rating': '3.8333333333333335', 'review_count': '18'}, {'business_ref': 'businessref_4', 'avg_rating': '5.0', 'review_count': '7'}, {'business_ref': 'businessref_64', 'avg_rating': '3.7142857142857144', 'review_count': '7'}, {'business_ref': 'businessref_10', 'avg_rating': '4.1875', 'review_count': '16'}, {'business_ref': 'businessref_23', 'avg_rating': '3.4444444444444446', 'review_count': '9'}, {'business_ref': 'businessref_49', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'business_ref': 'businessref_84', 'avg_rating': '5.0', 'review_count': '4'}, {'business_ref': 'businessref_11', 'avg_rating': '4.2', 'review_count': '10'}, {'business_ref': 'businessref_41', 'avg_rating': '4.0', 'review_count': '4'}, {'business_ref': 'businessref_82', 'avg_rating': '4.309523809523809', 'review_count': '42'}, {'business_ref': 'businessref_35', 'avg_rating': '4.125', 'review_count': '8'}, {'business_ref': 'businessref_45', 'avg_rating': '3.3863636363636362', 'review_count': '44'}, {'business_ref': 'businessref_77', 'avg_rating': '2.5476190476190474', 'review_count': '42'}, {'business_ref': 'businessref_27', 'avg_rating': '3.3214285714285716', 'review_count': '28'}, {'business_ref': 'businessref_50', 'avg_rating': '2.4285714285714284', 'review_count': '7'}, {'business_ref': 'businessref_76', 'avg_rating': '3.5555555555555554', 'review_count': '9'}, {'business_ref': 'businessref_75', 'avg_rating': '4.0', 'review_count': '5'}, {'business_ref': 'businessref_95', 'avg_rating': '2.1666666666666665', 'review_count': '6'}, {'business_ref': 'businessref_40', 'avg_rating': '4.476190476190476', 'review_count': '21'}, {'business_ref': 'businessref_61', 'avg_rating': '2.4705882352941178', 'review_count': '17'}, {'business_ref': 'businessref_92', 'avg_rating': '4.575757575757576', 'review_count': '33'}, {'business_ref': 'businessref_94', 'avg_rating': '4.066666666666666', 'review_count': '30'}, {'business_ref': 'businessref_7', 'avg_rating': '3.75', 'review_count': '16'}, {'business_ref': 'businessref_63', 'avg_rating': '2.8333333333333335', 'review_count': '6'}, {'business_ref': 'businessref_83', 'avg_rating': '4.833333333333333', 'review_count': '6'}, {'business_ref': 'businessref_96', 'avg_rating': '3.8863636363636362', 'review_count': '44'}, {'business_ref': 'businessref_22', 'avg_rating': '2.8181818181818183', 'review_count': '11'}, {'business_ref': 'businessref_20', 'avg_rating': '3.2142857142857144', 'review_count': '42'}, {'business_ref': 'businessref_18', 'avg_rating': '1.8181818181818181', 'review_count': '11'}, {'business_ref': 'businessref_14', 'avg_rating': '3.4', 'review_count': '25'}, {'business_ref': 'businessref_3', 'avg_rating': '2.0', 'review_count': '4'}, {'business_ref': 'businessref_69', 'avg_rating': '4.222222222222222', 'review_count': '9'}, {'business_ref': 'businessref_98', 'avg_rating': '1.2', 'review_count': '5'}, {'business_ref': 'businessref_28', 'avg_rating': '4.055555555555555', 'review_count': '18'}, {'business_ref': 'businessref_70', 'avg_rating': '4.777777777777778', 'review_count': '9'}, {'business_ref': 'businessref_79', 'avg_rating': '4.627906976744186', 'review_count': '43'}, {'business_ref': 'businessref_44', 'avg_rating': '2.9285714285714284', 'review_count': '42'}, {'business_ref': 'businessref_13', 'avg_rating': '3.9166666666666665', 'review_count': '12'}, {'business_ref': 'businessref_87', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'business_ref': 'businessref_66', 'avg_rating': '2.1818181818181817', 'review_count': '44'}, {'business_ref': 'businessref_9', 'avg_rating': '4.435897435897436', 'review_count': '39'}, {'business_ref': 'businessref_25', 'avg_rating': '4.444444444444445', 'review_count': '36'}, {'business_ref': 'businessref_2', 'avg_rating': '4.769230769230769', 'review_count': '13'}, {'business_ref': 'businessref_74', 'avg_rating': '2.8333333333333335', 'review_count': '6'}, {'business_ref': 'businessref_47', 'avg_rating': '3.9047619047619047', 'review_count': '42'}, {'business_ref': 'businessref_16', 'avg_rating': '3.024390243902439', 'review_count': '41'}, {'business_ref': 'businessref_46', 'avg_rating': '4.181818181818182', 'review_count': '44'}, {'business_ref': 'businessref_91', 'avg_rating': '4.911111111111111', 'review_count': '45'}, {'business_ref': 'businessref_1', 'avg_rating': '4.333333333333333', 'review_count': '6'}, {'business_ref': 'businessref_55', 'avg_rating': '4.918918918918919', 'review_count': '37'}, {'business_ref': 'businessref_73', 'avg_rating': '5.0', 'review_count': '5'}, {'business_ref': 'businessref_6', 'avg_rating': '4.0', 'review_count': '37'}, {'business_ref': 'businessref_71', 'avg_rating': '3.268292682926829', 'review_count': '41'}, {'business_ref': 'businessref_38', 'avg_rating': '3.1176470588235294', 'review_count': '17'}, {'business_ref': 'businessref_32', 'avg_rating': '3.4285714285714284', 'review_count': '7'}, {'business_ref': 'businessref_30', 'avg_rating': '3.6', 'review_count': '5'}, {'business_ref': 'businessref_59', 'avg_rating': '4.6', 'review_count': '30'}, {'business_ref': 'businessref_5', 'avg_rating': '1.6', 'review_count': '5'}, {'business_ref': 'businessref_29', 'avg_rating': '3.9047619047619047', 'review_count': '21'}, {'business_ref': 'businessref_58', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'business_ref': 'businessref_39', 'avg_rating': '4.125', 'review_count': '8'}, {'business_ref': 'businessref_100', 'avg_rating': '4.0', 'review_count': '4'}, {'business_ref': 'businessref_81', 'avg_rating': '3.6666666666666665', 'review_count': '6'}, {'business_ref': 'businessref_93', 'avg_rating': '2.857142857142857', 'review_count': '7'}, {'business_ref': 'businessref_67', 'avg_rating': '3.3260869565217392', 'review_count': '46'}, {'business_ref': 'businessref_15', 'avg_rating': '3.5294117647058822', 'review_count': '17'}, {'business_ref': 'businessref_54', 'avg_rating': '3.5', 'review_count': '10'}, {'business_ref': 'businessref_33', 'avg_rating': '3.5217391304347827', 'review_count': '23'}, {'business_ref': 'businessref_89', 'avg_rating': '3.04', 'review_count': '25'}, {'business_ref': 'businessref_24', 'avg_rating': '3.289473684210526', 'review_count': '38'}, {'business_ref': 'businessref_36', 'avg_rating': '4.090909090909091', 'review_count': '44'}, {'business_ref': 'businessref_12', 'avg_rating': '3.730769230769231', 'review_count': '26'}, {'business_ref': 'businessref_60', 'avg_rating': '2.0', 'review_count': '32'}, {'business_ref': 'businessref_52', 'avg_rating': '4.166666666666667', 'review_count': '6'}, {'business_ref': 'businessref_43', 'avg_rating': '3.0476190476190474', 'review_count': '21'}, {'business_ref': 'businessref_48', 'avg_rating': '3.3846153846153846', 'review_count': '13'}, {'business_ref': 'businessref_17', 'avg_rating': '3.9', 'review_count': '10'}, {'business_ref': 'businessref_31', 'avg_rating': '1.5', 'review_count': '14'}, {'business_ref': 'businessref_78', 'avg_rating': '5.0', 'review_count': '6'}, {'business_ref': 'businessref_99', 'avg_rating': '3.2', 'review_count': '5'}, {'business_ref': 'businessref_51', 'avg_rating': '3.9714285714285715', 'review_count': '35'}, {'business_ref': 'businessref_53', 'avg_rating': '3.7142857142857144', 'review_count': '7'}, {'business_ref': 'businessref_80', 'avg_rating': '1.8888888888888888', 'review_count': '9'}, {'business_ref': 'businessref_19', 'avg_rating': '3.3333333333333335', 'review_count': '6'}]}

exec(code, env_args)
