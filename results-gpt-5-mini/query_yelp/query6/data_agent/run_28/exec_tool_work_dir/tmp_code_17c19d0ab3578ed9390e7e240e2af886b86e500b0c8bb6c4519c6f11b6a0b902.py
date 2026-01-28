code = """import json
import pandas as pd

# Load reviews from storage variable
reviews = var_call_8wwSnndRy9m0zNq4PSYIjdDP

# Load business list from file path stored in var_call_2SdLCh6cBWoVaWihuTjiCCoU
with open(var_call_2SdLCh6cBWoVaWihuTjiCCoU, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

# Create DataFrame for reviews
rev_df = pd.DataFrame(reviews)
if rev_df.empty:
    result = {"error": "No reviews in the specified date range."}
else:
    # Convert rating to numeric
    rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
    # Map business_ref to business_id by replacing prefix
    rev_df['business_id'] = rev_df['business_ref'].str.replace('businessref_', 'businessid_')

    # Group by business_id to compute count and mean
    grp = rev_df.groupby('business_id').agg(review_count=('rating','count'), avg_rating=('rating','mean')).reset_index()

    # Filter businesses with at least 5 reviews
    grp_filtered = grp[grp['review_count'] >= 5]

    if grp_filtered.empty:
        result = {"error": "No business has at least 5 reviews in the given date range."}
    else:
        # Find highest average rating
        max_avg = grp_filtered['avg_rating'].max()
        candidates = grp_filtered[grp_filtered['avg_rating'] == max_avg]
        # If tie, pick one with highest review_count
        candidates = candidates.sort_values(by=['review_count','business_id'], ascending=[False, True])
        top = candidates.iloc[0]

        bid = top['business_id']
        avg_rating = float(round(top['avg_rating'], 4))
        rcount = int(top['review_count'])

        # Find business document
        biz_doc = None
        for b in businesses:
            if b.get('business_id') == bid:
                biz_doc = b
                break

        name = biz_doc.get('name') if biz_doc else None
        categories = biz_doc.get('categories') if biz_doc else None
        description = biz_doc.get('description') if biz_doc else None

        # Try to extract category info from description if categories missing
        def extract_categories_from_description(desc):
            if not desc:
                return None
            # Try to find last ' in ' and take the substring after it
            idx = desc.lower().rfind(' in ')
            if idx != -1:
                cat = desc[idx+4:]
                # Remove trailing punctuation
                cat = cat.strip(' .')
                return cat
            return desc

        category_info = categories if categories else extract_categories_from_description(description)

        result = {
            'business_id': bid,
            'name': name,
            'category': category_info,
            'average_rating': avg_rating,
            'review_count_in_period': rcount
        }

# Print result in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_hxk9lwZZLS6C7G8KmJFjPUve': ['checkin', 'business'], 'var_call_kM0z5KLVcWKE8eGzWVF3AKH5': ['review', 'tip', 'user'], 'var_call_2SdLCh6cBWoVaWihuTjiCCoU': 'file_storage/call_2SdLCh6cBWoVaWihuTjiCCoU.json', 'var_call_8wwSnndRy9m0zNq4PSYIjdDP': [{'review_id': 'reviewid_76', 'user_id': 'userid_793', 'business_ref': 'businessref_16', 'rating': '1', 'date': '2016-01-01 02:46:00'}, {'review_id': 'reviewid_459', 'user_id': 'userid_1397', 'business_ref': 'businessref_23', 'rating': '5', 'date': '2016-06-28 02:18:33'}, {'review_id': 'reviewid_78', 'user_id': 'userid_643', 'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-03-12 14:19:00'}, {'review_id': 'reviewid_1383', 'user_id': 'userid_938', 'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-05-24 23:15:00'}, {'review_id': 'reviewid_190', 'user_id': 'userid_144', 'business_ref': 'businessref_96', 'rating': '5', 'date': '2016-02-25 04:58:04'}, {'review_id': 'reviewid_31', 'user_id': 'userid_321', 'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-05-15 04:34:00'}, {'review_id': 'reviewid_1588', 'user_id': 'userid_1987', 'business_ref': 'businessref_47', 'rating': '5', 'date': '2016-06-24 19:38:03'}, {'review_id': 'reviewid_1447', 'user_id': 'userid_306', 'business_ref': 'businessref_37', 'rating': '5', 'date': '2016-06-02 18:48:00'}, {'review_id': 'reviewid_1715', 'user_id': 'None', 'business_ref': 'businessref_8', 'rating': '4', 'date': '2016-02-24 18:52:00'}, {'review_id': 'reviewid_1075', 'user_id': 'userid_1820', 'business_ref': 'businessref_43', 'rating': '4', 'date': '2016-05-16 22:46:00'}, {'review_id': 'reviewid_842', 'user_id': 'userid_1533', 'business_ref': 'businessref_14', 'rating': '3', 'date': '2016-05-06 16:02:13'}, {'review_id': 'reviewid_1510', 'user_id': 'userid_1688', 'business_ref': 'businessref_21', 'rating': '1', 'date': '2016-06-01 12:40:27'}, {'review_id': 'reviewid_1594', 'user_id': 'None', 'business_ref': 'businessref_16', 'rating': '3', 'date': '2016-05-17 07:05:00'}, {'review_id': 'reviewid_1149', 'user_id': 'None', 'business_ref': 'businessref_31', 'rating': '1', 'date': '2016-04-19 23:46:00'}, {'review_id': 'reviewid_742', 'user_id': 'userid_202', 'business_ref': 'businessref_30', 'rating': '2', 'date': '2016-03-08 05:52:00'}, {'review_id': 'reviewid_677', 'user_id': 'userid_242', 'business_ref': 'businessref_81', 'rating': '1', 'date': '2016-03-25 21:45:04'}, {'review_id': 'reviewid_1947', 'user_id': 'userid_702', 'business_ref': 'businessref_71', 'rating': '5', 'date': '2016-01-04 02:38:00'}, {'review_id': 'reviewid_1664', 'user_id': 'None', 'business_ref': 'businessref_31', 'rating': '1', 'date': '2016-06-20 23:50:23'}, {'review_id': 'reviewid_1330', 'user_id': 'None', 'business_ref': 'businessref_46', 'rating': '5', 'date': '2016-03-28 01:57:00'}, {'review_id': 'reviewid_1438', 'user_id': 'None', 'business_ref': 'businessref_99', 'rating': '5', 'date': '2016-05-23 05:02:00'}, {'review_id': 'reviewid_1421', 'user_id': 'userid_831', 'business_ref': 'businessref_40', 'rating': '5', 'date': '2016-06-20 15:01:00'}, {'review_id': 'reviewid_1325', 'user_id': 'userid_127', 'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-04-02 23:09:00'}, {'review_id': 'reviewid_1340', 'user_id': 'None', 'business_ref': 'businessref_68', 'rating': '1', 'date': '2016-03-10 23:52:49'}, {'review_id': 'reviewid_1335', 'user_id': 'userid_1270', 'business_ref': 'businessref_11', 'rating': '5', 'date': '2016-06-03 20:33:00'}, {'review_id': 'reviewid_629', 'user_id': 'userid_39', 'business_ref': 'businessref_21', 'rating': '1', 'date': '2016-05-10 20:15:12'}, {'review_id': 'reviewid_1718', 'user_id': 'userid_176', 'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-05-08 03:51:05'}, {'review_id': 'reviewid_1769', 'user_id': 'None', 'business_ref': 'businessref_8', 'rating': '3', 'date': '2016-06-27 11:15:38'}, {'review_id': 'reviewid_1323', 'user_id': 'userid_125', 'business_ref': 'businessref_46', 'rating': '5', 'date': '2016-03-13 00:55:00'}, {'review_id': 'reviewid_903', 'user_id': 'userid_1332', 'business_ref': 'businessref_68', 'rating': '1', 'date': '2016-03-29 10:58:00'}, {'review_id': 'reviewid_122', 'user_id': 'None', 'business_ref': 'businessref_88', 'rating': '5', 'date': '2016-06-26 17:45:00'}, {'review_id': 'reviewid_1324', 'user_id': 'None', 'business_ref': 'businessref_9', 'rating': '2', 'date': '2016-01-01 19:40:00'}, {'review_id': 'reviewid_1902', 'user_id': 'userid_219', 'business_ref': 'businessref_71', 'rating': '1', 'date': '2016-05-12 21:06:18'}, {'review_id': 'reviewid_647', 'user_id': 'userid_1612', 'business_ref': 'businessref_28', 'rating': '5', 'date': '2016-03-02 22:59:37'}, {'review_id': 'reviewid_95', 'user_id': 'None', 'business_ref': 'businessref_71', 'rating': '5', 'date': '2016-02-17 00:37:00'}, {'review_id': 'reviewid_1592', 'user_id': 'userid_1815', 'business_ref': 'businessref_37', 'rating': '5', 'date': '2016-05-25 15:30:00'}, {'review_id': 'reviewid_1088', 'user_id': 'userid_1138', 'business_ref': 'businessref_9', 'rating': '3', 'date': '2016-04-29 21:21:00'}, {'review_id': 'reviewid_950', 'user_id': 'userid_1578', 'business_ref': 'businessref_17', 'rating': '5', 'date': '2016-03-12 15:27:00'}, {'review_id': 'reviewid_1937', 'user_id': 'userid_589', 'business_ref': 'businessref_82', 'rating': '4', 'date': '2016-01-11 20:06:01'}]}

exec(code, env_args)
