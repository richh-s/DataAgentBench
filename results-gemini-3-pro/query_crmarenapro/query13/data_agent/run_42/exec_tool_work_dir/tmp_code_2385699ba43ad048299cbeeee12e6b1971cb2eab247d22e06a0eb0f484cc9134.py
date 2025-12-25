code = """# Re-run logic to print top 3
import json
import pandas as pd
from datetime import datetime

with open(locals()['var_function-call-10538729336970164776'], 'r') as f:
    orders = json.load(f)

with open(locals()['var_function-call-18218870300946417486'], 'r') as f:
    order_items = json.load(f)

def clean_id(i):
    if i:
        return i.strip().lstrip('#')
    return i

def parse_date(d):
    try:
        return datetime.strptime(d.strip(), "%Y-%m-%d")
    except:
        return None

end_date = datetime(2022, 11, 25)
start_date = datetime(2022, 6, 25)

valid_orders = {} 
for o in orders:
    oid = clean_id(o.get('Id'))
    owner = clean_id(o.get('OwnerId'))
    ed_str = o.get('EffectiveDate')
    
    if oid and owner and ed_str:
        ed = parse_date(ed_str)
        if ed and start_date <= ed <= end_date:
            valid_orders[oid] = owner

agent_sales = {} 
for item in order_items:
    oid = clean_id(item.get('OrderId'))
    if oid in valid_orders:
        owner = valid_orders[oid]
        try:
            qty = float(item.get('Quantity', 0))
            price = float(item.get('UnitPrice', 0))
            amount = qty * price
            agent_sales[owner] = agent_sales.get(owner, 0.0) + amount
        except:
            continue

sorted_agents = sorted(agent_sales.items(), key=lambda x: x[1], reverse=True)
print("__RESULT__:")
print(json.dumps(sorted_agents[:5]))"""

env_args = {'var_function-call-8865015021441327750': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_function-call-8492865969588159566': [{'Id': '802Wt0000078wz3IAA', 'OrderId': '801Wt00000PGSYIIA5', 'Product2Id': '#01tWt000006hVTJIA2', 'Quantity': '15.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027Pa1IAE'}], 'var_function-call-13644732684706579904': [{'Count(*)': '163'}], 'var_function-call-13383086869522481019': [{'Count(*)': '689'}], 'var_function-call-10538729336970164776': 'file_storage/function-call-10538729336970164776.json', 'var_function-call-18218870300946417486': 'file_storage/function-call-18218870300946417486.json', 'var_function-call-9321551169244151235': '005Wt000003NIXCIA4'}

exec(code, env_args)
