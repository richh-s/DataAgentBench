code = """import json
import pandas as pd

rows = var_call_pmRhPCz8OIEpHQ6qclqFNDJe

df = pd.DataFrame(rows)
df['case_count'] = df['case_count'].astype(int)

# Compute mean and std
mean = df['case_count'].mean()
std = df['case_count'].std(ddof=0)

# Define "significantly exceeds" as > mean + 1 std
threshold = mean + std

candidates = df[df['case_count'] > threshold]

# Map YYYY-MM to month name, select the one with highest case_count if multiple
if not candidates.empty:
    candidates = candidates.sort_values(['case_count', 'month'], ascending=[False, True])
    top = candidates.iloc[0]
    year, month_num = top['month'].split('-')
    month_name = pd.to_datetime(top['month'] + '-01').strftime('%B')
    result = month_name
else:
    result = None

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_oKiy7WQTQlVvhtF6LrgMiJLH': [], 'var_call_4syhpqkorGJSAHvt9qgHWHLb': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_pmRhPCz8OIEpHQ6qclqFNDJe': [{'month': '2020-07', 'case_count': '2'}, {'month': '2020-09', 'case_count': '4'}, {'month': '2020-10', 'case_count': '2'}, {'month': '2020-11', 'case_count': '4'}, {'month': '2020-12', 'case_count': '1'}, {'month': '2021-01', 'case_count': '3'}, {'month': '2021-02', 'case_count': '2'}, {'month': '2021-03', 'case_count': '5'}]}

exec(code, env_args)
