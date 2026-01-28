code = """import pandas as pd
import json

# Load query results from storage variables
contacts = pd.DataFrame(var_call_zLJsgybul3g76Iu1U80wLYyq)
orderitems = pd.DataFrame(var_call_fCQiVj18ny0SRkR9hyAvXvDy)

# Helper to clean ids
def clean_id(x):
    if pd.isna(x):
        return x
    return str(x).strip().lstrip('#')

# Clean relevant id fields
contacts['Id'] = contacts['Id'].apply(clean_id)
contacts['AccountId'] = contacts['AccountId'].apply(clean_id)
orderitems['AccountId'] = orderitems['AccountId'].apply(clean_id)
orderitems['Product2Id'] = orderitems['Product2Id'].apply(clean_id)
orderitems['EffectiveDate'] = pd.to_datetime(orderitems['EffectiveDate'], errors='coerce')

# Given today's date
today = pd.to_datetime('2021-07-15')
# Compute last month range
first_of_this_month = today.replace(day=1)
last_month_end = first_of_this_month - pd.Timedelta(days=1)
last_month_start = last_month_end.replace(day=1)

# Get contact account id
if contacts.empty:
    result = None
else:
    contact_account = contacts.loc[0, 'AccountId']
    # Filter orderitems by account and effective date in last month
    mask = (
        orderitems['AccountId'].apply(lambda x: clean_id(x) == clean_id(contact_account)) &
        (orderitems['EffectiveDate'] >= last_month_start) &
        (orderitems['EffectiveDate'] <= last_month_end)
    )
    filtered = orderitems[mask].copy()
    # If multiple, choose the most recent EffectiveDate
    if not filtered.empty:
        filtered = filtered.sort_values('EffectiveDate', ascending=False)
        product_id = filtered.iloc[0]['Product2Id']
        result = clean_id(product_id)
    else:
        result = None

# Prepare output as JSON-serializable string
output = json.dumps(result)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_zLJsgybul3g76Iu1U80wLYyq': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_fCQiVj18ny0SRkR9hyAvXvDy': [{'OrderItemId': '#802Wt00000792tlIAA', 'OrderId': '801Wt00000PGXwDIAX', 'Product2Id': '#01tWt000006hVmfIAE', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-11-01'}, {'OrderItemId': '#802Wt00000798qNIAQ', 'OrderId': '801Wt00000PGXwDIAX', 'Product2Id': '01tWt000006hVY9IAM', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-11-01'}, {'OrderItemId': '#802Wt0000079AVbIAM', 'OrderId': '801Wt00000PGXwDIAX', 'Product2Id': '01tWt000006hV57IAE', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-11-01'}, {'OrderItemId': '#802Wt0000079AsAIAU', 'OrderId': '801Wt00000PGXwDIAX', 'Product2Id': '01tWt000006hV58IAE', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-11-01'}, {'OrderItemId': '802Wt000007959PIAQ', 'OrderId': '801Wt00000PGXwDIAX', 'Product2Id': '#01tWt000006hV8LIAU', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-11-01'}, {'OrderItemId': '802Wt0000079986IAA', 'OrderId': '801Wt00000PGXwDIAX', 'Product2Id': '01tWt000006hV6jIAE', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-11-01'}, {'OrderItemId': '802Wt0000079AU1IAM', 'OrderId': '801Wt00000PHRYWIA5', 'Product2Id': '01tWt000006hV8LIAU', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15'}]}

exec(code, env_args)
