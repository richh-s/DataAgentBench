code = """import json
import pandas as pd
import datetime

# Load Order Items
# Path is in locals()['var_function-call-14046360423355083313']
with open(locals()['var_function-call-14046360423355083313'], 'r') as f:
    order_items = json.load(f)

# Load Cases
# Path is in locals()['var_function-call-6667994660044802622']
with open(locals()['var_function-call-6667994660044802622'], 'r') as f:
    cases = json.load(f)

# Helper for cleaning IDs
def clean_id(x):
    if x and isinstance(x, str):
        return x.lstrip('#').strip()
    return x

# Process Order Items
target_product_id = "01tWt000006hVJdIAM"
valid_order_item_ids = set()

for item in order_items:
    pid = clean_id(item.get('Product2Id'))
    if pid == target_product_id:
        oid = clean_id(item.get('Id'))
        if oid:
            valid_order_item_ids.add(oid)

print(f"DEBUG: Found {len(valid_order_item_ids)} valid OrderItems for product {target_product_id}")

# Process Cases
relevant_cases = []
for case in cases:
    oid = clean_id(case.get('orderitemid__c'))
    if oid in valid_order_item_ids:
        relevant_cases.append(case)

print(f"DEBUG: Found {len(relevant_cases)} cases linked to the product")

# Create DataFrame
df = pd.DataFrame(relevant_cases)
if not df.empty:
    df['createddate'] = pd.to_datetime(df['createddate'])

    # Filter by date [2020-06-10, 2021-04-10]
    today = pd.to_datetime("2021-04-10").tz_localize('UTC')
    start_date = today - pd.DateOffset(months=10)
    
    # Ensure createddate is timezone aware or handle it
    # The sample date "2023-07-02T11:00:00.000+0000" is TZ aware.
    
    mask = (df['createddate'] >= start_date) & (df['createddate'] <= today + pd.Timedelta(days=1))
    df_filtered = df[mask].copy()
    
    print(f"DEBUG: Found {len(df_filtered)} cases in the date range")

    # Group by Month
    df_filtered['Month'] = df_filtered['createddate'].dt.month_name()
    df_filtered['YearMonth'] = df_filtered['createddate'].dt.to_period('M')
    
    counts = df_filtered.groupby('YearMonth').size()
    counts_named = df_filtered.groupby('Month').size()
    
    result = {str(k): int(v) for k, v in counts.items()}
    result_named = {str(k): int(v) for k, v in counts_named.items()}
else:
    result = {}
    result_named = {}

print("__RESULT__:")
print(json.dumps({"counts": result, "counts_named": result_named}))"""

env_args = {'var_function-call-15147835606305365127': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-15147835606305361998': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-6667994660044800741': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-6667994660044802622': 'file_storage/function-call-6667994660044802622.json', 'var_function-call-15954347864961491755': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1}, 'var_function-call-14046360423355084056': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-14046360423355083313': 'file_storage/function-call-14046360423355083313.json'}

exec(code, env_args)
