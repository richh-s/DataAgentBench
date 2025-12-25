code = """import json
import pandas as pd

# Load data
contracts_path = locals()['var_function-call-8963602642089365156']
opportunities_path = locals()['var_function-call-8963602642089362577']
line_items_path = locals()['var_function-call-8963602642089364094']
# pricebooks is small, direct
pricebooks_list = locals()['var_function-call-8963602642089361515']

with open(contracts_path, 'r') as f:
    contracts = json.load(f)
with open(opportunities_path, 'r') as f:
    opportunities = json.load(f)
with open(line_items_path, 'r') as f:
    line_items = json.load(f)

# Helper to clean ID
def clean_id(x):
    if x and isinstance(x, str):
        if x.startswith('#'):
            return x[1:]
        return x
    return x

# Helper to clean Date
def clean_date(x):
    if x and isinstance(x, str):
        return x.strip()
    return None

# 1. Process Contracts
valid_contract_ids = set()
start_date = "2022-06-25"
end_date = "2022-11-25"

for c in contracts:
    cid = clean_id(c.get('Id'))
    cdate = clean_date(c.get('CompanySignedDate'))
    
    if cdate:
        if start_date <= cdate <= end_date:
            valid_contract_ids.add(cid)

# 2. Process Opportunities
valid_opps = {} # OppId -> OwnerId
for o in opportunities:
    oid = clean_id(o.get('Id'))
    contract_id = clean_id(o.get('ContractID__c'))
    owner_id = clean_id(o.get('OwnerId'))
    
    if contract_id in valid_contract_ids:
        valid_opps[oid] = owner_id

# 3. Process Pricebooks
pb_map = {} # PBEntryId -> UnitPrice
for p in pricebooks_list:
    pbid = clean_id(p.get('Id'))
    try:
        price = float(p.get('UnitPrice'))
        pb_map[pbid] = price
    except:
        pass

# 4. Calculate Sales
sales_by_agent = {} # OwnerId -> TotalSales

for li in line_items:
    opp_id = clean_id(li.get('OpportunityId'))
    
    if opp_id in valid_opps:
        agent_id = valid_opps[opp_id]
        pbid = clean_id(li.get('PricebookEntryId'))
        qty_str = li.get('Quantity')
        
        try:
            qty = float(qty_str)
            price = pb_map.get(pbid, 0.0)
            amount = qty * price
            
            sales_by_agent[agent_id] = sales_by_agent.get(agent_id, 0.0) + amount
        except:
            continue

# Find top agent
top_agent = None
max_sales = -1.0

for agent, sales in sales_by_agent.items():
    if sales > max_sales:
        max_sales = sales
        top_agent = agent

print("__RESULT__:")
print(json.dumps(top_agent))"""

