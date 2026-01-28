code = """import json, re, pandas as pd

# Load wifi businesses from file if needed
wifi_data = var_call_EZNzTfYZSvfvlH9yF62CX7jm
if isinstance(wifi_data, str):
    with open(wifi_data, 'r') as f:
        wifi_data = json.load(f)

wifi_df = pd.DataFrame(wifi_data)

# Extract US state from description: pattern ', XX,' where XX is two uppercase letters.
# Ensure it's US state/territory: filter against known USPS abbreviations.
us_states = set('AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY DC'.split())

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r',\s*([A-Z]{2})\s*,', desc)
    if m:
        st = m.group(1)
        return st if st in us_states else None
    return None

wifi_df['state'] = wifi_df['description'].map(extract_state)
wifi_df = wifi_df.dropna(subset=['state','business_id'])

# Count wifi businesses per state
counts = wifi_df.groupby('state', as_index=False).agg(wifi_business_count=('business_id','nunique'))
counts = counts.sort_values(['wifi_business_count','state'], ascending=[False, True])

top_state = counts.iloc[0]['state'] if len(counts) else None

# Map businessid_ -> businessref_
wifi_df['business_ref'] = wifi_df['business_id'].str.replace('businessid_', 'businessref_', regex=False)

ratings_df = pd.DataFrame(var_call_IetG6wNfNodnVqon71ruAlxd)
ratings_df['avg_rating'] = ratings_df['avg_rating'].astype(float)

# Compute average of business avg ratings for wifi businesses in top state
if top_state is not None:
    top_business_refs = wifi_df.loc[wifi_df['state']==top_state, 'business_ref'].dropna().unique()
    merged = ratings_df[ratings_df['business_ref'].isin(top_business_refs)]
    avg_rating_top = float(merged['avg_rating'].mean()) if len(merged) else None
    wifi_count_top = int(counts.iloc[0]['wifi_business_count'])
else:
    avg_rating_top = None
    wifi_count_top = 0

result = {
    'state': top_state,
    'wifi_business_count': wifi_count_top,
    'average_rating': None if avg_rating_top is None else round(avg_rating_top, 4)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_EZNzTfYZSvfvlH9yF62CX7jm': 'file_storage/call_EZNzTfYZSvfvlH9yF62CX7jm.json', 'var_call_IetG6wNfNodnVqon71ruAlxd': [{'business_ref': 'businessref_47', 'avg_rating': '3.9047619047619047'}, {'business_ref': 'businessref_16', 'avg_rating': '3.024390243902439'}, {'business_ref': 'businessref_46', 'avg_rating': '4.181818181818182'}, {'business_ref': 'businessref_91', 'avg_rating': '4.911111111111111'}, {'business_ref': 'businessref_1', 'avg_rating': '4.333333333333333'}, {'business_ref': 'businessref_55', 'avg_rating': '4.918918918918919'}, {'business_ref': 'businessref_73', 'avg_rating': '5.0'}, {'business_ref': 'businessref_6', 'avg_rating': '4.0'}, {'business_ref': 'businessref_71', 'avg_rating': '3.268292682926829'}, {'business_ref': 'businessref_38', 'avg_rating': '3.1176470588235294'}, {'business_ref': 'businessref_32', 'avg_rating': '3.4285714285714284'}, {'business_ref': 'businessref_30', 'avg_rating': '3.6'}, {'business_ref': 'businessref_79', 'avg_rating': '4.627906976744186'}, {'business_ref': 'businessref_44', 'avg_rating': '2.9285714285714284'}, {'business_ref': 'businessref_13', 'avg_rating': '3.9166666666666665'}, {'business_ref': 'businessref_87', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_66', 'avg_rating': '2.1818181818181817'}, {'business_ref': 'businessref_9', 'avg_rating': '4.435897435897436'}, {'business_ref': 'businessref_25', 'avg_rating': '4.444444444444445'}, {'business_ref': 'businessref_2', 'avg_rating': '4.769230769230769'}, {'business_ref': 'businessref_74', 'avg_rating': '2.8333333333333335'}, {'business_ref': 'businessref_59', 'avg_rating': '4.6'}, {'business_ref': 'businessref_5', 'avg_rating': '1.6'}, {'business_ref': 'businessref_29', 'avg_rating': '3.9047619047619047'}, {'business_ref': 'businessref_58', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_39', 'avg_rating': '4.125'}, {'business_ref': 'businessref_100', 'avg_rating': '4.0'}, {'business_ref': 'businessref_81', 'avg_rating': '3.6666666666666665'}, {'business_ref': 'businessref_93', 'avg_rating': '2.857142857142857'}, {'business_ref': 'businessref_67', 'avg_rating': '3.3260869565217392'}, {'business_ref': 'businessref_15', 'avg_rating': '3.5294117647058822'}, {'business_ref': 'businessref_54', 'avg_rating': '3.5'}, {'business_ref': 'businessref_33', 'avg_rating': '3.5217391304347827'}, {'business_ref': 'businessref_89', 'avg_rating': '3.04'}, {'business_ref': 'businessref_24', 'avg_rating': '3.289473684210526'}, {'business_ref': 'businessref_36', 'avg_rating': '4.090909090909091'}, {'business_ref': 'businessref_12', 'avg_rating': '3.730769230769231'}, {'business_ref': 'businessref_60', 'avg_rating': '2.0'}, {'business_ref': 'businessref_52', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_43', 'avg_rating': '3.0476190476190474'}, {'business_ref': 'businessref_48', 'avg_rating': '3.3846153846153846'}, {'business_ref': 'businessref_17', 'avg_rating': '3.9'}, {'business_ref': 'businessref_31', 'avg_rating': '1.5'}, {'business_ref': 'businessref_78', 'avg_rating': '5.0'}, {'business_ref': 'businessref_99', 'avg_rating': '3.2'}, {'business_ref': 'businessref_51', 'avg_rating': '3.9714285714285715'}, {'business_ref': 'businessref_53', 'avg_rating': '3.7142857142857144'}, {'business_ref': 'businessref_80', 'avg_rating': '1.8888888888888888'}, {'business_ref': 'businessref_19', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_57', 'avg_rating': '1.9047619047619047'}, {'business_ref': 'businessref_85', 'avg_rating': '3.3863636363636362'}, {'business_ref': 'businessref_86', 'avg_rating': '3.739130434782609'}, {'business_ref': 'businessref_37', 'avg_rating': '3.2083333333333335'}, {'business_ref': 'businessref_42', 'avg_rating': '4.083333333333333'}, {'business_ref': 'businessref_97', 'avg_rating': '4.294117647058823'}, {'business_ref': 'businessref_8', 'avg_rating': '2.8222222222222224'}, {'business_ref': 'businessref_90', 'avg_rating': '1.0'}, {'business_ref': 'businessref_72', 'avg_rating': '4.6'}, {'business_ref': 'businessref_56', 'avg_rating': '2.3333333333333335'}, {'business_ref': 'businessref_62', 'avg_rating': '3.0'}, {'business_ref': 'businessref_95', 'avg_rating': '2.1666666666666665'}, {'business_ref': 'businessref_40', 'avg_rating': '4.476190476190476'}, {'business_ref': 'businessref_61', 'avg_rating': '2.4705882352941178'}, {'business_ref': 'businessref_92', 'avg_rating': '4.575757575757576'}, {'business_ref': 'businessref_94', 'avg_rating': '4.066666666666666'}, {'business_ref': 'businessref_7', 'avg_rating': '3.75'}, {'business_ref': 'businessref_63', 'avg_rating': '2.8333333333333335'}, {'business_ref': 'businessref_83', 'avg_rating': '4.833333333333333'}, {'business_ref': 'businessref_34', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_21', 'avg_rating': '2.0285714285714285'}, {'business_ref': 'businessref_26', 'avg_rating': '1.7083333333333333'}, {'business_ref': 'businessref_68', 'avg_rating': '1.7619047619047619'}, {'business_ref': 'businessref_88', 'avg_rating': '3.212121212121212'}, {'business_ref': 'businessref_65', 'avg_rating': '3.8333333333333335'}, {'business_ref': 'businessref_4', 'avg_rating': '5.0'}, {'business_ref': 'businessref_82', 'avg_rating': '4.309523809523809'}, {'business_ref': 'businessref_35', 'avg_rating': '4.125'}, {'business_ref': 'businessref_45', 'avg_rating': '3.3863636363636362'}, {'business_ref': 'businessref_77', 'avg_rating': '2.5476190476190474'}, {'business_ref': 'businessref_27', 'avg_rating': '3.3214285714285716'}, {'business_ref': 'businessref_50', 'avg_rating': '2.4285714285714284'}, {'business_ref': 'businessref_76', 'avg_rating': '3.5555555555555554'}, {'business_ref': 'businessref_75', 'avg_rating': '4.0'}, {'business_ref': 'businessref_96', 'avg_rating': '3.8863636363636362'}, {'business_ref': 'businessref_22', 'avg_rating': '2.8181818181818183'}, {'business_ref': 'businessref_20', 'avg_rating': '3.2142857142857144'}, {'business_ref': 'businessref_18', 'avg_rating': '1.8181818181818181'}, {'business_ref': 'businessref_14', 'avg_rating': '3.4'}, {'business_ref': 'businessref_3', 'avg_rating': '2.0'}, {'business_ref': 'businessref_69', 'avg_rating': '4.222222222222222'}, {'business_ref': 'businessref_98', 'avg_rating': '1.2'}, {'business_ref': 'businessref_28', 'avg_rating': '4.055555555555555'}, {'business_ref': 'businessref_70', 'avg_rating': '4.777777777777778'}, {'business_ref': 'businessref_64', 'avg_rating': '3.7142857142857144'}, {'business_ref': 'businessref_10', 'avg_rating': '4.1875'}, {'business_ref': 'businessref_23', 'avg_rating': '3.4444444444444446'}, {'business_ref': 'businessref_49', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_84', 'avg_rating': '5.0'}, {'business_ref': 'businessref_11', 'avg_rating': '4.2'}, {'business_ref': 'businessref_41', 'avg_rating': '4.0'}]}

exec(code, env_args)
