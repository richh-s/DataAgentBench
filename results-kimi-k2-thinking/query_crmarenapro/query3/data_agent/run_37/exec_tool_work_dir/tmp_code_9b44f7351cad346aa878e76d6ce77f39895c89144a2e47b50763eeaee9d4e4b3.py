code = """# Examine the opportunity and tasks data to determine correct stage
oppty = var_functions.query_db:0
tasks = var_functions.query_db:2

print("Opportunity details:")
print(f"Current Stage: {oppty[0]['StageName']}")
print(f"Probability: {oppty[0]['Probability']}%")
print(f"Close Date: {oppty[0]['CloseDate']}")
print(f"Amount: ${oppty[0]['Amount']}")

print("\nTasks on opportunity:")
for t in tasks:
    print(f"- {t['Subject']}: {t['Status']}, Priority: {t['Priority']}, Due: {t['ActivityDate']}")
    if t['Description']:
        print(f"  Description: {t['Description']}")

# Determine if stage is accurate
print("\n=== ANALYSIS ===")
print("Current stage: Discovery")
print("Tasks present:")

proposal_related = 0
negotiation_related = 0
contract_related = 0
discovery_related = 0

for t in tasks:
    subject_lower = t['Subject'].lower()
    desc_lower = t['Description'].lower() if t['Description'] else ""
    
    if 'proposal' in subject_lower or 'proposal' in desc_lower:
        proposal_related += 1
    if 'negotiation' in subject_lower or 'negotiation' in desc_lower:
        negotiation_related += 1
    if 'contract' in subject_lower or 'contract' in desc_lower:
        contract_related += 1
    if 'demo' in subject_lower or 'case studies' in subject_lower:
        discovery_related += 1

print(f"- Proposal-related tasks: {proposal_related}")
print(f"- Negotiation-related tasks: {negotiation_related}")
print(f"- Contract-related tasks: {contract_related}")
print(f"- Discovery-related tasks: {discovery_related}")

print("\n=== CONCLUSION ===")
print("Based on tasks indicating proposal preparation (In Progress), negotiation meetings,")
print("and contract preparation, this opportunity appears to be beyond the Discovery stage.")
print("No quotes found in database, but tasks suggest Negotiation is more appropriate.")

result = "Negotiation"
print("__RESULT__:")
print(result)"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'Probability': '85.0', 'Amount': '61666.225', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20'}], 'var_functions.query_db:2': [{'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started', 'ActivityDate': '2022-02-20', 'Subject': 'Prepare contract for approval   ', 'Description': 'Draft the final contract for review and signature'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NIx1IAG', 'Priority': 'Low', 'Status': 'Not Started', 'ActivityDate': '2022-01-18', 'Subject': 'Send case studies', 'Description': 'Provide case studies and testimonials to reinforce the value proposition'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}, {'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'Normal', 'Status': 'In Progress', 'ActivityDate': '2022-01-10', 'Subject': 'Prepare tailored proposal', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives"}], 'var_functions.query_db:5': []}

exec(code, env_args)
