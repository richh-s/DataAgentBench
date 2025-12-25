code = """import json, pandas as pd, os

# Load full business result from file
path = var_call_LwtcOXGrJP4oxxhLznZq3lYs
if isinstance(path, str) and os.path.isfile(path):
    with open(path, 'r') as f:
        business_records = json.load(f)
else:
    business_records = var_call_LwtcOXGrJP4oxxhLznZq3lYs

biz_df = pd.DataFrame(business_records)[['business_id','review_count','description']]

# Extract US state from description by looking for patterns 
state_abbrevs = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

import re

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # Look for ", XX" where XX is state
    m = re.search(r",\s+([A-Z]{2})\b", desc)
    if m and m.group(1) in state_abbrevs:
        return m.group(1)
    # Also handle patterns like "This Philadelphia, PA location"
    m = re.search(r"\b([A-Z][a-zA-Z]+),\s+([A-Z]{2})\b", desc)
    if m and m.group(2) in state_abbrevs:
        return m.group(2)
    return None

biz_df['state'] = biz_df['description'].apply(extract_state)

# Normalize review_count to int
biz_df['review_count'] = pd.to_numeric(biz_df['review_count'], errors='coerce').fillna(0).astype(int)

# Aggregate total reviews per state (using business review_count as proxy for number of reviews)
state_reviews = biz_df.groupby('state', dropna=True)['review_count'].sum().reset_index()

# Map review aggregates from review table to businesses and then to states
rev_df = pd.DataFrame(var_call_jl7ECRmNcsB3IFjXkKOTjSNv)
# derive business_id from business_ref
rev_df['business_id'] = rev_df['business_ref'].str.replace('businessref_','businessid_', regex=False)

# convert types
rev_df['review_num'] = pd.to_numeric(rev_df['review_num'])
rev_df['avg_rating'] = pd.to_numeric(rev_df['avg_rating'])

# join with biz_df to get state per business
merged = pd.merge(rev_df, biz_df[['business_id','state']], on='business_id', how='left')

# compute total number of reviews per state from actual review table
state_reviews_from_reviews = merged.groupby('state', dropna=True)['review_num'].sum().reset_index(name='total_reviews')

# identify state with max reviews
idx = state_reviews_from_reviews['total_reviews'].idxmax()
max_state = state_reviews_from_reviews.loc[idx, 'state']

# compute average rating of businesses in that state (weighted by number of reviews)
state_subset = merged[merged['state'] == max_state]
weighted_avg = (state_subset['avg_rating'] * state_subset['review_num']).sum() / state_subset['review_num'].sum()

result = {
    'state_with_most_reviews': max_state,
    'total_reviews_in_state': int(state_reviews_from_reviews.loc[idx, 'total_reviews']),
    'average_rating_in_state': round(float(weighted_avg), 3)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_LwtcOXGrJP4oxxhLznZq3lYs': 'file_storage/call_LwtcOXGrJP4oxxhLznZq3lYs.json', 'var_call_jl7ECRmNcsB3IFjXkKOTjSNv': [{'business_ref': 'businessref_47', 'review_num': '42', 'avg_rating': '3.9047619047619047'}, {'business_ref': 'businessref_16', 'review_num': '41', 'avg_rating': '3.024390243902439'}, {'business_ref': 'businessref_46', 'review_num': '44', 'avg_rating': '4.181818181818182'}, {'business_ref': 'businessref_91', 'review_num': '45', 'avg_rating': '4.911111111111111'}, {'business_ref': 'businessref_1', 'review_num': '6', 'avg_rating': '4.333333333333333'}, {'business_ref': 'businessref_55', 'review_num': '37', 'avg_rating': '4.918918918918919'}, {'business_ref': 'businessref_73', 'review_num': '5', 'avg_rating': '5.0'}, {'business_ref': 'businessref_6', 'review_num': '37', 'avg_rating': '4.0'}, {'business_ref': 'businessref_71', 'review_num': '41', 'avg_rating': '3.268292682926829'}, {'business_ref': 'businessref_38', 'review_num': '17', 'avg_rating': '3.1176470588235294'}, {'business_ref': 'businessref_32', 'review_num': '7', 'avg_rating': '3.4285714285714284'}, {'business_ref': 'businessref_30', 'review_num': '5', 'avg_rating': '3.6'}, {'business_ref': 'businessref_66', 'review_num': '44', 'avg_rating': '2.1818181818181817'}, {'business_ref': 'businessref_9', 'review_num': '39', 'avg_rating': '4.435897435897436'}, {'business_ref': 'businessref_25', 'review_num': '36', 'avg_rating': '4.444444444444445'}, {'business_ref': 'businessref_2', 'review_num': '13', 'avg_rating': '4.769230769230769'}, {'business_ref': 'businessref_74', 'review_num': '6', 'avg_rating': '2.8333333333333335'}, {'business_ref': 'businessref_81', 'review_num': '6', 'avg_rating': '3.6666666666666665'}, {'business_ref': 'businessref_93', 'review_num': '7', 'avg_rating': '2.857142857142857'}, {'business_ref': 'businessref_67', 'review_num': '46', 'avg_rating': '3.3260869565217392'}, {'business_ref': 'businessref_15', 'review_num': '17', 'avg_rating': '3.5294117647058822'}, {'business_ref': 'businessref_54', 'review_num': '10', 'avg_rating': '3.5'}, {'business_ref': 'businessref_33', 'review_num': '23', 'avg_rating': '3.5217391304347827'}, {'business_ref': 'businessref_89', 'review_num': '25', 'avg_rating': '3.04'}, {'business_ref': 'businessref_24', 'review_num': '38', 'avg_rating': '3.289473684210526'}, {'business_ref': 'businessref_36', 'review_num': '44', 'avg_rating': '4.090909090909091'}, {'business_ref': 'businessref_12', 'review_num': '26', 'avg_rating': '3.730769230769231'}, {'business_ref': 'businessref_60', 'review_num': '32', 'avg_rating': '2.0'}, {'business_ref': 'businessref_52', 'review_num': '6', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_43', 'review_num': '21', 'avg_rating': '3.0476190476190474'}, {'business_ref': 'businessref_48', 'review_num': '13', 'avg_rating': '3.3846153846153846'}, {'business_ref': 'businessref_17', 'review_num': '10', 'avg_rating': '3.9'}, {'business_ref': 'businessref_31', 'review_num': '14', 'avg_rating': '1.5'}, {'business_ref': 'businessref_78', 'review_num': '6', 'avg_rating': '5.0'}, {'business_ref': 'businessref_99', 'review_num': '5', 'avg_rating': '3.2'}, {'business_ref': 'businessref_59', 'review_num': '30', 'avg_rating': '4.6'}, {'business_ref': 'businessref_5', 'review_num': '5', 'avg_rating': '1.6'}, {'business_ref': 'businessref_29', 'review_num': '21', 'avg_rating': '3.9047619047619047'}, {'business_ref': 'businessref_58', 'review_num': '6', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_39', 'review_num': '8', 'avg_rating': '4.125'}, {'business_ref': 'businessref_100', 'review_num': '4', 'avg_rating': '4.0'}, {'business_ref': 'businessref_51', 'review_num': '35', 'avg_rating': '3.9714285714285715'}, {'business_ref': 'businessref_53', 'review_num': '7', 'avg_rating': '3.7142857142857144'}, {'business_ref': 'businessref_80', 'review_num': '9', 'avg_rating': '1.8888888888888888'}, {'business_ref': 'businessref_19', 'review_num': '6', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_95', 'review_num': '6', 'avg_rating': '2.1666666666666665'}, {'business_ref': 'businessref_40', 'review_num': '21', 'avg_rating': '4.476190476190476'}, {'business_ref': 'businessref_61', 'review_num': '17', 'avg_rating': '2.4705882352941178'}, {'business_ref': 'businessref_92', 'review_num': '33', 'avg_rating': '4.575757575757576'}, {'business_ref': 'businessref_94', 'review_num': '30', 'avg_rating': '4.066666666666666'}, {'business_ref': 'businessref_7', 'review_num': '16', 'avg_rating': '3.75'}, {'business_ref': 'businessref_63', 'review_num': '6', 'avg_rating': '2.8333333333333335'}, {'business_ref': 'businessref_83', 'review_num': '6', 'avg_rating': '4.833333333333333'}, {'business_ref': 'businessref_57', 'review_num': '42', 'avg_rating': '1.9047619047619047'}, {'business_ref': 'businessref_85', 'review_num': '44', 'avg_rating': '3.3863636363636362'}, {'business_ref': 'businessref_86', 'review_num': '46', 'avg_rating': '3.739130434782609'}, {'business_ref': 'businessref_37', 'review_num': '24', 'avg_rating': '3.2083333333333335'}, {'business_ref': 'businessref_42', 'review_num': '12', 'avg_rating': '4.083333333333333'}, {'business_ref': 'businessref_97', 'review_num': '17', 'avg_rating': '4.294117647058823'}, {'business_ref': 'businessref_8', 'review_num': '45', 'avg_rating': '2.8222222222222224'}, {'business_ref': 'businessref_90', 'review_num': '3', 'avg_rating': '1.0'}, {'business_ref': 'businessref_72', 'review_num': '5', 'avg_rating': '4.6'}, {'business_ref': 'businessref_56', 'review_num': '6', 'avg_rating': '2.3333333333333335'}, {'business_ref': 'businessref_62', 'review_num': '7', 'avg_rating': '3.0'}, {'business_ref': 'businessref_64', 'review_num': '7', 'avg_rating': '3.7142857142857144'}, {'business_ref': 'businessref_10', 'review_num': '16', 'avg_rating': '4.1875'}, {'business_ref': 'businessref_23', 'review_num': '9', 'avg_rating': '3.4444444444444446'}, {'business_ref': 'businessref_49', 'review_num': '6', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_84', 'review_num': '4', 'avg_rating': '5.0'}, {'business_ref': 'businessref_11', 'review_num': '10', 'avg_rating': '4.2'}, {'business_ref': 'businessref_41', 'review_num': '4', 'avg_rating': '4.0'}, {'business_ref': 'businessref_82', 'review_num': '42', 'avg_rating': '4.309523809523809'}, {'business_ref': 'businessref_35', 'review_num': '8', 'avg_rating': '4.125'}, {'business_ref': 'businessref_45', 'review_num': '44', 'avg_rating': '3.3863636363636362'}, {'business_ref': 'businessref_77', 'review_num': '42', 'avg_rating': '2.5476190476190474'}, {'business_ref': 'businessref_27', 'review_num': '28', 'avg_rating': '3.3214285714285716'}, {'business_ref': 'businessref_50', 'review_num': '7', 'avg_rating': '2.4285714285714284'}, {'business_ref': 'businessref_76', 'review_num': '9', 'avg_rating': '3.5555555555555554'}, {'business_ref': 'businessref_75', 'review_num': '5', 'avg_rating': '4.0'}, {'business_ref': 'businessref_96', 'review_num': '44', 'avg_rating': '3.8863636363636362'}, {'business_ref': 'businessref_22', 'review_num': '11', 'avg_rating': '2.8181818181818183'}, {'business_ref': 'businessref_20', 'review_num': '42', 'avg_rating': '3.2142857142857144'}, {'business_ref': 'businessref_18', 'review_num': '11', 'avg_rating': '1.8181818181818181'}, {'business_ref': 'businessref_14', 'review_num': '25', 'avg_rating': '3.4'}, {'business_ref': 'businessref_3', 'review_num': '4', 'avg_rating': '2.0'}, {'business_ref': 'businessref_69', 'review_num': '9', 'avg_rating': '4.222222222222222'}, {'business_ref': 'businessref_98', 'review_num': '5', 'avg_rating': '1.2'}, {'business_ref': 'businessref_28', 'review_num': '18', 'avg_rating': '4.055555555555555'}, {'business_ref': 'businessref_70', 'review_num': '9', 'avg_rating': '4.777777777777778'}, {'business_ref': 'businessref_79', 'review_num': '43', 'avg_rating': '4.627906976744186'}, {'business_ref': 'businessref_44', 'review_num': '42', 'avg_rating': '2.9285714285714284'}, {'business_ref': 'businessref_13', 'review_num': '12', 'avg_rating': '3.9166666666666665'}, {'business_ref': 'businessref_87', 'review_num': '6', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_34', 'review_num': '9', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_21', 'review_num': '35', 'avg_rating': '2.0285714285714285'}, {'business_ref': 'businessref_26', 'review_num': '24', 'avg_rating': '1.7083333333333333'}, {'business_ref': 'businessref_68', 'review_num': '21', 'avg_rating': '1.7619047619047619'}, {'business_ref': 'businessref_88', 'review_num': '33', 'avg_rating': '3.212121212121212'}, {'business_ref': 'businessref_65', 'review_num': '18', 'avg_rating': '3.8333333333333335'}, {'business_ref': 'businessref_4', 'review_num': '7', 'avg_rating': '5.0'}]}

exec(code, env_args)
