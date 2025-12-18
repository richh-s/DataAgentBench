code = """import pandas as pd
import re
import json

business_data_path = locals()['var_function-call-3946981326793507827']
with open(business_data_path, 'r') as f:
    business_data = json.load(f)

review_data_path = locals()['var_function-call-11093514392210888319']
with open(review_data_path, 'r') as f:
    review_data = json.load(f)

business_df = pd.DataFrame(business_data)
review_df = pd.DataFrame(review_data)

# Extract state from description using a more robust regex
def extract_state(description):
    if description:
        match = re.search(r'(?:in |\b)([A-Z]{2})(?:, |$|\.)', description)
        if match:
            return match.group(1)
    return None

business_df['state'] = business_df['description'].apply(extract_state)
business_df['review_count'] = pd.to_numeric(business_df['review_count'], errors='coerce').fillna(0).astype(int)

# Filter out rows where state is None before grouping
state_review_counts = business_df.dropna(subset=['state']).groupby('state')['review_count'].sum().reset_index()

if not state_review_counts.empty:
    highest_reviews_state = state_review_counts.loc[state_review_counts['review_count'].idxmax()]
    # Filter businesses in the highest review state
    businesses_in_highest_reviews_state = business_df[business_df['state'] == highest_reviews_state['state']]
    business_ids_in_highest_reviews_state = businesses_in_highest_reviews_state['business_id'].tolist()
    # Convert business_ids to the 'businessref_' format for joining with the review table
    business_refs_in_highest_reviews_state = [bid.replace("businessid_", "businessref_") for bid in business_ids_in_highest_reviews_state]

    # Filter reviews for businesses in the highest review state
    reviews_in_highest_reviews_state = review_df[review_df['business_ref'].isin(business_refs_in_highest_reviews_state)]
    reviews_in_highest_reviews_state['rating'] = pd.to_numeric(reviews_in_highest_reviews_state['rating'], errors='coerce')
    average_rating = reviews_in_highest_reviews_state['rating'].mean()

    print('__RESULT__:')
    print(json.dumps({
        'highest_reviews_state': highest_reviews_state['state'],
        'total_review_count': highest_reviews_state['review_count'],
        'average_rating': average_rating
    }))
else:
    print('__RESULT__:')
    print(json.dumps({
        'highest_reviews_state': None,
        'total_review_count': 0,
        'average_rating': None
    }))"""

env_args = {'var_function-call-9618331980219053062': 'file_storage/function-call-9618331980219053062.json', 'var_function-call-6370443003077374768': 'file_storage/function-call-6370443003077374768.json', 'var_function-call-16808447539076397221': {'highest_reviews_state': None, 'business_refs_in_highest_reviews_state': []}, 'var_function-call-7770531584723226662': 'file_storage/function-call-7770531584723226662.json', 'var_function-call-11093514392210888319': 'file_storage/function-call-11093514392210888319.json', 'var_function-call-9392684596927445495': {'highest_reviews_state': None, 'total_review_count': 0, 'average_rating': None}, 'var_function-call-3946981326793507827': 'file_storage/function-call-3946981326793507827.json'}

exec(code, env_args)
