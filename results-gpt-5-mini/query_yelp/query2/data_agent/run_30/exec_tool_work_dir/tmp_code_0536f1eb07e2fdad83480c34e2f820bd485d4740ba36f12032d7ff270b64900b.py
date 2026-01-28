code = """import json
# load the query results from storage variables
mongo_summary = var_call_m2YtzRPLa7WizmpRqjtHMKvq
sql_rows = var_call_uLbHRtTa14P1tJ7MQCM6GhQT

# compute weighted average rating for the state using review counts per business
total_reviews_state = 0
weighted_sum = 0.0
per_business = {}
for row in sql_rows:
    br = row['business_ref']
    avg = float(row['avg_rating'])
    cnt = int(row['review_count'])
    per_business[br] = {'avg_rating': avg, 'review_count': cnt}
    weighted_sum += avg * cnt
    total_reviews_state += cnt

# If counts from SQL differ from Mongo review_count sums, prefer SQL review counts for ratings calculation
state_avg = None
if total_reviews_state > 0:
    state_avg = weighted_sum / total_reviews_state

result = {
    'state': mongo_summary['top_state'],
    'total_reviews_mongo_sum': mongo_summary['total_reviews'],
    'total_reviews_sql_sum': total_reviews_state,
    'state_avg_rating': round(state_avg, 4) if state_avg is not None else None,
    'businesses': per_business
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_xWfIHppBYVI5V3bR6C567uBd': ['checkin', 'business'], 'var_call_lxffYFPxofRD6xUi4HnwHzM2': 'file_storage/call_lxffYFPxofRD6xUi4HnwHzM2.json', 'var_call_m2YtzRPLa7WizmpRqjtHMKvq': {'top_state': 'MO', 'total_reviews': 2243, 'business_refs': ['businessref_47', 'businessref_64', 'businessref_10', 'businessref_24', 'businessref_30', 'businessref_96', 'businessref_11', 'businessref_4', 'businessref_46']}, 'var_call_uLbHRtTa14P1tJ7MQCM6GhQT': [{'business_ref': 'businessref_24', 'avg_rating': '3.289473684210526', 'review_count': '38'}, {'business_ref': 'businessref_47', 'avg_rating': '3.9047619047619047', 'review_count': '42'}, {'business_ref': 'businessref_46', 'avg_rating': '4.181818181818182', 'review_count': '44'}, {'business_ref': 'businessref_30', 'avg_rating': '3.6', 'review_count': '5'}, {'business_ref': 'businessref_4', 'avg_rating': '5.0', 'review_count': '7'}, {'business_ref': 'businessref_96', 'avg_rating': '3.8863636363636362', 'review_count': '44'}, {'business_ref': 'businessref_64', 'avg_rating': '3.7142857142857144', 'review_count': '7'}, {'business_ref': 'businessref_10', 'avg_rating': '4.1875', 'review_count': '16'}, {'business_ref': 'businessref_11', 'avg_rating': '4.2', 'review_count': '10'}]}

exec(code, env_args)
