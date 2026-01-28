code = """import json
import pandas as pd
import re

# Load business records from the provided JSON file path
business_filepath = var_call_1Plp48T8J2xfzr0cih1BZzK4
with open(business_filepath, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# Load reviews records from provided JSON file path
reviews_filepath = var_call_raJucT0UJR5M4hdDYZzFlbzV
with open(reviews_filepath, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Create DataFrames
df_biz = pd.DataFrame(businesses)
# Keep only business_id and description
df_biz = df_biz[["business_id", "description"]]

# Function to extract state (2-letter) from description
state_pattern = re.compile(r",\s*([A-Z]{2})(?:[,\s]|$)")

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pattern.search(desc)
    if m:
        return m.group(1)
    # try alternate pattern: ' in City, ST' explicit
    m2 = re.search(r"in [^,]+,\s*([A-Z]{2})", desc)
    if m2:
        return m2.group(1)
    return None

df_biz['state'] = df_biz['description'].apply(extract_state)
# Drop businesses with no detected state
df_biz = df_biz.dropna(subset=['state'])

# Map business_id (businessid_#) to business_ref_#
# Convert 'businessid_49' -> 'businessref_49'
df_biz['business_ref'] = df_biz['business_id'].str.replace('businessid_', 'businessref_', regex=False)

# Reviews DataFrame
df_rev = pd.DataFrame(reviews)
# Ensure rating numeric
df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
# Drop rows with missing business_ref or rating
df_rev = df_rev.dropna(subset=['business_ref', 'rating'])

# Merge reviews with business states
merged = df_rev.merge(df_biz[['business_ref', 'state']], on='business_ref', how='left')
# Drop reviews where state is missing (no matching business)
merged = merged.dropna(subset=['state'])

# Group by state to compute total reviews and average rating
grp = merged.groupby('state').agg(total_reviews=('rating', 'count'), avg_rating=('rating', 'mean')).reset_index()
# If no data, handle
if grp.empty:
    result = {'state': None, 'total_reviews': 0, 'avg_rating': None}
else:
    # Find state with max total_reviews
    max_row = grp.loc[grp['total_reviews'].idxmax()]
    # Format avg_rating as float with reasonable precision
    result = {
        'state': str(max_row['state']),
        'total_reviews': int(max_row['total_reviews']),
        'avg_rating': float(round(max_row['avg_rating'], 4))
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gSp5XcdiWERe0bZgTL2OQjXx': ['business', 'checkin'], 'var_call_cYXxmYHmTDf9QCeiedERkIxV': ['review', 'tip', 'user'], 'var_call_1Plp48T8J2xfzr0cih1BZzK4': 'file_storage/call_1Plp48T8J2xfzr0cih1BZzK4.json', 'var_call_nAr23XJk3f3aTiVvZsQhbOEG': [{'business_ref': 'businessref_95', 'review_count_state': '6', 'avg_rating': '2.1666666666666665'}, {'business_ref': 'businessref_40', 'review_count_state': '21', 'avg_rating': '4.476190476190476'}, {'business_ref': 'businessref_61', 'review_count_state': '17', 'avg_rating': '2.4705882352941178'}, {'business_ref': 'businessref_92', 'review_count_state': '33', 'avg_rating': '4.575757575757576'}, {'business_ref': 'businessref_94', 'review_count_state': '30', 'avg_rating': '4.066666666666666'}, {'business_ref': 'businessref_7', 'review_count_state': '16', 'avg_rating': '3.75'}, {'business_ref': 'businessref_63', 'review_count_state': '6', 'avg_rating': '2.8333333333333335'}, {'business_ref': 'businessref_83', 'review_count_state': '6', 'avg_rating': '4.833333333333333'}, {'business_ref': 'businessref_64', 'review_count_state': '7', 'avg_rating': '3.7142857142857144'}, {'business_ref': 'businessref_10', 'review_count_state': '16', 'avg_rating': '4.1875'}, {'business_ref': 'businessref_23', 'review_count_state': '9', 'avg_rating': '3.4444444444444446'}, {'business_ref': 'businessref_49', 'review_count_state': '6', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_84', 'review_count_state': '4', 'avg_rating': '5.0'}, {'business_ref': 'businessref_11', 'review_count_state': '10', 'avg_rating': '4.2'}, {'business_ref': 'businessref_41', 'review_count_state': '4', 'avg_rating': '4.0'}, {'business_ref': 'businessref_47', 'review_count_state': '42', 'avg_rating': '3.9047619047619047'}, {'business_ref': 'businessref_16', 'review_count_state': '41', 'avg_rating': '3.024390243902439'}, {'business_ref': 'businessref_46', 'review_count_state': '44', 'avg_rating': '4.181818181818182'}, {'business_ref': 'businessref_91', 'review_count_state': '45', 'avg_rating': '4.911111111111111'}, {'business_ref': 'businessref_1', 'review_count_state': '6', 'avg_rating': '4.333333333333333'}, {'business_ref': 'businessref_55', 'review_count_state': '37', 'avg_rating': '4.918918918918919'}, {'business_ref': 'businessref_73', 'review_count_state': '5', 'avg_rating': '5.0'}, {'business_ref': 'businessref_6', 'review_count_state': '37', 'avg_rating': '4.0'}, {'business_ref': 'businessref_71', 'review_count_state': '41', 'avg_rating': '3.268292682926829'}, {'business_ref': 'businessref_38', 'review_count_state': '17', 'avg_rating': '3.1176470588235294'}, {'business_ref': 'businessref_32', 'review_count_state': '7', 'avg_rating': '3.4285714285714284'}, {'business_ref': 'businessref_30', 'review_count_state': '5', 'avg_rating': '3.6'}, {'business_ref': 'businessref_82', 'review_count_state': '42', 'avg_rating': '4.309523809523809'}, {'business_ref': 'businessref_35', 'review_count_state': '8', 'avg_rating': '4.125'}, {'business_ref': 'businessref_45', 'review_count_state': '44', 'avg_rating': '3.3863636363636362'}, {'business_ref': 'businessref_79', 'review_count_state': '43', 'avg_rating': '4.627906976744186'}, {'business_ref': 'businessref_44', 'review_count_state': '42', 'avg_rating': '2.9285714285714284'}, {'business_ref': 'businessref_13', 'review_count_state': '12', 'avg_rating': '3.9166666666666665'}, {'business_ref': 'businessref_87', 'review_count_state': '6', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_34', 'review_count_state': '9', 'avg_rating': '3.3333333333333335'}, {'business_ref': 'businessref_21', 'review_count_state': '35', 'avg_rating': '2.0285714285714285'}, {'business_ref': 'businessref_26', 'review_count_state': '24', 'avg_rating': '1.7083333333333333'}, {'business_ref': 'businessref_68', 'review_count_state': '21', 'avg_rating': '1.7619047619047619'}, {'business_ref': 'businessref_88', 'review_count_state': '33', 'avg_rating': '3.212121212121212'}, {'business_ref': 'businessref_65', 'review_count_state': '18', 'avg_rating': '3.8333333333333335'}, {'business_ref': 'businessref_4', 'review_count_state': '7', 'avg_rating': '5.0'}, {'business_ref': 'businessref_77', 'review_count_state': '42', 'avg_rating': '2.5476190476190474'}, {'business_ref': 'businessref_27', 'review_count_state': '28', 'avg_rating': '3.3214285714285716'}, {'business_ref': 'businessref_50', 'review_count_state': '7', 'avg_rating': '2.4285714285714284'}, {'business_ref': 'businessref_76', 'review_count_state': '9', 'avg_rating': '3.5555555555555554'}, {'business_ref': 'businessref_75', 'review_count_state': '5', 'avg_rating': '4.0'}, {'business_ref': 'businessref_66', 'review_count_state': '44', 'avg_rating': '2.1818181818181817'}, {'business_ref': 'businessref_9', 'review_count_state': '39', 'avg_rating': '4.435897435897436'}, {'business_ref': 'businessref_25', 'review_count_state': '36', 'avg_rating': '4.444444444444445'}, {'business_ref': 'businessref_2', 'review_count_state': '13', 'avg_rating': '4.769230769230769'}, {'business_ref': 'businessref_74', 'review_count_state': '6', 'avg_rating': '2.8333333333333335'}, {'business_ref': 'businessref_96', 'review_count_state': '44', 'avg_rating': '3.8863636363636362'}, {'business_ref': 'businessref_22', 'review_count_state': '11', 'avg_rating': '2.8181818181818183'}, {'business_ref': 'businessref_20', 'review_count_state': '42', 'avg_rating': '3.2142857142857144'}, {'business_ref': 'businessref_18', 'review_count_state': '11', 'avg_rating': '1.8181818181818181'}, {'business_ref': 'businessref_14', 'review_count_state': '25', 'avg_rating': '3.4'}, {'business_ref': 'businessref_3', 'review_count_state': '4', 'avg_rating': '2.0'}, {'business_ref': 'businessref_69', 'review_count_state': '9', 'avg_rating': '4.222222222222222'}, {'business_ref': 'businessref_98', 'review_count_state': '5', 'avg_rating': '1.2'}, {'business_ref': 'businessref_28', 'review_count_state': '18', 'avg_rating': '4.055555555555555'}, {'business_ref': 'businessref_70', 'review_count_state': '9', 'avg_rating': '4.777777777777778'}, {'business_ref': 'businessref_59', 'review_count_state': '30', 'avg_rating': '4.6'}, {'business_ref': 'businessref_5', 'review_count_state': '5', 'avg_rating': '1.6'}, {'business_ref': 'businessref_29', 'review_count_state': '21', 'avg_rating': '3.9047619047619047'}, {'business_ref': 'businessref_58', 'review_count_state': '6', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_39', 'review_count_state': '8', 'avg_rating': '4.125'}, {'business_ref': 'businessref_100', 'review_count_state': '4', 'avg_rating': '4.0'}, {'business_ref': 'businessref_81', 'review_count_state': '6', 'avg_rating': '3.6666666666666665'}, {'business_ref': 'businessref_93', 'review_count_state': '7', 'avg_rating': '2.857142857142857'}, {'business_ref': 'businessref_67', 'review_count_state': '46', 'avg_rating': '3.3260869565217392'}, {'business_ref': 'businessref_15', 'review_count_state': '17', 'avg_rating': '3.5294117647058822'}, {'business_ref': 'businessref_54', 'review_count_state': '10', 'avg_rating': '3.5'}, {'business_ref': 'businessref_33', 'review_count_state': '23', 'avg_rating': '3.5217391304347827'}, {'business_ref': 'businessref_89', 'review_count_state': '25', 'avg_rating': '3.04'}, {'business_ref': 'businessref_24', 'review_count_state': '38', 'avg_rating': '3.289473684210526'}, {'business_ref': 'businessref_36', 'review_count_state': '44', 'avg_rating': '4.090909090909091'}, {'business_ref': 'businessref_12', 'review_count_state': '26', 'avg_rating': '3.730769230769231'}, {'business_ref': 'businessref_60', 'review_count_state': '32', 'avg_rating': '2.0'}, {'business_ref': 'businessref_52', 'review_count_state': '6', 'avg_rating': '4.166666666666667'}, {'business_ref': 'businessref_43', 'review_count_state': '21', 'avg_rating': '3.0476190476190474'}, {'business_ref': 'businessref_48', 'review_count_state': '13', 'avg_rating': '3.3846153846153846'}, {'business_ref': 'businessref_17', 'review_count_state': '10', 'avg_rating': '3.9'}, {'business_ref': 'businessref_31', 'review_count_state': '14', 'avg_rating': '1.5'}, {'business_ref': 'businessref_78', 'review_count_state': '6', 'avg_rating': '5.0'}, {'business_ref': 'businessref_99', 'review_count_state': '5', 'avg_rating': '3.2'}, {'business_ref': 'businessref_57', 'review_count_state': '42', 'avg_rating': '1.9047619047619047'}, {'business_ref': 'businessref_85', 'review_count_state': '44', 'avg_rating': '3.3863636363636362'}, {'business_ref': 'businessref_86', 'review_count_state': '46', 'avg_rating': '3.739130434782609'}, {'business_ref': 'businessref_37', 'review_count_state': '24', 'avg_rating': '3.2083333333333335'}, {'business_ref': 'businessref_42', 'review_count_state': '12', 'avg_rating': '4.083333333333333'}, {'business_ref': 'businessref_97', 'review_count_state': '17', 'avg_rating': '4.294117647058823'}, {'business_ref': 'businessref_8', 'review_count_state': '45', 'avg_rating': '2.8222222222222224'}, {'business_ref': 'businessref_90', 'review_count_state': '3', 'avg_rating': '1.0'}, {'business_ref': 'businessref_72', 'review_count_state': '5', 'avg_rating': '4.6'}, {'business_ref': 'businessref_56', 'review_count_state': '6', 'avg_rating': '2.3333333333333335'}, {'business_ref': 'businessref_62', 'review_count_state': '7', 'avg_rating': '3.0'}, {'business_ref': 'businessref_51', 'review_count_state': '35', 'avg_rating': '3.9714285714285715'}, {'business_ref': 'businessref_53', 'review_count_state': '7', 'avg_rating': '3.7142857142857144'}, {'business_ref': 'businessref_80', 'review_count_state': '9', 'avg_rating': '1.8888888888888888'}, {'business_ref': 'businessref_19', 'review_count_state': '6', 'avg_rating': '3.3333333333333335'}], 'var_call_raJucT0UJR5M4hdDYZzFlbzV': 'file_storage/call_raJucT0UJR5M4hdDYZzFlbzV.json'}

exec(code, env_args)
