code = """import json

def clean_id(s):
    if not s: return s
    return s.strip().lstrip('#')

with open(locals()['var_function_call_1289442840733417554'], 'r') as f:
    orders = json.load(f)

with open(locals()['var_function_call_3848014298267230215'], 'r') as f:
    order_items = json.load(f)

# Filter orders
start_date = "2022-06-25"
end_date = "2022-11-25"

valid_orders = {} # cleaned_order_id -> cleaned_owner_id
for o in orders:
    d = o.get("EffectiveDate")
    if d and start_date <= d <= end_date:
        oid = clean_id(o.get("Id"))
        owner = clean_id(o.get("OwnerId"))
        valid_orders[oid] = owner

# Calculate sales
agent_sales = {}

for item in order_items:
    oid = clean_id(item.get("OrderId"))
    if oid in valid_orders:
        qty = float(item.get("Quantity", 0))
        price = float(item.get("UnitPrice", 0))
        amount = qty * price
        
        agent = valid_orders[oid]
        agent_sales[agent] = agent_sales.get(agent, 0.0) + amount

# Find top agent
top_agent = None
max_sales = -1.0

for agent, sales in agent_sales.items():
    if sales > max_sales:
        max_sales = sales
        top_agent = agent

print("__RESULT__:")
print(json.dumps(top_agent))"""

env_args = {'var_function-call-16849797917628781025': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_function-call-17724745355506277871': [{'Id': '802Wt0000078wz3IAA', 'OrderId': '801Wt00000PGSYIIA5', 'Product2Id': '#01tWt000006hVTJIA2', 'Quantity': '15.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027Pa1IAE'}], 'var_function-call-18394971466215593984': [{'count(*)': '15'}], 'var_function-call-7639015736888719898': [{'count(*)': '163'}], 'var_function-call-12633912330071630748': [{'count(*)': '689'}], 'var_function-call-1289442840733417554': 'file_storage/function-call-1289442840733417554.json', 'var_function-call-3848014298267230215': 'file_storage/function-call-3848014298267230215.json'}

exec(code, env_args)
