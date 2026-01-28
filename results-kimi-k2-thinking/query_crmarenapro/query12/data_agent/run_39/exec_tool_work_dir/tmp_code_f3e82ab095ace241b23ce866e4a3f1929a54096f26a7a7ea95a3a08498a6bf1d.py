code = """import json
import pandas as pd
from datetime import datetime

# Read the data from the previous query
data = locals()['var_functions.query_db:28']

if not data:
    print("__RESULT__:")
    print(json.dumps("No data found for April 2023 contracts"))
else:
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Parse dates and calculate turnaround
    df['created_dt'] = pd.to_datetime(df['CreatedDate'])
    df['signed_dt'] = pd.to_datetime(df['CompanySignedDate'])
    df['turnaround_days'] = (df['signed_dt'] - df['created_dt']).dt.days
    
    # Calculate average turnaround by agent
    agent_stats = df.groupby('OwnerId').agg({
        'turnaround_days': ['mean', 'count']
    }).round(2)
    
    agent_stats.columns = ['avg_turnaround', 'opportunity_count']
    agent_stats = agent_stats.reset_index()
    
    # Sort by average turnaround (quickest first)
    agent_stats = agent_stats.sort_values('avg_turnaround')
    
    # Get the agent with quickest average turnaround
    quickest_agent = agent_stats.iloc[0]
    
    result = {
        'agent_id': quickest_agent['OwnerId'],
        'avg_turnaround_days': float(quickest_agent['avg_turnaround']),
        'opportunity_count': int(quickest_agent['opportunity_count'])
    }
    
    print("__RESULT__:")
    print(json.dumps(result['agent_id']))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGeJIIA1', 'ContactId': '003Wt00000JqvQiIAJ', 'OwnerId': '005Wt000003NIqXIAW', 'Probability': '75.0', 'Amount': '182448.4965', 'StageName': 'Qualification', 'Name': 'InnoSphere Labs - EDA Innovation Expansion', 'Description': 'InnoSphere Labs is exploring advanced EDA solutions to enhance their R&D capabilities. They are particularly interested in the AI Cirku-Tech for rapid circuit prototyping, and the EcoPCB Creator for environmentally-friendly design processes. Additionally, CloudLink Designer could improve their team collaboration across global projects.', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'CloseDate': '2024-02-15'}], 'var_functions.query_db:5': [{'Id': '#800Wt00000DD0SZIA1', 'AccountId': '001Wt00000PGZmfIAH', 'Status': 'Activated  ', 'StartDate': '2021-07-20', 'CustomerSignedDate': '2021-07-15', 'CompanySignedDate': '2021-07-16', 'Description': 'This contract solidifies the expanded partnership with Quantum Dynamics LLC for the provision of advanced AI-powered EDA tools, focusing on enhancing their quantum computing technology developments.', 'ContractTerm': '24'}], 'var_functions.query_db:7': [{'Id': '800Wt00000DE9FGIA1', 'CompanySignedDate': '2023-04-15', 'OpportunityId': '006Wt000007BI41IAG', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'OwnerId': '005Wt000003NDEBIA4'}], 'var_functions.query_db:8': [{'OpportunityId': '006Wt000007BI41IAG', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15', 'OwnerId': '005Wt000003NDEBIA4'}], 'var_functions.query_db:10': [{'OwnerId': '005Wt000003NDEBIA4', 'OpportunityId': '006Wt000007BI41IAG', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15'}], 'var_functions.query_db:12': [{'count': '1'}], 'var_functions.query_db:14': [{'Id': '006Wt000007BI41IAG', 'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'ContractId': '800Wt00000DE9FGIA1', 'CompanySignedDate': '2023-04-15'}], 'var_functions.query_db:16': [{'Id': '800Wt00000DE9FGIA1', 'CompanySignedDate': '2023-04-15'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:26': [{'Id': '800Wt00000DE9FGIA1', 'CompanySignedDate': '2023-04-15'}], 'var_functions.query_db:28': [{'Id': '006Wt000007BI41IAG', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'OwnerId': '005Wt000003NDEBIA4', 'ContractId': '800Wt00000DE9FGIA1', 'CompanySignedDate': '2023-04-15'}], 'var_functions.query_db:30': [{'Id': '800Wt00000DE9FGIA1', 'CompanySignedDate': '2023-04-15'}]}

exec(code, env_args)
