code = """import json

# Load data
opps = locals()['var_function-call-8258048349809593031']
items = locals()['var_function-call-1224518047950652746']
prices1 = locals()['var_function-call-2643572218047501224']
prices2 = locals()['var_function-call-1161226472684447054']

# Build price map
price_map = {}
for p in prices1 + prices2:
    # Normalize ID: remove leading # if present, or keep both variants?
    # The LineItems have clean IDs. The PricebookEntries have clean or # IDs.
    # If I clean the PricebookEntry ID, I can match with LineItem ID.
    clean_id = p['Id'].lstrip('#')
    price_map[clean_id] = float(p['UnitPrice'])
    price_map[p['Id']] = float(p['UnitPrice']) # Also keep original just in case

# Calculate sales per agent
agent_sales = {}

# Map OppId to OwnerId
opp_owner = {o['Id']: o['OwnerId'] for o in opps}
# Handle potential corruption in OppId matching? 
# The OppIds in 'opps' came from sales_pipeline.
# The OppIds in 'items' came from sales_pipeline.
# So they should match directly.
# But 'opps' result might have #.
# Let's normalize OppId map too.
opp_owner_clean = {o['Id'].lstrip('#'): o['OwnerId'] for o in opps}

for item in items:
    oid = item['OpportunityId'].lstrip('#')
    pbid = item['PricebookEntryId'].lstrip('#')
    qty = float(item['Quantity'])
    
    if pbid in price_map:
        uprice = price_map[pbid]
        amount = qty * uprice
        
        if oid in opp_owner_clean:
            agent = opp_owner_clean[oid]
            agent_sales[agent] = agent_sales.get(agent, 0) + amount
        else:
            # Maybe the opp id in item doesn't match?
            pass
    else:
        # Price missing?
        pass

# Find top agent
top_agent = None
max_sales = -1

for agent, sales in agent_sales.items():
    if sales > max_sales:
        max_sales = sales
        top_agent = agent

print("__RESULT__:")
print(json.dumps(top_agent))"""

