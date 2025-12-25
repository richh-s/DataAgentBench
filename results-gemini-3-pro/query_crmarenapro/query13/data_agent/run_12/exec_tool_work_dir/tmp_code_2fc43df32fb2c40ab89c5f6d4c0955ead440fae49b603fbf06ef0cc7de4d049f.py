code = """import json
import pandas as pd

# Load data
contracts = json.loads(open(locals()['var_function-call-10327746493149238310']).read())
opportunities = json.loads(open(locals()['var_function-call-13946496229795720004']).read())
line_items = json.loads(open(locals()['var_function-call-6192671190439857498']).read())
pricebook_entries = locals()['var_function-call-8189512320069881452']

# Helper to clean ID
def clean_id(val):
    if val is None:
        return None
    val = str(val).strip()
    if val.startswith('#'):
        val = val[1:]
    return val

# 1. Filter Contracts
eligible_contracts = set()
start_date = '2022-06-25'
end_date = '2022-11-25'

for c in contracts:
    cid = clean_id(c.get('Id'))
    cdate = c.get('CompanySignedDate')
    if cdate and start_date <= cdate <= end_date:
        eligible_contracts.add(cid)

print(f"Eligible contracts: {len(eligible_contracts)}")

# 2. Map PricebookEntry UnitPrice
pb_map = {}
for pb in pricebook_entries:
    pbid = clean_id(pb.get('Id'))
    price = pb.get('UnitPrice')
    if price:
        pb_map[pbid] = float(price)

# 3. Identify Eligible Opportunities
eligible_opps = {} # OppId -> OwnerId
for opp in opportunities:
    contract_id = clean_id(opp.get('ContractID__c'))
    if contract_id in eligible_contracts:
        opp_id = clean_id(opp.get('Id'))
        owner_id = clean_id(opp.get('OwnerId'))
        eligible_opps[opp_id] = owner_id

print(f"Eligible opportunities: {len(eligible_opps)}")

# 4. Calculate Sales
agent_sales = {}

for li in line_items:
    opp_id = clean_id(li.get('OpportunityId'))
    if opp_id in eligible_opps:
        pb_id = clean_id(li.get('PricebookEntryId'))
        qty = float(li.get('Quantity') or 0)
        unit_price = pb_map.get(pb_id, 0.0)
        amount = qty * unit_price
        
        agent = eligible_opps[opp_id]
        if agent:
            agent_sales[agent] = agent_sales.get(agent, 0.0) + amount

# 5. Find top agent
top_agent = None
max_sales = -1.0

for agent, sales in agent_sales.items():
    if sales > max_sales:
        max_sales = sales
        top_agent = agent

print("__RESULT__:")
print(json.dumps(top_agent))"""

