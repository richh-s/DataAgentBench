code = """import pandas as pd
import json

# Load Order Items
order_items = locals()['var_function-call-455465860512101407']
# Load Cases
with open(locals()['var_function-call-2577931855183809706'], 'r') as f:
    cases = json.load(f)

# Helper to clean ID
def clean_id(x):
    if not isinstance(x, str):
        return ""
    x = x.strip()
    if x.startswith('#'):
        return x[1:]
    return x

# Prepare Order Item IDs set
valid_order_item_ids = set()

for item in order_items:
    oid = clean_id(item['Id'])
    if oid:
        valid_order_item_ids.add(oid)

# Process Cases
case_data = []
for c in cases:
    oid = clean_id(c.get('orderitemid__c'))
    if oid in valid_order_item_ids:
        case_data.append(c)

df = pd.DataFrame(case_data)
result = {}

if not df.empty:
    # Convert createddate to datetime
    # Dates are like "2023-07-02T11:00:00.000+0000"
    df['createddate'] = pd.to_datetime(df['createddate'])
    
    # Filter for past 10 months: 2020-06-10 to 2021-04-10
    # Assuming UTC for comparison
    start_date = pd.Timestamp("2020-06-10").tz_localize('UTC')
    end_date = pd.Timestamp("2021-04-10").tz_localize('UTC')
    
    mask = (df['createddate'] >= start_date) & (df['createddate'] <= end_date)
    df_filtered = df[mask].copy()
    
    if not df_filtered.empty:
        df_filtered['month_year'] = df_filtered['createddate'].dt.to_period('M')
        counts = df_filtered['month_year'].value_counts().sort_index()
        result = {str(k): int(v) for k, v in counts.items()}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2501921911844964614': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-2501921911844962647': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-455465860512101407': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_function-call-2577931855183809706': 'file_storage/function-call-2577931855183809706.json'}

exec(code, env_args)
