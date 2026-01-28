code = """import json, re, os
from datetime import datetime
from collections import defaultdict

# Load data
opp_list = var_functions.query_db:10
contract_file = var_functions.query_db:12

if isinstance(contract_file, str):
    with open(contract_file, 'r') as f:
        contract_list = json.load(f)
else:
    contract_list = contract_file

def clean_id(val):
    if not val:
        return None
    val = str(val).strip()
    if val.startswith('#'):
        val = val[1:].strip()
    return val if val else None

# Clean opportunities
opps = []
for rec in opp_list:
    oid = clean_id(rec.get('Id'))
    owner = clean_id(rec.get('OwnerId'))
    cid = clean_id(rec.get('ContractID__c'))
    created_str = rec.get('CreatedDate')
    if not all([oid, owner, cid, created_str]):
        continue
    try:
        created_dt = datetime.fromisoformat(created_str.replace('Z', '+00:00'))
    except Exception:
        continue
    opps.append({
        'Id': oid,
        'OwnerId': owner,
        'ContractID__c': cid,
        'CreatedDate': created_dt
    })

# Build contract date map
contracts = {}
for rec in contract_list:
    cid = clean_id(rec.get('Id'))
    cs_date_str = rec.get('CompanySignedDate')
    if not cid or not cs_date_str:
        continue
    try:
        cs_date = datetime.strptime(cs_date_str, '%Y-%m-%d').date()
    except Exception:
        continue
    contracts[cid] = cs_date

# Compute turnaround for valid opps
valid_opps = []
for opp in opps:
    cid = opp['ContractID__c']
    if cid not in contracts:
        continue
    cs_date = contracts[cid]
    # Ensure signed date not before creation
    if cs_date < opp['CreatedDate'].date():
        continue
    opp['CompanySignedDate'] = cs_date
    delta_days = (cs_date - opp['CreatedDate'].date()).days
    opp['TurnaroundDays'] = delta_days
    valid_opps.append(opp)

# Group by owner, compute average days
owner_days = defaultdict(list)
for opp in valid_opps:
    owner_days[opp['OwnerId']].append(opp['TurnaroundDays'])

owner_avg = {owner: sum(days)/len(days) for owner, days in owner_days.items()}

# Find min average owner
if owner_avg:
    min_avg = min(owner_avg.values())
    best_owners = [owner for owner, avg in owner_avg.items() if abs(avg - min_avg) < 1e-9]
    best_owner = best_owners[0]
else:
    best_owner = None

print('__RESULT__:')
print(json.dumps(best_owner))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGeJIIA1', 'ContactId': '003Wt00000JqvQiIAJ', 'OwnerId': '005Wt000003NIqXIAW', 'Probability': '75.0', 'Amount': '182448.4965', 'StageName': 'Qualification', 'Name': 'InnoSphere Labs - EDA Innovation Expansion', 'Description': 'InnoSphere Labs is exploring advanced EDA solutions to enhance their R&D capabilities. They are particularly interested in the AI Cirku-Tech for rapid circuit prototyping, and the EcoPCB Creator for environmentally-friendly design processes. Additionally, CloudLink Designer could improve their team collaboration across global projects.', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'CloseDate': '2024-02-15'}, {'Id': '006Wt000007Aw3WIAS', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGzsMIAT', 'ContactId': '#003Wt00000JqyQEIAZ', 'OwnerId': '005Wt000003NIc1IAG', 'Probability': '75.0', 'Amount': '22238.547', 'StageName': 'Quote', 'Name': 'TechPulse-PrimeEdge Strategic Collaboration ', 'Description': "TechPulse Solutions is poised to empower PrimeEdge Technology with its suite of cutting-edge EDA tools, including AI Cirku-Tech and SecureAnalytics Pro. By integrating solutions like DesignWave Automation and CloudLink Designer, TechPulse aims to enhance workflow automation and secure data optimization within PrimeEdge's operations. This opportunity also leverages OptiPower Manager to pursue sustainable electronics development, ensuring PrimeEdge stays at the forefront of IT innovation.", 'CreatedDate': '2024-04-05T12:15:30.000+0000', 'CloseDate': '2024-06-15'}, {'Id': '006Wt000007Aw3XIAS', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGYx5IAH', 'ContactId': '003Wt00000JquRPIAZ', 'OwnerId': '#005Wt000003NJZhIAO', 'Probability': '75.0', 'Amount': '10019.8045', 'StageName': 'Quote', 'Name': 'Quantum Designs Partnership Initiative', 'Description': 'TechPulse Solutions presents Quantum Designs with an integrated EDA suite, combining the robust capabilities of PulseSim Pro and AI Cirku-Tech for advanced semiconductor solutions. Emphasizing security, SecureFlow Suite ensures compliance and safeguarding critical data. The partnership focuses on streamlining PCB development with EcoPCB Creator, enhancing both innovation and sustainability.', 'CreatedDate': '2021-02-10T14:23:45.000+0000', 'CloseDate': '2021-05-30'}, {'Id': '006Wt000007Aya9IAC', 'ContractID__c': 'None', 'AccountId': '001Wt00000PHViXIAX', 'ContactId': '003Wt00000Jqvk1IAB', 'OwnerId': '005Wt000003NDJ0IAO', 'Probability': '75.0', 'Amount': '19002.1475', 'StageName': 'Discovery', 'Name': 'Nova Healthcare Tech Strategic Enhancement', 'Description': "Leveraging TechPulse Solutions' AI Cirku-Tech for rapid prototype advancements and SecureFlow Suite for enhanced security compliance, Nova Healthcare Tech can revolutionize their service offerings. By integrating CollabCircuit Hub, interdepartmental communication will improve significantly, facilitating more efficient project management. The adoption of QuantumPCB Modeler could provide Nova Healthcare Tech with cutting-edge tech solutions, further enhancing patient care and service quality.", 'CreatedDate': '2023-08-11T09:30:00.000+0000', 'CloseDate': '2023-11-30'}, {'Id': '006Wt000007AyaAIAS', 'ContractID__c': 'None', 'AccountId': '001Wt00000PHVk9IAH', 'ContactId': '003Wt00000Jqv0wIAB', 'OwnerId': '005Wt000003NJxtIAG', 'Probability': '85.0', 'Amount': '22249.0175', 'StageName': 'Negotiation   ', 'Name': 'LiftTech Smart Integration Project', 'Description': "LiftTech Elevations aims to enhance its building automation systems using AI-driven EDA tools like CircuitAI Innovator and EcoPCB Creator. By integrating advanced security features with SecureAnalytics Pro, they can bolster data protection and compliance. The collaboration with TechPulse Solutions promises to streamline LiftTech's workflows with DesignWave Automation, ensuring seamless system operations.", 'CreatedDate': '2022-07-20T14:13:45.000+0000', 'CloseDate': '2023-11-15'}], 'var_functions.query_db:2': [{'Id': '#800Wt00000DD0SZIA1', 'AccountId': '001Wt00000PGZmfIAH', 'Status': 'Activated  ', 'StartDate': '2021-07-20', 'CustomerSignedDate': '2021-07-15', 'CompanySignedDate': '2021-07-16', 'Description': 'This contract solidifies the expanded partnership with Quantum Dynamics LLC for the provision of advanced AI-powered EDA tools, focusing on enhancing their quantum computing technology developments.', 'ContractTerm': '24'}, {'Id': '800Wt00000DD0SaIAL', 'AccountId': '001Wt00000PGXrLIAX', 'Status': 'Activated', 'StartDate': '2021-10-01', 'CustomerSignedDate': '2021-09-28', 'CompanySignedDate': '2021-09-28', 'Description': 'This contract outlines the collaboration between TechPulse Solutions and DataGuard Insights for EDA integration and security enhancements, providing comprehensive support and streamlining operational efficiencies within the DataGuard systems.', 'ContractTerm': '12'}, {'Id': '#800Wt00000DD0SbIAL', 'AccountId': '001Wt00000PGXrLIAX', 'Status': 'Activated   ', 'StartDate': '2023-07-15', 'CustomerSignedDate': '2023-07-11', 'CompanySignedDate': '2023-07-12', 'Description': 'Contract detailing the secure integration and optimization services to be implemented for DataGuard Insights, focusing on integrating CryptSecure Core and SecureFlow Suite into existing systems for enhanced data management and security. This includes AI-powered solution deployment, comprehensive training, and support.', 'ContractTerm': '12'}, {'Id': '800Wt00000DDDuRIAX', 'AccountId': '001Wt00000PGYgxIAH', 'Status': 'Activated ', 'StartDate': '2024-05-01', 'CustomerSignedDate': '2024-04-15', 'CompanySignedDate': '2024-04-16', 'Description': 'This contract establishes a collaboration between TechPulse Solutions and EcoShield Technologies to enhance environmental tech solutions using AI-powered electronic design automation (EDA) tools, focusing on sustainability and energy efficiency.', 'ContractTerm': '12'}, {'Id': '800Wt00000DDNFUIA5', 'AccountId': '#001Wt00000PGeJIIA1', 'Status': 'Activated', 'StartDate': '2023-08-01', 'CustomerSignedDate': '2023-07-01', 'CompanySignedDate': '2023-07-02', 'Description': "The contract facilitates the Innovative R&D Transformation project for InnoSphere Labs utilizing TechPulse Solutions' EDA tools, ensuring seamless integration and optimization of their research operations.", 'ContractTerm': '12'}], 'var_functions.query_db:4': [{'Id': '#006Wt000007B1klIAC', 'OwnerId': '#005Wt000003NBylIAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T09:00:34.000+0000'}, {'Id': '006Wt000007B49NIAS', 'OwnerId': '005Wt000003NIs9IAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-25T14:32:51.000+0000'}, {'Id': '006Wt000007B62sIAC', 'OwnerId': '005Wt000003NJZhIAO', 'ContractID__c': 'None', 'CreatedDate': '2023-04-04T10:15:30.000+0000'}, {'Id': '006Wt000007B6itIAC', 'OwnerId': '#005Wt000003NJMnIAO', 'ContractID__c': 'None', 'CreatedDate': '2023-04-25T09:45:30.000+0000'}, {'Id': '#006Wt000007B7tQIAS', 'OwnerId': '005Wt000003NIfGIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:20:30.000+0000'}, {'Id': '#006Wt000007B7yJIAS', 'OwnerId': '#005Wt000003NEdJIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:30:45.000+0000'}, {'Id': '006Wt000007B8CqIAK', 'OwnerId': '005Wt000003NInKIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T09:30:45.000+0000'}, {'Id': '#006Wt000007B8FyIAK', 'OwnerId': '005Wt000003NIovIAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:30:15.000+0000'}, {'Id': '#006Wt000007BA3JIAW', 'OwnerId': '005Wt000003NF9WIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-02T10:15:30.000+0000'}, {'Id': '006Wt000007BABLIA4', 'OwnerId': '005Wt000003NDEBIA4', 'ContractID__c': 'None', 'CreatedDate': '2023-04-01T14:47:23.000+0000'}, {'Id': '006Wt000007BAHlIAO', 'OwnerId': '#005Wt000003NFhPIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-19T15:30:45.000+0000'}, {'Id': '006Wt000007BAPrIAO', 'OwnerId': '005Wt000003NJxtIAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:15:32.000+0000'}, {'Id': '006Wt000007BBDrIAO', 'OwnerId': '005Wt000003NJ1pIAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-10T10:30:15.000+0000'}, {'Id': '006Wt000007BBc1IAG', 'OwnerId': '005Wt000003NEtPIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:14:32.000+0000'}, {'Id': '006Wt000007BCLEIA4', 'OwnerId': '005Wt000003NJBVIA4', 'ContractID__c': 'None', 'CreatedDate': '2023-04-27T11:22:30.000+0000'}, {'Id': '006Wt000007BCTFIA4', 'OwnerId': '#005Wt000003NBcBIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-20T11:15:33.000+0000'}, {'Id': '#006Wt000007BChmIAG', 'OwnerId': '005Wt000003NJgAIAW', 'ContractID__c': '800Wt00000DE9FFIA1', 'CreatedDate': '2023-04-25T10:45:30.000+0000'}, {'Id': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'ContractID__c': '800Wt00000DE8sgIAD', 'CreatedDate': '2023-04-10T10:15:30.000+0000'}, {'Id': '#006Wt000007BDXPIA4', 'OwnerId': '005Wt000003NJ0EIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:45:00.000+0000'}, {'Id': '006Wt000007BDcEIAW', 'OwnerId': '005Wt000003NIAbIAO', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:32:45.000+0000'}, {'Id': '006Wt000007BDpAIAW', 'OwnerId': '005Wt000003NEtPIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:30:15.000+0000'}, {'Id': '006Wt000007BETVIA4', 'OwnerId': '#005Wt000003NJjNIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-20T11:34:22.000+0000'}, {'Id': '#006Wt000007BEV4IAO', 'OwnerId': '005Wt000003NFRKIA4', 'ContractID__c': 'None', 'CreatedDate': '2023-04-05T14:23:45.000+0000'}, {'Id': '006Wt000007BFUOIA4', 'OwnerId': '005Wt000003NHpdIAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-05T10:15:30.000+0000'}, {'Id': '006Wt000007BGAIIA4', 'OwnerId': '005Wt000003NIdeIAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-11T12:45:33.000+0000'}, {'Id': '#006Wt000007BGDVIA4', 'OwnerId': '005Wt000003NBcBIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-10T11:20:45.000+0000'}, {'Id': '006Wt000007BHPhIAO', 'OwnerId': '#005Wt000003NEa3IAG', 'ContractID__c': '800Wt00000DE9ryIAD', 'CreatedDate': '2023-04-15T09:12:34.000+0000'}, {'Id': '#006Wt000007BHZNIA4', 'OwnerId': '005Wt000003NIaPIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-10T14:25:30.000+0000'}, {'Id': '#006Wt000007BHfpIAG', 'OwnerId': '005Wt000003NIqXIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-17T14:37:45.000+0000'}, {'Id': '006Wt000007BHr7IAG', 'OwnerId': '005Wt000003NIfGIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-01T09:45:23.000+0000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': '005Wt000003NJgAIAW', 'var_functions.query_db:10': [{'Id': '#006Wt000007B1klIAC', 'OwnerId': '#005Wt000003NBylIAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T09:00:34.000+0000'}, {'Id': '006Wt000007B49NIAS', 'OwnerId': '005Wt000003NIs9IAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-25T14:32:51.000+0000'}, {'Id': '006Wt000007B62sIAC', 'OwnerId': '005Wt000003NJZhIAO', 'ContractID__c': 'None', 'CreatedDate': '2023-04-04T10:15:30.000+0000'}, {'Id': '006Wt000007B6itIAC', 'OwnerId': '#005Wt000003NJMnIAO', 'ContractID__c': 'None', 'CreatedDate': '2023-04-25T09:45:30.000+0000'}, {'Id': '#006Wt000007B7tQIAS', 'OwnerId': '005Wt000003NIfGIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:20:30.000+0000'}, {'Id': '#006Wt000007B7yJIAS', 'OwnerId': '#005Wt000003NEdJIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:30:45.000+0000'}, {'Id': '006Wt000007B8CqIAK', 'OwnerId': '005Wt000003NInKIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T09:30:45.000+0000'}, {'Id': '#006Wt000007B8FyIAK', 'OwnerId': '005Wt000003NIovIAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:30:15.000+0000'}, {'Id': '#006Wt000007BA3JIAW', 'OwnerId': '005Wt000003NF9WIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-02T10:15:30.000+0000'}, {'Id': '006Wt000007BABLIA4', 'OwnerId': '005Wt000003NDEBIA4', 'ContractID__c': 'None', 'CreatedDate': '2023-04-01T14:47:23.000+0000'}, {'Id': '006Wt000007BAHlIAO', 'OwnerId': '#005Wt000003NFhPIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-19T15:30:45.000+0000'}, {'Id': '006Wt000007BAPrIAO', 'OwnerId': '005Wt000003NJxtIAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:15:32.000+0000'}, {'Id': '006Wt000007BBDrIAO', 'OwnerId': '005Wt000003NJ1pIAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-10T10:30:15.000+0000'}, {'Id': '006Wt000007BBc1IAG', 'OwnerId': '005Wt000003NEtPIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:14:32.000+0000'}, {'Id': '006Wt000007BCLEIA4', 'OwnerId': '005Wt000003NJBVIA4', 'ContractID__c': 'None', 'CreatedDate': '2023-04-27T11:22:30.000+0000'}, {'Id': '006Wt000007BCTFIA4', 'OwnerId': '#005Wt000003NBcBIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-20T11:15:33.000+0000'}, {'Id': '#006Wt000007BChmIAG', 'OwnerId': '005Wt000003NJgAIAW', 'ContractID__c': '800Wt00000DE9FFIA1', 'CreatedDate': '2023-04-25T10:45:30.000+0000'}, {'Id': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'ContractID__c': '800Wt00000DE8sgIAD', 'CreatedDate': '2023-04-10T10:15:30.000+0000'}, {'Id': '#006Wt000007BDXPIA4', 'OwnerId': '005Wt000003NJ0EIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:45:00.000+0000'}, {'Id': '006Wt000007BDcEIAW', 'OwnerId': '005Wt000003NIAbIAO', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:32:45.000+0000'}, {'Id': '006Wt000007BDpAIAW', 'OwnerId': '005Wt000003NEtPIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:30:15.000+0000'}, {'Id': '006Wt000007BETVIA4', 'OwnerId': '#005Wt000003NJjNIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-20T11:34:22.000+0000'}, {'Id': '#006Wt000007BEV4IAO', 'OwnerId': '005Wt000003NFRKIA4', 'ContractID__c': 'None', 'CreatedDate': '2023-04-05T14:23:45.000+0000'}, {'Id': '006Wt000007BFUOIA4', 'OwnerId': '005Wt000003NHpdIAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-05T10:15:30.000+0000'}, {'Id': '006Wt000007BGAIIA4', 'OwnerId': '005Wt000003NIdeIAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-11T12:45:33.000+0000'}, {'Id': '#006Wt000007BGDVIA4', 'OwnerId': '005Wt000003NBcBIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-10T11:20:45.000+0000'}, {'Id': '006Wt000007BHPhIAO', 'OwnerId': '#005Wt000003NEa3IAG', 'ContractID__c': '800Wt00000DE9ryIAD', 'CreatedDate': '2023-04-15T09:12:34.000+0000'}, {'Id': '#006Wt000007BHZNIA4', 'OwnerId': '005Wt000003NIaPIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-10T14:25:30.000+0000'}, {'Id': '#006Wt000007BHfpIAG', 'OwnerId': '005Wt000003NIqXIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-17T14:37:45.000+0000'}, {'Id': '006Wt000007BHr7IAG', 'OwnerId': '005Wt000003NIfGIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-01T09:45:23.000+0000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
