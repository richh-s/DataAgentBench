code = """import json
import pandas as pd
# var_call_Km8OJg4IQ5l3VSAHWnDpDwIa is available from previous query
reviews = var_call_Km8OJg4IQ5l3VSAHWnDpDwIa
# Create DataFrame
df = pd.DataFrame(reviews)
if df.empty:
    out = {"top_business_refs": [], "details": {}}
else:
    # convert types
    df['rating'] = df['rating'].astype(int)
    # group
    grp = df.groupby('business_ref').rating.agg(['count','mean']).reset_index()
    grp = grp[grp['count'] >= 5]
    if grp.empty:
        out = {"top_business_refs": [], "details": {}}
    else:
        max_avg = grp['mean'].max()
        top = grp[grp['mean'] == max_avg]
        # prepare details
        details = {}
        top_refs = []
        for _, row in top.iterrows():
            br = row['business_ref']
            top_refs.append(br)
            details[br] = {"count": int(row['count']), "avg_rating": float(round(row['mean'],4))}
        out = {"top_business_refs": top_refs, "details": details}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_nxan9JOOklMC1Hki6yRJecHY': ['business', 'checkin'], 'var_call_1HKZhwYXD4JMGQCEYLkBUxmq': ['review', 'tip', 'user'], 'var_call_XSWjuK0qdB4pLDP5ttjbRgff': 'file_storage/call_XSWjuK0qdB4pLDP5ttjbRgff.json', 'var_call_Km8OJg4IQ5l3VSAHWnDpDwIa': [{'review_id': 'reviewid_76', 'business_ref': 'businessref_16', 'rating': '1', 'date': '2016-01-01 02:46:00'}, {'review_id': 'reviewid_459', 'business_ref': 'businessref_23', 'rating': '5', 'date': '2016-06-28 02:18:33'}, {'review_id': 'reviewid_78', 'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-03-12 14:19:00'}, {'review_id': 'reviewid_1383', 'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-05-24 23:15:00'}, {'review_id': 'reviewid_190', 'business_ref': 'businessref_96', 'rating': '5', 'date': '2016-02-25 04:58:04'}, {'review_id': 'reviewid_31', 'business_ref': 'businessref_8', 'rating': '5', 'date': '2016-05-15 04:34:00'}, {'review_id': 'reviewid_1588', 'business_ref': 'businessref_47', 'rating': '5', 'date': '2016-06-24 19:38:03'}, {'review_id': 'reviewid_1447', 'business_ref': 'businessref_37', 'rating': '5', 'date': '2016-06-02 18:48:00'}, {'review_id': 'reviewid_1715', 'business_ref': 'businessref_8', 'rating': '4', 'date': '2016-02-24 18:52:00'}, {'review_id': 'reviewid_1075', 'business_ref': 'businessref_43', 'rating': '4', 'date': '2016-05-16 22:46:00'}, {'review_id': 'reviewid_842', 'business_ref': 'businessref_14', 'rating': '3', 'date': '2016-05-06 16:02:13'}, {'review_id': 'reviewid_1510', 'business_ref': 'businessref_21', 'rating': '1', 'date': '2016-06-01 12:40:27'}, {'review_id': 'reviewid_1594', 'business_ref': 'businessref_16', 'rating': '3', 'date': '2016-05-17 07:05:00'}, {'review_id': 'reviewid_1149', 'business_ref': 'businessref_31', 'rating': '1', 'date': '2016-04-19 23:46:00'}, {'review_id': 'reviewid_742', 'business_ref': 'businessref_30', 'rating': '2', 'date': '2016-03-08 05:52:00'}, {'review_id': 'reviewid_677', 'business_ref': 'businessref_81', 'rating': '1', 'date': '2016-03-25 21:45:04'}, {'review_id': 'reviewid_1947', 'business_ref': 'businessref_71', 'rating': '5', 'date': '2016-01-04 02:38:00'}, {'review_id': 'reviewid_1664', 'business_ref': 'businessref_31', 'rating': '1', 'date': '2016-06-20 23:50:23'}, {'review_id': 'reviewid_1330', 'business_ref': 'businessref_46', 'rating': '5', 'date': '2016-03-28 01:57:00'}, {'review_id': 'reviewid_1438', 'business_ref': 'businessref_99', 'rating': '5', 'date': '2016-05-23 05:02:00'}, {'review_id': 'reviewid_1421', 'business_ref': 'businessref_40', 'rating': '5', 'date': '2016-06-20 15:01:00'}, {'review_id': 'reviewid_1325', 'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-04-02 23:09:00'}, {'review_id': 'reviewid_1340', 'business_ref': 'businessref_68', 'rating': '1', 'date': '2016-03-10 23:52:49'}, {'review_id': 'reviewid_1335', 'business_ref': 'businessref_11', 'rating': '5', 'date': '2016-06-03 20:33:00'}, {'review_id': 'reviewid_629', 'business_ref': 'businessref_21', 'rating': '1', 'date': '2016-05-10 20:15:12'}, {'review_id': 'reviewid_1718', 'business_ref': 'businessref_9', 'rating': '5', 'date': '2016-05-08 03:51:05'}, {'review_id': 'reviewid_1769', 'business_ref': 'businessref_8', 'rating': '3', 'date': '2016-06-27 11:15:38'}, {'review_id': 'reviewid_1323', 'business_ref': 'businessref_46', 'rating': '5', 'date': '2016-03-13 00:55:00'}, {'review_id': 'reviewid_903', 'business_ref': 'businessref_68', 'rating': '1', 'date': '2016-03-29 10:58:00'}, {'review_id': 'reviewid_122', 'business_ref': 'businessref_88', 'rating': '5', 'date': '2016-06-26 17:45:00'}, {'review_id': 'reviewid_1324', 'business_ref': 'businessref_9', 'rating': '2', 'date': '2016-01-01 19:40:00'}, {'review_id': 'reviewid_1902', 'business_ref': 'businessref_71', 'rating': '1', 'date': '2016-05-12 21:06:18'}, {'review_id': 'reviewid_647', 'business_ref': 'businessref_28', 'rating': '5', 'date': '2016-03-02 22:59:37'}, {'review_id': 'reviewid_95', 'business_ref': 'businessref_71', 'rating': '5', 'date': '2016-02-17 00:37:00'}, {'review_id': 'reviewid_1592', 'business_ref': 'businessref_37', 'rating': '5', 'date': '2016-05-25 15:30:00'}, {'review_id': 'reviewid_1088', 'business_ref': 'businessref_9', 'rating': '3', 'date': '2016-04-29 21:21:00'}, {'review_id': 'reviewid_950', 'business_ref': 'businessref_17', 'rating': '5', 'date': '2016-03-12 15:27:00'}, {'review_id': 'reviewid_1937', 'business_ref': 'businessref_82', 'rating': '4', 'date': '2016-01-11 20:06:01'}]}

exec(code, env_args)
