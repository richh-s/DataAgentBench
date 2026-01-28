code = """import json
import re

# Load case data
case_data = [
    {
        "id": "#500Wt00000DDyznIAD",
        "priority": "High",
        "subject": "Scalability Problems ",
        "description": "I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.",
        "status": "Waiting on Customer",
        "contactid": "003Wt00000JqoiZIAR",
        "createddate": "2022-09-22T19:28:00.000+0000",
        "closeddate": "None",
        "orderitemid__c": "802Wt000007928FIAQ",
        "issueid__c": "#a03Wt00000JqxtvIAB",
        "accountid": "001Wt00000PGaZCIA1",
        "ownerid": "005Wt000003NHsrIAG"
    }
]

# Check if description contains competitor mentions
competitor_mentions = []
description = case_data[0]['description']

# List of competitor-related keywords from knowledge articles
competitor_keywords = [
    'quantum', 'adaptive design', 'nanodesign', 'ai chip', 'circuitwave',
    'flexeda', 'qpcb', 'modeler', 'quantumpcb', 'nano', 'adaptive'
]

description_lower = description.lower()
for keyword in competitor_keywords:
    if keyword in description_lower:
        competitor_mentions.append(keyword)

print('__RESULT__:')
print(json.dumps({
    'case_id': case_data[0]['id'],
    'description': description,
    'competitor_mentions': competitor_mentions,
    'potential_breach': len(competitor_mentions) > 0
}))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [], 'var_functions.query_db:14': [], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
