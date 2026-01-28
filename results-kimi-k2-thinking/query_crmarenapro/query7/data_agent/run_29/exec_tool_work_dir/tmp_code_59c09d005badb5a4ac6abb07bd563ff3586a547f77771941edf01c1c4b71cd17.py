code = """import json

# Get the stored results
case_result = locals()['var_functions.query_db:2']
issue_result = locals()['var_functions.query_db:6']
knowledge_result = locals()['var_functions.query_db:8']

# Load knowledge articles if it's a file path
if isinstance(knowledge_result, str) and knowledge_result.endswith('.json'):
    with open(knowledge_result, 'r') as f:
        knowledge_articles = json.load(f)
else:
    knowledge_articles = knowledge_result

# Look for knowledge article that defines breach conditions
breach_article_id = None
for article in knowledge_articles:
    article_text = (article.get('faq_answer__c', '') + ' ' + article.get('summary', '')).lower()
    if 'scalability enhancement package' in article_text and \
       '30 days after the purchase date' in article_text and \
       'validity period of 365 days' in article_text:
        breach_article_id = article.get('id')
        break

print("__RESULT__:")
print(json.dumps(breach_article_id))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_functions.query_db:4': [], 'var_functions.query_db:6': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
