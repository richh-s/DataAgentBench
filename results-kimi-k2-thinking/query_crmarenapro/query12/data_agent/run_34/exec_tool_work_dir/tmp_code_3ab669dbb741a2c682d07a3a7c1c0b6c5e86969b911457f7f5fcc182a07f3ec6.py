code = """import pandas as pd
import json
from datetime import datetime
import numpy as np

# Load the data
contracts_file = locals()['var_functions.query_db:10']
april_opps_file = locals()['var_functions.query_db:14']

with open(contracts_file, 'r') as f:
    contracts = json.load(f)

with open(april_opps_file, 'r') as f:
    april_opportunities = json.load(f)

# Convert to DataFrames
df_contracts = pd.DataFrame(contracts)
df_april_opps = pd.DataFrame(april_opportunities)

# Clean ID fields
def clean_id(id_value):
    if pd.isna(id_value) or id_value is None or str(id_value).strip().lower() == "none":
        return None
    if isinstance(id_value, str):
        return id_value.replace('#', '').strip()
    return str(id_value)

# Apply cleaning
df_contracts['Id_clean'] = df_contracts['Id'].apply(clean_id)
df_contracts['AccountId_clean'] = df_contracts['AccountId'].apply(clean_id)
df_april_opps['Id_clean'] = df_april_opps['Id'].apply(clean_id)
df_april_opps['ContractID__c_clean'] = df_april_opps['ContractID__c'].apply(clean_id)
df_april_opps['AccountId_clean'] = df_april_opps['AccountId'].apply(clean_id)
df_april_opps['OwnerId_clean'] = df_april_opps['OwnerId'].apply(clean_id)

# Convert dates
df_contracts['CompanySignedDate'] = pd.to_datetime(df_contracts['CompanySignedDate'], errors='coerce')
df_april_opps['CreatedDate'] = pd.to_datetime(df_april_opps['CreatedDate'], errors='coerce')

# Create a contracts lookup by ID and by AccountId
contracts_by_id = df_contracts.set_index('Id_clean')['CompanySignedDate'].to_dict()

# For each April opportunity, try to find its contract and calculate turnaround
turnaround_data = []

for idx, opp in df_april_opps.iterrows():
    contract_signed_date = None
    
    # Method 1: Try direct contract ID match
    if pd.notna(opp['ContractID__c_clean']):
        contract_signed_date = contracts_by_id.get(opp['ContractID__c_clean'])
    
    turnaround_days = None
    if pd.notna(opp['CreatedDate']) and pd.notna(contract_signed_date):
        turnaround_days = (contract_signed_date - opp['CreatedDate']).days
        
        # Only include if turnaround is positive (contract signed after creation)
        if turnaround_days >= 0:
            turnaround_data.append({
                'OpportunityId': opp['Id_clean'],
                'OwnerId': opp['OwnerId_clean'],
                'CreatedDate': opp['CreatedDate'],
                'ContractSignedDate': contract_signed_date,
                'TurnaroundDays': turnaround_days
            })

# Convert to DataFrame
df_turnaround = pd.DataFrame(turnaround_data)

print("__RESULT__:")
result_dict = {
    "total_april_opps": int(len(df_april_opps)),
    "opps_with_contract_match": int(len(df_turnaround)),
    "sample_turnaround": df_turnaround.head(3).to_dict('records') if len(df_turnaround) > 0 else []
}

# Convert datetime objects to strings for JSON serialization
for i, record in enumerate(result_dict["sample_turnaround"]):
    if 'CreatedDate' in record and pd.notna(record['CreatedDate']):
        result_dict["sample_turnaround"][i]['CreatedDate'] = record['CreatedDate'].isoformat()
    if 'ContractSignedDate' in record and pd.notna(record['ContractSignedDate']):
        result_dict["sample_turnaround"][i]['ContractSignedDate'] = record['ContractSignedDate'].isoformat()

# Calculate average turnaround by owner if we have data
if len(df_turnaround) > 0:
    avg_turnaround = df_turnaround.groupby('OwnerId')['TurnaroundDays'].agg(['mean', 'count']).reset_index()
    avg_turnaround = avg_turnaround[avg_turnaround['count'] >= 1]  # At least 1 opportunity
    avg_turnaround = avg_turnaround.sort_values('mean')
    
    result_dict["avg_turnaround_by_owner"] = avg_turnaround.head(5).to_dict('records')
    if len(avg_turnaround) > 0:
        result_dict["quickest_agent"] = avg_turnaround.iloc[0]['OwnerId']
        result_dict["quickest_agent_avg_days"] = float(avg_turnaround.iloc[0]['mean'])
else:
    result_dict["avg_turnaround_by_owner"] = []
    result_dict["quickest_agent"] = None

print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGeJIIA1', 'ContactId': '003Wt00000JqvQiIAJ', 'OwnerId': '005Wt000003NIqXIAW', 'Probability': '75.0', 'Amount': '182448.4965', 'StageName': 'Qualification', 'Name': 'InnoSphere Labs - EDA Innovation Expansion', 'Description': 'InnoSphere Labs is exploring advanced EDA solutions to enhance their R&D capabilities. They are particularly interested in the AI Cirku-Tech for rapid circuit prototyping, and the EcoPCB Creator for environmentally-friendly design processes. Additionally, CloudLink Designer could improve their team collaboration across global projects.', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'CloseDate': '2024-02-15'}, {'Id': '006Wt000007Aw3WIAS', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGzsMIAT', 'ContactId': '#003Wt00000JqyQEIAZ', 'OwnerId': '005Wt000003NIc1IAG', 'Probability': '75.0', 'Amount': '22238.547', 'StageName': 'Quote', 'Name': 'TechPulse-PrimeEdge Strategic Collaboration ', 'Description': "TechPulse Solutions is poised to empower PrimeEdge Technology with its suite of cutting-edge EDA tools, including AI Cirku-Tech and SecureAnalytics Pro. By integrating solutions like DesignWave Automation and CloudLink Designer, TechPulse aims to enhance workflow automation and secure data optimization within PrimeEdge's operations. This opportunity also leverages OptiPower Manager to pursue sustainable electronics development, ensuring PrimeEdge stays at the forefront of IT innovation.", 'CreatedDate': '2024-04-05T12:15:30.000+0000', 'CloseDate': '2024-06-15'}, {'Id': '006Wt000007Aw3XIAS', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGYx5IAH', 'ContactId': '003Wt00000JquRPIAZ', 'OwnerId': '#005Wt000003NJZhIAO', 'Probability': '75.0', 'Amount': '10019.8045', 'StageName': 'Quote', 'Name': 'Quantum Designs Partnership Initiative', 'Description': 'TechPulse Solutions presents Quantum Designs with an integrated EDA suite, combining the robust capabilities of PulseSim Pro and AI Cirku-Tech for advanced semiconductor solutions. Emphasizing security, SecureFlow Suite ensures compliance and safeguarding critical data. The partnership focuses on streamlining PCB development with EcoPCB Creator, enhancing both innovation and sustainability.', 'CreatedDate': '2021-02-10T14:23:45.000+0000', 'CloseDate': '2021-05-30'}, {'Id': '006Wt000007Aya9IAC', 'ContractID__c': 'None', 'AccountId': '001Wt00000PHViXIAX', 'ContactId': '003Wt00000Jqvk1IAB', 'OwnerId': '005Wt000003NDJ0IAO', 'Probability': '75.0', 'Amount': '19002.1475', 'StageName': 'Discovery', 'Name': 'Nova Healthcare Tech Strategic Enhancement', 'Description': "Leveraging TechPulse Solutions' AI Cirku-Tech for rapid prototype advancements and SecureFlow Suite for enhanced security compliance, Nova Healthcare Tech can revolutionize their service offerings. By integrating CollabCircuit Hub, interdepartmental communication will improve significantly, facilitating more efficient project management. The adoption of QuantumPCB Modeler could provide Nova Healthcare Tech with cutting-edge tech solutions, further enhancing patient care and service quality.", 'CreatedDate': '2023-08-11T09:30:00.000+0000', 'CloseDate': '2023-11-30'}, {'Id': '006Wt000007AyaAIAS', 'ContractID__c': 'None', 'AccountId': '001Wt00000PHVk9IAH', 'ContactId': '003Wt00000Jqv0wIAB', 'OwnerId': '005Wt000003NJxtIAG', 'Probability': '85.0', 'Amount': '22249.0175', 'StageName': 'Negotiation   ', 'Name': 'LiftTech Smart Integration Project', 'Description': "LiftTech Elevations aims to enhance its building automation systems using AI-driven EDA tools like CircuitAI Innovator and EcoPCB Creator. By integrating advanced security features with SecureAnalytics Pro, they can bolster data protection and compliance. The collaboration with TechPulse Solutions promises to streamline LiftTech's workflows with DesignWave Automation, ensuring seamless system operations.", 'CreatedDate': '2022-07-20T14:13:45.000+0000', 'CloseDate': '2023-11-15'}], 'var_functions.query_db:5': [{'Id': '#800Wt00000DD0SZIA1', 'AccountId': '001Wt00000PGZmfIAH', 'Status': 'Activated  ', 'StartDate': '2021-07-20', 'CustomerSignedDate': '2021-07-15', 'CompanySignedDate': '2021-07-16', 'Description': 'This contract solidifies the expanded partnership with Quantum Dynamics LLC for the provision of advanced AI-powered EDA tools, focusing on enhancing their quantum computing technology developments.', 'ContractTerm': '24'}, {'Id': '800Wt00000DD0SaIAL', 'AccountId': '001Wt00000PGXrLIAX', 'Status': 'Activated', 'StartDate': '2021-10-01', 'CustomerSignedDate': '2021-09-28', 'CompanySignedDate': '2021-09-28', 'Description': 'This contract outlines the collaboration between TechPulse Solutions and DataGuard Insights for EDA integration and security enhancements, providing comprehensive support and streamlining operational efficiencies within the DataGuard systems.', 'ContractTerm': '12'}, {'Id': '#800Wt00000DD0SbIAL', 'AccountId': '001Wt00000PGXrLIAX', 'Status': 'Activated   ', 'StartDate': '2023-07-15', 'CustomerSignedDate': '2023-07-11', 'CompanySignedDate': '2023-07-12', 'Description': 'Contract detailing the secure integration and optimization services to be implemented for DataGuard Insights, focusing on integrating CryptSecure Core and SecureFlow Suite into existing systems for enhanced data management and security. This includes AI-powered solution deployment, comprehensive training, and support.', 'ContractTerm': '12'}, {'Id': '800Wt00000DDDuRIAX', 'AccountId': '001Wt00000PGYgxIAH', 'Status': 'Activated ', 'StartDate': '2024-05-01', 'CustomerSignedDate': '2024-04-15', 'CompanySignedDate': '2024-04-16', 'Description': 'This contract establishes a collaboration between TechPulse Solutions and EcoShield Technologies to enhance environmental tech solutions using AI-powered electronic design automation (EDA) tools, focusing on sustainability and energy efficiency.', 'ContractTerm': '12'}, {'Id': '800Wt00000DDNFUIA5', 'AccountId': '#001Wt00000PGeJIIA1', 'Status': 'Activated', 'StartDate': '2023-08-01', 'CustomerSignedDate': '2023-07-01', 'CompanySignedDate': '2023-07-02', 'Description': "The contract facilitates the Innovative R&D Transformation project for InnoSphere Labs utilizing TechPulse Solutions' EDA tools, ensuring seamless integration and optimization of their research operations.", 'ContractTerm': '12'}], 'var_functions.query_db:6': [{'StageName': 'Closed'}, {'StageName': 'Closed '}, {'StageName': 'Closed  '}, {'StageName': 'Closed   '}, {'StageName': 'Discovery'}, {'StageName': 'Discovery '}, {'StageName': 'Discovery  '}, {'StageName': 'Discovery   '}, {'StageName': 'Negotiation'}, {'StageName': 'Negotiation '}, {'StageName': 'Negotiation  '}, {'StageName': 'Negotiation   '}, {'StageName': 'Qualification'}, {'StageName': 'Qualification '}, {'StageName': 'Qualification  '}, {'StageName': 'Qualification   '}, {'StageName': 'Quote'}, {'StageName': 'Quote '}, {'StageName': 'Quote  '}, {'StageName': 'Quote   '}], 'var_functions.execute_python:9': {'opportunity_count': 5, 'contract_count': 5, 'sample_opportunity': {'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGeJIIA1', 'ContactId': '003Wt00000JqvQiIAJ', 'OwnerId': '005Wt000003NIqXIAW', 'Probability': '75.0', 'Amount': '182448.4965', 'StageName': 'Qualification', 'Name': 'InnoSphere Labs - EDA Innovation Expansion', 'Description': 'InnoSphere Labs is exploring advanced EDA solutions to enhance their R&D capabilities. They are particularly interested in the AI Cirku-Tech for rapid circuit prototyping, and the EcoPCB Creator for environmentally-friendly design processes. Additionally, CloudLink Designer could improve their team collaboration across global projects.', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'CloseDate': '2024-02-15'}, 'sample_contract': {'Id': '#800Wt00000DD0SZIA1', 'AccountId': '001Wt00000PGZmfIAH', 'Status': 'Activated  ', 'StartDate': '2021-07-20', 'CustomerSignedDate': '2021-07-15', 'CompanySignedDate': '2021-07-16', 'Description': 'This contract solidifies the expanded partnership with Quantum Dynamics LLC for the provision of advanced AI-powered EDA tools, focusing on enhancing their quantum computing technology developments.', 'ContractTerm': '24'}}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'april_opps_count': 30, 'contracts_count': 163, 'sample_april_opp': {'Id': '#006Wt000007B1klIAC', 'ContractID__c': 'None', 'AccountId': '001Wt00000PH90cIAD', 'ContactId': '003Wt00000Jqe4vIAB', 'OwnerId': '#005Wt000003NBylIAG', 'Probability': '75.0', 'Amount': '14163.726', 'StageName': 'Negotiation', 'Name': 'InspireTech Collaboration Expansion', 'Description': "InspireTech Consulting is seeking cutting-edge EDA tools to optimize their consulting offerings. TechPulse Solution's AI Cirku-Tech and SecureFlow Suite provide ideal solutions for rapid prototyping and superior security. The integration of CloudLink Designer will further enhance InspireTech's global project capabilities.", 'CreatedDate': '2023-04-15T09:00:34.000+0000', 'CloseDate': '2023-12-20'}, 'sample_contract': {'Id': '#800Wt00000DD0SZIA1', 'AccountId': '001Wt00000PGZmfIAH', 'Status': 'Activated  ', 'StartDate': '2021-07-20', 'CustomerSignedDate': '2021-07-15', 'CompanySignedDate': '2021-07-16', 'Description': 'This contract solidifies the expanded partnership with Quantum Dynamics LLC for the provision of advanced AI-powered EDA tools, focusing on enhancing their quantum computing technology developments.', 'ContractTerm': '24'}}, 'var_functions.execute_python:20': {'april_opps_shape': [30, 12], 'contracts_shape': [163, 8], 'unique_contract_ids_in_april_opps': 4, 'contract_id_sample': ['None', '800Wt00000DE9FFIA1', '800Wt00000DE8sgIAD', '800Wt00000DE9ryIAD']}, 'var_functions.query_db:24': [{'StageName': 'Closed'}, {'StageName': 'Closed  '}], 'var_functions.execute_python:26': {'total_closed_april': 5, 'sample_closed': [{'Id_clean': '006Wt000007B8CqIAK', 'CreatedDate': '2023-04-15T09:30:45+00:00', 'ContractID__c_clean': None, 'StageName': 'Closed'}, {'Id_clean': '006Wt000007B8FyIAK', 'CreatedDate': '2023-04-15T10:30:15+00:00', 'ContractID__c_clean': None, 'StageName': 'Closed'}, {'Id_clean': '006Wt000007BChmIAG', 'CreatedDate': '2023-04-25T10:45:30+00:00', 'ContractID__c_clean': '800Wt00000DE9FFIA1', 'StageName': 'Closed'}]}}

exec(code, env_args)
