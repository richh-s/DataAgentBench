code = """import json

# Load data using locals() for keys with hyphens
contracts_path = locals()['var_function-call-1963038768124185691']
opportunities_path = locals()['var_function-call-1963038768124182756']
line_items_path = locals()['var_function-call-1963038768124183917']
pricebook_entries = locals()['var_function-call-1963038768124185078']

with open(contracts_path, 'r') as f:
    contracts = json.load(f)
with open(opportunities_path, 'r') as f:
    opportunities = json.load(f)
with open(line_items_path, 'r') as f:
    line_items = json.load(f)

# Clean ID helper
def clean_id(x):
    if x is None:
        return None
    s = str(x).strip()
    if s.startswith('#'):
        return s[1:]
    return s

# 1. Process Contracts
# Filter by date: 2022-06-25 to 2022-11-25
valid_contract_ids = set()
start_date = "2022-06-25"
end_date = "2022-11-25"

for c in contracts:
    cid = clean_id(c.get('Id'))
    cdate = c.get('CompanySignedDate')
    if cdate and cid:
        cdate = cdate.strip()
        if start_date <= cdate <= end_date:
            valid_contract_ids.add(cid)

# 2. Process Opportunities
# Filter by valid contract
valid_opps = {} # Id -> OwnerId
for o in opportunities:
    oid = clean_id(o.get('Id'))
    con_id = clean_id(o.get('ContractID__c'))
    owner_id = clean_id(o.get('OwnerId'))
    
    if oid and con_id in valid_contract_ids and owner_id:
        valid_opps[oid] = owner_id

# 3. Process PricebookEntries
# Map Id -> UnitPrice
pb_map = {}
for pb in pricebook_entries:
    pbid = clean_id(pb.get('Id'))
    price = pb.get('UnitPrice')
    if pbid and price:
        pb_map[pbid] = float(price)

# 4. Process Line Items and Calculate Sales
agent_sales = {} # OwnerId -> TotalSales

for li in line_items:
    oid = clean_id(li.get('OpportunityId'))
    pbid = clean_id(li.get('PricebookEntryId'))
    qty = li.get('Quantity')
    
    if oid in valid_opps and pbid in pb_map and qty is not None:
        sales = float(qty) * pb_map[pbid]
        owner = valid_opps[oid]
        
        agent_sales[owner] = agent_sales.get(owner, 0.0) + sales

# 5. Find Top Agent
top_agent = None
max_sales = -1.0

for agent, sales in agent_sales.items():
    if sales > max_sales:
        max_sales = sales
        top_agent = agent

print("__RESULT__:")
print(json.dumps(top_agent))"""

