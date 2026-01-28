code = """import json
import pandas as pd
from datetime import datetime

# Load opportunities data from April 2023
opportunities = var_functions.query_db:2
print(f"Number of opportunities loaded: {len(opportunities)}")

# Filter opportunities with valid contract IDs (not 'None')
opportunities_with_contracts = [opp for opp in opportunities if opp['ContractID__c'] and opp['ContractID__c'] != 'None']
print(f"Opportunities with contracts: {len(opportunities_with_contracts)}")

# Extract contract IDs from those opportunities
contract_ids = [opp['ContractID__c'] for opp in opportunities_with_contracts]
print(f"Contract IDs: {contract_ids}")

# Load the contracts file
contracts_file = var_functions.query_db:5
with open(contracts_file, 'r') as f:
    contracts = json.load(f)

print(f"Total contracts loaded: {len(contracts)}")

# Filter to only the contracts we're interested in
relevant_contracts = [c for c in contracts if c['Id'] in contract_ids]
print(f"Relevant contracts for our opportunities: {len(relevant_contracts)}")

# Create a dictionary mapping contract ID to contract data
contract_dict = {c['Id']: c for c in relevant_contracts}

# Calculate sales cycle for each opportunity with a contract
sales_cycles = []

for opp in opportunities_with_contracts:
    contract_id = opp['ContractID__c']
    if contract_id in contract_dict:
        contract = contract_dict[contract_id]
        
        # Parse dates
        created_date_str = opp['CreatedDate']
        company_signed_date_str = contract['CompanySignedDate']
        
        # Parse CreatedDate (ISO format with timezone)
        created_date = datetime.fromisoformat(created_date_str.replace('Z', '+00:00'))
        
        # Parse CompanySignedDate (YYYY-MM-DD format)
        company_signed_date = datetime.fromisoformat(company_signed_date_str + 'T00:00:00+00:00')
        
        # Calculate days difference
        days_diff = (company_signed_date - created_date).days
        
        sales_cycles.append({
            'OpportunityId': opp['Id'],
            'OwnerId': opp['OwnerId'],
            'CreatedDate': created_date_str,
            'CompanySignedDate': company_signed_date_str,
            'SalesCycleDays': days_diff
        })

print(f"Calculated sales cycles for {len(sales_cycles)} opportunities")

# Print a few examples for validation
if sales_cycles:
    for sc in sales_cycles[:5]:
        print(f"  {sc['OwnerId']}: {sc['SalesCycleDays']} days")

print("\nNow processing to find agent with quickest average turnaround...")

# Group by OwnerId and calculate average sales cycle
from collections import defaultdict
owner_sales_cycles = defaultdict(list)

for sc in sales_cycles:
    owner_sales_cycles[sc['OwnerId']].append(sc['SalesCycleDays'])

# Calculate averages
owner_averages = {}
for owner, cycles in owner_sales_cycles.items():
    avg_cycle = sum(cycles) / len(cycles)
    owner_averages[owner] = {
        'average_days': avg_cycle,
        'opportunity_count': len(cycles)
    }

# Sort by average days (quickest first)
sorted_owners = sorted(owner_averages.items(), key=lambda x: x[1]['average_days'])

print(f"\nNumber of agents with sales cycles: {len(sorted_owners)}")
for i, (owner_id, data) in enumerate(sorted_owners[:5]):
    print(f"  {i+1}. Agent {owner_id}: {data['average_days']:.2f} days avg, {data['opportunity_count']} opportunities")

if sorted_owners:
    quickest_agent = sorted_owners[0]
    result = quickest_agent[0]
else:
    result = None

print(f"\nQuickest agent: {result}")

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.execute_python:0': 'Ready to query databases', 'var_functions.query_db:2': [{'Id': '#006Wt000007B1klIAC', 'OwnerId': '#005Wt000003NBylIAG', 'CreatedDate': '2023-04-15T09:00:34.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007B49NIAS', 'OwnerId': '005Wt000003NIs9IAG', 'CreatedDate': '2023-04-25T14:32:51.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007B62sIAC', 'OwnerId': '005Wt000003NJZhIAO', 'CreatedDate': '2023-04-04T10:15:30.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007B6itIAC', 'OwnerId': '#005Wt000003NJMnIAO', 'CreatedDate': '2023-04-25T09:45:30.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007B7tQIAS', 'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-15T10:20:30.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007B7yJIAS', 'OwnerId': '#005Wt000003NEdJIAW', 'CreatedDate': '2023-04-15T10:30:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007B8CqIAK', 'OwnerId': '005Wt000003NInKIAW', 'CreatedDate': '2023-04-15T09:30:45.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007B8FyIAK', 'OwnerId': '005Wt000003NIovIAG', 'CreatedDate': '2023-04-15T10:30:15.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BA3JIAW', 'OwnerId': '005Wt000003NF9WIAW', 'CreatedDate': '2023-04-02T10:15:30.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BABLIA4', 'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2023-04-01T14:47:23.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BAHlIAO', 'OwnerId': '#005Wt000003NFhPIAW', 'CreatedDate': '2023-04-19T15:30:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BAPrIAO', 'OwnerId': '005Wt000003NJxtIAG', 'CreatedDate': '2023-04-15T10:15:32.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BBDrIAO', 'OwnerId': '005Wt000003NJ1pIAG', 'CreatedDate': '2023-04-10T10:30:15.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BBc1IAG', 'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15T10:14:32.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BCLEIA4', 'OwnerId': '005Wt000003NJBVIA4', 'CreatedDate': '2023-04-27T11:22:30.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BCTFIA4', 'OwnerId': '#005Wt000003NBcBIAW', 'CreatedDate': '2023-04-20T11:15:33.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BChmIAG', 'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'ContractID__c': '800Wt00000DE9FFIA1'}, {'Id': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'ContractID__c': '800Wt00000DE8sgIAD'}, {'Id': '#006Wt000007BDXPIA4', 'OwnerId': '005Wt000003NJ0EIAW', 'CreatedDate': '2023-04-15T10:45:00.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BDcEIAW', 'OwnerId': '005Wt000003NIAbIAO', 'CreatedDate': '2023-04-15T10:32:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BDpAIAW', 'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15T10:30:15.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BETVIA4', 'OwnerId': '#005Wt000003NJjNIAW', 'CreatedDate': '2023-04-20T11:34:22.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BEV4IAO', 'OwnerId': '005Wt000003NFRKIA4', 'CreatedDate': '2023-04-05T14:23:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BFUOIA4', 'OwnerId': '005Wt000003NHpdIAG', 'CreatedDate': '2023-04-05T10:15:30.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BGAIIA4', 'OwnerId': '005Wt000003NIdeIAG', 'CreatedDate': '2023-04-11T12:45:33.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BGDVIA4', 'OwnerId': '005Wt000003NBcBIAW', 'CreatedDate': '2023-04-10T11:20:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BHPhIAO', 'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'ContractID__c': '800Wt00000DE9ryIAD'}, {'Id': '#006Wt000007BHZNIA4', 'OwnerId': '005Wt000003NIaPIAW', 'CreatedDate': '2023-04-10T14:25:30.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BHfpIAG', 'OwnerId': '005Wt000003NIqXIAW', 'CreatedDate': '2023-04-17T14:37:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BHr7IAG', 'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-01T09:45:23.000+0000', 'ContractID__c': 'None'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
