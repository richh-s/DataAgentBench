code = """import json
import pandas as pd
import re

# Access the query result from storage
data = locals()['var_functions.query_db:6']

# Clean data - remove leading # from IDs and convert numeric fields
cleaned_data = []
for row in data:
    cleaned_row = {}
    for key, value in row.items():
        if key in ['OwnerId', 'OrderId']:
            # Remove leading # and trailing whitespace
            cleaned_value = re.sub(r'^#', '', str(value)).strip()
            cleaned_row[key] = cleaned_value
        elif key in ['Quantity', 'UnitPrice']:
            # Convert to float
            cleaned_row[key] = float(value)
        else:
            cleaned_row[key] = value
    cleaned_data.append(cleaned_row)

# Create DataFrame
df = pd.DataFrame(cleaned_data)

# Calculate sales amount per order item
df['SalesAmount'] = df['Quantity'] * df['UnitPrice']

# Aggregate sales per agent
agent_sales = df.groupby('OwnerId')['SalesAmount'].sum().reset_index()

# Sort by sales amount in descending order
agent_sales_sorted = agent_sales.sort_values('SalesAmount', ascending=False)

# Get the top agent
top_agent = agent_sales_sorted.iloc[0]['OwnerId'] if not agent_sales_sorted.empty else None

print('__RESULT__:')
print(json.dumps(top_agent))"""

env_args = {'var_functions.list_db:0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.list_db:2': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:6': [{'OrderId': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'EffectiveDate': '2022-09-15', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'OrderId': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'EffectiveDate': '2022-09-15', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO', 'EffectiveDate': '2022-07-10', 'Quantity': '15.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO', 'EffectiveDate': '2022-07-10', 'Quantity': '8.0', 'UnitPrice': '503.4905'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01', 'Quantity': '14.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '20.0', 'UnitPrice': '450.4915'}, {'OrderId': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '30.0', 'UnitPrice': '390.9915'}, {'OrderId': '801Wt00000PH4FMIA1', 'OwnerId': '#005Wt000003NJmbIAG', 'EffectiveDate': '2022-09-15', 'Quantity': '10.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'EffectiveDate': '2022-07-01', 'Quantity': '20.0', 'UnitPrice': '390.9915'}, {'OrderId': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'EffectiveDate': '2022-07-01', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'OrderId': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'EffectiveDate': '2022-07-01', 'Quantity': '50.0', 'UnitPrice': '450.4915'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '1.0', 'UnitPrice': '399.99'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '3.0', 'UnitPrice': '499.99'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '5.0', 'UnitPrice': '427.4905'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '7.0', 'UnitPrice': '455.9905'}, {'OrderId': '801Wt00000PHHhDIAX', 'OwnerId': '#005Wt000003NITxIAO', 'EffectiveDate': '2022-08-01', 'Quantity': '12.0', 'UnitPrice': '314.991'}, {'OrderId': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'EffectiveDate': '2022-09-15', 'Quantity': '10.0', 'UnitPrice': '449.991'}, {'OrderId': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'EffectiveDate': '2022-09-15', 'Quantity': '12.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'EffectiveDate': '2022-09-15', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01', 'Quantity': '16.0', 'UnitPrice': '440.991'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01', 'Quantity': '5.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01', 'Quantity': '7.0', 'UnitPrice': '379.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '#801Wt00000PHVkDIAX', 'OwnerId': '005Wt000003NJt3IAG', 'EffectiveDate': '2022-08-15', 'Quantity': '3.0', 'UnitPrice': '599.99'}, {'OrderId': '801Wt00000PHVqfIAH', 'OwnerId': '005Wt000003NDEBIA4', 'EffectiveDate': '2022-09-20', 'Quantity': '10.0', 'UnitPrice': '539.991'}, {'OrderId': '#801Wt00000PHWptIAH', 'OwnerId': '005Wt000003NJ0EIAW', 'EffectiveDate': '2022-09-25', 'Quantity': '2.0', 'UnitPrice': '339.99'}, {'OrderId': '#801Wt00000PHWptIAH', 'OwnerId': '005Wt000003NJ0EIAW', 'EffectiveDate': '2022-09-25', 'Quantity': '3.0', 'UnitPrice': '529.99'}], 'var_functions.query_db:9': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}]}

exec(code, env_args)
