code = """import pandas as pd
import json

opp_items = locals()['var_function-call-11037518409619249767']
price_entries = locals()['var_function-call-11037518409619248518']

# Process Pricebook
price_map = {}
for entry in price_entries:
    raw_id = entry['Id']
    clean_id = raw_id.lstrip('#')
    try:
        price = float(entry['UnitPrice'])
    except:
        price = 0.0
    price_map[clean_id] = price

# Process Sales
sales_by_agent = {}

for item in opp_items:
    owner_id = item['OwnerId']
    try:
        qty = float(item['Quantity'])
    except:
        qty = 0.0
    pb_id = item['PricebookEntryId']
    clean_pb_id = pb_id.lstrip('#')
    
    if clean_pb_id in price_map:
        unit_price = price_map[clean_pb_id]
        amount = qty * unit_price
        
        if owner_id not in sales_by_agent:
            sales_by_agent[owner_id] = 0.0
        sales_by_agent[owner_id] += amount

# Find top agent
top_agent = None
max_sales = -1.0

for agent, sales in sales_by_agent.items():
    if sales > max_sales:
        max_sales = sales
        top_agent = agent

print("__RESULT__:")
print(json.dumps(top_agent))"""

env_args = {'var_function-call-4957158246162620387': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_function-call-4957158246162619548': [{'Id': '#800Wt00000DD0SZIA1', 'AccountId': '001Wt00000PGZmfIAH', 'Status': 'Activated  ', 'StartDate': '2021-07-20', 'CustomerSignedDate': '2021-07-15', 'CompanySignedDate': '2021-07-16', 'Description': 'This contract solidifies the expanded partnership with Quantum Dynamics LLC for the provision of advanced AI-powered EDA tools, focusing on enhancing their quantum computing technology developments.', 'ContractTerm': '24'}], 'var_function-call-4957158246162618709': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGeJIIA1', 'ContactId': '003Wt00000JqvQiIAJ', 'OwnerId': '005Wt000003NIqXIAW', 'Probability': '75.0', 'Amount': '182448.4965', 'StageName': 'Qualification', 'Name': 'InnoSphere Labs - EDA Innovation Expansion', 'Description': 'InnoSphere Labs is exploring advanced EDA solutions to enhance their R&D capabilities. They are particularly interested in the AI Cirku-Tech for rapid circuit prototyping, and the EcoPCB Creator for environmentally-friendly design processes. Additionally, CloudLink Designer could improve their team collaboration across global projects.', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'CloseDate': '2024-02-15'}], 'var_function-call-3013834187475695314': [{'COUNT(*)': '15'}], 'var_function-call-3013834187475697347': [{'count_star()': '16'}], 'var_function-call-7614373227106312584': [{'count(DISTINCT o.Id)': '12'}], 'var_function-call-11037518409619249767': [{'OwnerId': '005Wt000003NJkzIAG', 'Quantity': '8.0', 'PricebookEntryId': '01uWt0000027PIHIA2'}, {'OwnerId': '005Wt000003NGwoIAG', 'Quantity': '10.0', 'PricebookEntryId': '01uWt0000027P5NIAU'}, {'OwnerId': '005Wt000003NJmbIAG', 'Quantity': '7.0', 'PricebookEntryId': '01uWt0000027PtOIAU'}, {'OwnerId': '005Wt000003NBp4IAG', 'Quantity': '2.0', 'PricebookEntryId': '01uWt0000027P8cIAE'}, {'OwnerId': '005Wt000003NBp4IAG', 'Quantity': '3.0', 'PricebookEntryId': '01uWt0000027P5NIAU'}, {'OwnerId': '005Wt000003NCegIAG', 'Quantity': '8.0', 'PricebookEntryId': '01uWt0000027P5NIAU'}, {'OwnerId': '005Wt000003NGwoIAG', 'Quantity': '8.0', 'PricebookEntryId': '01uWt0000027PjhIAE'}, {'OwnerId': '005Wt000003NCegIAG', 'Quantity': '10.0', 'PricebookEntryId': '01uWt0000027P3lIAE'}, {'OwnerId': '005Wt000003NCegIAG', 'Quantity': '12.0', 'PricebookEntryId': '01uWt0000027P8cIAE'}, {'OwnerId': '005Wt000003NGFHIA4', 'Quantity': '10.0', 'PricebookEntryId': '01uWt0000027P5NIAU'}, {'OwnerId': '005Wt000003NBp4IAG', 'Quantity': '4.0', 'PricebookEntryId': '01uWt0000027P6zIAE'}, {'OwnerId': '005Wt000003NGFHIA4', 'Quantity': '15.0', 'PricebookEntryId': '01uWt0000027P6zIAE'}, {'OwnerId': '005Wt000003NGFHIA4', 'Quantity': '8.0', 'PricebookEntryId': '01uWt0000027P8cIAE'}, {'OwnerId': '005Wt000003NEa3IAG', 'Quantity': '20.0', 'PricebookEntryId': '01uWt0000027PLVIA2'}, {'OwnerId': '005Wt000003NEa3IAG', 'Quantity': '50.0', 'PricebookEntryId': '01uWt0000027PIIIA2'}, {'OwnerId': '005Wt000003NEa3IAG', 'Quantity': '30.0', 'PricebookEntryId': '01uWt0000027PJtIAM'}, {'OwnerId': '005Wt000003NBp4IAG', 'Quantity': '10.0', 'PricebookEntryId': '01uWt0000027P6zIAE'}, {'OwnerId': '005Wt000003NJkzIAG', 'Quantity': '12.0', 'PricebookEntryId': '01uWt0000027P8bIAE'}, {'OwnerId': '005Wt000003NBp4IAG', 'Quantity': '3.0', 'PricebookEntryId': '01uWt0000027PF3IAM'}, {'OwnerId': '005Wt000003NJmcIAG', 'Quantity': '6.0', 'PricebookEntryId': '01uWt0000027P8cIAE'}, {'OwnerId': '005Wt000003NDEBIA4', 'Quantity': '8.0', 'PricebookEntryId': '01uWt0000027P5NIAU'}, {'OwnerId': '005Wt000003NJmbIAG', 'Quantity': '3.0', 'PricebookEntryId': '01uWt0000027P5NIAU'}, {'OwnerId': '005Wt000003NBp4IAG', 'Quantity': '9.0', 'PricebookEntryId': '01uWt0000027PjhIAE'}, {'OwnerId': '005Wt000003NJkzIAG', 'Quantity': '15.0', 'PricebookEntryId': '01uWt0000027P6zIAE'}, {'OwnerId': '005Wt000003NDEBIA4', 'Quantity': '10.0', 'PricebookEntryId': '01uWt0000027P8cIAE'}], 'var_function-call-11037518409619248518': [{'Id': '01uWt0000027P3lIAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027P3mIAE', 'UnitPrice': '489.99'}, {'Id': '01uWt0000027P5NIAU', 'UnitPrice': '599.99'}, {'Id': '#01uWt0000027P6zIAE', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027P8bIAE', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027P8cIAE', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PBpIAM', 'UnitPrice': '449.99'}, {'Id': '01uWt0000027PDRIA2', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PF3IAM', 'UnitPrice': '549.99'}, {'Id': '#01uWt0000027PGfIAM', 'UnitPrice': '479.99'}, {'Id': '01uWt0000027PIHIA2', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PIIIA2', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PIJIA2', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PJtIAM', 'UnitPrice': '649.99'}, {'Id': '01uWt0000027PLVIA2', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027PN7IAM', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027POjIAM', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027POkIAM', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PQLIA2', 'UnitPrice': '489.99'}, {'Id': '#01uWt0000027PRxIAM', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PTZIA2', 'UnitPrice': '449.99'}, {'Id': '#01uWt0000027PTaIAM', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PVBIA2', 'UnitPrice': '339.99'}, {'Id': '#01uWt0000027PWnIAM', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PYPIA2', 'UnitPrice': '319.99'}, {'Id': '01uWt0000027Pa1IAE', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PbdIAE', 'UnitPrice': '389.99'}, {'Id': '01uWt0000027PdFIAU', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PerIAE', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PgTIAU', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PgUIAU', 'UnitPrice': '379.99'}, {'Id': '01uWt0000027Pi5IAE', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PjhIAE', 'UnitPrice': '549.99'}, {'Id': '01uWt0000027PlJIAU', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027PmvIAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PoXIAU', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027Pq9IAE', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PrlIAE', 'UnitPrice': '369.99'}, {'Id': '#01uWt0000027PtNIAU', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PtOIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PuzIAE', 'UnitPrice': '629.99'}, {'Id': '01uWt0000027PwbIAE', 'UnitPrice': '559.99'}, {'Id': '#01uWt0000027PyDIAU', 'UnitPrice': '649.99'}, {'Id': '#01uWt0000027PzpIAE', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027Q1RIAU', 'UnitPrice': '579.99'}, {'Id': '#01uWt0000027Q33IAE', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027Q34IAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027Q4fIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Q6HIAU', 'UnitPrice': '619.99'}]}

exec(code, env_args)
