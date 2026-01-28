code = """# Load and analyze the data
import json
import datetime

# Get the opportunities from April 2023
opportunities = locals()['var_functions.query_db:22']

# Get the contracts (stored as a file path)
contracts_file = locals()['var_functions.query_db:24']
with open(contracts_file, 'r') as f:
    contracts = json.load(f)

print('Loaded', len(opportunities), 'opportunities from April 2023')
print('Loaded', len(contracts), 'contracts')

# Count opportunities with valid contract IDs
opps_with_contracts = []
for opp in opportunities:
    if opp.get('ContractID__c') and opp.get('ContractID__c') != 'None':
        opps_with_contracts.append(opp)

print('Opportunities with contracts:', len(opps_with_contracts))

# Create contract lookup with normalized IDs
def normalize_id(id_str):
    if not id_str:
        return None
    return id_str.strip()

contract_dict = {}
for c in contracts:
    key = normalize_id(c['Id'])
    if key:
        contract_dict[key] = c

print('Contract dictionary created with', len(contract_dict), 'entries')

# Find matches and calculate turnaround times
matches = []
for opp in opps_with_contracts:
    opp_contract_id = normalize_id(opp['ContractID__c'])
    if opp_contract_id and opp_contract_id in contract_dict:
        contract = contract_dict[opp_contract_id]
        
        # Parse dates
        try:
            created_date = datetime.datetime.fromisoformat(opp['CreatedDate'].replace('Z', '+00:00'))
            signed_date = datetime.datetime.strptime(contract['CompanySignedDate'], '%Y-%m-%d').replace(tzinfo=datetime.timezone.utc)
            
            turnaround_days = (signed_date - created_date).days
            
            matches.append({
                'opp_id': opp['Id'],
                'owner_id': normalize_id(opp['OwnerId']),
                'created_date': opp['CreatedDate'],
                'contract_id': opp_contract_id,
                'signed_date': contract['CompanySignedDate'],
                'turnaround_days': turnaround_days
            })
        except Exception as e:
            print('Error processing:', e)

print('Found', len(matches), 'matching opportunity-contract pairs with valid dates')

if not matches:
    print('ERROR: No matches found')
    output = {'error': 'no_matches'}
else:
    # Group by owner and calculate average turnaround
    from collections import defaultdict
    
    owner_stats = defaultdict(lambda: {'total_days': 0, 'count': 0})
    
    for match in matches:
        owner_id = match['owner_id']
        owner_stats[owner_id]['total_days'] += match['turnaround_days']
        owner_stats[owner_id]['count'] += 1
    
    # Calculate averages
    owner_averages = []
    for owner_id, stats in owner_stats.items():
        avg = stats['total_days'] / stats['count']
        owner_averages.append({
            'owner_id': owner_id,
            'avg_turnaround': avg,
            'count': stats['count']
        })
    
    # Sort by average turnaround
    owner_averages.sort(key=lambda x: x['avg_turnaround'])
    
    print('Top agents by average turnaround:')
    for i, agent in enumerate(owner_averages[:5]):
        print(f"  {i+1}. {agent['owner_id']}: {agent['avg_turnaround']:.2f} days ({agent['count']} deals)")
    
    if owner_averages:
        output = {'quickest_agent_id': owner_averages[0]['owner_id']}
    else:
        output = {'error': 'no_averages'}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'Id': '006Wt000007AvVeIAK', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIqXIAW'}, {'Id': '006Wt000007Aw3WIAS', 'CreatedDate': '2024-04-05T12:15:30.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIc1IAG'}, {'Id': '006Wt000007Aw3XIAS', 'CreatedDate': '2021-02-10T14:23:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NJZhIAO'}, {'Id': '006Wt000007Aya9IAC', 'CreatedDate': '2023-08-11T09:30:00.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NDJ0IAO'}, {'Id': '006Wt000007AyaAIAS', 'CreatedDate': '2022-07-20T14:13:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJxtIAG'}, {'Id': '006Wt000007AyaBIAS', 'CreatedDate': '2023-08-14T10:30:00.000+0000', 'ContractID__c': '800Wt00000DE9DdIAL', 'OwnerId': '005Wt000003NErnIAG'}, {'Id': '#006Wt000007AyaCIAS', 'CreatedDate': '2020-12-18T14:35:47.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NEdJIAW'}, {'Id': '#006Wt000007AyaDIAS', 'CreatedDate': '2021-05-13T10:30:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIybIAG'}, {'Id': '006Wt000007Ayi2IAC', 'CreatedDate': '2021-03-02T10:45:30.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIdeIAG'}, {'Id': '006Wt000007AywiIAC', 'CreatedDate': '2021-11-05T10:15:30.000+0000', 'ContractID__c': '800Wt00000DE45uIAD', 'OwnerId': '005Wt000003NBsIIAW'}], 'var_functions.query_db:4': [{'Id': '#800Wt00000DD0SZIA1', 'CompanySignedDate': '2021-07-16'}, {'Id': '800Wt00000DD0SaIAL', 'CompanySignedDate': '2021-09-28'}, {'Id': '#800Wt00000DD0SbIAL', 'CompanySignedDate': '2023-07-12'}, {'Id': '800Wt00000DDDuRIAX', 'CompanySignedDate': '2024-04-16'}, {'Id': '800Wt00000DDNFUIA5', 'CompanySignedDate': '2023-07-02'}, {'Id': '800Wt00000DDNFVIA5', 'CompanySignedDate': '2021-06-26'}, {'Id': '800Wt00000DDNlnIAH', 'CompanySignedDate': '2022-09-02'}, {'Id': '800Wt00000DDPXRIA5', 'CompanySignedDate': '2022-04-22'}, {'Id': '800Wt00000DDPXSIA5', 'CompanySignedDate': '2023-02-25'}, {'Id': '800Wt00000DDPXTIA5', 'CompanySignedDate': '2023-10-13'}], 'var_functions.query_db:22': [{'Id': '#006Wt000007B1klIAC', 'CreatedDate': '2023-04-15T09:00:34.000+0000', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NBylIAG'}, {'Id': '006Wt000007B49NIAS', 'CreatedDate': '2023-04-25T14:32:51.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIs9IAG'}, {'Id': '006Wt000007B62sIAC', 'CreatedDate': '2023-04-04T10:15:30.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJZhIAO'}, {'Id': '006Wt000007B6itIAC', 'CreatedDate': '2023-04-25T09:45:30.000+0000', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NJMnIAO'}, {'Id': '#006Wt000007B7tQIAS', 'CreatedDate': '2023-04-15T10:20:30.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIfGIAW'}, {'Id': '#006Wt000007B7yJIAS', 'CreatedDate': '2023-04-15T10:30:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NEdJIAW'}, {'Id': '006Wt000007B8CqIAK', 'CreatedDate': '2023-04-15T09:30:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NInKIAW'}, {'Id': '#006Wt000007B8FyIAK', 'CreatedDate': '2023-04-15T10:30:15.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIovIAG'}, {'Id': '#006Wt000007BA3JIAW', 'CreatedDate': '2023-04-02T10:15:30.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NF9WIAW'}, {'Id': '006Wt000007BABLIA4', 'CreatedDate': '2023-04-01T14:47:23.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NDEBIA4'}, {'Id': '006Wt000007BAHlIAO', 'CreatedDate': '2023-04-19T15:30:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NFhPIAW'}, {'Id': '006Wt000007BAPrIAO', 'CreatedDate': '2023-04-15T10:15:32.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJxtIAG'}, {'Id': '006Wt000007BBDrIAO', 'CreatedDate': '2023-04-10T10:30:15.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJ1pIAG'}, {'Id': '006Wt000007BBc1IAG', 'CreatedDate': '2023-04-15T10:14:32.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NEtPIAW'}, {'Id': '006Wt000007BCLEIA4', 'CreatedDate': '2023-04-27T11:22:30.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJBVIA4'}, {'Id': '006Wt000007BCTFIA4', 'CreatedDate': '2023-04-20T11:15:33.000+0000', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NBcBIAW'}, {'Id': '#006Wt000007BChmIAG', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'ContractID__c': '800Wt00000DE9FFIA1', 'OwnerId': '005Wt000003NJgAIAW'}, {'Id': '006Wt000007BDApIAO', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'ContractID__c': '800Wt00000DE8sgIAD', 'OwnerId': '005Wt000003NISMIA4'}, {'Id': '#006Wt000007BDXPIA4', 'CreatedDate': '2023-04-15T10:45:00.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJ0EIAW'}, {'Id': '006Wt000007BDcEIAW', 'CreatedDate': '2023-04-15T10:32:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIAbIAO'}, {'Id': '006Wt000007BDpAIAW', 'CreatedDate': '2023-04-15T10:30:15.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NEtPIAW'}, {'Id': '006Wt000007BETVIA4', 'CreatedDate': '2023-04-20T11:34:22.000+0000', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NJjNIAW'}, {'Id': '#006Wt000007BEV4IAO', 'CreatedDate': '2023-04-05T14:23:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NFRKIA4'}, {'Id': '006Wt000007BFUOIA4', 'CreatedDate': '2023-04-05T10:15:30.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NHpdIAG'}, {'Id': '006Wt000007BGAIIA4', 'CreatedDate': '2023-04-11T12:45:33.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIdeIAG'}, {'Id': '#006Wt000007BGDVIA4', 'CreatedDate': '2023-04-10T11:20:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NBcBIAW'}, {'Id': '006Wt000007BHPhIAO', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'ContractID__c': '800Wt00000DE9ryIAD', 'OwnerId': '#005Wt000003NEa3IAG'}, {'Id': '#006Wt000007BHZNIA4', 'CreatedDate': '2023-04-10T14:25:30.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIaPIAW'}, {'Id': '#006Wt000007BHfpIAG', 'CreatedDate': '2023-04-17T14:37:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIqXIAW'}, {'Id': '006Wt000007BHr7IAG', 'CreatedDate': '2023-04-01T09:45:23.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIfGIAW'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
