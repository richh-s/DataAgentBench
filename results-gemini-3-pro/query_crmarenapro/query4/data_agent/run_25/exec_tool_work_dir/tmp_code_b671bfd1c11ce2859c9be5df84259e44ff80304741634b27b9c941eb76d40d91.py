code = """import pandas as pd
import json

with open(locals()['var_function-call-2269822306977592115'], 'r') as f:
    cases_data = json.load(f)
order_items_data = locals()['var_function-call-2269822306977591614']

df_cases = pd.DataFrame(cases_data)
df_order_items = pd.DataFrame(order_items_data)

def clean_id(x):
    if pd.isna(x): return x
    return str(x).strip().lstrip('#')

df_cases['orderitemid_clean'] = df_cases['orderitemid__c'].apply(clean_id)
df_order_items['Id_clean'] = df_order_items['Id'].apply(clean_id)

target_ids = set(df_order_items['Id_clean'])
df_cases_filtered = df_cases[df_cases['orderitemid_clean'].isin(target_ids)].copy()
df_cases_filtered['createddate'] = pd.to_datetime(df_cases_filtered['createddate'])

# Group by month for all data
df_cases_filtered['month_year'] = df_cases_filtered['createddate'].dt.strftime('%Y-%m')
all_counts = df_cases_filtered.groupby('month_year').size().reset_index(name='count')

print("__RESULT__:")
print(all_counts.to_json(orient='records'))"""

env_args = {'var_function-call-5265069770845645301': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-5265069770845645176': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-2269822306977592115': 'file_storage/function-call-2269822306977592115.json', 'var_function-call-2269822306977591614': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_function-call-16421328970170364157': [{'month_year': '2020-09', 'month_name': 'September', 'count': 1}, {'month_year': '2020-11', 'month_name': 'November', 'count': 2}, {'month_year': '2021-03', 'month_name': 'March', 'count': 1}]}

exec(code, env_args)
