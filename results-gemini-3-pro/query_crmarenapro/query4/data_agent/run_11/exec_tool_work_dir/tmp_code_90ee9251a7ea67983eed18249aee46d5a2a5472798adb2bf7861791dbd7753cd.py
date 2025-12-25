code = """import json
import pandas as pd

# Load Order Items
order_items = locals()['var_function-call-2782911535086022320']
# Clean OrderItem Ids
valid_order_item_ids = set()
for item in order_items:
    oid = item['Id']
    if oid.startswith('#'):
        oid = oid[1:]
    valid_order_item_ids.add(oid)

# Load Cases
cases_path = locals()['var_function-call-2782911535086019411']
with open(cases_path, 'r') as f:
    cases = json.load(f)

# Convert to DataFrame
df_cases = pd.DataFrame(cases)

# Clean orderitemid__c
def clean_id(x):
    if pd.isna(x):
        return x
    if isinstance(x, str) and x.startswith('#'):
        return x[1:]
    return x

df_cases['clean_order_item_id'] = df_cases['orderitemid__c'].apply(clean_id)

# Filter by Valid Order Items
df_cases = df_cases[df_cases['clean_order_item_id'].isin(valid_order_item_ids)]

# Convert createddate to datetime
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'])

# Filter by Date Range (Past 10 months from 2021-04-10)
# Range: 2020-06-10 to 2021-04-10
end_date = pd.Timestamp("2021-04-10").replace(tzinfo=df_cases['createddate'].dt.tz)
start_date = end_date - pd.DateOffset(months=10)

df_cases_filtered = df_cases[(df_cases['createddate'] >= start_date) & (df_cases['createddate'] <= end_date)]

# Group by Month Name
# "Return only the month name" -> assuming full month name or Month-Year. I'll print counts to inspect.
df_cases_filtered['month_year'] = df_cases_filtered['createddate'].dt.strftime('%Y-%m')
df_cases_filtered['month_name'] = df_cases_filtered['createddate'].dt.strftime('%B')

monthly_counts = df_cases_filtered.groupby('month_year')['month_name'].count()
monthly_names = df_cases_filtered.groupby('month_year')['month_name'].first()

result_list = []
for my, count in monthly_counts.items():
    result_list.append({'month': monthly_names[my], 'year_month': my, 'count': count})

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-14108611946275025966': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-14108611946275028411': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-2782911535086022320': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-2782911535086019411': 'file_storage/function-call-2782911535086019411.json'}

exec(code, env_args)
