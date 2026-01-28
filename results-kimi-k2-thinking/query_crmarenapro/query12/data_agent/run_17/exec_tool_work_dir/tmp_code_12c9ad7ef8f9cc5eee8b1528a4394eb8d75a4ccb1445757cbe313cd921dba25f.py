code = """import pandas as pd, json, os

# Load the data from the file
file_path = 'file_storage/functions.query_db:12.json'
with open(file_path, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Clean ID columns by removing leading #
for col in ['OpportunityId', 'AgentId', 'ContractId']:
    if col in df.columns:
        df[col] = df[col].astype(str).str.replace('^#', '', regex=True).str.strip()

# Convert dates to datetime
df['OpportunityCreatedDate'] = pd.to_datetime(df['OpportunityCreatedDate'], utc=True)
df['ContractSignedDate'] = pd.to_datetime(df['ContractSignedDate'], errors='coerce', utc=True)

# Handle CloseDate (convert if it exists, may be date or string)
if 'CloseDate' in df.columns:
    df['CloseDate'] = pd.to_datetime(df['CloseDate'], errors='coerce', utc=True)

# Filter for April 2023 opportunities
april_mask = (df['OpportunityCreatedDate'].dt.year == 2023) & (df['OpportunityCreatedDate'].dt.month == 4)
df_april = df[april_mask].copy()

# For opportunities without ContractSignedDate, fallback to CloseDate
if 'CloseDate' in df_april.columns:
    df_april['EndDate'] = df_april['ContractSignedDate'].combine_first(df_april['CloseDate'])
else:
    df_april['EndDate'] = df_april['ContractSignedDate']

# Filter out rows where EndDate is missing or not after creation date
df_valid = df_april[df_april['EndDate'].notna()].copy()

# Calculate turnaround days (only positive values)
df_valid['TurnaroundDays'] = (df_valid['EndDate'] - df_valid['OpportunityCreatedDate']).dt.days

# Filter for positive turnaround days only (signature after creation)
df_valid['TurnaroundDays'] = df_valid['TurnaroundDays'].where(df_valid['TurnaroundDays'] > 0, None)
df_valid = df_valid.dropna(subset=['TurnaroundDays'])

# Group by agent to find average turnaround time
agent_stats = df_valid.groupby('AgentId').agg({'TurnaroundDays': ['mean', 'count']}).reset_index()
agent_stats.columns = ['AgentId', 'AvgTurnaround', 'OpportunityCount']

# Find agent with minimum average turnaround
best_result = None
if not agent_stats.empty:
    # Sort by average turnaround and get the first one
    agent_stats_sorted = agent_stats.sort_values('AvgTurnaround')
    best_agent = agent_stats_sorted.iloc[0]
    
    best_result = {
        'best_agent_id': best_agent['AgentId'],
        'average_turnaround_days': round(best_agent['AvgTurnaround'], 2),
        'opportunity_count': int(best_agent['OpportunityCount']),
        'total_agents_considered': len(agent_stats_sorted)
    }
else:
    best_result = {'error': 'No valid opportunities found for April 2023 with complete contract data'}

print('__RESULT__:')
print(json.dumps(best_result))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGeJIIA1', 'ContactId': '003Wt00000JqvQiIAJ', 'OwnerId': '005Wt000003NIqXIAW', 'Probability': '75.0', 'Amount': '182448.4965', 'StageName': 'Qualification', 'Name': 'InnoSphere Labs - EDA Innovation Expansion', 'Description': 'InnoSphere Labs is exploring advanced EDA solutions to enhance their R&D capabilities. They are particularly interested in the AI Cirku-Tech for rapid circuit prototyping, and the EcoPCB Creator for environmentally-friendly design processes. Additionally, CloudLink Designer could improve their team collaboration across global projects.', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'CloseDate': '2024-02-15'}, {'Id': '006Wt000007Aw3WIAS', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGzsMIAT', 'ContactId': '#003Wt00000JqyQEIAZ', 'OwnerId': '005Wt000003NIc1IAG', 'Probability': '75.0', 'Amount': '22238.547', 'StageName': 'Quote', 'Name': 'TechPulse-PrimeEdge Strategic Collaboration ', 'Description': "TechPulse Solutions is poised to empower PrimeEdge Technology with its suite of cutting-edge EDA tools, including AI Cirku-Tech and SecureAnalytics Pro. By integrating solutions like DesignWave Automation and CloudLink Designer, TechPulse aims to enhance workflow automation and secure data optimization within PrimeEdge's operations. This opportunity also leverages OptiPower Manager to pursue sustainable electronics development, ensuring PrimeEdge stays at the forefront of IT innovation.", 'CreatedDate': '2024-04-05T12:15:30.000+0000', 'CloseDate': '2024-06-15'}, {'Id': '006Wt000007Aw3XIAS', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGYx5IAH', 'ContactId': '003Wt00000JquRPIAZ', 'OwnerId': '#005Wt000003NJZhIAO', 'Probability': '75.0', 'Amount': '10019.8045', 'StageName': 'Quote', 'Name': 'Quantum Designs Partnership Initiative', 'Description': 'TechPulse Solutions presents Quantum Designs with an integrated EDA suite, combining the robust capabilities of PulseSim Pro and AI Cirku-Tech for advanced semiconductor solutions. Emphasizing security, SecureFlow Suite ensures compliance and safeguarding critical data. The partnership focuses on streamlining PCB development with EcoPCB Creator, enhancing both innovation and sustainability.', 'CreatedDate': '2021-02-10T14:23:45.000+0000', 'CloseDate': '2021-05-30'}, {'Id': '006Wt000007Aya9IAC', 'ContractID__c': 'None', 'AccountId': '001Wt00000PHViXIAX', 'ContactId': '003Wt00000Jqvk1IAB', 'OwnerId': '005Wt000003NDJ0IAO', 'Probability': '75.0', 'Amount': '19002.1475', 'StageName': 'Discovery', 'Name': 'Nova Healthcare Tech Strategic Enhancement', 'Description': "Leveraging TechPulse Solutions' AI Cirku-Tech for rapid prototype advancements and SecureFlow Suite for enhanced security compliance, Nova Healthcare Tech can revolutionize their service offerings. By integrating CollabCircuit Hub, interdepartmental communication will improve significantly, facilitating more efficient project management. The adoption of QuantumPCB Modeler could provide Nova Healthcare Tech with cutting-edge tech solutions, further enhancing patient care and service quality.", 'CreatedDate': '2023-08-11T09:30:00.000+0000', 'CloseDate': '2023-11-30'}, {'Id': '006Wt000007AyaAIAS', 'ContractID__c': 'None', 'AccountId': '001Wt00000PHVk9IAH', 'ContactId': '003Wt00000Jqv0wIAB', 'OwnerId': '005Wt000003NJxtIAG', 'Probability': '85.0', 'Amount': '22249.0175', 'StageName': 'Negotiation   ', 'Name': 'LiftTech Smart Integration Project', 'Description': "LiftTech Elevations aims to enhance its building automation systems using AI-driven EDA tools like CircuitAI Innovator and EcoPCB Creator. By integrating advanced security features with SecureAnalytics Pro, they can bolster data protection and compliance. The collaboration with TechPulse Solutions promises to streamline LiftTech's workflows with DesignWave Automation, ensuring seamless system operations.", 'CreatedDate': '2022-07-20T14:13:45.000+0000', 'CloseDate': '2023-11-15'}], 'var_functions.query_db:2': [{'Id': '#800Wt00000DD0SZIA1', 'AccountId': '001Wt00000PGZmfIAH', 'Status': 'Activated  ', 'StartDate': '2021-07-20', 'CustomerSignedDate': '2021-07-15', 'CompanySignedDate': '2021-07-16', 'Description': 'This contract solidifies the expanded partnership with Quantum Dynamics LLC for the provision of advanced AI-powered EDA tools, focusing on enhancing their quantum computing technology developments.', 'ContractTerm': '24'}, {'Id': '800Wt00000DD0SaIAL', 'AccountId': '001Wt00000PGXrLIAX', 'Status': 'Activated', 'StartDate': '2021-10-01', 'CustomerSignedDate': '2021-09-28', 'CompanySignedDate': '2021-09-28', 'Description': 'This contract outlines the collaboration between TechPulse Solutions and DataGuard Insights for EDA integration and security enhancements, providing comprehensive support and streamlining operational efficiencies within the DataGuard systems.', 'ContractTerm': '12'}, {'Id': '#800Wt00000DD0SbIAL', 'AccountId': '001Wt00000PGXrLIAX', 'Status': 'Activated   ', 'StartDate': '2023-07-15', 'CustomerSignedDate': '2023-07-11', 'CompanySignedDate': '2023-07-12', 'Description': 'Contract detailing the secure integration and optimization services to be implemented for DataGuard Insights, focusing on integrating CryptSecure Core and SecureFlow Suite into existing systems for enhanced data management and security. This includes AI-powered solution deployment, comprehensive training, and support.', 'ContractTerm': '12'}, {'Id': '800Wt00000DDDuRIAX', 'AccountId': '001Wt00000PGYgxIAH', 'Status': 'Activated ', 'StartDate': '2024-05-01', 'CustomerSignedDate': '2024-04-15', 'CompanySignedDate': '2024-04-16', 'Description': 'This contract establishes a collaboration between TechPulse Solutions and EcoShield Technologies to enhance environmental tech solutions using AI-powered electronic design automation (EDA) tools, focusing on sustainability and energy efficiency.', 'ContractTerm': '12'}, {'Id': '800Wt00000DDNFUIA5', 'AccountId': '#001Wt00000PGeJIIA1', 'Status': 'Activated', 'StartDate': '2023-08-01', 'CustomerSignedDate': '2023-07-01', 'CompanySignedDate': '2023-07-02', 'Description': "The contract facilitates the Innovative R&D Transformation project for InnoSphere Labs utilizing TechPulse Solutions' EDA tools, ensuring seamless integration and optimization of their research operations.", 'ContractTerm': '12'}], 'var_functions.query_db:4': [{'total_opportunities': '1170'}], 'var_functions.query_db:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:26': {'data_type': "<class 'str'>", 'is_json_file': True, 'preview_start': 'file_storage/functions.query_db:12.json', 'record_count': 1170}}

exec(code, env_args)
