code = """import json
import pandas as pd

rows = var_call_ksk2lznhrZo8bftD4nVTBzyN

df = pd.DataFrame(rows)
df['case_count'] = df['case_count'].astype(int)

# Determine if any month significantly exceeds others using a simple z-score > 2
mean = df['case_count'].mean()
std = df['case_count'].std(ddof=0)

if std == 0:
    significant_months = []
else:
    df['z'] = (df['case_count'] - mean) / std
    significant_months = df[df['z'] > 2]['month_start'].tolist()

# Map month_start to month name
month_name = None
if len(significant_months) > 0:
    # Use the first significant month
    month = pd.to_datetime(significant_months[0])
    month_name = month.strftime('%B')

result = month_name

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_hGIrbMqThpwF5qtirHVadiYd': [{'table_name': 'Case'}, {'table_name': 'knowledge__kav'}, {'table_name': 'issue__c'}, {'table_name': 'casehistory__c'}, {'table_name': 'emailmessage'}, {'table_name': 'livechattranscript'}], 'var_call_xpUZgOr5exsPvGvQ73gI5IJD': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_WDa5rhBkoKXtzXfgdjKChaMt': [{'createddate': '2023-07-02T11:00:00.000+0000'}, {'createddate': '2020-12-29T08:36:00.000+0000'}, {'createddate': '2023-09-30T11:30:00.000+0000'}, {'createddate': '2022-08-05T14:30:00.000+0000'}, {'createddate': '2020-09-01T10:30:00.000+0000'}], 'var_call_ksk2lznhrZo8bftD4nVTBzyN': [{'month_start': '2020-07-01', 'case_count': '2'}, {'month_start': '2020-09-01', 'case_count': '4'}, {'month_start': '2020-10-01', 'case_count': '2'}, {'month_start': '2020-11-01', 'case_count': '4'}, {'month_start': '2020-12-01', 'case_count': '1'}, {'month_start': '2021-01-01', 'case_count': '3'}, {'month_start': '2021-02-01', 'case_count': '2'}, {'month_start': '2021-03-01', 'case_count': '5'}]}

exec(code, env_args)
