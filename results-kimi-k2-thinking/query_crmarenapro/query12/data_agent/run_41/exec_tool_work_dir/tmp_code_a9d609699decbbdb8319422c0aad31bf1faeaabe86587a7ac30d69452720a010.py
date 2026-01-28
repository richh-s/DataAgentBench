code = """# Access variables through locals() since they have special characters in names
opportunities = locals()['var_functions.query_db:2']
contracts = locals()['var_functions.query_db:4']

print('Number of opportunities:', len(opportunities))
print('Number of contracts:', len(contracts))

if opportunities:
    print('\nSample opportunities:')
    for i, opp in enumerate(opportunities[:3]):
        print(' ', i, ':', opp)
    
    print('\nOpportunity fields:', list(opportunities[0].keys()))

if contracts:
    print('\nSample contracts:')
    for i, contract in enumerate(contracts[:3]):
        print(' ', i, ':', contract)
    
    print('\nContract fields:', list(contracts[0].keys()))

print('\nSuccess - variables accessed correctly')"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'Id': '006Wt000007AvVeIAK', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIqXIAW'}, {'Id': '006Wt000007Aw3WIAS', 'CreatedDate': '2024-04-05T12:15:30.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIc1IAG'}, {'Id': '006Wt000007Aw3XIAS', 'CreatedDate': '2021-02-10T14:23:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NJZhIAO'}, {'Id': '006Wt000007Aya9IAC', 'CreatedDate': '2023-08-11T09:30:00.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NDJ0IAO'}, {'Id': '006Wt000007AyaAIAS', 'CreatedDate': '2022-07-20T14:13:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJxtIAG'}, {'Id': '006Wt000007AyaBIAS', 'CreatedDate': '2023-08-14T10:30:00.000+0000', 'ContractID__c': '800Wt00000DE9DdIAL', 'OwnerId': '005Wt000003NErnIAG'}, {'Id': '#006Wt000007AyaCIAS', 'CreatedDate': '2020-12-18T14:35:47.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NEdJIAW'}, {'Id': '#006Wt000007AyaDIAS', 'CreatedDate': '2021-05-13T10:30:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIybIAG'}, {'Id': '006Wt000007Ayi2IAC', 'CreatedDate': '2021-03-02T10:45:30.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIdeIAG'}, {'Id': '006Wt000007AywiIAC', 'CreatedDate': '2021-11-05T10:15:30.000+0000', 'ContractID__c': '800Wt00000DE45uIAD', 'OwnerId': '005Wt000003NBsIIAW'}], 'var_functions.query_db:4': [{'Id': '#800Wt00000DD0SZIA1', 'CompanySignedDate': '2021-07-16'}, {'Id': '800Wt00000DD0SaIAL', 'CompanySignedDate': '2021-09-28'}, {'Id': '#800Wt00000DD0SbIAL', 'CompanySignedDate': '2023-07-12'}, {'Id': '800Wt00000DDDuRIAX', 'CompanySignedDate': '2024-04-16'}, {'Id': '800Wt00000DDNFUIA5', 'CompanySignedDate': '2023-07-02'}, {'Id': '800Wt00000DDNFVIA5', 'CompanySignedDate': '2021-06-26'}, {'Id': '800Wt00000DDNlnIAH', 'CompanySignedDate': '2022-09-02'}, {'Id': '800Wt00000DDPXRIA5', 'CompanySignedDate': '2022-04-22'}, {'Id': '800Wt00000DDPXSIA5', 'CompanySignedDate': '2023-02-25'}, {'Id': '800Wt00000DDPXTIA5', 'CompanySignedDate': '2023-10-13'}]}

exec(code, env_args)
