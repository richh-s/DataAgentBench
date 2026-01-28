code = """# Let's read the knowledge articles results from the file
import json

# The knowledge articles result is in var_functions.query_db:12
knowledge_file = var_functions.query_db:12

# Read the file
with open(knowledge_file, 'r') as f:
    knowledge_articles = json.load(f)

# Print the titles to see what's relevant
print('__RESULT__:')
print(json.dumps([{
    'id': article.get('id'),
    'title': article.get('title'),
    'summary': article.get('summary', '')[:200]
} for article in knowledge_articles[:10]]))"""

env_args = {'var_functions.query_db:2': [], 'var_functions.query_db:5': [{'id': 'a04Wt00000535bOIAQ', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_functions.query_db:9': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_functions.query_db:8': [], 'var_functions.query_db:10': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [], 'var_functions.query_db:19': []}

exec(code, env_args)