env_args = {'var_function-call-7272592447511463972': [{'cid': '0', 'name': 'Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'AccountId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'EffectiveDate', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'Pricebook2Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'OwnerId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-7272592447511464141': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'AccountId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Status', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'StartDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CustomerSignedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CompanySignedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContractTerm', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-2543048916252449700': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OpportunityId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Product2Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'PricebookEntryId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Quantity', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'TotalPrice', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-2543048916252449599': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContractID__c', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'AccountId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContactId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OwnerId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Probability', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Amount', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'StageName', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Name', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CreatedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CloseDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-2543048916252449498': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}, {'Id': '801Wt00000PFsjQIAT', 'AccountId': '#001Wt00000PHVqdIAH', 'Status': 'Activated', 'EffectiveDate': '2021-09-30', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NGjwIAG'}, {'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'Status': 'Activated', 'EffectiveDate': '2022-09-15', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIiUIAW'}], 'var_function-call-2543048916252449397': [{'Id': '#800Wt00000DD0SZIA1', 'AccountId': '001Wt00000PGZmfIAH', 'Status': 'Activated  ', 'StartDate': '2021-07-20', 'CustomerSignedDate': '2021-07-15', 'CompanySignedDate': '2021-07-16', 'Description': 'This contract solidifies the expanded partnership with Quantum Dynamics LLC for the provision of advanced AI-powered EDA tools, focusing on enhancing their quantum computing technology developments.', 'ContractTerm': '24'}, {'Id': '800Wt00000DD0SaIAL', 'AccountId': '001Wt00000PGXrLIAX', 'Status': 'Activated', 'StartDate': '2021-10-01', 'CustomerSignedDate': '2021-09-28', 'CompanySignedDate': '2021-09-28', 'Description': 'This contract outlines the collaboration between TechPulse Solutions and DataGuard Insights for EDA integration and security enhancements, providing comprehensive support and streamlining operational efficiencies within the DataGuard systems.', 'ContractTerm': '12'}, {'Id': '#800Wt00000DD0SbIAL', 'AccountId': '001Wt00000PGXrLIAX', 'Status': 'Activated   ', 'StartDate': '2023-07-15', 'CustomerSignedDate': '2023-07-11', 'CompanySignedDate': '2023-07-12', 'Description': 'Contract detailing the secure integration and optimization services to be implemented for DataGuard Insights, focusing on integrating CryptSecure Core and SecureFlow Suite into existing systems for enhanced data management and security. This includes AI-powered solution deployment, comprehensive training, and support.', 'ContractTerm': '12'}], 'var_function-call-8896743263262244061': [{'count_star()': '163'}], 'var_function-call-8896743263262243290': [{'count_star()': '1170'}], 'var_function-call-8896743263262242519': [{'count_star()': '4926'}], 'var_function-call-8896743263262241748': [{'COUNT(*)': '50'}], 'var_function-call-8963602642089365156': 'file_storage/function-call-8963602642089365156.json', 'var_function-call-8963602642089362577': 'file_storage/function-call-8963602642089362577.json', 'var_function-call-8963602642089364094': 'file_storage/function-call-8963602642089364094.json', 'var_function-call-8963602642089361515': [{'Id': '01uWt0000027P3lIAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027P3mIAE', 'UnitPrice': '489.99'}, {'Id': '01uWt0000027P5NIAU', 'UnitPrice': '599.99'}, {'Id': '#01uWt0000027P6zIAE', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027P8bIAE', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027P8cIAE', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PBpIAM', 'UnitPrice': '449.99'}, {'Id': '01uWt0000027PDRIA2', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PF3IAM', 'UnitPrice': '549.99'}, {'Id': '#01uWt0000027PGfIAM', 'UnitPrice': '479.99'}, {'Id': '01uWt0000027PIHIA2', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PIIIA2', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PIJIA2', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PJtIAM', 'UnitPrice': '649.99'}, {'Id': '01uWt0000027PLVIA2', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027PN7IAM', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027POjIAM', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027POkIAM', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PQLIA2', 'UnitPrice': '489.99'}, {'Id': '#01uWt0000027PRxIAM', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PTZIA2', 'UnitPrice': '449.99'}, {'Id': '#01uWt0000027PTaIAM', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PVBIA2', 'UnitPrice': '339.99'}, {'Id': '#01uWt0000027PWnIAM', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PYPIA2', 'UnitPrice': '319.99'}, {'Id': '01uWt0000027Pa1IAE', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PbdIAE', 'UnitPrice': '389.99'}, {'Id': '01uWt0000027PdFIAU', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PerIAE', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PgTIAU', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PgUIAU', 'UnitPrice': '379.99'}, {'Id': '01uWt0000027Pi5IAE', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PjhIAE', 'UnitPrice': '549.99'}, {'Id': '01uWt0000027PlJIAU', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027PmvIAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PoXIAU', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027Pq9IAE', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PrlIAE', 'UnitPrice': '369.99'}, {'Id': '#01uWt0000027PtNIAU', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PtOIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PuzIAE', 'UnitPrice': '629.99'}, {'Id': '01uWt0000027PwbIAE', 'UnitPrice': '559.99'}, {'Id': '#01uWt0000027PyDIAU', 'UnitPrice': '649.99'}, {'Id': '#01uWt0000027PzpIAE', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027Q1RIAU', 'UnitPrice': '579.99'}, {'Id': '#01uWt0000027Q33IAE', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027Q34IAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027Q4fIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Q6HIAU', 'UnitPrice': '619.99'}]}

exec(code, env_args)
