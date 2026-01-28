code = """import json
import pandas as pd

# Load review data from previous query (available as var_call_UyE2t6TmDPXZTkdCnrEZWwJM)
reviews = var_call_UyE2t6TmDPXZTkdCnrEZWwJM

# Load business data from the JSON file path (var_call_TYtFlxaMhRoWxF0pfIjfA5Jx)
business_file_path = var_call_TYtFlxaMhRoWxF0pfIjfA5Jx
with open(business_file_path, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# Create DataFrames
rev_df = pd.DataFrame(reviews)
# Ensure rating numeric
rev_df['rating'] = rev_df['rating'].astype(int)

# Aggregate by business_ref
agg = rev_df.groupby('business_ref').agg(review_count=('rating','count'), avg_rating=('rating','mean')).reset_index()

# Filter to businesses with at least 5 reviews
agg_filtered = agg[agg['review_count'] >= 5].copy()

result = None
if not agg_filtered.empty:
    # Round avg for comparison precision
    agg_filtered['avg_rating'] = agg_filtered['avg_rating'].astype(float)
    # Find max avg
    max_avg = agg_filtered['avg_rating'].max()
    candidates = agg_filtered[agg_filtered['avg_rating'] == max_avg].copy()
    if len(candidates) > 1:
        # tie-breaker: choose highest review_count
        max_count = candidates['review_count'].max()
        candidates = candidates[candidates['review_count'] == max_count]
    chosen = candidates.iloc[0]
    biz_ref = chosen['business_ref']
    biz_id = biz_ref.replace('businessref_', 'businessid_')
    # Find business in businesses list
    biz_record = None
    for b in businesses:
        if b.get('business_id') == biz_id:
            biz_record = b
            break
    name = biz_record.get('name') if biz_record is not None else None
    description = biz_record.get('description') if biz_record is not None else None

    # Try to heuristically extract categories from description
    categories = None
    if description:
        desc = description
        # patterns to look for
        patterns = ['including', 'in the category of', 'offers a range of services in', 'offers a diverse range of services and products in', 'offers a delightful array of options ranging from', 'offers a wide range of services, including']
        found = False
        for p in patterns:
            low = desc.lower()
            if p in low:
                idx = low.find(p)
                # extract substring after pattern
                sub = desc[idx+len(p):].strip()
                # remove leading punctuation
                if sub.startswith(':') or sub.startswith(',') or sub.startswith('.'):
                    sub = sub[1:].strip()
                # truncate at sentence end
                for end in ['.', ' This', ' Located', ' offering', '\n']:
                    pos = sub.find(end)
                    if pos != -1:
                        sub = sub[:pos]
                categories = sub
                found = True
                break
        if not found:
            # fallback: take last clause after last comma
            parts = desc.split(' in ')
            if len(parts) > 1:
                categories = parts[-1]
            else:
                categories = desc

    result = {
        'business_ref': biz_ref,
        'business_id': biz_id,
        'name': name,
        'avg_rating': round(float(chosen['avg_rating']), 3),
        'review_count': int(chosen['review_count']),
        'categories': categories
    }

# Print according to required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_aLQuuNGjWyMipuIGPlgwTsHi': ['checkin', 'business'], 'var_call_4HgJJRfh7IH8Afcf50l54IqR': ['review', 'tip', 'user'], 'var_call_TYtFlxaMhRoWxF0pfIjfA5Jx': 'file_storage/call_TYtFlxaMhRoWxF0pfIjfA5Jx.json', 'var_call_UyE2t6TmDPXZTkdCnrEZWwJM': [{'business_ref': 'businessref_16', 'rating': '1', 'date': '2016-01-01 02:46:00'}, {'business_ref': 'businessref_23', 'rating': '5', 'date': '2016-06-28 02:18:33'}, {'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-03-12 14:19:00'}, {'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-05-24 23:15:00'}, {'business_ref': 'businessref_96', 'rating': '5', 'date': '2016-02-25 04:58:04'}, {'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-05-15 04:34:00'}, {'business_ref': 'businessref_47', 'rating': '5', 'date': '2016-06-24 19:38:03'}, {'business_ref': 'businessref_37', 'rating': '5', 'date': '2016-06-02 18:48:00'}, {'business_ref': 'businessref_8', 'rating': '4', 'date': '2016-02-24 18:52:00'}, {'business_ref': 'businessref_43', 'rating': '4', 'date': '2016-05-16 22:46:00'}, {'business_ref': 'businessref_14', 'rating': '3', 'date': '2016-05-06 16:02:13'}, {'business_ref': 'businessref_21', 'rating': '1', 'date': '2016-06-01 12:40:27'}, {'business_ref': 'businessref_16', 'rating': '3', 'date': '2016-05-17 07:05:00'}, {'business_ref': 'businessref_31', 'rating': '1', 'date': '2016-04-19 23:46:00'}, {'business_ref': 'businessref_30', 'rating': '2', 'date': '2016-03-08 05:52:00'}, {'business_ref': 'businessref_81', 'rating': '1', 'date': '2016-03-25 21:45:04'}, {'business_ref': 'businessref_71', 'rating': '5', 'date': '2016-01-04 02:38:00'}, {'business_ref': 'businessref_31', 'rating': '1', 'date': '2016-06-20 23:50:23'}, {'business_ref': 'businessref_46', 'rating': '5', 'date': '2016-03-28 01:57:00'}, {'business_ref': 'businessref_99', 'rating': '5', 'date': '2016-05-23 05:02:00'}, {'business_ref': 'businessref_40', 'rating': '5', 'date': '2016-06-20 15:01:00'}, {'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-04-02 23:09:00'}, {'business_ref': 'businessref_68', 'rating': '1', 'date': '2016-03-10 23:52:49'}, {'business_ref': 'businessref_11', 'rating': '5', 'date': '2016-06-03 20:33:00'}, {'business_ref': 'businessref_21', 'rating': '1', 'date': '2016-05-10 20:15:12'}, {'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-05-08 03:51:05'}, {'business_ref': 'businessref_8', 'rating': '3', 'date': '2016-06-27 11:15:38'}, {'business_ref': 'businessref_46', 'rating': '5', 'date': '2016-03-13 00:55:00'}, {'business_ref': 'businessref_68', 'rating': '1', 'date': '2016-03-29 10:58:00'}, {'business_ref': 'businessref_88', 'rating': '5', 'date': '2016-06-26 17:45:00'}, {'business_ref': 'businessref_9', 'rating': '2', 'date': '2016-01-01 19:40:00'}, {'business_ref': 'businessref_71', 'rating': '1', 'date': '2016-05-12 21:06:18'}, {'business_ref': 'businessref_28', 'rating': '5', 'date': '2016-03-02 22:59:37'}, {'business_ref': 'businessref_71', 'rating': '5', 'date': '2016-02-17 00:37:00'}, {'business_ref': 'businessref_37', 'rating': '5', 'date': '2016-05-25 15:30:00'}, {'business_ref': 'businessref_9', 'rating': '3', 'date': '2016-04-29 21:21:00'}, {'business_ref': 'businessref_17', 'rating': '5', 'date': '2016-03-12 15:27:00'}, {'business_ref': 'businessref_82', 'rating': '4', 'date': '2016-01-11 20:06:01'}]}

exec(code, env_args)
