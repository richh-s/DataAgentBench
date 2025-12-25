code = """import json

# Retrieve stored data
pipeline_data = locals()['var_function-call-13606270176446543216']
pricing_data = locals()['var_function-call-95621474381825026']

# Helper to clean IDs
def clean_id(val):
    if not val:
        return ""
    val = str(val).strip()
    if val.startswith("#"):
        val = val[1:]
    return val

# Build price map
price_map = {}
for item in pricing_data:
    raw_id = item['Id']
    # Price might be string, convert to float
    try:
        price = float(item['UnitPrice'])
    except:
        price = 0.0
    
    clean_key = clean_id(raw_id)
    price_map[clean_key] = price

# Calculate totals per agent
totals = {}
for row in pipeline_data:
    pid = clean_id(row['PricebookEntryId'])
    owner = clean_id(row['OwnerId'])
    
    try:
        qty = float(row['Quantity'])
    except:
        qty = 0.0
        
    unit_price = price_map.get(pid, 0.0)
    amount = qty * unit_price
    
    if owner not in totals:
        totals[owner] = 0.0
    totals[owner] += amount

# Find top agent
top_agent = None
max_sales = -1.0

for agent, sales in totals.items():
    if sales > max_sales:
        max_sales = sales
        top_agent = agent

print("__RESULT__:")
print(json.dumps(top_agent))"""

env_args = {'var_function-call-5799114275567237712': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_function-call-5799114275567238829': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGeJIIA1', 'ContactId': '003Wt00000JqvQiIAJ', 'OwnerId': '005Wt000003NIqXIAW', 'Probability': '75.0', 'Amount': '182448.4965', 'StageName': 'Qualification', 'Name': 'InnoSphere Labs - EDA Innovation Expansion', 'Description': 'InnoSphere Labs is exploring advanced EDA solutions to enhance their R&D capabilities. They are particularly interested in the AI Cirku-Tech for rapid circuit prototyping, and the EcoPCB Creator for environmentally-friendly design processes. Additionally, CloudLink Designer could improve their team collaboration across global projects.', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'CloseDate': '2024-02-15'}], 'var_function-call-3302918475087994634': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OpportunityId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Product2Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'PricebookEntryId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Quantity', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'TotalPrice', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-3302918475087991137': [{'cid': '0', 'name': 'Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'AccountId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'EffectiveDate', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'Pricebook2Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'OwnerId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-3302918475087991736': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'AccountId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Status', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'StartDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CustomerSignedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CompanySignedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContractTerm', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-13606270176446543216': [{'PricebookEntryId': '01uWt0000027PIHIA2', 'Quantity': '8.0', 'OwnerId': '005Wt000003NJkzIAG'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '10.0', 'OwnerId': '005Wt000003NGwoIAG'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'Quantity': '7.0', 'OwnerId': '005Wt000003NJmbIAG'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'OwnerId': '005Wt000003NBp4IAG'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '3.0', 'OwnerId': '005Wt000003NBp4IAG'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '8.0', 'OwnerId': '005Wt000003NCegIAG'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'Quantity': '8.0', 'OwnerId': '005Wt000003NGwoIAG'}, {'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'OwnerId': '005Wt000003NCegIAG'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '12.0', 'OwnerId': '005Wt000003NCegIAG'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '10.0', 'OwnerId': '005Wt000003NGFHIA4'}, {'PricebookEntryId': '01uWt0000027P6zIAE', 'Quantity': '4.0', 'OwnerId': '005Wt000003NBp4IAG'}, {'PricebookEntryId': '01uWt0000027P6zIAE', 'Quantity': '15.0', 'OwnerId': '005Wt000003NGFHIA4'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '8.0', 'OwnerId': '005Wt000003NGFHIA4'}, {'PricebookEntryId': '01uWt0000027PLVIA2', 'Quantity': '20.0', 'OwnerId': '005Wt000003NEa3IAG'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'Quantity': '50.0', 'OwnerId': '005Wt000003NEa3IAG'}, {'PricebookEntryId': '01uWt0000027PJtIAM', 'Quantity': '30.0', 'OwnerId': '005Wt000003NEa3IAG'}, {'PricebookEntryId': '01uWt0000027P6zIAE', 'Quantity': '10.0', 'OwnerId': '005Wt000003NBp4IAG'}, {'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '12.0', 'OwnerId': '005Wt000003NJkzIAG'}, {'PricebookEntryId': '01uWt0000027PF3IAM', 'Quantity': '3.0', 'OwnerId': '005Wt000003NBp4IAG'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '6.0', 'OwnerId': '005Wt000003NJmcIAG'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '8.0', 'OwnerId': '005Wt000003NDEBIA4'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '3.0', 'OwnerId': '005Wt000003NJmbIAG'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'Quantity': '9.0', 'OwnerId': '005Wt000003NBp4IAG'}, {'PricebookEntryId': '01uWt0000027P6zIAE', 'Quantity': '15.0', 'OwnerId': '005Wt000003NJkzIAG'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '10.0', 'OwnerId': '005Wt000003NDEBIA4'}], 'var_function-call-95621474381825026': [{'Id': '01uWt0000027P3lIAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027P3mIAE', 'UnitPrice': '489.99'}, {'Id': '01uWt0000027P5NIAU', 'UnitPrice': '599.99'}, {'Id': '#01uWt0000027P6zIAE', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027P8bIAE', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027P8cIAE', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PBpIAM', 'UnitPrice': '449.99'}, {'Id': '01uWt0000027PDRIA2', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PF3IAM', 'UnitPrice': '549.99'}, {'Id': '#01uWt0000027PGfIAM', 'UnitPrice': '479.99'}, {'Id': '01uWt0000027PIHIA2', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PIIIA2', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PIJIA2', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PJtIAM', 'UnitPrice': '649.99'}, {'Id': '01uWt0000027PLVIA2', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027PN7IAM', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027POjIAM', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027POkIAM', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PQLIA2', 'UnitPrice': '489.99'}, {'Id': '#01uWt0000027PRxIAM', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PTZIA2', 'UnitPrice': '449.99'}, {'Id': '#01uWt0000027PTaIAM', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PVBIA2', 'UnitPrice': '339.99'}, {'Id': '#01uWt0000027PWnIAM', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PYPIA2', 'UnitPrice': '319.99'}, {'Id': '01uWt0000027Pa1IAE', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PbdIAE', 'UnitPrice': '389.99'}, {'Id': '01uWt0000027PdFIAU', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PerIAE', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PgTIAU', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PgUIAU', 'UnitPrice': '379.99'}, {'Id': '01uWt0000027Pi5IAE', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PjhIAE', 'UnitPrice': '549.99'}, {'Id': '01uWt0000027PlJIAU', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027PmvIAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PoXIAU', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027Pq9IAE', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PrlIAE', 'UnitPrice': '369.99'}, {'Id': '#01uWt0000027PtNIAU', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PtOIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PuzIAE', 'UnitPrice': '629.99'}, {'Id': '01uWt0000027PwbIAE', 'UnitPrice': '559.99'}, {'Id': '#01uWt0000027PyDIAU', 'UnitPrice': '649.99'}, {'Id': '#01uWt0000027PzpIAE', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027Q1RIAU', 'UnitPrice': '579.99'}, {'Id': '#01uWt0000027Q33IAE', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027Q34IAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027Q4fIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Q6HIAU', 'UnitPrice': '619.99'}]}

exec(code, env_args)
