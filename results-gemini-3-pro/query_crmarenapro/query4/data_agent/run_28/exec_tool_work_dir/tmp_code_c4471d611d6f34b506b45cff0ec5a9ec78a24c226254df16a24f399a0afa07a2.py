code = """import json
import pandas as pd

order_items = locals()['var_function-call-8526324655233561326']
valid_order_ids = set()
for item in order_items:
    oid = str(item['Id']).strip()
    if oid.startswith('#'):
        oid = oid[1:]
    valid_order_ids.add(oid)

file_path = locals()['var_function-call-9326357835235136414']
with open(file_path, 'r') as f:
    cases_data = json.load(f)

df = pd.DataFrame(cases_data)
df['clean_oid'] = df['orderitemid__c'].fillna('').astype(str).str.strip().apply(lambda x: x[1:] if x.startswith('#') else x)
df_target = df[df['clean_oid'].isin(valid_order_ids)].copy()
df_target['created_dt'] = pd.to_datetime(df_target['createddate'])

end_date = pd.Timestamp("2021-04-10").tz_localize('UTC')
start_date = end_date - pd.DateOffset(months=10)

mask = (df_target['created_dt'] >= start_date) & (df_target['created_dt'] <= end_date)
df_filtered = df_target[mask].copy()

# Print details
details = df_filtered[['id', 'createddate', 'clean_oid']].to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(details))"""

env_args = {'var_function-call-8526324655233561326': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-9326357835235136414': 'file_storage/function-call-9326357835235136414.json', 'var_function-call-16380928904925848253': {'November': 2, 'January': 1, 'September': 1, 'March': 1}, 'var_function-call-15395679336017644715': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}]}

exec(code, env_args)
