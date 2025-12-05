code = """import json, re, pandas as pd

# Load full business data from file
path = var_call_1RLFaKB7lns84WTo8GY3YfwJ
with open(path, 'r') as f:
    business_records = json.load(f)

biz_df = pd.DataFrame(business_records)

# Extract state from description using regex patterns like ', XX,' or ', XX ' before ZIP or city
state_pattern = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pattern.search(desc)
    if m:
        return m.group(1)
    return None

biz_df['state'] = biz_df['description'].apply(extract_state)

# Map business_id -> state
biz_df['business_ref'] = biz_df['business_id'].str.replace('businessid_', 'businessref_', regex=False)
state_map = biz_df.set_index('business_ref')['state']

review_df = pd.DataFrame(var_call_erTHDSUjdbTA2fyzDHKW6t7Z)
review_df['review_cnt'] = review_df['review_cnt'].astype(int)
review_df['avg_rating'] = review_df['avg_rating'].astype(float)

# Join reviews with state
merged = review_df.join(state_map, on='business_ref', how='left')

# Drop rows without state
merged = merged.dropna(subset=['state'])

state_group = merged.groupby('state').agg(total_reviews=('review_cnt', 'sum'), avg_rating=('avg_rating', 'mean')).reset_index()

# State with max reviews
top = state_group.sort_values('total_reviews', ascending=False).iloc[0]

result = {
    'state': top['state'],
    'total_reviews': int(top['total_reviews']),
    'average_business_rating_in_state': round(float(top['avg_rating']), 3)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_1RLFaKB7lns84WTo8GY3YfwJ': 'file_storage/call_1RLFaKB7lns84WTo8GY3YfwJ.json', 'var_call_erTHDSUjdbTA2fyzDHKW6t7Z': [{'business_ref': 'businessref_79', 'review_cnt': '43', 'avg_rating': '4.627906976744186'}, {'business_ref': 'businessref_44', 'review_cnt': '42', 'avg_rating': '2.9285714285714284'}, {'business_ref': 'businessref_13', 'review_cnt': '12', 'avg_rating': '3.9166666666666665'}, {'business_ref': 'businessref_87', 'review_cnt': '6', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_66', 'review_cnt': '44', 'avg_rating': '2.1818181818181817'}, {'business_ref': 'businessref_9', 'review_cnt': '39', 'avg_rating': '4.435897435897436'}, {'business_ref': 'businessref_25', 'review_cnt': '36', 'avg_rating': '4.444444444444445'}, {'business_ref': 'businessref_2', 'review_cnt': '13', 'avg_rating': '4.769230769230769'}, {'business_ref': 'businessref_74', 'review_cnt': '6', 'avg_rating': '2.8333333333333335'}, {'business_ref': 'businessref_59', 'review_cnt': '30', 'avg_rating': '4.6'}, {'business_ref': 'businessref_5', 'review_cnt': '5', 'avg_rating': '1.6'}, {'business_ref': 'businessref_29', 'review_cnt': '21', 'avg_rating': '3.9047619047619047'}, {'business_ref': 'businessref_58', 'review_cnt': '6', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_39', 'review_cnt': '8', 'avg_rating': '4.125'}, {'business_ref': 'businessref_100', 'review_cnt': '4', 'avg_rating': '4.0'}, {'business_ref': 'businessref_81', 'review_cnt': '6', 'avg_rating': '3.6666666666666665'}, {'business_ref': 'businessref_93', 'review_cnt': '7', 'avg_rating': '2.857142857142857'}, {'business_ref': 'businessref_67', 'review_cnt': '46', 'avg_rating': '3.3260869565217392'}, {'business_ref': 'businessref_15', 'review_cnt': '17', 'avg_rating': '3.5294117647058822'}, {'business_ref': 'businessref_54', 'review_cnt': '10', 'avg_rating': '3.5'}, {'business_ref': 'businessref_33', 'review_cnt': '23', 'avg_rating': '3.5217391304347827'}, {'business_ref': 'businessref_89', 'review_cnt': '25', 'avg_rating': '3.04'}, {'business_ref': 'businessref_24', 'review_cnt': '38', 'avg_rating': '3.289473684210526'}, {'business_ref': 'businessref_36', 'review_cnt': '44', 'avg_rating': '4.090909090909091'}, {'business_ref': 'businessref_12', 'review_cnt': '26', 'avg_rating': '3.730769230769231'}, {'business_ref': 'businessref_60', 'review_cnt': '32', 'avg_rating': '2.0'}, {'business_ref': 'businessref_52', 'review_cnt': '6', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_43', 'review_cnt': '21', 'avg_rating': '3.0476190476190474'}, {'business_ref': 'businessref_48', 'review_cnt': '13', 'avg_rating': '3.3846153846153846'}, {'business_ref': 'businessref_17', 'review_cnt': '10', 'avg_rating': '3.9'}, {'business_ref': 'businessref_31', 'review_cnt': '14', 'avg_rating': '1.5'}, {'business_ref': 'businessref_78', 'review_cnt': '6', 'avg_rating': '5.0'}, {'business_ref': 'businessref_99', 'review_cnt': '5', 'avg_rating': '3.2'}, {'business_ref': 'businessref_51', 'review_cnt': '35', 'avg_rating': '3.9714285714285715'}, {'business_ref': 'businessref_53', 'review_cnt': '7', 'avg_rating': '3.7142857142857144'}, {'business_ref': 'businessref_80', 'review_cnt': '9', 'avg_rating': '1.8888888888888888'}, {'business_ref': 'businessref_19', 'review_cnt': '6', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_57', 'review_cnt': '42', 'avg_rating': '1.9047619047619047'}, {'business_ref': 'businessref_85', 'review_cnt': '44', 'avg_rating': '3.3863636363636362'}, {'business_ref': 'businessref_86', 'review_cnt': '46', 'avg_rating': '3.739130434782609'}, {'business_ref': 'businessref_37', 'review_cnt': '24', 'avg_rating': '3.2083333333333335'}, {'business_ref': 'businessref_42', 'review_cnt': '12', 'avg_rating': '4.083333333333333'}, {'business_ref': 'businessref_97', 'review_cnt': '17', 'avg_rating': '4.294117647058823'}, {'business_ref': 'businessref_8', 'review_cnt': '45', 'avg_rating': '2.8222222222222224'}, {'business_ref': 'businessref_90', 'review_cnt': '3', 'avg_rating': '1.0'}, {'business_ref': 'businessref_72', 'review_cnt': '5', 'avg_rating': '4.6'}, {'business_ref': 'businessref_56', 'review_cnt': '6', 'avg_rating': '2.3333333333333335'}, {'business_ref': 'businessref_62', 'review_cnt': '7', 'avg_rating': '3.0'}, {'business_ref': 'businessref_34', 'review_cnt': '9', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_21', 'review_cnt': '35', 'avg_rating': '2.0285714285714285'}, {'business_ref': 'businessref_26', 'review_cnt': '24', 'avg_rating': '1.7083333333333333'}, {'business_ref': 'businessref_68', 'review_cnt': '21', 'avg_rating': '1.7619047619047619'}, {'business_ref': 'businessref_88', 'review_cnt': '33', 'avg_rating': '3.212121212121212'}, {'business_ref': 'businessref_65', 'review_cnt': '18', 'avg_rating': '3.8333333333333335'}, {'business_ref': 'businessref_4', 'review_cnt': '7', 'avg_rating': '5.0'}, {'business_ref': 'businessref_64', 'review_cnt': '7', 'avg_rating': '3.7142857142857144'}, {'business_ref': 'businessref_10', 'review_cnt': '16', 'avg_rating': '4.1875'}, {'business_ref': 'businessref_23', 'review_cnt': '9', 'avg_rating': '3.4444444444444446'}, {'business_ref': 'businessref_49', 'review_cnt': '6', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_84', 'review_cnt': '4', 'avg_rating': '5.0'}, {'business_ref': 'businessref_11', 'review_cnt': '10', 'avg_rating': '4.2'}, {'business_ref': 'businessref_41', 'review_cnt': '4', 'avg_rating': '4.0'}, {'business_ref': 'businessref_82', 'review_cnt': '42', 'avg_rating': '4.309523809523809'}, {'business_ref': 'businessref_35', 'review_cnt': '8', 'avg_rating': '4.125'}, {'business_ref': 'businessref_45', 'review_cnt': '44', 'avg_rating': '3.3863636363636362'}, {'business_ref': 'businessref_77', 'review_cnt': '42', 'avg_rating': '2.5476190476190474'}, {'business_ref': 'businessref_27', 'review_cnt': '28', 'avg_rating': '3.3214285714285716'}, {'business_ref': 'businessref_50', 'review_cnt': '7', 'avg_rating': '2.4285714285714284'}, {'business_ref': 'businessref_76', 'review_cnt': '9', 'avg_rating': '3.5555555555555554'}, {'business_ref': 'businessref_75', 'review_cnt': '5', 'avg_rating': '4.0'}, {'business_ref': 'businessref_96', 'review_cnt': '44', 'avg_rating': '3.8863636363636362'}, {'business_ref': 'businessref_22', 'review_cnt': '11', 'avg_rating': '2.8181818181818183'}, {'business_ref': 'businessref_20', 'review_cnt': '42', 'avg_rating': '3.2142857142857144'}, {'business_ref': 'businessref_18', 'review_cnt': '11', 'avg_rating': '1.8181818181818181'}, {'business_ref': 'businessref_14', 'review_cnt': '25', 'avg_rating': '3.4'}, {'business_ref': 'businessref_3', 'review_cnt': '4', 'avg_rating': '2.0'}, {'business_ref': 'businessref_69', 'review_cnt': '9', 'avg_rating': '4.222222222222222'}, {'business_ref': 'businessref_98', 'review_cnt': '5', 'avg_rating': '1.2'}, {'business_ref': 'businessref_28', 'review_cnt': '18', 'avg_rating': '4.055555555555555'}, {'business_ref': 'businessref_70', 'review_cnt': '9', 'avg_rating': '4.777777777777778'}, {'business_ref': 'businessref_47', 'review_cnt': '42', 'avg_rating': '3.9047619047619047'}, {'business_ref': 'businessref_16', 'review_cnt': '41', 'avg_rating': '3.024390243902439'}, {'business_ref': 'businessref_46', 'review_cnt': '44', 'avg_rating': '4.181818181818182'}, {'business_ref': 'businessref_91', 'review_cnt': '45', 'avg_rating': '4.911111111111111'}, {'business_ref': 'businessref_1', 'review_cnt': '6', 'avg_rating': '4.333333333333333'}, {'business_ref': 'businessref_55', 'review_cnt': '37', 'avg_rating': '4.918918918918919'}, {'business_ref': 'businessref_73', 'review_cnt': '5', 'avg_rating': '5.0'}, {'business_ref': 'businessref_6', 'review_cnt': '37', 'avg_rating': '4.0'}, {'business_ref': 'businessref_71', 'review_cnt': '41', 'avg_rating': '3.268292682926829'}, {'business_ref': 'businessref_38', 'review_cnt': '17', 'avg_rating': '3.1176470588235294'}, {'business_ref': 'businessref_32', 'review_cnt': '7', 'avg_rating': '3.4285714285714284'}, {'business_ref': 'businessref_30', 'review_cnt': '5', 'avg_rating': '3.6'}, {'business_ref': 'businessref_95', 'review_cnt': '6', 'avg_rating': '2.1666666666666665'}, {'business_ref': 'businessref_40', 'review_cnt': '21', 'avg_rating': '4.476190476190476'}, {'business_ref': 'businessref_61', 'review_cnt': '17', 'avg_rating': '2.4705882352941178'}, {'business_ref': 'businessref_92', 'review_cnt': '33', 'avg_rating': '4.575757575757576'}, {'business_ref': 'businessref_94', 'review_cnt': '30', 'avg_rating': '4.066666666666666'}, {'business_ref': 'businessref_7', 'review_cnt': '16', 'avg_rating': '3.75'}, {'business_ref': 'businessref_63', 'review_cnt': '6', 'avg_rating': '2.8333333333333335'}, {'business_ref': 'businessref_83', 'review_cnt': '6', 'avg_rating': '4.833333333333333'}]}

exec(code, env_args)
