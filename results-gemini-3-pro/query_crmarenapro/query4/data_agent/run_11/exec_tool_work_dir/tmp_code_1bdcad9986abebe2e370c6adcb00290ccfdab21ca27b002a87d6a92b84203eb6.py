code = """import json
import pandas as pd

# Load Order Items (using previous result)
order_items = locals()['var_function-call-8635919969418049399']
valid_order_item_ids = set()
for item in order_items:
    oid = str(item['Id']).strip()
    if oid.startswith('#'):
        oid = oid[1:]
    valid_order_item_ids.add(oid)

# Load Cases
cases_path = locals()['var_function-call-2782911535086019411']
with open(cases_path, 'r') as f:
    cases = json.load(f)

df_cases = pd.DataFrame(cases)

# Helper to clean ID
def clean_id(x):
    if pd.isna(x):
        return None
    x = str(x).strip()
    if x.startswith('#'):
        x = x[1:]
    return x

df_cases['clean_order_item_id'] = df_cases['orderitemid__c'].apply(clean_id)

# Filter 1: Linked via OrderItem
mask_linked = df_cases['clean_order_item_id'].isin(valid_order_item_ids)

# Filter 2: Text Search (Subject or Description)
# Note: Case sensitive or insensitive? SQL LIKE is usually insensitive in Postgres if using ILIKE, but I used LIKE.
# Standard SQL LIKE is case sensitive. Postgres LIKE is case sensitive.
# I used LIKE '%SecureAnalytics Pro%'. If the text is "secureanalytics pro", I missed it.
# Let's use Python for case-insensitive search.
term = "SecureAnalytics Pro".lower()
mask_text = (df_cases['subject'].str.lower().str.contains(term, na=False)) | \
            (df_cases['description'].str.lower().str.contains(term, na=False))

# Combine
df_relevant = df_cases[mask_linked | mask_text].copy()

# Filter by Date
df_relevant['createddate'] = pd.to_datetime(df_relevant['createddate'])
ref_date = pd.Timestamp("2021-04-10").replace(tzinfo=df_relevant['createddate'].dt.tz)
start_date = ref_date - pd.DateOffset(months=10)

df_final = df_relevant[(df_relevant['createddate'] >= start_date) & (df_relevant['createddate'] <= ref_date)].copy()

# Group
df_final['month_name'] = df_final['createddate'].dt.strftime('%B')
df_final['year_month'] = df_final['createddate'].dt.strftime('%Y-%m')

monthly_counts = df_final.groupby(['year_month', 'month_name']).size()

print("__RESULT__:")
print(json.dumps(monthly_counts.to_dict())) # Keys will be stringified tuples"""

env_args = {'var_function-call-14108611946275025966': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-14108611946275028411': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-2782911535086022320': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-2782911535086019411': 'file_storage/function-call-2782911535086019411.json', 'var_function-call-9973046957187302705': [{'month': 'September', 'year_month': '2020-09', 'count': 1}, {'month': 'November', 'year_month': '2020-11', 'count': 2}, {'month': 'January', 'year_month': '2021-01', 'count': 1}, {'month': 'March', 'year_month': '2021-03', 'count': 1}], 'var_function-call-8635919969418049399': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-17923261169044884893': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-2351273765046909147': '{"(\'2020-09\', \'September\')":1,"(\'2020-11\', \'November\')":2,"(\'2021-01\', \'January\')":1,"(\'2021-03\', \'March\')":1}', 'var_function-call-16942555923741209744': [{'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000'}], 'var_function-call-15535718314260660164': [], 'var_function-call-15535718314260656951': [{'count': '0'}]}

exec(code, env_args)
