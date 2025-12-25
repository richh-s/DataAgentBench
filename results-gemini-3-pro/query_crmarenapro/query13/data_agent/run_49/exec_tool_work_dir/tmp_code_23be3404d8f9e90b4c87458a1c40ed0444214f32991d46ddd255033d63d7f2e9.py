code = """import json
import pandas as pd

# Load data
contracts_raw = locals()['var_function-call-11580169875619354345']
price_entries_raw = locals()['var_function-call-11580169875619354484']

with open(locals()['var_function-call-11580169875619353026'], 'r') as f:
    opportunities_raw = json.load(f)

with open(locals()['var_function-call-11580169875619355803'], 'r') as f:
    line_items_raw = json.load(f)

# Helper to clean IDs
def clean_id(val):
    if val is None:
        return None
    s = str(val).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

# 1. Process Contracts (already filtered by date)
eligible_contract_ids = set()
for c in contracts_raw:
    eligible_contract_ids.add(clean_id(c['Id']))

# 2. Process Opportunities
# We need map: OppId -> OwnerId
# Only for eligible contracts
eligible_opp_owners = {} # OppId -> OwnerId
for opp in opportunities_raw:
    cid = clean_id(opp.get('ContractID__c'))
    if cid in eligible_contract_ids:
        oid = clean_id(opp['Id'])
        owner = clean_id(opp.get('OwnerId'))
        eligible_opp_owners[oid] = owner

# 3. Process PricebookEntries
# Map: PricebookEntryId -> UnitPrice
price_map = {}
for pe in price_entries_raw:
    pid = clean_id(pe['Id'])
    try:
        u_price = float(pe['UnitPrice'])
        price_map[pid] = u_price
    except:
        continue

# 4. Process LineItems and Calculate Sales
agent_sales = {} # OwnerId -> TotalSales

for li in line_items_raw:
    opp_id = clean_id(li.get('OpportunityId'))
    
    # Check eligibility
    if opp_id not in eligible_opp_owners:
        continue
        
    owner_id = eligible_opp_owners[opp_id]
    
    # Get Price
    pbe_id = clean_id(li.get('PricebookEntryId'))
    unit_price = price_map.get(pbe_id, 0.0)
    
    # Get Quantity
    try:
        qty = float(li.get('Quantity', 0))
    except:
        qty = 0.0
        
    amount = qty * unit_price
    
    agent_sales[owner_id] = agent_sales.get(owner_id, 0.0) + amount

# 5. Find Top Agent
top_agent = None
max_sales = -1.0

for agent, sales in agent_sales.items():
    if sales > max_sales:
        max_sales = sales
        top_agent = agent

print("__RESULT__:")
print(json.dumps(top_agent))"""

