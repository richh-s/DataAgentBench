code = """import json, pandas as pd, re, os

# Load full Mongo result from file
path = var_call_drbBPgYqN9lqzqpJQz9X5Gxi
with open(path, 'r') as f:
    wifi_businesses = json.load(f)

wifi_df = pd.DataFrame(wifi_businesses)

# Extract WiFi-offering businesses (exclude 'no')
wifi_df['wifi_value'] = wifi_df['attributes'].apply(lambda a: a.get('WiFi') if isinstance(a, dict) else None)
wifi_df['wifi_value_clean'] = wifi_df['wifi_value'].astype(str).str.lower()
mask_offer = wifi_df['wifi_value_clean'].str.contains('free') | wifi_df['wifi_value_clean'].str.contains('paid')
wifi_df = wifi_df[mask_offer].copy()

# Parse state abbreviation from description, assuming pattern "City, ST" before country or period
state_pattern = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pattern.search(desc)
    if not m:
        return None
    return m.group(1)

wifi_df['state'] = wifi_df['description'].apply(extract_state)

# Keep only U.S. states (exclude non-US like AB). Simple filter: known US state codes
us_states = {"AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"}
wifi_df = wifi_df[wifi_df['state'].isin(us_states)].copy()

# Map business_id (businessid_x) to business_ref (businessref_x)
wifi_df['business_ref'] = wifi_df['business_id'].str.replace('businessid_', 'businessref_', regex=False)

# Load ratings
ratings_df = pd.DataFrame(var_call_6IAq5nsCqcnIbiHgH85hQOw2)
ratings_df['avg_rating'] = ratings_df['avg_rating'].astype(float)

# Join WiFi businesses with ratings
merged = pd.merge(wifi_df[['business_ref','state']], ratings_df, on='business_ref', how='left')

# Compute counts and average rating per state
state_group = merged.groupby('state').agg(business_count=('business_ref','nunique'), state_avg_rating=('avg_rating','mean')).reset_index()

# Get state with max businesses
state_group = state_group.sort_values(['business_count','state'], ascending=[False, True])

if state_group.empty:
    result = {"state": None, "business_count": 0, "average_rating": None}
else:
    top = state_group.iloc[0]
    result = {"state": top['state'], "business_count": int(top['business_count']), "average_rating": round(float(top['state_avg_rating']), 3) if pd.notnull(top['state_avg_rating']) else None}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_drbBPgYqN9lqzqpJQz9X5Gxi': 'file_storage/call_drbBPgYqN9lqzqpJQz9X5Gxi.json', 'var_call_6IAq5nsCqcnIbiHgH85hQOw2': [{'business_ref': 'businessref_79', 'avg_rating': '4.627906976744186'}, {'business_ref': 'businessref_44', 'avg_rating': '2.9285714285714284'}, {'business_ref': 'businessref_13', 'avg_rating': '3.9166666666666665'}, {'business_ref': 'businessref_87', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_66', 'avg_rating': '2.1818181818181817'}, {'business_ref': 'businessref_9', 'avg_rating': '4.435897435897436'}, {'business_ref': 'businessref_25', 'avg_rating': '4.444444444444445'}, {'business_ref': 'businessref_2', 'avg_rating': '4.769230769230769'}, {'business_ref': 'businessref_74', 'avg_rating': '2.8333333333333335'}, {'business_ref': 'businessref_59', 'avg_rating': '4.6'}, {'business_ref': 'businessref_5', 'avg_rating': '1.6'}, {'business_ref': 'businessref_29', 'avg_rating': '3.9047619047619047'}, {'business_ref': 'businessref_58', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_39', 'avg_rating': '4.125'}, {'business_ref': 'businessref_100', 'avg_rating': '4.0'}, {'business_ref': 'businessref_47', 'avg_rating': '3.9047619047619047'}, {'business_ref': 'businessref_16', 'avg_rating': '3.024390243902439'}, {'business_ref': 'businessref_46', 'avg_rating': '4.181818181818182'}, {'business_ref': 'businessref_91', 'avg_rating': '4.911111111111111'}, {'business_ref': 'businessref_1', 'avg_rating': '4.333333333333333'}, {'business_ref': 'businessref_55', 'avg_rating': '4.918918918918919'}, {'business_ref': 'businessref_73', 'avg_rating': '5.0'}, {'business_ref': 'businessref_6', 'avg_rating': '4.0'}, {'business_ref': 'businessref_71', 'avg_rating': '3.268292682926829'}, {'business_ref': 'businessref_38', 'avg_rating': '3.1176470588235294'}, {'business_ref': 'businessref_32', 'avg_rating': '3.4285714285714284'}, {'business_ref': 'businessref_30', 'avg_rating': '3.6'}, {'business_ref': 'businessref_81', 'avg_rating': '3.6666666666666665'}, {'business_ref': 'businessref_93', 'avg_rating': '2.857142857142857'}, {'business_ref': 'businessref_67', 'avg_rating': '3.3260869565217392'}, {'business_ref': 'businessref_15', 'avg_rating': '3.5294117647058822'}, {'business_ref': 'businessref_54', 'avg_rating': '3.5'}, {'business_ref': 'businessref_33', 'avg_rating': '3.5217391304347827'}, {'business_ref': 'businessref_89', 'avg_rating': '3.04'}, {'business_ref': 'businessref_24', 'avg_rating': '3.289473684210526'}, {'business_ref': 'businessref_36', 'avg_rating': '4.090909090909091'}, {'business_ref': 'businessref_12', 'avg_rating': '3.730769230769231'}, {'business_ref': 'businessref_60', 'avg_rating': '2.0'}, {'business_ref': 'businessref_52', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_31', 'avg_rating': '1.5'}, {'business_ref': 'businessref_78', 'avg_rating': '5.0'}, {'business_ref': 'businessref_99', 'avg_rating': '3.2'}, {'business_ref': 'businessref_43', 'avg_rating': '3.0476190476190474'}, {'business_ref': 'businessref_48', 'avg_rating': '3.3846153846153846'}, {'business_ref': 'businessref_17', 'avg_rating': '3.9'}, {'business_ref': 'businessref_51', 'avg_rating': '3.9714285714285715'}, {'business_ref': 'businessref_53', 'avg_rating': '3.7142857142857144'}, {'business_ref': 'businessref_80', 'avg_rating': '1.8888888888888888'}, {'business_ref': 'businessref_19', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_57', 'avg_rating': '1.9047619047619047'}, {'business_ref': 'businessref_85', 'avg_rating': '3.3863636363636362'}, {'business_ref': 'businessref_86', 'avg_rating': '3.739130434782609'}, {'business_ref': 'businessref_37', 'avg_rating': '3.2083333333333335'}, {'business_ref': 'businessref_42', 'avg_rating': '4.083333333333333'}, {'business_ref': 'businessref_97', 'avg_rating': '4.294117647058823'}, {'business_ref': 'businessref_8', 'avg_rating': '2.8222222222222224'}, {'business_ref': 'businessref_90', 'avg_rating': '1.0'}, {'business_ref': 'businessref_72', 'avg_rating': '4.6'}, {'business_ref': 'businessref_56', 'avg_rating': '2.3333333333333335'}, {'business_ref': 'businessref_62', 'avg_rating': '3.0'}, {'business_ref': 'businessref_34', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_21', 'avg_rating': '2.0285714285714285'}, {'business_ref': 'businessref_26', 'avg_rating': '1.7083333333333333'}, {'business_ref': 'businessref_68', 'avg_rating': '1.7619047619047619'}, {'business_ref': 'businessref_88', 'avg_rating': '3.212121212121212'}, {'business_ref': 'businessref_65', 'avg_rating': '3.8333333333333335'}, {'business_ref': 'businessref_4', 'avg_rating': '5.0'}, {'business_ref': 'businessref_95', 'avg_rating': '2.1666666666666665'}, {'business_ref': 'businessref_40', 'avg_rating': '4.476190476190476'}, {'business_ref': 'businessref_61', 'avg_rating': '2.4705882352941178'}, {'business_ref': 'businessref_92', 'avg_rating': '4.575757575757576'}, {'business_ref': 'businessref_94', 'avg_rating': '4.066666666666666'}, {'business_ref': 'businessref_7', 'avg_rating': '3.75'}, {'business_ref': 'businessref_63', 'avg_rating': '2.8333333333333335'}, {'business_ref': 'businessref_83', 'avg_rating': '4.833333333333333'}, {'business_ref': 'businessref_82', 'avg_rating': '4.309523809523809'}, {'business_ref': 'businessref_35', 'avg_rating': '4.125'}, {'business_ref': 'businessref_45', 'avg_rating': '3.3863636363636362'}, {'business_ref': 'businessref_77', 'avg_rating': '2.5476190476190474'}, {'business_ref': 'businessref_27', 'avg_rating': '3.3214285714285716'}, {'business_ref': 'businessref_50', 'avg_rating': '2.4285714285714284'}, {'business_ref': 'businessref_76', 'avg_rating': '3.5555555555555554'}, {'business_ref': 'businessref_75', 'avg_rating': '4.0'}, {'business_ref': 'businessref_96', 'avg_rating': '3.8863636363636362'}, {'business_ref': 'businessref_22', 'avg_rating': '2.8181818181818183'}, {'business_ref': 'businessref_20', 'avg_rating': '3.2142857142857144'}, {'business_ref': 'businessref_18', 'avg_rating': '1.8181818181818181'}, {'business_ref': 'businessref_14', 'avg_rating': '3.4'}, {'business_ref': 'businessref_3', 'avg_rating': '2.0'}, {'business_ref': 'businessref_69', 'avg_rating': '4.222222222222222'}, {'business_ref': 'businessref_98', 'avg_rating': '1.2'}, {'business_ref': 'businessref_28', 'avg_rating': '4.055555555555555'}, {'business_ref': 'businessref_70', 'avg_rating': '4.777777777777778'}, {'business_ref': 'businessref_64', 'avg_rating': '3.7142857142857144'}, {'business_ref': 'businessref_10', 'avg_rating': '4.1875'}, {'business_ref': 'businessref_23', 'avg_rating': '3.4444444444444446'}, {'business_ref': 'businessref_49', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_84', 'avg_rating': '5.0'}, {'business_ref': 'businessref_11', 'avg_rating': '4.2'}, {'business_ref': 'businessref_41', 'avg_rating': '4.0'}]}

exec(code, env_args)
