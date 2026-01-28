code = """import json, pandas as pd

df = pd.DataFrame(var_call_VdQbPGKOfvkEMMkgtnlFCG9O)
# counts as int
if not df.empty:
    df['case_count'] = df['case_count'].astype(int)
    # find month with max cases
    max_row = df.loc[df['case_count'].idxmax()]
    # month name
    month_name = pd.to_datetime(max_row['month_start']).month_name()
else:
    month_name = None

print('__RESULT__:')
print(json.dumps({'month_name': month_name}))"""

env_args = {'var_call_VdQbPGKOfvkEMMkgtnlFCG9O': [{'month_start': '2020-07-01 00:00:00', 'case_count': '2'}, {'month_start': '2020-09-01 00:00:00', 'case_count': '4'}, {'month_start': '2020-10-01 00:00:00', 'case_count': '2'}, {'month_start': '2020-11-01 00:00:00', 'case_count': '4'}, {'month_start': '2020-12-01 00:00:00', 'case_count': '1'}, {'month_start': '2021-01-01 00:00:00', 'case_count': '3'}, {'month_start': '2021-02-01 00:00:00', 'case_count': '2'}, {'month_start': '2021-03-01 00:00:00', 'case_count': '5'}], 'var_call_Ysj2pqA11LF3kVJW3V9OTIhx': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}]}

exec(code, env_args)
