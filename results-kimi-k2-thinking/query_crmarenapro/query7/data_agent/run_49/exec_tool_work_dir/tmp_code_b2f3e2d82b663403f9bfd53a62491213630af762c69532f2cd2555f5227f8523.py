code = """import json

# Read the knowledge articles
try:
    with open(locals()['var_functions.query_db:4'], 'r') as f:
        knowledge_articles = json.load(f)
except:
    knowledge_articles = locals().get('var_functions.query_db:4', [])

# Read the case details
case_details = locals()['var_functions.query_db:2']
issue_details = locals()['var_functions.query_db:8']

print("__RESULT__:")
print(json.dumps({
    "case_description": case_details[0]['description'],
    "issue_description": issue_details[0]['description__c'],
    "knowledge_articles_count": len(knowledge_articles)
}))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}]}

exec(code, env_args)
