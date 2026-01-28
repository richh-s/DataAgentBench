code = """import pandas as pd
import json
# var_call_H4bTDZbuSTr5EAbCsL2JxIOU is available from storage
records = var_call_H4bTDZbuSTr5EAbCsL2JxIOU

df = pd.DataFrame(records)
# ensure types
if not df.empty:
    df['rating'] = df['rating'].astype(int)
# group
grp = df.groupby('business_ref').agg(count=('rating','size'), avg_rating=('rating','mean')).reset_index()
# filter at least 5
grp5 = grp[grp['count'] >= 5]

# prepare output
if grp5.empty:
    result = {"top_business_refs": [], "message": "No businesses with at least 5 reviews in the period."}
else:
    max_avg = grp5['avg_rating'].max()
    top = grp5[grp5['avg_rating'] == max_avg].sort_values(by=['count','business_ref'], ascending=[False,True])
    # take top one
    top_row = top.iloc[0]
    top_business_ref = top_row['business_ref']
    top_count = int(top_row['count'])
    top_avg = float(round(top_row['avg_rating'],4))
    # convert business_ref prefix
    if top_business_ref.startswith('businessref_'):
        top_business_id = 'businessid_' + top_business_ref.split('businessref_')[1]
    else:
        top_business_id = top_business_ref
    result = {"top_business_ref": top_business_ref, "top_business_id": top_business_id, "count": top_count, "avg_rating": top_avg}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_MYsnnNuG6u8OCGrkl56BNTSg': ['checkin', 'business'], 'var_call_ciWff6UmvCEwLHNmVPbH44UO': ['review', 'tip', 'user'], 'var_call_uq4fVJdhnn5dJ4BtkqGFrCML': 'file_storage/call_uq4fVJdhnn5dJ4BtkqGFrCML.json', 'var_call_H4bTDZbuSTr5EAbCsL2JxIOU': [{'business_ref': 'businessref_16', 'rating': '1', 'date': '2016-01-01 02:46:00'}, {'business_ref': 'businessref_23', 'rating': '5', 'date': '2016-06-28 02:18:33'}, {'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-03-12 14:19:00'}, {'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-05-24 23:15:00'}, {'business_ref': 'businessref_96', 'rating': '5', 'date': '2016-02-25 04:58:04'}, {'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-05-15 04:34:00'}, {'business_ref': 'businessref_47', 'rating': '5', 'date': '2016-06-24 19:38:03'}, {'business_ref': 'businessref_37', 'rating': '5', 'date': '2016-06-02 18:48:00'}, {'business_ref': 'businessref_8', 'rating': '4', 'date': '2016-02-24 18:52:00'}, {'business_ref': 'businessref_43', 'rating': '4', 'date': '2016-05-16 22:46:00'}, {'business_ref': 'businessref_14', 'rating': '3', 'date': '2016-05-06 16:02:13'}, {'business_ref': 'businessref_21', 'rating': '1', 'date': '2016-06-01 12:40:27'}, {'business_ref': 'businessref_16', 'rating': '3', 'date': '2016-05-17 07:05:00'}, {'business_ref': 'businessref_31', 'rating': '1', 'date': '2016-04-19 23:46:00'}, {'business_ref': 'businessref_30', 'rating': '2', 'date': '2016-03-08 05:52:00'}, {'business_ref': 'businessref_81', 'rating': '1', 'date': '2016-03-25 21:45:04'}, {'business_ref': 'businessref_71', 'rating': '5', 'date': '2016-01-04 02:38:00'}, {'business_ref': 'businessref_31', 'rating': '1', 'date': '2016-06-20 23:50:23'}, {'business_ref': 'businessref_46', 'rating': '5', 'date': '2016-03-28 01:57:00'}, {'business_ref': 'businessref_99', 'rating': '5', 'date': '2016-05-23 05:02:00'}, {'business_ref': 'businessref_40', 'rating': '5', 'date': '2016-06-20 15:01:00'}, {'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-04-02 23:09:00'}, {'business_ref': 'businessref_68', 'rating': '1', 'date': '2016-03-10 23:52:49'}, {'business_ref': 'businessref_11', 'rating': '5', 'date': '2016-06-03 20:33:00'}, {'business_ref': 'businessref_21', 'rating': '1', 'date': '2016-05-10 20:15:12'}, {'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-05-08 03:51:05'}, {'business_ref': 'businessref_8', 'rating': '3', 'date': '2016-06-27 11:15:38'}, {'business_ref': 'businessref_46', 'rating': '5', 'date': '2016-03-13 00:55:00'}, {'business_ref': 'businessref_68', 'rating': '1', 'date': '2016-03-29 10:58:00'}, {'business_ref': 'businessref_88', 'rating': '5', 'date': '2016-06-26 17:45:00'}, {'business_ref': 'businessref_9', 'rating': '2', 'date': '2016-01-01 19:40:00'}, {'business_ref': 'businessref_71', 'rating': '1', 'date': '2016-05-12 21:06:18'}, {'business_ref': 'businessref_28', 'rating': '5', 'date': '2016-03-02 22:59:37'}, {'business_ref': 'businessref_71', 'rating': '5', 'date': '2016-02-17 00:37:00'}, {'business_ref': 'businessref_37', 'rating': '5', 'date': '2016-05-25 15:30:00'}, {'business_ref': 'businessref_9', 'rating': '3', 'date': '2016-04-29 21:21:00'}, {'business_ref': 'businessref_17', 'rating': '5', 'date': '2016-03-12 15:27:00'}, {'business_ref': 'businessref_82', 'rating': '4', 'date': '2016-01-11 20:06:01'}]}

exec(code, env_args)
