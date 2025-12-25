code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-6504895578308259406'], 'r') as f:
    opps = pd.DataFrame(json.load(f))
with open(locals()['var_function-call-6504895578308258827'], 'r') as f:
    contracts = pd.DataFrame(json.load(f))

# Normalize IDs
def normalize_id(x):
    if pd.isna(x):
        return None
    return str(x).strip().lstrip('#')

opps['ContractID__c'] = opps['ContractID__c'].apply(normalize_id)
opps['OwnerId'] = opps['OwnerId'].apply(normalize_id)
contracts['Id'] = contracts['Id'].apply(normalize_id)

# Merge
df = pd.merge(opps, contracts, left_on='ContractID__c', right_on='Id', how='inner', suffixes=('_opp', '_con'))

# Convert dates
df['CreatedDate'] = pd.to_datetime(df['CreatedDate']).dt.tz_localize(None)
df['CompanySignedDate'] = pd.to_datetime(df['CompanySignedDate'])

# Calculate duration in days
df['Duration'] = (df['CompanySignedDate'] - df['CreatedDate']).dt.total_seconds() / (24 * 3600)

# Filter for April 2023 based on CompanySignedDate
april_2023_signed = df[
    (df['CompanySignedDate'] >= '2023-04-01') & 
    (df['CompanySignedDate'] <= '2023-04-30')
]

if april_2023_signed.empty:
    result = "No records found"
