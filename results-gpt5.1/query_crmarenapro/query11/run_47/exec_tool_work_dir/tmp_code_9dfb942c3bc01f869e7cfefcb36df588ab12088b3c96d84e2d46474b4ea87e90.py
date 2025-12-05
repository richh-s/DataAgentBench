code = """import json
from datetime import datetime

records = var_call_clI54JqloCqrXQBxuIivuede

cutoff_start = datetime.fromisoformat('2021-06-15T00:00:00')
cutoff_end = datetime.fromisoformat('2021-07-15T00:00:00')

# Filter to last month relative to 2021-07-15, i.e., 2021-06-15 to 2021-07-15
filtered = []
for r in records:
    dt = datetime.fromisoformat(r['CreatedDate'].replace('Z', '').split('+')[0])
    if cutoff_start <= dt < cutoff_end:
        filtered.append(r)

# If none in last month, fall back to latest overall
if filtered:
    target = max(filtered, key=lambda r: r['CreatedDate'])
else:
    target = max(records, key=lambda r: r['CreatedDate']) if records else None

product_id = target['Product2Id'] if target else None

result = json.dumps(product_id)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_wIykSVwF0Eu1DbvPTfaqfYCG': [], 'var_call_clI54JqloCqrXQBxuIivuede': [{'Product2Id': '01tWt000006hV57IAE', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-05T09:47:23.000+0000'}, {'Product2Id': '#01tWt000006hV8LIAU', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-01T10:15:30.000+0000'}, {'Product2Id': '01tWt000006hVmfIAE', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-05T09:47:23.000+0000'}, {'Product2Id': '01tWt000006hUgwIAE', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-04-15T14:22:35.000+0000'}, {'Product2Id': '01tWt000006hTUkIAM', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-15T10:27:45.000+0000'}, {'Product2Id': '01tWt000006hVgDIAU', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-04-15T14:22:35.000+0000'}, {'Product2Id': '01tWt000006hVY9IAM', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-05T09:47:23.000+0000'}, {'Product2Id': '01tWt000006hV6jIAE', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-05T09:47:23.000+0000'}, {'Product2Id': '01tWt000006hV8LIAU', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-15T10:27:45.000+0000'}, {'Product2Id': '01tWt000006hV9xIAE', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-01T10:15:30.000+0000'}, {'Product2Id': '01tWt000006hV8LIAU', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-05T09:47:23.000+0000'}, {'Product2Id': '01tWt000006hVebIAE', 'ContactId': '#003Wt00000Jqy8SIAR', 'CreatedDate': '2021-04-10T11:15:45.000+0000'}, {'Product2Id': '01tWt000006hV58IAE', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-05T09:47:23.000+0000'}], 'var_call_4qDMaqH49RxXjxrjYjJSGtL8': []}

exec(code, env_args)
