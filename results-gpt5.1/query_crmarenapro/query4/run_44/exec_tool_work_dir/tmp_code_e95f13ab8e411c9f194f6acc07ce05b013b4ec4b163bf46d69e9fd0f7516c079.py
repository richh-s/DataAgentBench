code = """import json
import pandas as pd

data = var_call_Fi3BOxTC9u9LP6FhATmdm6TV

if not data:
    result = None
else:
    df = pd.DataFrame(data)
    df['case_count'] = df['case_count'].astype(int)
    mean = df['case_count'].mean()
    std = df['case_count'].std(ddof=0)
    threshold = mean + 1.0 * std
    sig = df[df['case_count'] >= threshold]
    if sig.empty:
        result = None
    else:
        max_row = sig.sort_values('case_count', ascending=False).iloc[0]
        ym = max_row['year_month']
        year, month = ym.split('-')
        month_name = pd.to_datetime(ym + '-01').strftime('%B')
        result = month_name

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Fi3BOxTC9u9LP6FhATmdm6TV': [{'year_month': '2020-06', 'case_count': '2'}, {'year_month': '2020-07', 'case_count': '4'}, {'year_month': '2020-08', 'case_count': '1'}, {'year_month': '2020-09', 'case_count': '1'}, {'year_month': '2020-10', 'case_count': '3'}, {'year_month': '2020-11', 'case_count': '2'}, {'year_month': '2020-12', 'case_count': '1'}, {'year_month': '2021-01', 'case_count': '4'}, {'year_month': '2021-02', 'case_count': '1'}, {'year_month': '2021-03', 'case_count': '1'}]}

exec(code, env_args)