env_args = {'var_function-call-12753893354687958802': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_function-call-12753893354687956703': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGeJIIA1', 'ContactId': '003Wt00000JqvQiIAJ', 'OwnerId': '005Wt000003NIqXIAW', 'Probability': '75.0', 'Amount': '182448.4965', 'StageName': 'Qualification', 'Name': 'InnoSphere Labs - EDA Innovation Expansion', 'Description': 'InnoSphere Labs is exploring advanced EDA solutions to enhance their R&D capabilities. They are particularly interested in the AI Cirku-Tech for rapid circuit prototyping, and the EcoPCB Creator for environmentally-friendly design processes. Additionally, CloudLink Designer could improve their team collaboration across global projects.', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'CloseDate': '2024-02-15'}], 'var_function-call-12753893354687958700': [{'Id': '#800Wt00000DD0SZIA1', 'AccountId': '001Wt00000PGZmfIAH', 'Status': 'Activated  ', 'StartDate': '2021-07-20', 'CustomerSignedDate': '2021-07-15', 'CompanySignedDate': '2021-07-16', 'Description': 'This contract solidifies the expanded partnership with Quantum Dynamics LLC for the provision of advanced AI-powered EDA tools, focusing on enhancing their quantum computing technology developments.', 'ContractTerm': '24'}], 'var_function-call-12753893354687956601': [{'Id': '802Wt0000078wz3IAA', 'OrderId': '801Wt00000PGSYIIA5', 'Product2Id': '#01tWt000006hVTJIA2', 'Quantity': '15.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027Pa1IAE'}], 'var_function-call-3555034377926942453': [{'cid': '0', 'name': 'Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'AccountId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'EffectiveDate', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'Pricebook2Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'OwnerId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-3555034377926939044': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContractID__c', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'AccountId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContactId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OwnerId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Probability', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Amount', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'StageName', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Name', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CreatedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CloseDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-11580169875619354345': [{'Id': '800Wt00000DDNlnIAH', 'CompanySignedDate': '2022-09-02'}, {'Id': '800Wt00000DDe3OIAT', 'CompanySignedDate': '2022-09-20'}, {'Id': '800Wt00000DDeg6IAD', 'CompanySignedDate': '2022-07-18'}, {'Id': '800Wt00000DDzZLIA1', 'CompanySignedDate': '2022-10-26'}, {'Id': '#800Wt00000DDzvrIAD', 'CompanySignedDate': '2022-08-30'}, {'Id': '800Wt00000DE0FHIA1', 'CompanySignedDate': '2022-08-02'}, {'Id': '800Wt00000DE0TiIAL', 'CompanySignedDate': '2022-09-10'}, {'Id': '800Wt00000DE2vLIAT', 'CompanySignedDate': '2022-06-29'}, {'Id': '800Wt00000DE98oIAD', 'CompanySignedDate': '2022-11-10'}, {'Id': '800Wt00000DE9GrIAL', 'CompanySignedDate': '2022-06-30'}, {'Id': '#800Wt00000DE9ITIA1', 'CompanySignedDate': '2022-09-11'}, {'Id': '#800Wt00000DE9SAIA1', 'CompanySignedDate': '2022-09-30'}, {'Id': '800Wt00000DE9YbIAL', 'CompanySignedDate': '2022-11-22'}, {'Id': '#800Wt00000DE9lVIAT', 'CompanySignedDate': '2022-06-26'}, {'Id': '800Wt00000DE9qLIAT', 'CompanySignedDate': '2022-09-01'}, {'Id': '800Wt00000DE9rxIAD', 'CompanySignedDate': '2022-09-19'}], 'var_function-call-11580169875619353026': 'file_storage/function-call-11580169875619353026.json', 'var_function-call-11580169875619355803': 'file_storage/function-call-11580169875619355803.json', 'var_function-call-11580169875619354484': [{'Id': '01uWt0000027P3lIAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027P3mIAE', 'UnitPrice': '489.99'}, {'Id': '01uWt0000027P5NIAU', 'UnitPrice': '599.99'}, {'Id': '#01uWt0000027P6zIAE', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027P8bIAE', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027P8cIAE', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PBpIAM', 'UnitPrice': '449.99'}, {'Id': '01uWt0000027PDRIA2', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PF3IAM', 'UnitPrice': '549.99'}, {'Id': '#01uWt0000027PGfIAM', 'UnitPrice': '479.99'}, {'Id': '01uWt0000027PIHIA2', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PIIIA2', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PIJIA2', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PJtIAM', 'UnitPrice': '649.99'}, {'Id': '01uWt0000027PLVIA2', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027PN7IAM', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027POjIAM', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027POkIAM', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PQLIA2', 'UnitPrice': '489.99'}, {'Id': '#01uWt0000027PRxIAM', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PTZIA2', 'UnitPrice': '449.99'}, {'Id': '#01uWt0000027PTaIAM', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PVBIA2', 'UnitPrice': '339.99'}, {'Id': '#01uWt0000027PWnIAM', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PYPIA2', 'UnitPrice': '319.99'}, {'Id': '01uWt0000027Pa1IAE', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PbdIAE', 'UnitPrice': '389.99'}, {'Id': '01uWt0000027PdFIAU', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PerIAE', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PgTIAU', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PgUIAU', 'UnitPrice': '379.99'}, {'Id': '01uWt0000027Pi5IAE', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PjhIAE', 'UnitPrice': '549.99'}, {'Id': '01uWt0000027PlJIAU', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027PmvIAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PoXIAU', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027Pq9IAE', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PrlIAE', 'UnitPrice': '369.99'}, {'Id': '#01uWt0000027PtNIAU', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PtOIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PuzIAE', 'UnitPrice': '629.99'}, {'Id': '01uWt0000027PwbIAE', 'UnitPrice': '559.99'}, {'Id': '#01uWt0000027PyDIAU', 'UnitPrice': '649.99'}, {'Id': '#01uWt0000027PzpIAE', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027Q1RIAU', 'UnitPrice': '579.99'}, {'Id': '#01uWt0000027Q33IAE', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027Q34IAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027Q4fIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Q6HIAU', 'UnitPrice': '619.99'}]}

exec(code, env_args)
