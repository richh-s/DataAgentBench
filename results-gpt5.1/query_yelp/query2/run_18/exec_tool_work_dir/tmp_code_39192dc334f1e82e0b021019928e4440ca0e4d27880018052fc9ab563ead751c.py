code = """import json, re, pandas as pd
from pathlib import Path

# Load full business data from file
file_path = var_call_Ve3BZjLicJrgX2LlnLOlLztc
with open(file_path, 'r') as f:
    business_records = json.load(f)

# Create DataFrames
biz_df = pd.DataFrame(business_records)
rev_df = pd.DataFrame(var_call_dZ9zeJB8M06sWYkNFY2DwlxP)

# Extract state abbreviation from description, assuming pattern like ", XX," or " XX " before ZIP
state_pattern = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pattern.search(desc)
    if m:
        return m.group(1)
    return None

biz_df['state'] = biz_df['description'].apply(extract_state)

# Normalize business_id to business_ref
biz_df['business_ref'] = biz_df['business_id'].str.replace('businessid_', 'businessref_', regex=False)

# Merge review aggregates with business to get states
merged = pd.merge(rev_df, biz_df[['business_ref', 'state']], on='business_ref', how='left')

# Drop rows without a state
merged = merged.dropna(subset=['state'])

# Convert types
merged['review_count'] = merged['review_count'].astype(float)
merged['avg_rating'] = merged['avg_rating'].astype(float)

# Aggregate per state: total reviews and weighted average rating
state_group = merged.groupby('state').apply(
    lambda g: pd.Series({
        'total_reviews': g['review_count'].sum(),
        'avg_rating_weighted': (g['avg_rating'] * g['review_count']).sum() / g['review_count'].sum()
    })
).reset_index()

# Find state with max reviews
top_state_row = state_group.sort_values('total_reviews', ascending=False).iloc[0]

result = {
    'state_with_most_reviews': top_state_row['state'],
    'total_reviews': float(top_state_row['total_reviews']),
    'average_business_rating_in_state': float(round(top_state_row['avg_rating_weighted'], 3))
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Ve3BZjLicJrgX2LlnLOlLztc': 'file_storage/call_Ve3BZjLicJrgX2LlnLOlLztc.json', 'var_call_dZ9zeJB8M06sWYkNFY2DwlxP': [{'business_ref': 'businessref_47', 'review_count': '42', 'avg_rating': '3.9047619047619047'}, {'business_ref': 'businessref_16', 'review_count': '41', 'avg_rating': '3.024390243902439'}, {'business_ref': 'businessref_46', 'review_count': '44', 'avg_rating': '4.181818181818182'}, {'business_ref': 'businessref_91', 'review_count': '45', 'avg_rating': '4.911111111111111'}, {'business_ref': 'businessref_1', 'review_count': '6', 'avg_rating': '4.333333333333333'}, {'business_ref': 'businessref_55', 'review_count': '37', 'avg_rating': '4.918918918918919'}, {'business_ref': 'businessref_73', 'review_count': '5', 'avg_rating': '5.0'}, {'business_ref': 'businessref_6', 'review_count': '37', 'avg_rating': '4.0'}, {'business_ref': 'businessref_71', 'review_count': '41', 'avg_rating': '3.268292682926829'}, {'business_ref': 'businessref_38', 'review_count': '17', 'avg_rating': '3.1176470588235294'}, {'business_ref': 'businessref_32', 'review_count': '7', 'avg_rating': '3.4285714285714284'}, {'business_ref': 'businessref_30', 'review_count': '5', 'avg_rating': '3.6'}, {'business_ref': 'businessref_66', 'review_count': '44', 'avg_rating': '2.1818181818181817'}, {'business_ref': 'businessref_9', 'review_count': '39', 'avg_rating': '4.435897435897436'}, {'business_ref': 'businessref_25', 'review_count': '36', 'avg_rating': '4.444444444444445'}, {'business_ref': 'businessref_2', 'review_count': '13', 'avg_rating': '4.769230769230769'}, {'business_ref': 'businessref_74', 'review_count': '6', 'avg_rating': '2.8333333333333335'}, {'business_ref': 'businessref_79', 'review_count': '43', 'avg_rating': '4.627906976744186'}, {'business_ref': 'businessref_44', 'review_count': '42', 'avg_rating': '2.9285714285714284'}, {'business_ref': 'businessref_13', 'review_count': '12', 'avg_rating': '3.9166666666666665'}, {'business_ref': 'businessref_87', 'review_count': '6', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_81', 'review_count': '6', 'avg_rating': '3.6666666666666665'}, {'business_ref': 'businessref_93', 'review_count': '7', 'avg_rating': '2.857142857142857'}, {'business_ref': 'businessref_67', 'review_count': '46', 'avg_rating': '3.3260869565217392'}, {'business_ref': 'businessref_15', 'review_count': '17', 'avg_rating': '3.5294117647058822'}, {'business_ref': 'businessref_54', 'review_count': '10', 'avg_rating': '3.5'}, {'business_ref': 'businessref_33', 'review_count': '23', 'avg_rating': '3.5217391304347827'}, {'business_ref': 'businessref_89', 'review_count': '25', 'avg_rating': '3.04'}, {'business_ref': 'businessref_24', 'review_count': '38', 'avg_rating': '3.289473684210526'}, {'business_ref': 'businessref_36', 'review_count': '44', 'avg_rating': '4.090909090909091'}, {'business_ref': 'businessref_12', 'review_count': '26', 'avg_rating': '3.730769230769231'}, {'business_ref': 'businessref_60', 'review_count': '32', 'avg_rating': '2.0'}, {'business_ref': 'businessref_52', 'review_count': '6', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_43', 'review_count': '21', 'avg_rating': '3.0476190476190474'}, {'business_ref': 'businessref_48', 'review_count': '13', 'avg_rating': '3.3846153846153846'}, {'business_ref': 'businessref_17', 'review_count': '10', 'avg_rating': '3.9'}, {'business_ref': 'businessref_31', 'review_count': '14', 'avg_rating': '1.5'}, {'business_ref': 'businessref_78', 'review_count': '6', 'avg_rating': '5.0'}, {'business_ref': 'businessref_99', 'review_count': '5', 'avg_rating': '3.2'}, {'business_ref': 'businessref_51', 'review_count': '35', 'avg_rating': '3.9714285714285715'}, {'business_ref': 'businessref_53', 'review_count': '7', 'avg_rating': '3.7142857142857144'}, {'business_ref': 'businessref_80', 'review_count': '9', 'avg_rating': '1.8888888888888888'}, {'business_ref': 'businessref_19', 'review_count': '6', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_57', 'review_count': '42', 'avg_rating': '1.9047619047619047'}, {'business_ref': 'businessref_85', 'review_count': '44', 'avg_rating': '3.3863636363636362'}, {'business_ref': 'businessref_86', 'review_count': '46', 'avg_rating': '3.739130434782609'}, {'business_ref': 'businessref_37', 'review_count': '24', 'avg_rating': '3.2083333333333335'}, {'business_ref': 'businessref_42', 'review_count': '12', 'avg_rating': '4.083333333333333'}, {'business_ref': 'businessref_97', 'review_count': '17', 'avg_rating': '4.294117647058823'}, {'business_ref': 'businessref_8', 'review_count': '45', 'avg_rating': '2.8222222222222224'}, {'business_ref': 'businessref_90', 'review_count': '3', 'avg_rating': '1.0'}, {'business_ref': 'businessref_72', 'review_count': '5', 'avg_rating': '4.6'}, {'business_ref': 'businessref_56', 'review_count': '6', 'avg_rating': '2.3333333333333335'}, {'business_ref': 'businessref_62', 'review_count': '7', 'avg_rating': '3.0'}, {'business_ref': 'businessref_95', 'review_count': '6', 'avg_rating': '2.1666666666666665'}, {'business_ref': 'businessref_40', 'review_count': '21', 'avg_rating': '4.476190476190476'}, {'business_ref': 'businessref_61', 'review_count': '17', 'avg_rating': '2.4705882352941178'}, {'business_ref': 'businessref_92', 'review_count': '33', 'avg_rating': '4.575757575757576'}, {'business_ref': 'businessref_94', 'review_count': '30', 'avg_rating': '4.066666666666666'}, {'business_ref': 'businessref_7', 'review_count': '16', 'avg_rating': '3.75'}, {'business_ref': 'businessref_63', 'review_count': '6', 'avg_rating': '2.8333333333333335'}, {'business_ref': 'businessref_83', 'review_count': '6', 'avg_rating': '4.833333333333333'}, {'business_ref': 'businessref_34', 'review_count': '9', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_21', 'review_count': '35', 'avg_rating': '2.0285714285714285'}, {'business_ref': 'businessref_26', 'review_count': '24', 'avg_rating': '1.7083333333333333'}, {'business_ref': 'businessref_68', 'review_count': '21', 'avg_rating': '1.7619047619047619'}, {'business_ref': 'businessref_88', 'review_count': '33', 'avg_rating': '3.212121212121212'}, {'business_ref': 'businessref_65', 'review_count': '18', 'avg_rating': '3.8333333333333335'}, {'business_ref': 'businessref_4', 'review_count': '7', 'avg_rating': '5.0'}, {'business_ref': 'businessref_64', 'review_count': '7', 'avg_rating': '3.7142857142857144'}, {'business_ref': 'businessref_10', 'review_count': '16', 'avg_rating': '4.1875'}, {'business_ref': 'businessref_23', 'review_count': '9', 'avg_rating': '3.4444444444444446'}, {'business_ref': 'businessref_49', 'review_count': '6', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_84', 'review_count': '4', 'avg_rating': '5.0'}, {'business_ref': 'businessref_11', 'review_count': '10', 'avg_rating': '4.2'}, {'business_ref': 'businessref_41', 'review_count': '4', 'avg_rating': '4.0'}, {'business_ref': 'businessref_82', 'review_count': '42', 'avg_rating': '4.309523809523809'}, {'business_ref': 'businessref_35', 'review_count': '8', 'avg_rating': '4.125'}, {'business_ref': 'businessref_45', 'review_count': '44', 'avg_rating': '3.3863636363636362'}, {'business_ref': 'businessref_59', 'review_count': '30', 'avg_rating': '4.6'}, {'business_ref': 'businessref_5', 'review_count': '5', 'avg_rating': '1.6'}, {'business_ref': 'businessref_29', 'review_count': '21', 'avg_rating': '3.9047619047619047'}, {'business_ref': 'businessref_58', 'review_count': '6', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_39', 'review_count': '8', 'avg_rating': '4.125'}, {'business_ref': 'businessref_100', 'review_count': '4', 'avg_rating': '4.0'}, {'business_ref': 'businessref_96', 'review_count': '44', 'avg_rating': '3.8863636363636362'}, {'business_ref': 'businessref_22', 'review_count': '11', 'avg_rating': '2.8181818181818183'}, {'business_ref': 'businessref_20', 'review_count': '42', 'avg_rating': '3.2142857142857144'}, {'business_ref': 'businessref_18', 'review_count': '11', 'avg_rating': '1.8181818181818181'}, {'business_ref': 'businessref_14', 'review_count': '25', 'avg_rating': '3.4'}, {'business_ref': 'businessref_3', 'review_count': '4', 'avg_rating': '2.0'}, {'business_ref': 'businessref_69', 'review_count': '9', 'avg_rating': '4.222222222222222'}, {'business_ref': 'businessref_98', 'review_count': '5', 'avg_rating': '1.2'}, {'business_ref': 'businessref_28', 'review_count': '18', 'avg_rating': '4.055555555555555'}, {'business_ref': 'businessref_70', 'review_count': '9', 'avg_rating': '4.777777777777778'}, {'business_ref': 'businessref_77', 'review_count': '42', 'avg_rating': '2.5476190476190474'}, {'business_ref': 'businessref_27', 'review_count': '28', 'avg_rating': '3.3214285714285716'}, {'business_ref': 'businessref_50', 'review_count': '7', 'avg_rating': '2.4285714285714284'}, {'business_ref': 'businessref_76', 'review_count': '9', 'avg_rating': '3.5555555555555554'}, {'business_ref': 'businessref_75', 'review_count': '5', 'avg_rating': '4.0'}]}

exec(code, env_args)
