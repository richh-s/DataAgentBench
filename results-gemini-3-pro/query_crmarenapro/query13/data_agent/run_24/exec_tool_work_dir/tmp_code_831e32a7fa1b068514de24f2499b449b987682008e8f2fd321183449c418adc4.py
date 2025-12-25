code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-4250088271154245686'], 'r') as f:
    contracts = json.load(f)
with open(locals()['var_function-call-4250088271154248763'], 'r') as f:
    opportunities = json.load(f)
with open(locals()['var_function-call-4250088271154247744'], 'r') as f:
    line_items = json.load(f)
pricebook_entries = locals()['var_function-call-4250088271154246725']

# Helper to clean ID
def clean_id(val):
    if not isinstance(val, str):
        return str(val)
    val = val.strip()
    if val.startswith('#'):
        return val[1:]
    return val

# Process Contracts
valid_contract_ids = set()
start_date = "2022-06-25"
end_date = "2022-11-25"

for c in contracts:
    c_date = c.get('CompanySignedDate')
    if c_date and c_date != 'None':
        # Assuming date format YYYY-MM-DD
        if start_date <= c_date <= end_date:
            valid_contract_ids.add(clean_id(c.get('Id')))

# Process Opportunities
# We need to map Opportunity Id to OwnerId, but only for eligible ones
eligible_opps = {} # OppId -> OwnerId
for opp in opportunities:
    contract_id = opp.get('ContractID__c')
    if contract_id and contract_id != 'None':
        clean_cid = clean_id(contract_id)
        if clean_cid in valid_contract_ids:
            eligible_opps[clean_id(opp.get('Id'))] = clean_id(opp.get('OwnerId'))

# Process PricebookEntries
price_map = {} # PBEntryId -> UnitPrice (float)
for pb in pricebook_entries:
    pid = clean_id(pb.get('Id'))
    try:
        price = float(pb.get('UnitPrice'))
        price_map[pid] = price
    except:
        pass

# Calculate Sales by Owner
owner_sales = {} # OwnerId -> Total Sales

for item in line_items:
    opp_id = clean_id(item.get('OpportunityId'))
    if opp_id in eligible_opps:
        owner_id = eligible_opps[opp_id]
        pb_entry_id = clean_id(item.get('PricebookEntryId'))
        quantity = 0
        try:
            quantity = float(item.get('Quantity'))
        except:
            quantity = 0
            
        unit_price = price_map.get(pb_entry_id, 0.0)
        amount = quantity * unit_price
        
        owner_sales[owner_id] = owner_sales.get(owner_id, 0.0) + amount

# Find Top Agent
top_agent = None
max_sales = -1.0

for agent, sales in owner_sales.items():
    if sales > max_sales:
        max_sales = sales
        top_agent = agent

print("__RESULT__:")
print(json.dumps(top_agent))"""

env_args = {'var_function-call-5757279413097381701': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_function-call-5757279413097380400': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGeJIIA1', 'ContactId': '003Wt00000JqvQiIAJ', 'OwnerId': '005Wt000003NIqXIAW', 'Probability': '75.0', 'Amount': '182448.4965', 'StageName': 'Qualification', 'Name': 'InnoSphere Labs - EDA Innovation Expansion', 'Description': 'InnoSphere Labs is exploring advanced EDA solutions to enhance their R&D capabilities. They are particularly interested in the AI Cirku-Tech for rapid circuit prototyping, and the EcoPCB Creator for environmentally-friendly design processes. Additionally, CloudLink Designer could improve their team collaboration across global projects.', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'CloseDate': '2024-02-15'}], 'var_function-call-5757279413097379099': [{'Id': '#800Wt00000DD0SZIA1', 'AccountId': '001Wt00000PGZmfIAH', 'Status': 'Activated  ', 'StartDate': '2021-07-20', 'CustomerSignedDate': '2021-07-15', 'CompanySignedDate': '2021-07-16', 'Description': 'This contract solidifies the expanded partnership with Quantum Dynamics LLC for the provision of advanced AI-powered EDA tools, focusing on enhancing their quantum computing technology developments.', 'ContractTerm': '24'}], 'var_function-call-6517723049906274112': [{'cid': '0', 'name': 'Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'AccountId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'EffectiveDate', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'Pricebook2Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'OwnerId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-6517723049906272441': [{'cid': '0', 'name': 'Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'OrderId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Product2Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'Quantity', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'UnitPrice', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'PriceBookEntryId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-3835977147311339231': [{'Id': '00kWt000002HF9qIAG', 'OpportunityId': '006Wt000007BAfxIAG', 'Product2Id': '01tWt000006hVhpIAE', 'PricebookEntryId': '01uWt0000027P3mIAE', 'Quantity': '8.0', 'TotalPrice': '3723.924'}], 'var_function-call-4250088271154245686': 'file_storage/function-call-4250088271154245686.json', 'var_function-call-4250088271154248763': 'file_storage/function-call-4250088271154248763.json', 'var_function-call-4250088271154247744': 'file_storage/function-call-4250088271154247744.json', 'var_function-call-4250088271154246725': [{'Id': '01uWt0000027P3lIAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027P3mIAE', 'UnitPrice': '489.99'}, {'Id': '01uWt0000027P5NIAU', 'UnitPrice': '599.99'}, {'Id': '#01uWt0000027P6zIAE', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027P8bIAE', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027P8cIAE', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PBpIAM', 'UnitPrice': '449.99'}, {'Id': '01uWt0000027PDRIA2', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PF3IAM', 'UnitPrice': '549.99'}, {'Id': '#01uWt0000027PGfIAM', 'UnitPrice': '479.99'}, {'Id': '01uWt0000027PIHIA2', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PIIIA2', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PIJIA2', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PJtIAM', 'UnitPrice': '649.99'}, {'Id': '01uWt0000027PLVIA2', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027PN7IAM', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027POjIAM', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027POkIAM', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PQLIA2', 'UnitPrice': '489.99'}, {'Id': '#01uWt0000027PRxIAM', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PTZIA2', 'UnitPrice': '449.99'}, {'Id': '#01uWt0000027PTaIAM', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PVBIA2', 'UnitPrice': '339.99'}, {'Id': '#01uWt0000027PWnIAM', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PYPIA2', 'UnitPrice': '319.99'}, {'Id': '01uWt0000027Pa1IAE', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PbdIAE', 'UnitPrice': '389.99'}, {'Id': '01uWt0000027PdFIAU', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PerIAE', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PgTIAU', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PgUIAU', 'UnitPrice': '379.99'}, {'Id': '01uWt0000027Pi5IAE', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PjhIAE', 'UnitPrice': '549.99'}, {'Id': '01uWt0000027PlJIAU', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027PmvIAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PoXIAU', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027Pq9IAE', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PrlIAE', 'UnitPrice': '369.99'}, {'Id': '#01uWt0000027PtNIAU', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PtOIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PuzIAE', 'UnitPrice': '629.99'}, {'Id': '01uWt0000027PwbIAE', 'UnitPrice': '559.99'}, {'Id': '#01uWt0000027PyDIAU', 'UnitPrice': '649.99'}, {'Id': '#01uWt0000027PzpIAE', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027Q1RIAU', 'UnitPrice': '579.99'}, {'Id': '#01uWt0000027Q33IAE', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027Q34IAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027Q4fIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Q6HIAU', 'UnitPrice': '619.99'}]}

exec(code, env_args)