env_args = {'var_function-call-1439226136930535522': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_function-call-956329507705697281': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGeJIIA1', 'ContactId': '003Wt00000JqvQiIAJ', 'OwnerId': '005Wt000003NIqXIAW', 'Probability': '75.0', 'Amount': '182448.4965', 'StageName': 'Qualification', 'Name': 'InnoSphere Labs - EDA Innovation Expansion', 'Description': 'InnoSphere Labs is exploring advanced EDA solutions to enhance their R&D capabilities. They are particularly interested in the AI Cirku-Tech for rapid circuit prototyping, and the EcoPCB Creator for environmentally-friendly design processes. Additionally, CloudLink Designer could improve their team collaboration across global projects.', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'CloseDate': '2024-02-15'}], 'var_function-call-17426391982604854805': [{'Id': '#800Wt00000DD0SZIA1', 'AccountId': '001Wt00000PGZmfIAH', 'Status': 'Activated  ', 'StartDate': '2021-07-20', 'CustomerSignedDate': '2021-07-15', 'CompanySignedDate': '2021-07-16', 'Description': 'This contract solidifies the expanded partnership with Quantum Dynamics LLC for the provision of advanced AI-powered EDA tools, focusing on enhancing their quantum computing technology developments.', 'ContractTerm': '24'}], 'var_function-call-3590336326613724905': [{'sql': 'CREATE TABLE "Order" (\n"Id" TEXT,\n  "AccountId" TEXT,\n  "Status" TEXT,\n  "EffectiveDate" TEXT,\n  "Pricebook2Id" TEXT,\n  "OwnerId" TEXT\n)'}], 'var_function-call-1952542891905655352': [{'Id': '800Wt00000DDNlnIAH', 'CompanySignedDate': '2022-09-02'}, {'Id': '800Wt00000DDe3OIAT', 'CompanySignedDate': '2022-09-20'}, {'Id': '800Wt00000DDeg6IAD', 'CompanySignedDate': '2022-07-18'}, {'Id': '800Wt00000DDzZLIA1', 'CompanySignedDate': '2022-10-26'}, {'Id': '#800Wt00000DDzvrIAD', 'CompanySignedDate': '2022-08-30'}, {'Id': '800Wt00000DE0FHIA1', 'CompanySignedDate': '2022-08-02'}, {'Id': '800Wt00000DE0TiIAL', 'CompanySignedDate': '2022-09-10'}, {'Id': '800Wt00000DE2vLIAT', 'CompanySignedDate': '2022-06-29'}, {'Id': '800Wt00000DE98oIAD', 'CompanySignedDate': '2022-11-10'}, {'Id': '800Wt00000DE9GrIAL', 'CompanySignedDate': '2022-06-30'}, {'Id': '#800Wt00000DE9ITIA1', 'CompanySignedDate': '2022-09-11'}, {'Id': '#800Wt00000DE9SAIA1', 'CompanySignedDate': '2022-09-30'}, {'Id': '800Wt00000DE9YbIAL', 'CompanySignedDate': '2022-11-22'}, {'Id': '#800Wt00000DE9lVIAT', 'CompanySignedDate': '2022-06-26'}, {'Id': '800Wt00000DE9qLIAT', 'CompanySignedDate': '2022-09-01'}, {'Id': '800Wt00000DE9rxIAD', 'CompanySignedDate': '2022-09-19'}], 'var_function-call-18428208470016686395': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_function-call-10327746493149238310': 'file_storage/function-call-10327746493149238310.json', 'var_function-call-13946496229795720004': 'file_storage/function-call-13946496229795720004.json', 'var_function-call-6192671190439857498': 'file_storage/function-call-6192671190439857498.json', 'var_function-call-8189512320069881452': [{'Id': '01uWt0000027P3lIAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027P3mIAE', 'UnitPrice': '489.99'}, {'Id': '01uWt0000027P5NIAU', 'UnitPrice': '599.99'}, {'Id': '#01uWt0000027P6zIAE', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027P8bIAE', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027P8cIAE', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PBpIAM', 'UnitPrice': '449.99'}, {'Id': '01uWt0000027PDRIA2', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PF3IAM', 'UnitPrice': '549.99'}, {'Id': '#01uWt0000027PGfIAM', 'UnitPrice': '479.99'}, {'Id': '01uWt0000027PIHIA2', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PIIIA2', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PIJIA2', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PJtIAM', 'UnitPrice': '649.99'}, {'Id': '01uWt0000027PLVIA2', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027PN7IAM', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027POjIAM', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027POkIAM', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PQLIA2', 'UnitPrice': '489.99'}, {'Id': '#01uWt0000027PRxIAM', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PTZIA2', 'UnitPrice': '449.99'}, {'Id': '#01uWt0000027PTaIAM', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PVBIA2', 'UnitPrice': '339.99'}, {'Id': '#01uWt0000027PWnIAM', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PYPIA2', 'UnitPrice': '319.99'}, {'Id': '01uWt0000027Pa1IAE', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PbdIAE', 'UnitPrice': '389.99'}, {'Id': '01uWt0000027PdFIAU', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PerIAE', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PgTIAU', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PgUIAU', 'UnitPrice': '379.99'}, {'Id': '01uWt0000027Pi5IAE', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PjhIAE', 'UnitPrice': '549.99'}, {'Id': '01uWt0000027PlJIAU', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027PmvIAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PoXIAU', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027Pq9IAE', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PrlIAE', 'UnitPrice': '369.99'}, {'Id': '#01uWt0000027PtNIAU', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PtOIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PuzIAE', 'UnitPrice': '629.99'}, {'Id': '01uWt0000027PwbIAE', 'UnitPrice': '559.99'}, {'Id': '#01uWt0000027PyDIAU', 'UnitPrice': '649.99'}, {'Id': '#01uWt0000027PzpIAE', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027Q1RIAU', 'UnitPrice': '579.99'}, {'Id': '#01uWt0000027Q33IAE', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027Q34IAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027Q4fIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Q6HIAU', 'UnitPrice': '619.99'}]}

exec(code, env_args)