env_args = {'var_function-call-3335699659846479295': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'AccountId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Status', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'StartDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CustomerSignedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CompanySignedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContractTerm', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-9694212357224474726': [{'cid': '0', 'name': 'Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'AccountId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'EffectiveDate', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'Pricebook2Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'OwnerId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-9694212357224476435': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContractID__c', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'AccountId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'ContactId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OwnerId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Probability', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Amount', 'column_type': 'DOUBLE', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'StageName', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Name', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Description', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CreatedDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'CloseDate', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-9072198076641195581': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}, {'Id': '801Wt00000PFsjQIAT', 'AccountId': '#001Wt00000PHVqdIAH', 'Status': 'Activated', 'EffectiveDate': '2021-09-30', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NGjwIAG'}, {'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'Status': 'Activated', 'EffectiveDate': '2022-09-15', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFtAmIAL', 'AccountId': '001Wt00000PHVdhIAH', 'Status': 'Activated  ', 'EffectiveDate': '2020-09-01', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PFtAnIAL', 'AccountId': '#001Wt00000PGaNjIAL', 'Status': 'Activated', 'EffectiveDate': '2023-06-01', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NEdJIAW'}], 'var_function-call-7773031435937721979': [{'CompanySignedDate': '2021-07-16'}, {'CompanySignedDate': '2021-09-28'}, {'CompanySignedDate': '2023-07-12'}, {'CompanySignedDate': '2024-04-16'}, {'CompanySignedDate': '2023-07-02'}], 'var_function-call-3305530749461673646': [{'Id': '800Wt00000DDNlnIAH'}, {'Id': '800Wt00000DDe3OIAT'}, {'Id': '800Wt00000DDeg6IAD'}, {'Id': '800Wt00000DDzZLIA1'}, {'Id': '#800Wt00000DDzvrIAD'}, {'Id': '800Wt00000DE0FHIA1'}, {'Id': '800Wt00000DE0TiIAL'}, {'Id': '800Wt00000DE2vLIAT'}, {'Id': '800Wt00000DE98oIAD'}, {'Id': '800Wt00000DE9GrIAL'}, {'Id': '#800Wt00000DE9ITIA1'}, {'Id': '#800Wt00000DE9SAIA1'}, {'Id': '800Wt00000DE9YbIAL'}, {'Id': '#800Wt00000DE9lVIAT'}, {'Id': '800Wt00000DE9qLIAT'}, {'Id': '800Wt00000DE9rxIAD'}], 'var_function-call-8258048349809593031': [{'Id': '#006Wt000007B5bTIAS', 'OwnerId': '005Wt000003NJ53IAG', 'ContractID__c': '800Wt00000DDe3OIAT'}, {'Id': '006Wt000007B6u8IAC', 'OwnerId': '005Wt000003NEa3IAG', 'ContractID__c': '800Wt00000DE2vLIAT'}, {'Id': '006Wt000007B8PgIAK', 'OwnerId': '005Wt000003NBp4IAG', 'ContractID__c': '800Wt00000DE0FHIA1'}, {'Id': '006Wt000007BAY1IAO', 'OwnerId': '005Wt000003NJmbIAG', 'ContractID__c': '800Wt00000DE0TiIAL'}, {'Id': '006Wt000007BBqXIAW', 'OwnerId': '005Wt000003NCegIAG', 'ContractID__c': '800Wt00000DDNlnIAH'}, {'Id': '006Wt000007BBs9IAG', 'OwnerId': '005Wt000003NGwoIAG', 'ContractID__c': '800Wt00000DE98oIAD'}, {'Id': '006Wt000007BCLCIA4', 'OwnerId': '005Wt000003NGFHIA4', 'ContractID__c': '800Wt00000DE9GrIAL'}, {'Id': '#006Wt000007BEgMIAW', 'OwnerId': '005Wt000003NJmcIAG', 'ContractID__c': '800Wt00000DE9YbIAL'}, {'Id': '#006Wt000007BFaoIAG', 'OwnerId': '005Wt000003NDEBIA4', 'ContractID__c': '800Wt00000DDzZLIA1'}, {'Id': '006Wt000007BHBBIA4', 'OwnerId': '005Wt000003NBp4IAG', 'ContractID__c': '800Wt00000DE9qLIAT'}, {'Id': '006Wt000007BHCpIAO', 'OwnerId': '005Wt000003NJkzIAG', 'ContractID__c': '800Wt00000DDeg6IAD'}, {'Id': '#006Wt000007BHJFIA4', 'OwnerId': '005Wt000003NHzJIAW', 'ContractID__c': '800Wt00000DE9rxIAD'}], 'var_function-call-9727473200444007826': "SELECT OpportunityId, PricebookEntryId, Quantity FROM OpportunityLineItem WHERE OpportunityId IN ('#006Wt000007B5bTIAS', '006Wt000007B6u8IAC', '006Wt000007B8PgIAK', '006Wt000007BAY1IAO', '006Wt000007BBqXIAW', '006Wt000007BBs9IAG', '006Wt000007BCLCIA4', '#006Wt000007BEgMIAW', '#006Wt000007BFaoIAG', '006Wt000007BHBBIA4', '006Wt000007BHCpIAO', '#006Wt000007BHJFIA4')", 'var_function-call-1224518047950652746': [{'OpportunityId': '006Wt000007BHCpIAO', 'PricebookEntryId': '01uWt0000027PIHIA2', 'Quantity': '8.0'}, {'OpportunityId': '006Wt000007BBs9IAG', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '10.0'}, {'OpportunityId': '006Wt000007BAY1IAO', 'PricebookEntryId': '01uWt0000027PtOIAU', 'Quantity': '7.0'}, {'OpportunityId': '006Wt000007B8PgIAK', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0'}, {'OpportunityId': '006Wt000007B8PgIAK', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '3.0'}, {'OpportunityId': '006Wt000007BBqXIAW', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '8.0'}, {'OpportunityId': '006Wt000007BBs9IAG', 'PricebookEntryId': '01uWt0000027PjhIAE', 'Quantity': '8.0'}, {'OpportunityId': '006Wt000007BBqXIAW', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0'}, {'OpportunityId': '006Wt000007BBqXIAW', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '12.0'}, {'OpportunityId': '006Wt000007BCLCIA4', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '10.0'}, {'OpportunityId': '006Wt000007B8PgIAK', 'PricebookEntryId': '01uWt0000027P6zIAE', 'Quantity': '4.0'}, {'OpportunityId': '006Wt000007BCLCIA4', 'PricebookEntryId': '01uWt0000027P6zIAE', 'Quantity': '15.0'}, {'OpportunityId': '006Wt000007BCLCIA4', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '8.0'}, {'OpportunityId': '006Wt000007B6u8IAC', 'PricebookEntryId': '01uWt0000027PLVIA2', 'Quantity': '20.0'}, {'OpportunityId': '006Wt000007B6u8IAC', 'PricebookEntryId': '01uWt0000027PIIIA2', 'Quantity': '50.0'}, {'OpportunityId': '006Wt000007B6u8IAC', 'PricebookEntryId': '01uWt0000027PJtIAM', 'Quantity': '30.0'}, {'OpportunityId': '006Wt000007BHBBIA4', 'PricebookEntryId': '01uWt0000027P6zIAE', 'Quantity': '10.0'}, {'OpportunityId': '006Wt000007BHCpIAO', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '12.0'}, {'OpportunityId': '006Wt000007B8PgIAK', 'PricebookEntryId': '01uWt0000027PF3IAM', 'Quantity': '3.0'}, {'OpportunityId': '#006Wt000007BEgMIAW', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '6.0'}, {'OpportunityId': '#006Wt000007BFaoIAG', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '8.0'}, {'OpportunityId': '006Wt000007BAY1IAO', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '3.0'}, {'OpportunityId': '006Wt000007BHBBIA4', 'PricebookEntryId': '01uWt0000027PjhIAE', 'Quantity': '9.0'}, {'OpportunityId': '006Wt000007BHCpIAO', 'PricebookEntryId': '01uWt0000027P6zIAE', 'Quantity': '15.0'}, {'OpportunityId': '#006Wt000007BFaoIAG', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '10.0'}], 'var_function-call-4805509632586205464': "SELECT Id, UnitPrice FROM PricebookEntry WHERE Id IN ('01uWt0000027P3lIAE', '01uWt0000027P5NIAU', '01uWt0000027PjhIAE', '01uWt0000027PF3IAM', '01uWt0000027P6zIAE', '01uWt0000027PIIIA2', '01uWt0000027PJtIAM', '01uWt0000027P8bIAE', '01uWt0000027P8cIAE', '01uWt0000027PIHIA2', '01uWt0000027PtOIAU', '01uWt0000027PLVIA2')", 'var_function-call-2643572218047501224': [{'Id': '01uWt0000027P3lIAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027P5NIAU', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027P8cIAE', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PF3IAM', 'UnitPrice': '549.99'}, {'Id': '01uWt0000027PIHIA2', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PIIIA2', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PJtIAM', 'UnitPrice': '649.99'}, {'Id': '01uWt0000027PLVIA2', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PjhIAE', 'UnitPrice': '549.99'}, {'Id': '01uWt0000027PtOIAU', 'UnitPrice': '529.99'}], 'var_function-call-1161226472684447054': [{'Id': '#01uWt0000027P6zIAE', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027P8bIAE', 'UnitPrice': '349.99'}]}

exec(code, env_args)
