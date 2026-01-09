code = """import json, pandas as pd
rows = var_call_SVyDaXJqmICQTi3HwiH5Uh7J
df = pd.DataFrame(rows)
df['case_count'] = df['case_count'].astype(int)
df['month_start'] = pd.to_datetime(df['month_start'])
# past 10 months window relative to 2021-04-10: 2020-07 through 2021-04
all_months = pd.date_range('2020-07-01','2021-04-01',freq='MS')
full = pd.DataFrame({'month_start': all_months}).merge(df, on='month_start', how='left').fillna({'case_count':0})
full['case_count']=full['case_count'].astype(int)
max_cnt = full['case_count'].max()
# detect if uniquely significantly exceeds: max >= 2* second_max and >0
sorted_counts = sorted(full['case_count'].tolist(), reverse=True)
second = sorted_counts[1] if len(sorted_counts)>1 else 0
significant = (max_cnt>0) and (max_cnt >= 2*second)
# choose month of max
month_name = full.loc[full['case_count'].idxmax(),'month_start'].strftime('%B')
# If not significant, still return month of max as best match per prompt
print('__RESULT__:')
print(json.dumps(month_name))"""

env_args = {'var_call_Ibe3S99tTPnmu2s6LdqzJftt': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_c8LRwg7NO0PfbWWYr6kXPrj0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_ay3czsak9zJhSXvWgu3u1hDL': [{'cnt': '19'}], 'var_call_jcFo6yqDN80gtmNXNvge7uPG': [{'orderitem_id': '802Wt0000078yuGIAQ'}, {'orderitem_id': '802Wt00000790mOIAQ'}, {'orderitem_id': '802Wt00000790zGIAQ'}, {'orderitem_id': '802Wt00000794F2IAI'}, {'orderitem_id': '802Wt000007968eIAA'}, {'orderitem_id': '802Wt00000796bfIAA'}, {'orderitem_id': '802Wt00000796qFIAQ'}, {'orderitem_id': '802Wt0000079734IAA'}, {'orderitem_id': '802Wt00000797W5IAI'}, {'orderitem_id': '802Wt00000797awIAA'}, {'orderitem_id': '802Wt00000797z7IAA'}, {'orderitem_id': '802Wt00000798VPIAY'}, {'orderitem_id': '802Wt00000798YdIAI'}, {'orderitem_id': '802Wt00000798okIAA'}, {'orderitem_id': '802Wt00000799o1IAA'}, {'orderitem_id': '802Wt0000079A2bIAE'}, {'orderitem_id': '802Wt0000079ACGIA2'}, {'orderitem_id': '802Wt0000079B0EIAU'}, {'orderitem_id': '802Wt0000079B6gIAE'}], 'var_call_SVyDaXJqmICQTi3HwiH5Uh7J': [{'month_start': '2020-09-01 00:00:00', 'case_count': '1'}, {'month_start': '2020-11-01 00:00:00', 'case_count': '2'}, {'month_start': '2021-01-01 00:00:00', 'case_count': '1'}, {'month_start': '2021-03-01 00:00:00', 'case_count': '1'}]}

exec(code, env_args)
