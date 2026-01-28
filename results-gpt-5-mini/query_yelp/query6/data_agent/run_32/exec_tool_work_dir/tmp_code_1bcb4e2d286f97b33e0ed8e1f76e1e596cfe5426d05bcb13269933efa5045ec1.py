code = """import json
import pandas as pd

# Load review data from storage variable
reviews = var_call_fzyEeGvWAZ1fGnR6HrJvcDBS
reviews_df = pd.DataFrame(reviews)
# Ensure ratings are integers
reviews_df['rating'] = reviews_df['rating'].astype(int)
# Convert business_ref to business_id format
reviews_df['business_id'] = reviews_df['business_ref'].str.replace('businessref_', 'businessid_')

# Aggregate ratings per business within the period
agg = reviews_df.groupby('business_id').agg(review_count=('rating','size'), avg_rating=('rating','mean')).reset_index()
# Filter businesses with at least 5 reviews
agg_filtered = agg[agg['review_count'] >= 5]

# Load business collection from JSON file path in storage
with open(var_call_BCG2Ia7wN4MkF2hepBlPlspM, 'r') as f:
    business_list = json.load(f)
business_df = pd.DataFrame(business_list)
# Keep only relevant fields
business_df = business_df[['business_id', 'name', 'description']]

# Merge aggregated ratings with business metadata
merged = pd.merge(agg_filtered, business_df, on='business_id', how='left')

result_list = []
if merged.empty:
    result = {"message": "No businesses with at least 5 reviews in the specified period."}
else:
    # Find highest average rating
    max_avg = merged['avg_rating'].max()
    winners = merged[merged['avg_rating'] == max_avg]

    # Helper to extract categories from description by taking substring after last ' in '
    def extract_categories(desc):
        if not isinstance(desc, str):
            return None
        idx = desc.rfind(' in ')
        if idx == -1:
            cat = desc
        else:
            cat = desc[idx+4:]
        cat = cat.strip()
        if cat.endswith('.'):
            cat = cat[:-1]
        return cat

    for _, row in winners.iterrows():
        categories = extract_categories(row.get('description'))
        result_list.append({
            'business_id': row['business_id'],
            'name': row.get('name'),
            'avg_rating': round(float(row['avg_rating']), 3),
            'review_count': int(row['review_count']),
            'categories': categories
        })
    result = {'top_average': round(float(max_avg),3), 'businesses': result_list}

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_fzyEeGvWAZ1fGnR6HrJvcDBS': [{'business_ref': 'businessref_16', 'rating': '1'}, {'business_ref': 'businessref_23', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_96', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '5'}, {'business_ref': 'businessref_47', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '4'}, {'business_ref': 'businessref_43', 'rating': '4'}, {'business_ref': 'businessref_14', 'rating': '3'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_16', 'rating': '3'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_30', 'rating': '2'}, {'business_ref': 'businessref_81', 'rating': '1'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_31', 'rating': '1'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_99', 'rating': '5'}, {'business_ref': 'businessref_40', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_11', 'rating': '5'}, {'business_ref': 'businessref_21', 'rating': '1'}, {'business_ref': 'businessref_9', 'rating': '5'}, {'business_ref': 'businessref_8', 'rating': '3'}, {'business_ref': 'businessref_46', 'rating': '5'}, {'business_ref': 'businessref_68', 'rating': '1'}, {'business_ref': 'businessref_88', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '2'}, {'business_ref': 'businessref_71', 'rating': '1'}, {'business_ref': 'businessref_28', 'rating': '5'}, {'business_ref': 'businessref_71', 'rating': '5'}, {'business_ref': 'businessref_37', 'rating': '5'}, {'business_ref': 'businessref_9', 'rating': '3'}, {'business_ref': 'businessref_17', 'rating': '5'}, {'business_ref': 'businessref_82', 'rating': '4'}], 'var_call_XygpdiWJxNhNtwYXVcvW7SP1': ['business', 'checkin'], 'var_call_BCG2Ia7wN4MkF2hepBlPlspM': 'file_storage/call_BCG2Ia7wN4MkF2hepBlPlspM.json'}

exec(code, env_args)
