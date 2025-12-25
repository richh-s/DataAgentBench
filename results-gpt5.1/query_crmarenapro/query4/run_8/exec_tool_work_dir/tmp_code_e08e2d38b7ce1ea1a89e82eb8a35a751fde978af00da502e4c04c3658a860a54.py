code = """import json
from datetime import datetime

records = var_call_HPlpVrLKTRIPCnKObmhaNKL9

counts = {}
for r in records:
    dt = datetime.fromisoformat(r['CreatedDate'].replace('Z', '').split('+')[0])
    month = dt.strftime('%B')
    counts[month] = counts.get(month, 0) + 1

# Past 10 months from 2021-04-10 inclusive: Jul 2020 to Apr 2021
order = ['July','August','September','October','November','December','January','February','March','April']
ordered_counts = {m: counts.get(m, 0) for m in order}

max_month = max(ordered_counts, key=ordered_counts.get)
max_val = ordered_counts[max_month]
second_val = sorted(ordered_counts.values(), reverse=True)[1] if len(ordered_counts) > 1 else 0

result = max_month if max_val >= second_val * 1.5 and max_val > 0 else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HPlpVrLKTRIPCnKObmhaNKL9': [{'OpportunityId': '006Wt000007B630IAC', 'CreatedDate': '2020-08-15T10:35:45.000+0000', 'Product2Id': '01tWt000006hVJdIAM'}, {'OpportunityId': '006Wt000007BD7aIAG', 'CreatedDate': '2021-01-15T10:45:30.000+0000', 'Product2Id': '01tWt000006hVJdIAM'}, {'OpportunityId': '006Wt000007BCZlIAO', 'CreatedDate': '2020-06-15T10:53:21.000+0000', 'Product2Id': '01tWt000006hVJdIAM'}, {'OpportunityId': '006Wt000007BA9jIAG', 'CreatedDate': '2020-06-15T09:14:27.000+0000', 'Product2Id': '01tWt000006hVJdIAM'}, {'OpportunityId': '006Wt000007BFnhIAG', 'CreatedDate': '2021-01-15T09:30:00.000+0000', 'Product2Id': '01tWt000006hVJdIAM'}, {'OpportunityId': '006Wt000007BISDIA4', 'CreatedDate': '2020-10-01T10:15:30.000+0000', 'Product2Id': '01tWt000006hVJdIAM'}, {'OpportunityId': '006Wt000007BBQkIAO', 'CreatedDate': '2021-02-01T15:22:30.000+0000', 'Product2Id': '01tWt000006hVJdIAM'}, {'OpportunityId': '006Wt000007B6xKIAS', 'CreatedDate': '2020-12-01T14:37:45.000+0000', 'Product2Id': '01tWt000006hVJdIAM'}, {'OpportunityId': '006Wt000007BD4MIAW', 'CreatedDate': '2020-07-15T10:45:00.000+0000', 'Product2Id': '01tWt000006hVJdIAM'}, {'OpportunityId': '006Wt000007B7yGIAS', 'CreatedDate': '2021-01-20T10:45:00.000+0000', 'Product2Id': '01tWt000006hVJdIAM'}, {'OpportunityId': '006Wt000007BBP9IAO', 'CreatedDate': '2021-01-10T10:45:23.000+0000', 'Product2Id': '#01tWt000006hVJdIAM'}, {'OpportunityId': '006Wt000007BINNIA4', 'CreatedDate': '2020-10-05T14:30:45.000+0000', 'Product2Id': '01tWt000006hVJdIAM'}, {'OpportunityId': '006Wt000007BDIsIAO', 'CreatedDate': '2020-11-12T10:45:38.000+0000', 'Product2Id': '01tWt000006hVJdIAM'}, {'OpportunityId': '006Wt000007BFXaIAO', 'CreatedDate': '2020-11-15T15:50:45.000+0000', 'Product2Id': '01tWt000006hVJdIAM'}, {'OpportunityId': '006Wt000007BAMjIAO', 'CreatedDate': '2020-09-15T15:45:32.000+0000', 'Product2Id': '01tWt000006hVJdIAM'}, {'OpportunityId': '006Wt000007BHuMIAW', 'CreatedDate': '2020-07-20T10:34:21.000+0000', 'Product2Id': '01tWt000006hVJdIAM'}, {'OpportunityId': '006Wt000007BIX4IAO', 'CreatedDate': '2020-07-10T14:35:47.000+0000', 'Product2Id': '01tWt000006hVJdIAM'}, {'OpportunityId': '006Wt000007BGi9IAG', 'CreatedDate': '2021-03-12T09:23:30.000+0000', 'Product2Id': '01tWt000006hVJdIAM'}, {'OpportunityId': '006Wt000007B9X2IAK', 'CreatedDate': '2020-10-05T09:45:00.000+0000', 'Product2Id': '01tWt000006hVJdIAM'}, {'OpportunityId': '006Wt000007BGtRIAW', 'CreatedDate': '2020-07-10T14:58:10.000+0000', 'Product2Id': '01tWt000006hVJdIAM'}]}

exec(code, env_args)
