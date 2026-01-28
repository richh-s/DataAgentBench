code = """import json
from datetime import datetime

# Load results
ops = var_functions.query_db_2
contracts = var_functions.query_query_5

print("Opportunities:", len(ops))
print("Contracts:", len(contracts))

# Create contract lookup
contract_dict = {c['Id']: c for c in contracts}

# Process opportunities
valid_ops = []
for op in ops:
    if op['ContractID__c'] and op['ContractID__c'] != 'None':
        if op['ContractID__c'] in contract_dict:
            # Parse dates
            created = datetime.strptime(op['CreatedDate'][:10], '%Y-%m-%d')
            contract_signed = datetime.strptime(contract_dict[op['ContractID__c']]['CompanySignedDate'], '%Y-%m-%d')
            
            # Calculate turnaround days
            turnaround = (contract_signed - created).days
            
            owner = op['OwnerId']
            # Clean up owner ID if it has leading #
            if owner.startswith('#'):
                owner = owner[1:]
                
            valid_ops.append({
                'op_id': op['Id'],
                'owner_id': owner,
                'turnaround_days': turnaround,
                'created': created.strftime('%Y-%m-%d'),
                'signed': contract_dict[op['ContractID__c']]['CompanySignedDate']
            })

print(f"Valid opportunities with contracts: {len(valid_ops)}")
for i, op in enumerate(valid_ops[:5]):
    print(f"  {i}: Owner={op['owner_id']}, Turnaround={op['turnaround_days']} days")

# Group by owner and calculate average
turnaround_by_owner = {}
for op in valid_ops:
    owner = op['owner_id']
    if owner not in turnaround_by_owner:
        turnaround_by_owner[owner] = []
    turnaround_by_owner[owner].append(op['turnaround_days'])

# Calculate averages
averages = {}
for owner, days_list in turnaround_by_owner.items():
    averages[owner] = sum(days_list) / len(days_list)

# Find quickest
sorted_averages = sorted(averages.items(), key=lambda x: x[1])
print("\nAll agents with average turnaround:")
for owner, avg in sorted_averages:
    print(f"  {owner}: {avg:.1f} days (count: {len(turnaround_by_owner[owner])})")

if sorted_averages:
    quickest_owner = sorted_averages[0][0]
    print(f"\nQuickest agent: {quickest_owner} with {sorted_averages[0][1]:.1f} days average")
    result = quickest_owner
else:
    result = "No data found"

__RESULT__:
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'Id': '#006Wt000007B5jWIAS', 'OwnerId': '005Wt000003NFB8IAO', 'CreatedDate': '2022-11-01T10:45:36.000+0000', 'CloseDate': '2023-04-28', 'ContractID__c': '800Wt00000DE97BIAT'}, {'Id': '006Wt000007B7OmIAK', 'OwnerId': '005Wt000003NBsIIAW', 'CreatedDate': '2020-03-10T09:22:30.000+0000', 'CloseDate': '2023-04-15', 'ContractID__c': 'None'}, {'Id': '006Wt000007B8RLIA0', 'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2022-11-15T10:32:45.000+0000', 'CloseDate': '2023-04-10', 'ContractID__c': '800Wt00000DE9aDIAT'}, {'Id': '006Wt000007BAfyIAG', 'OwnerId': '005Wt000003NJjNIAW', 'CreatedDate': '2022-11-02T11:23:48.000+0000', 'CloseDate': '2023-04-15', 'ContractID__c': 'None'}, {'Id': '006Wt000007BAjHIAW', 'OwnerId': '#005Wt000003NIfGIAW', 'CreatedDate': '2022-01-15T09:45:30.000+0000', 'CloseDate': '2023-04-11', 'ContractID__c': 'None'}, {'Id': '006Wt000007BBAcIAO', 'OwnerId': '#005Wt000003NBp4IAG', 'CreatedDate': '2022-09-01T10:15:00.000+0000', 'CloseDate': '2023-04-15', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BBH6IAO', 'OwnerId': '005Wt000003NJg9IAG', 'CreatedDate': '2022-09-14T14:32:54.000+0000', 'CloseDate': '2023-04-17', 'ContractID__c': 'None'}, {'Id': '006Wt000007BDU9IAO', 'OwnerId': '005Wt000003NJjNIAW', 'CreatedDate': '2023-02-20T14:45:30.000+0000', 'CloseDate': '2023-04-30', 'ContractID__c': '800Wt00000DE0ryIAD'}, {'Id': '006Wt000007BDUAIA4', 'OwnerId': '#005Wt000003NJmbIAG', 'CreatedDate': '2022-11-09T10:30:25.000+0000', 'CloseDate': '2023-04-20', 'ContractID__c': 'None'}, {'Id': '006Wt000007BHJGIA4', 'OwnerId': '005Wt000003NIiTIAW', 'CreatedDate': '2022-09-15T08:12:45.000+0000', 'CloseDate': '2023-04-01', 'ContractID__c': 'None'}, {'Id': '006Wt000007BHvzIAG', 'OwnerId': '005Wt000003NIljIAG', 'CreatedDate': '2022-07-15T10:30:45.000+0000', 'CloseDate': '2023-04-12', 'ContractID__c': 'None'}], 'var_functions.query_db:5': [{'Id': '800Wt00000DE97BIAT', 'CompanySignedDate': '2023-05-16'}, {'Id': '800Wt00000DE9aDIAT', 'CompanySignedDate': '2023-02-28'}]}

exec(code, env_args)