else:
    # Group by OwnerId and calculate average duration
    avg_turnaround = april_2023_signed.groupby('OwnerId')['Duration'].mean().reset_index()
    avg_turnaround = avg_turnaround.sort_values(by='Duration')
    result = avg_turnaround.iloc[0]['OwnerId']

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-10280457411289995763': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_function-call-18199363812371569520': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGeJIIA1', 'ContactId': '003Wt00000JqvQiIAJ', 'OwnerId': '005Wt000003NIqXIAW', 'Probability': '75.0', 'Amount': '182448.4965', 'StageName': 'Qualification', 'Name': 'InnoSphere Labs - EDA Innovation Expansion', 'Description': 'InnoSphere Labs is exploring advanced EDA solutions to enhance their R&D capabilities. They are particularly interested in the AI Cirku-Tech for rapid circuit prototyping, and the EcoPCB Creator for environmentally-friendly design processes. Additionally, CloudLink Designer could improve their team collaboration across global projects.', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'CloseDate': '2024-02-15'}, {'Id': '006Wt000007Aw3WIAS', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGzsMIAT', 'ContactId': '#003Wt00000JqyQEIAZ', 'OwnerId': '005Wt000003NIc1IAG', 'Probability': '75.0', 'Amount': '22238.547', 'StageName': 'Quote', 'Name': 'TechPulse-PrimeEdge Strategic Collaboration ', 'Description': "TechPulse Solutions is poised to empower PrimeEdge Technology with its suite of cutting-edge EDA tools, including AI Cirku-Tech and SecureAnalytics Pro. By integrating solutions like DesignWave Automation and CloudLink Designer, TechPulse aims to enhance workflow automation and secure data optimization within PrimeEdge's operations. This opportunity also leverages OptiPower Manager to pursue sustainable electronics development, ensuring PrimeEdge stays at the forefront of IT innovation.", 'CreatedDate': '2024-04-05T12:15:30.000+0000', 'CloseDate': '2024-06-15'}, {'Id': '006Wt000007Aw3XIAS', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGYx5IAH', 'ContactId': '003Wt00000JquRPIAZ', 'OwnerId': '#005Wt000003NJZhIAO', 'Probability': '75.0', 'Amount': '10019.8045', 'StageName': 'Quote', 'Name': 'Quantum Designs Partnership Initiative', 'Description': 'TechPulse Solutions presents Quantum Designs with an integrated EDA suite, combining the robust capabilities of PulseSim Pro and AI Cirku-Tech for advanced semiconductor solutions. Emphasizing security, SecureFlow Suite ensures compliance and safeguarding critical data. The partnership focuses on streamlining PCB development with EcoPCB Creator, enhancing both innovation and sustainability.', 'CreatedDate': '2021-02-10T14:23:45.000+0000', 'CloseDate': '2021-05-30'}, {'Id': '006Wt000007Aya9IAC', 'ContractID__c': 'None', 'AccountId': '001Wt00000PHViXIAX', 'ContactId': '003Wt00000Jqvk1IAB', 'OwnerId': '005Wt000003NDJ0IAO', 'Probability': '75.0', 'Amount': '19002.1475', 'StageName': 'Discovery', 'Name': 'Nova Healthcare Tech Strategic Enhancement', 'Description': "Leveraging TechPulse Solutions' AI Cirku-Tech for rapid prototype advancements and SecureFlow Suite for enhanced security compliance, Nova Healthcare Tech can revolutionize their service offerings. By integrating CollabCircuit Hub, interdepartmental communication will improve significantly, facilitating more efficient project management. The adoption of QuantumPCB Modeler could provide Nova Healthcare Tech with cutting-edge tech solutions, further enhancing patient care and service quality.", 'CreatedDate': '2023-08-11T09:30:00.000+0000', 'CloseDate': '2023-11-30'}, {'Id': '006Wt000007AyaAIAS', 'ContractID__c': 'None', 'AccountId': '001Wt00000PHVk9IAH', 'ContactId': '003Wt00000Jqv0wIAB', 'OwnerId': '005Wt000003NJxtIAG', 'Probability': '85.0', 'Amount': '22249.0175', 'StageName': 'Negotiation   ', 'Name': 'LiftTech Smart Integration Project', 'Description': "LiftTech Elevations aims to enhance its building automation systems using AI-driven EDA tools like CircuitAI Innovator and EcoPCB Creator. By integrating advanced security features with SecureAnalytics Pro, they can bolster data protection and compliance. The collaboration with TechPulse Solutions promises to streamline LiftTech's workflows with DesignWave Automation, ensuring seamless system operations.", 'CreatedDate': '2022-07-20T14:13:45.000+0000', 'CloseDate': '2023-11-15'}], 'var_function-call-18199363812371569811': [{'Id': '#800Wt00000DD0SZIA1', 'AccountId': '001Wt00000PGZmfIAH', 'Status': 'Activated  ', 'StartDate': '2021-07-20', 'CustomerSignedDate': '2021-07-15', 'CompanySignedDate': '2021-07-16', 'Description': 'This contract solidifies the expanded partnership with Quantum Dynamics LLC for the provision of advanced AI-powered EDA tools, focusing on enhancing their quantum computing technology developments.', 'ContractTerm': '24'}, {'Id': '800Wt00000DD0SaIAL', 'AccountId': '001Wt00000PGXrLIAX', 'Status': 'Activated', 'StartDate': '2021-10-01', 'CustomerSignedDate': '2021-09-28', 'CompanySignedDate': '2021-09-28', 'Description': 'This contract outlines the collaboration between TechPulse Solutions and DataGuard Insights for EDA integration and security enhancements, providing comprehensive support and streamlining operational efficiencies within the DataGuard systems.', 'ContractTerm': '12'}, {'Id': '#800Wt00000DD0SbIAL', 'AccountId': '001Wt00000PGXrLIAX', 'Status': 'Activated   ', 'StartDate': '2023-07-15', 'CustomerSignedDate': '2023-07-11', 'CompanySignedDate': '2023-07-12', 'Description': 'Contract detailing the secure integration and optimization services to be implemented for DataGuard Insights, focusing on integrating CryptSecure Core and SecureFlow Suite into existing systems for enhanced data management and security. This includes AI-powered solution deployment, comprehensive training, and support.', 'ContractTerm': '12'}, {'Id': '800Wt00000DDDuRIAX', 'AccountId': '001Wt00000PGYgxIAH', 'Status': 'Activated ', 'StartDate': '2024-05-01', 'CustomerSignedDate': '2024-04-15', 'CompanySignedDate': '2024-04-16', 'Description': 'This contract establishes a collaboration between TechPulse Solutions and EcoShield Technologies to enhance environmental tech solutions using AI-powered electronic design automation (EDA) tools, focusing on sustainability and energy efficiency.', 'ContractTerm': '12'}, {'Id': '800Wt00000DDNFUIA5', 'AccountId': '#001Wt00000PGeJIIA1', 'Status': 'Activated', 'StartDate': '2023-08-01', 'CustomerSignedDate': '2023-07-01', 'CompanySignedDate': '2023-07-02', 'Description': "The contract facilitates the Innovative R&D Transformation project for InnoSphere Labs utilizing TechPulse Solutions' EDA tools, ensuring seamless integration and optimization of their research operations.", 'ContractTerm': '12'}], 'var_function-call-17899316139087214392': [{'Id': '800Wt00000DE9FGIA1', 'CompanySignedDate': '2023-04-15'}], 'var_function-call-17899316139087216087': 'file_storage/function-call-17899316139087216087.json', 'var_function-call-3381006347337228956': [{'Month': '2023-01', 'Cnt': '5'}, {'Month': '2023-02', 'Cnt': '5'}, {'Month': '2023-03', 'Cnt': '3'}, {'Month': '2023-04', 'Cnt': '1'}, {'Month': '2023-05', 'Cnt': '3'}, {'Month': '2023-06', 'Cnt': '4'}, {'Month': '2023-07', 'Cnt': '4'}, {'Month': '2023-08', 'Cnt': '5'}, {'Month': '2023-09', 'Cnt': '4'}, {'Month': '2023-10', 'Cnt': '9'}, {'Month': '2023-11', 'Cnt': '4'}, {'Month': '2023-12', 'Cnt': '3'}], 'var_function-call-9657852530181734214': [{'Month': '2023-01', 'Cnt': '6'}, {'Month': '2023-02', 'Cnt': '10'}, {'Month': '2023-03', 'Cnt': '15'}, {'Month': '2023-04', 'Cnt': '11'}, {'Month': '2023-05', 'Cnt': '18'}, {'Month': '2023-06', 'Cnt': '31'}, {'Month': '2023-07', 'Cnt': '14'}, {'Month': '2023-08', 'Cnt': '18'}, {'Month': '2023-09', 'Cnt': '35'}, {'Month': '2023-10', 'Cnt': '25'}, {'Month': '2023-11', 'Cnt': '119'}, {'Month': '2023-12', 'Cnt': '162'}], 'var_function-call-17426704129607414228': [{'count_star()': '163'}], 'var_function-call-6504895578308259406': 'file_storage/function-call-6504895578308259406.json', 'var_function-call-6504895578308258827': 'file_storage/function-call-6504895578308258827.json'}

exec(code, env_args)
