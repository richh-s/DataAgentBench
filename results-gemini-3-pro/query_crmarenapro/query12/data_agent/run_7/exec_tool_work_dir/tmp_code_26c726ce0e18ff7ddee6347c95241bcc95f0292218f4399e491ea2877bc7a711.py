code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-1708808029556042775'], 'r') as f:
    contracts = json.load(f)
with open(locals()['var_function-call-118059550630705006'], 'r') as f:
    opportunities = json.load(f)

# Create DataFrames
df_c = pd.DataFrame(contracts)
df_o = pd.DataFrame(opportunities)

# Clean IDs
df_c['clean_id'] = df_c['Id'].apply(lambda x: x.strip().lstrip('#'))
df_o['clean_contract_id'] = df_o['ContractID__c'].apply(lambda x: x.strip().lstrip('#') if x else None)
df_o['clean_owner_id'] = df_o['OwnerId'].apply(lambda x: x.strip().lstrip('#') if x else None)

# Parse Dates
# CompanySignedDate is YYYY-MM-DD
df_c['signed_date'] = pd.to_datetime(df_c['CompanySignedDate'], errors='coerce')

# CreatedDate is ISO format
df_o['created_date'] = pd.to_datetime(df_o['CreatedDate'], errors='coerce')

# Filter Contracts for April 2023
# 2023-04-01 to 2023-04-30
start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')

df_c_apr = df_c[(df_c['signed_date'] >= start_date) & (df_c['signed_date'] <= end_date)].copy()

print(f"Contracts in April 2023: {len(df_c_apr)}")

# Join
# Inner join on contract id
merged = pd.merge(df_o, df_c_apr, left_on='clean_contract_id', right_on='clean_id', how='inner')

print(f"Merged records: {len(merged)}")

if len(merged) == 0:
    print("__RESULT__:")
    print(json.dumps("No records found"))
