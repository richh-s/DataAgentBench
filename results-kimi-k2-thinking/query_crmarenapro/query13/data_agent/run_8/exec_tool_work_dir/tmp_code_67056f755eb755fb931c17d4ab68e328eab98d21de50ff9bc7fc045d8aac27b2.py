code = """import json
import re

# Load the order data from the variable
order_data = locals()['var_functions.query_db:6']

# Function to clean ID fields (remove leading # and trailing whitespace)
def clean_id(id_value):
    if not id_value:
        return id_value
    # Remove leading # if present
    id_str = str(id_value)
    if id_str.startswith('#'):
        id_str = id_str[1:]
    # Remove trailing whitespace
    return id_str.strip()

# Calculate sales amount per OrderItem and sum by OwnerId
owner_sales = {}

for item in order_data:
    # Clean the OwnerId
    owner_id = clean_id(item['OwnerId'])
    
    # Calculate sales amount for this item
    quantity = float(item['Quantity'])
    unit_price = float(item['UnitPrice'])
    sales_amount = quantity * unit_price
    
    # Add to owner's total
    if owner_id not in owner_sales:
        owner_sales[owner_id] = 0
    owner_sales[owner_id] += sales_amount

# Find the owner with the highest sales
if owner_sales:
    top_owner = max(owner_sales.items(), key=lambda x: x[1])
    result = {
        "top_agent_id": top_owner[0],
        "total_sales": top_owner[1],
        "agent_count": len(owner_sales)
    }
else:
    result = {"error": "No sales data found"}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:6': [{'OrderId': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'EffectiveDate': '2022-09-15', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'OrderId': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'EffectiveDate': '2022-09-15', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO', 'EffectiveDate': '2022-07-10', 'Quantity': '15.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO', 'EffectiveDate': '2022-07-10', 'Quantity': '8.0', 'UnitPrice': '503.4905'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01', 'Quantity': '14.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '20.0', 'UnitPrice': '450.4915'}, {'OrderId': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '30.0', 'UnitPrice': '390.9915'}, {'OrderId': '801Wt00000PH4FMIA1', 'OwnerId': '#005Wt000003NJmbIAG', 'EffectiveDate': '2022-09-15', 'Quantity': '10.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'EffectiveDate': '2022-07-01', 'Quantity': '20.0', 'UnitPrice': '390.9915'}, {'OrderId': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'EffectiveDate': '2022-07-01', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'OrderId': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'EffectiveDate': '2022-07-01', 'Quantity': '50.0', 'UnitPrice': '450.4915'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '1.0', 'UnitPrice': '399.99'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '3.0', 'UnitPrice': '499.99'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '5.0', 'UnitPrice': '427.4905'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '7.0', 'UnitPrice': '455.9905'}, {'OrderId': '801Wt00000PHHhDIAX', 'OwnerId': '#005Wt000003NITxIAO', 'EffectiveDate': '2022-08-01', 'Quantity': '12.0', 'UnitPrice': '314.991'}, {'OrderId': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'EffectiveDate': '2022-09-15', 'Quantity': '10.0', 'UnitPrice': '449.991'}, {'OrderId': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'EffectiveDate': '2022-09-15', 'Quantity': '12.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'EffectiveDate': '2022-09-15', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01', 'Quantity': '16.0', 'UnitPrice': '440.991'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01', 'Quantity': '5.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01', 'Quantity': '7.0', 'UnitPrice': '379.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '#801Wt00000PHVkDIAX', 'OwnerId': '005Wt000003NJt3IAG', 'EffectiveDate': '2022-08-15', 'Quantity': '3.0', 'UnitPrice': '599.99'}, {'OrderId': '801Wt00000PHVqfIAH', 'OwnerId': '005Wt000003NDEBIA4', 'EffectiveDate': '2022-09-20', 'Quantity': '10.0', 'UnitPrice': '539.991'}, {'OrderId': '#801Wt00000PHWptIAH', 'OwnerId': '005Wt000003NJ0EIAW', 'EffectiveDate': '2022-09-25', 'Quantity': '2.0', 'UnitPrice': '339.99'}, {'OrderId': '#801Wt00000PHWptIAH', 'OwnerId': '005Wt000003NJ0EIAW', 'EffectiveDate': '2022-09-25', 'Quantity': '3.0', 'UnitPrice': '529.99'}], 'var_functions.execute_python:8': ['var_functions.query_db:6', '__builtins__', 'json', 'pd', 'datetime']}

exec(code, env_args)
