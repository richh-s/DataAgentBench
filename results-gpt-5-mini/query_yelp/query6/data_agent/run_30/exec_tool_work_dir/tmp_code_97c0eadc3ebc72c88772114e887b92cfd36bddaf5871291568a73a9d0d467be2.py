code = """import json
import pandas as pd
# load the review data from storage
rl = var_call_e3J6PhzEievHbPeYnP9V7hDX
# create DataFrame
df = pd.DataFrame(rl)
# convert types
if not df.empty:
    df['rating'] = df['rating'].astype(int)
    # group by business_ref
    agg = df.groupby('business_ref').rating.agg(['count','mean']).reset_index()
    agg = agg[agg['count'] >= 5]
    if agg.empty:
        result = {"top_business_refs": [], "message": "no_business_with_at_least_5_reviews"}
    else:
        # find max mean
        max_mean = agg['mean'].max()
        top = agg[agg['mean'] == max_mean].sort_values(['count','business_ref'], ascending=[False,True])
        # create list of top business_refs with their stats
        top_list = top.to_dict(orient='records')
        result = {"top_business_refs": top_list}
else:
    result = {"top_business_refs": [], "message": "no_review_data"}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_38YZlWae75kGSFwoU8e1NLZN': ['checkin', 'business'], 'var_call_uCHMMXnFjsCdFzdpUOKvMpJS': 'file_storage/call_uCHMMXnFjsCdFzdpUOKvMpJS.json', 'var_call_e3J6PhzEievHbPeYnP9V7hDX': [{'business_ref': 'businessref_16', 'rating': '1', 'date': '2016-01-01 02:46:00'}, {'business_ref': 'businessref_23', 'rating': '5', 'date': '2016-06-28 02:18:33'}, {'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-03-12 14:19:00'}, {'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-05-24 23:15:00'}, {'business_ref': 'businessref_96', 'rating': '5', 'date': '2016-02-25 04:58:04'}, {'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-05-15 04:34:00'}, {'business_ref': 'businessref_47', 'rating': '5', 'date': '2016-06-24 19:38:03'}, {'business_ref': 'businessref_37', 'rating': '5', 'date': '2016-06-02 18:48:00'}, {'business_ref': 'businessref_8', 'rating': '4', 'date': '2016-02-24 18:52:00'}, {'business_ref': 'businessref_43', 'rating': '4', 'date': '2016-05-16 22:46:00'}, {'business_ref': 'businessref_14', 'rating': '3', 'date': '2016-05-06 16:02:13'}, {'business_ref': 'businessref_21', 'rating': '1', 'date': '2016-06-01 12:40:27'}, {'business_ref': 'businessref_16', 'rating': '3', 'date': '2016-05-17 07:05:00'}, {'business_ref': 'businessref_31', 'rating': '1', 'date': '2016-04-19 23:46:00'}, {'business_ref': 'businessref_30', 'rating': '2', 'date': '2016-03-08 05:52:00'}, {'business_ref': 'businessref_81', 'rating': '1', 'date': '2016-03-25 21:45:04'}, {'business_ref': 'businessref_71', 'rating': '5', 'date': '2016-01-04 02:38:00'}, {'business_ref': 'businessref_31', 'rating': '1', 'date': '2016-06-20 23:50:23'}, {'business_ref': 'businessref_46', 'rating': '5', 'date': '2016-03-28 01:57:00'}, {'business_ref': 'businessref_99', 'rating': '5', 'date': '2016-05-23 05:02:00'}, {'business_ref': 'businessref_40', 'rating': '5', 'date': '2016-06-20 15:01:00'}, {'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-04-02 23:09:00'}, {'business_ref': 'businessref_68', 'rating': '1', 'date': '2016-03-10 23:52:49'}, {'business_ref': 'businessref_11', 'rating': '5', 'date': '2016-06-03 20:33:00'}, {'business_ref': 'businessref_21', 'rating': '1', 'date': '2016-05-10 20:15:12'}, {'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-05-08 03:51:05'}, {'business_ref': 'businessref_8', 'rating': '3', 'date': '2016-06-27 11:15:38'}, {'business_ref': 'businessref_46', 'rating': '5', 'date': '2016-03-13 00:55:00'}, {'business_ref': 'businessref_68', 'rating': '1', 'date': '2016-03-29 10:58:00'}, {'business_ref': 'businessref_88', 'rating': '5', 'date': '2016-06-26 17:45:00'}, {'business_ref': 'businessref_9', 'rating': '2', 'date': '2016-01-01 19:40:00'}, {'business_ref': 'businessref_71', 'rating': '1', 'date': '2016-05-12 21:06:18'}, {'business_ref': 'businessref_28', 'rating': '5', 'date': '2016-03-02 22:59:37'}, {'business_ref': 'businessref_71', 'rating': '5', 'date': '2016-02-17 00:37:00'}, {'business_ref': 'businessref_37', 'rating': '5', 'date': '2016-05-25 15:30:00'}, {'business_ref': 'businessref_9', 'rating': '3', 'date': '2016-04-29 21:21:00'}, {'business_ref': 'businessref_17', 'rating': '5', 'date': '2016-03-12 15:27:00'}, {'business_ref': 'businessref_82', 'rating': '4', 'date': '2016-01-11 20:06:01'}]}

exec(code, env_args)