else:
    # Calculate duration
    # Duration = Signed Date - Created Date (in days)
    # Note: CreatedDate has time, SignedDate does not (00:00:00).
    # If we want exact days, we might want to normalize CreatedDate to midnight or keep as is.
    # "number of days between" usually implies partial days or difference.
    # Let's normalize CreatedDate to date for day difference?
    # Policy: "number of days between ...". Usually D2 - D1.
    # If Created = Apr 1 10am, Signed = Apr 2. Diff = 0.58 days? Or 1 day?
    # Usually sales cycle is in days (float or int).
    # DuckDB `date_diff('day', ...)` usually counts boundaries or full days.
    # Let's use exact difference in days (float).
    
    # However, standard practice is days.
    # Let's subtract timestamps and get .days attribute or total_seconds / 86400
    
    # Ensure signed_date has timezone if created_date has timezone, or make created_date naive
    # created_date likely has timezone info (UTC). signed_date is naive.
    # Let's make created_date naive (UTC)
    merged['created_date'] = merged['created_date'].dt.tz_localize(None)
    
    merged['duration_days'] = (merged['signed_date'] - merged['created_date']).dt.total_seconds() / (24 * 3600)
    
    # Group by Agent
    grouped = merged.groupby('clean_owner_id')['duration_days'].mean().reset_index()
    grouped.columns = ['AgentId', 'AvgDuration']
    
    # Find min
    min_row = grouped.loc[grouped['AvgDuration'].idxmin()]
    
    result = min_row['AgentId']
    print("__RESULT__:")
    print(json.dumps(result))"""

env_args = {'var_function-call-16680709838416822807': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_function-call-17596226158453635157': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGeJIIA1', 'ContactId': '003Wt00000JqvQiIAJ', 'OwnerId': '005Wt000003NIqXIAW', 'Probability': '75.0', 'Amount': '182448.4965', 'StageName': 'Qualification', 'Name': 'InnoSphere Labs - EDA Innovation Expansion', 'Description': 'InnoSphere Labs is exploring advanced EDA solutions to enhance their R&D capabilities. They are particularly interested in the AI Cirku-Tech for rapid circuit prototyping, and the EcoPCB Creator for environmentally-friendly design processes. Additionally, CloudLink Designer could improve their team collaboration across global projects.', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'CloseDate': '2024-02-15'}, {'Id': '006Wt000007Aw3WIAS', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGzsMIAT', 'ContactId': '#003Wt00000JqyQEIAZ', 'OwnerId': '005Wt000003NIc1IAG', 'Probability': '75.0', 'Amount': '22238.547', 'StageName': 'Quote', 'Name': 'TechPulse-PrimeEdge Strategic Collaboration ', 'Description': "TechPulse Solutions is poised to empower PrimeEdge Technology with its suite of cutting-edge EDA tools, including AI Cirku-Tech and SecureAnalytics Pro. By integrating solutions like DesignWave Automation and CloudLink Designer, TechPulse aims to enhance workflow automation and secure data optimization within PrimeEdge's operations. This opportunity also leverages OptiPower Manager to pursue sustainable electronics development, ensuring PrimeEdge stays at the forefront of IT innovation.", 'CreatedDate': '2024-04-05T12:15:30.000+0000', 'CloseDate': '2024-06-15'}, {'Id': '006Wt000007Aw3XIAS', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGYx5IAH', 'ContactId': '003Wt00000JquRPIAZ', 'OwnerId': '#005Wt000003NJZhIAO', 'Probability': '75.0', 'Amount': '10019.8045', 'StageName': 'Quote', 'Name': 'Quantum Designs Partnership Initiative', 'Description': 'TechPulse Solutions presents Quantum Designs with an integrated EDA suite, combining the robust capabilities of PulseSim Pro and AI Cirku-Tech for advanced semiconductor solutions. Emphasizing security, SecureFlow Suite ensures compliance and safeguarding critical data. The partnership focuses on streamlining PCB development with EcoPCB Creator, enhancing both innovation and sustainability.', 'CreatedDate': '2021-02-10T14:23:45.000+0000', 'CloseDate': '2021-05-30'}], 'var_function-call-9854862025994729017': [{'Id': '#800Wt00000DD0SZIA1', 'AccountId': '001Wt00000PGZmfIAH', 'Status': 'Activated  ', 'StartDate': '2021-07-20', 'CustomerSignedDate': '2021-07-15', 'CompanySignedDate': '2021-07-16', 'Description': 'This contract solidifies the expanded partnership with Quantum Dynamics LLC for the provision of advanced AI-powered EDA tools, focusing on enhancing their quantum computing technology developments.', 'ContractTerm': '24'}, {'Id': '800Wt00000DD0SaIAL', 'AccountId': '001Wt00000PGXrLIAX', 'Status': 'Activated', 'StartDate': '2021-10-01', 'CustomerSignedDate': '2021-09-28', 'CompanySignedDate': '2021-09-28', 'Description': 'This contract outlines the collaboration between TechPulse Solutions and DataGuard Insights for EDA integration and security enhancements, providing comprehensive support and streamlining operational efficiencies within the DataGuard systems.', 'ContractTerm': '12'}, {'Id': '#800Wt00000DD0SbIAL', 'AccountId': '001Wt00000PGXrLIAX', 'Status': 'Activated   ', 'StartDate': '2023-07-15', 'CustomerSignedDate': '2023-07-11', 'CompanySignedDate': '2023-07-12', 'Description': 'Contract detailing the secure integration and optimization services to be implemented for DataGuard Insights, focusing on integrating CryptSecure Core and SecureFlow Suite into existing systems for enhanced data management and security. This includes AI-powered solution deployment, comprehensive training, and support.', 'ContractTerm': '12'}], 'var_function-call-17991755109309820788': [{'AgentId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15', 'DaysDiff': '304'}], 'var_function-call-11088537139778760752': [{'AgentId': '005Wt000003NDEBIA4', 'AvgTurnaround': '304.0'}], 'var_function-call-5838377092142678911': [{'NumAgents': '1', 'NumDeals': '1'}], 'var_function-call-6678105500249809657': [{'min(CompanySignedDate)': '2020-06-15', 'max(CompanySignedDate)': '2024-09-27'}], 'var_function-call-15020825200513619532': [{'ContractID__c': '800Wt00000DE9DdIAL'}, {'ContractID__c': '800Wt00000DE45uIAD'}, {'ContractID__c': '800Wt00000DDxHMIA1'}, {'ContractID__c': '800Wt00000DDsJGIA1'}, {'ContractID__c': '800Wt00000DDQ6vIAH'}, {'ContractID__c': '800Wt00000DE9qMIAT'}, {'ContractID__c': '800Wt00000DE0rxIAD'}, {'ContractID__c': '800Wt00000DDsBEIA1'}, {'ContractID__c': '800Wt00000DDxdvIAD'}, {'ContractID__c': '800Wt00000DDfifIAD'}], 'var_function-call-11299188937952929027': [{'Id': '#800Wt00000DD0SZIA1'}, {'Id': '800Wt00000DD0SaIAL'}, {'Id': '#800Wt00000DD0SbIAL'}, {'Id': '800Wt00000DDDuRIAX'}, {'Id': '800Wt00000DDNFUIA5'}, {'Id': '800Wt00000DDNFVIA5'}, {'Id': '800Wt00000DDNlnIAH'}, {'Id': '800Wt00000DDPXRIA5'}, {'Id': '800Wt00000DDPXSIA5'}, {'Id': '800Wt00000DDPXTIA5'}], 'var_function-call-11832943976677844304': [{'Id': '800Wt00000DE9FGIA1', 'CompanySignedDate': '2023-04-15'}], 'var_function-call-14070721480536403336': [{'Id': '006Wt000007BI41IAG', 'ContractID__c': '800Wt00000DE9FGIA1', 'AccountId': '001Wt00000PFrk1IAD', 'ContactId': '#003Wt00000JqczIIAR', 'OwnerId': '005Wt000003NDEBIA4', 'Probability': '87.0', 'Amount': '9639.8055', 'StageName': 'Closed  ', 'Name': 'SkyNet Tech-Driven Revolution', 'Description': "TechPulse Solutions aims to revolutionize SkyNet Technologies' drone and aviation systems by integrating AI Cirku-Tech and PulseSim Pro for enhanced design and simulation capabilities. QuantumPCB Modeler, already used by SkyNet, will be complemented with EcoPCB Creator for sustainable circuit development. Our collaboration will focus on seamless integration and enhanced productivity through CloudLink Designer.", 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'CloseDate': '2023-03-10'}], 'var_function-call-1658250837964880235': [{'Id': '#006Wt000007B5jWIAS', 'ContractID__c': '800Wt00000DE97BIAT', 'AccountId': '#001Wt00000PHVfJIAX', 'ContactId': '003Wt00000Jquw2IAB', 'OwnerId': '005Wt000003NFB8IAO', 'Probability': '85.0', 'Amount': '297493.625', 'StageName': 'Closed', 'Name': 'BrightTech Systems - Advanced EDA Integration', 'Description': "TechPulse Solutions offers BrightTech Systems a tailored EDA suite with products such as AI DesignShift, OptiPower Max, and CircuitSync Pro. These advanced tools support BrightTech's mission of innovative circuit design and power optimization. Our solution enhances communication networks, introducing efficiency and unparalleled connectivity improvements.", 'CreatedDate': '2022-11-01T10:45:36.000+0000', 'CloseDate': '2023-04-28'}, {'Id': '006Wt000007B8RLIA0', 'ContractID__c': '800Wt00000DE9aDIAT', 'AccountId': '001Wt00000PHVaUIAX', 'ContactId': '003Wt00000JqqVrIAJ', 'OwnerId': '005Wt000003NJgAIAW', 'Probability': '85.0', 'Amount': '8340.81', 'StageName': 'Closed', 'Name': 'GreenTech Fusion Partnership', 'Description': "TerraSync Solutions is set to enhance its sustainable technology offerings by integrating EcoPCB Creator and AIOptics Vision into their workflows. This partnership aims to optimize product efficiency and environmental impact reduction, highlighting TechPulse Solution's capabilities in providing advanced, eco-conscious technology solutions. The collaboration focuses on seamless implementation and sustainable innovation.", 'CreatedDate': '2022-11-15T10:32:45.000+0000', 'CloseDate': '2023-04-10'}, {'Id': '006Wt000007BDU9IAO', 'ContractID__c': '800Wt00000DE0ryIAD', 'AccountId': '#001Wt00000PGaNjIAL', 'ContactId': '#003Wt00000JqwxpIAB', 'OwnerId': '005Wt000003NJjNIAW', 'Probability': '85.0', 'Amount': '14184.2275', 'StageName': 'Closed', 'Name': 'MetaData Analytics AI Integration Opportunity', 'Description': 'TechPulse Solutions has an opportunity to expand its footprint with MetaData Analytics by offering PulseSim Pro and AI Cirku-Tech to enhance their analytical capabilities. The SecureFlow Suite can further bolster their data protection and compliance measures, aligning with their security-conscious ethos. Integrating CloudLink Designer could improve their global project collaboration and delivery efficiency.', 'CreatedDate': '2023-02-20T14:45:30.000+0000', 'CloseDate': '2023-04-30'}], 'var_function-call-6778240755771672783': [{'Id': '800Wt00000DE97BIAT', 'CompanySignedDate': '2023-05-16'}, {'Id': '800Wt00000DE9aDIAT', 'CompanySignedDate': '2023-02-28'}], 'var_function-call-11519750020943217982': [{'Id': '#800Wt00000DE0ryIAD', 'CompanySignedDate': '2023-05-12'}], 'var_function-call-6266415346757760821': [{'length(CompanySignedDate)': '10', 'count_star()': '163'}], 'var_function-call-5575293189177594508': [{'Id': '005Wt000003NDEBIA4', 'FirstName': 'Nadia', 'LastName': 'Al-Balushi', 'Email': 'nadia.albalushi@techagents.com', 'Phone': '234-555-8108', 'Username': '1745179504.5pzg7.nadia.albalushi@techagents.com', 'Alias': '-balushi', 'LanguageLocaleKey': 'en_US', 'EmailEncodingKey': 'UTF-8', 'TimeZoneSidKey': 'America/Los_Angeles', 'LocaleSidKey': 'en_US'}], 'var_function-call-5186043029245581407': [{'Id': '800Wt00000DE9FGIA1', 'CompanySignedDate': '2023-04-15'}], 'var_function-call-118059550630705006': 'file_storage/function-call-118059550630705006.json', 'var_function-call-1708808029556042775': 'file_storage/function-call-1708808029556042775.json'}

exec(code, env_args)