env_args = {'var_function-call-6653884283794909985': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_function-call-6653884283794909276': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGeJIIA1', 'ContactId': '003Wt00000JqvQiIAJ', 'OwnerId': '005Wt000003NIqXIAW', 'Probability': '75.0', 'Amount': '182448.4965', 'StageName': 'Qualification', 'Name': 'InnoSphere Labs - EDA Innovation Expansion', 'Description': 'InnoSphere Labs is exploring advanced EDA solutions to enhance their R&D capabilities. They are particularly interested in the AI Cirku-Tech for rapid circuit prototyping, and the EcoPCB Creator for environmentally-friendly design processes. Additionally, CloudLink Designer could improve their team collaboration across global projects.', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'CloseDate': '2024-02-15'}], 'var_function-call-15274844415972520572': [{'cid': '0', 'name': 'Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'AccountId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'EffectiveDate', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'Pricebook2Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'OwnerId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-15274844415972523961': [{'Id': '#800Wt00000DD0SZIA1', 'AccountId': '001Wt00000PGZmfIAH', 'Status': 'Activated  ', 'StartDate': '2021-07-20', 'CustomerSignedDate': '2021-07-15', 'CompanySignedDate': '2021-07-16', 'Description': 'This contract solidifies the expanded partnership with Quantum Dynamics LLC for the provision of advanced AI-powered EDA tools, focusing on enhancing their quantum computing technology developments.', 'ContractTerm': '24'}], 'var_function-call-15274844415972523254': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGeJIIA1', 'ContactId': '003Wt00000JqvQiIAJ', 'OwnerId': '005Wt000003NIqXIAW', 'Probability': '75.0', 'Amount': '182448.4965', 'StageName': 'Qualification', 'Name': 'InnoSphere Labs - EDA Innovation Expansion', 'Description': 'InnoSphere Labs is exploring advanced EDA solutions to enhance their R&D capabilities. They are particularly interested in the AI Cirku-Tech for rapid circuit prototyping, and the EcoPCB Creator for environmentally-friendly design processes. Additionally, CloudLink Designer could improve their team collaboration across global projects.', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'CloseDate': '2024-02-15'}], 'var_function-call-9222221826481673560': [{'Id': '00kWt000002HF9qIAG', 'OpportunityId': '006Wt000007BAfxIAG', 'Product2Id': '01tWt000006hVhpIAE', 'PricebookEntryId': '01uWt0000027P3mIAE', 'Quantity': '8.0', 'TotalPrice': '3723.924'}], 'var_function-call-1963038768124185691': 'file_storage/function-call-1963038768124185691.json', 'var_function-call-1963038768124182756': 'file_storage/function-call-1963038768124182756.json', 'var_function-call-1963038768124183917': 'file_storage/function-call-1963038768124183917.json', 'var_function-call-1963038768124185078': [{'Id': '01uWt0000027P3lIAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027P3mIAE', 'UnitPrice': '489.99'}, {'Id': '01uWt0000027P5NIAU', 'UnitPrice': '599.99'}, {'Id': '#01uWt0000027P6zIAE', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027P8bIAE', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027P8cIAE', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PBpIAM', 'UnitPrice': '449.99'}, {'Id': '01uWt0000027PDRIA2', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PF3IAM', 'UnitPrice': '549.99'}, {'Id': '#01uWt0000027PGfIAM', 'UnitPrice': '479.99'}, {'Id': '01uWt0000027PIHIA2', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PIIIA2', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PIJIA2', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PJtIAM', 'UnitPrice': '649.99'}, {'Id': '01uWt0000027PLVIA2', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027PN7IAM', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027POjIAM', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027POkIAM', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PQLIA2', 'UnitPrice': '489.99'}, {'Id': '#01uWt0000027PRxIAM', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PTZIA2', 'UnitPrice': '449.99'}, {'Id': '#01uWt0000027PTaIAM', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PVBIA2', 'UnitPrice': '339.99'}, {'Id': '#01uWt0000027PWnIAM', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PYPIA2', 'UnitPrice': '319.99'}, {'Id': '01uWt0000027Pa1IAE', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PbdIAE', 'UnitPrice': '389.99'}, {'Id': '01uWt0000027PdFIAU', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PerIAE', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PgTIAU', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PgUIAU', 'UnitPrice': '379.99'}, {'Id': '01uWt0000027Pi5IAE', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PjhIAE', 'UnitPrice': '549.99'}, {'Id': '01uWt0000027PlJIAU', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027PmvIAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PoXIAU', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027Pq9IAE', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PrlIAE', 'UnitPrice': '369.99'}, {'Id': '#01uWt0000027PtNIAU', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PtOIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PuzIAE', 'UnitPrice': '629.99'}, {'Id': '01uWt0000027PwbIAE', 'UnitPrice': '559.99'}, {'Id': '#01uWt0000027PyDIAU', 'UnitPrice': '649.99'}, {'Id': '#01uWt0000027PzpIAE', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027Q1RIAU', 'UnitPrice': '579.99'}, {'Id': '#01uWt0000027Q33IAE', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027Q34IAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027Q4fIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Q6HIAU', 'UnitPrice': '619.99'}]}

exec(code, env_args)
