code = """import json
import re

# Case data
case_data = [
    {"id": "#500Wt00000DDyznIAD", "priority": "High", "subject": "Scalability Problems ", "description": "I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.", "status": "Waiting on Customer", "contactid": "003Wt00000JqoiZIAR", "createddate": "2022-09-22T19:28:00.000+0000", "closeddate": "None", "orderitemid__c": "802Wt000007928FIAQ", "issueid__c": "a03Wt00000JqxtvIAB", "accountid": "001Wt00000PGaZCIA1", "ownerid": "005Wt000003NHsrIAG"}
]

# Issue data
issue_data = [
    {"id": "#a03Wt00000JqxtvIAB", "name": "Scalability Issue", "description__c": "Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts."}
]

# Load knowledge articles from files
with open('/tmp/tmp7y1x7z2v.json', 'r') as f:
    knowledge_scalability = json.load(f)

with open('/tmp/tmpg2q8r8v6.json', 'r') as f:
    knowledge_quantum = json.load(f)

with open('/tmp/tmpi6p9d6i3.json', 'r') as f:
    knowledge_policy = json.load(f)

print("Case data loaded successfully")
print("Issue data loaded successfully")
print(f"Knowledge articles - Scalability: {len(knowledge_scalability)}, Quantum: {len(knowledge_quantum)}, Policy: {len(knowledge_policy)}")

# Analyze the case
# The case subject mentions "Scalability Problems" with "QuantumPCB Modeler"
# The issue is "Scalability Issue" affecting TechPulse solutions

# Check if there are any policy articles that specifically mention limitations or known issues
# with QuantumPCB Modeler that would constitute a policy violation

has_policy_violation = False
policy_article_id = None

# Look through quantum articles for any mention of limitations or policies
for article in knowledge_quantum:
    id_clean = article.get('id', '').replace('#', '')
    title = article.get('title', '').lower()
    summary = article.get('summary', '').lower()
    content = article.get('faq_answer__c', '').lower()
    
    # Check if article mentions limitations, known issues, or policies
    if 'limitation' in title or 'limitation' in summary or 'limitation' in content:
        has_policy_violation = True
        policy_article_id = article.get('id', '')
        break
    if 'known issue' in title or 'known issue' in summary or 'known issue' in content:
        has_policy_violation = True
        policy_article_id = article.get('id', '')
        break
    if 'policy' in title or 'policy' in summary or 'policy' in content:
        has_policy_violation = True
        policy_article_id = article.get('id', '')
        break

# Check policy articles specifically
for article in knowledge_policy:
    id_clean = article.get('id', '').replace('#', '')
    title = article.get('title', '').lower()
    summary = article.get('summary', '').lower()
    content = article.get('faq_answer__c', '').lower()
    
    # Look for SLA or policy violations related to support
    if 'sla' in title or 'sla' in summary or 'sla' in content:
        # Check if it's related to scalability or known issues
        if 'scalabilit' in content or 'known issue' in content or 'limitation' in content:
            has_policy_violation = True
            policy_article_id = article.get('id', '')
            break

result = {"violation": has_policy_violation, "article_id": policy_article_id}

# Print result in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_functions.query_db:5': [{'id': 'a04Wt00000535bOIAQ', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_functions.query_db:6': [], 'var_functions.query_db:10': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
