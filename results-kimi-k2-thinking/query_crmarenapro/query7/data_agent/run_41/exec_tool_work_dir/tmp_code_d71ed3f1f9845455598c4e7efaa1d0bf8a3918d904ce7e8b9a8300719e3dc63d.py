code = """import json

# Check the query results
knowledge_data_key = 'var_functions.query_db:8'
# If the result is too large, it might be a file path. Let's check the actual value.
# Get the actual data - it might be a string path
knowledge_data = locals().get('var_functions.query_db:8', '[]')

# Check if it's a file path (string) or actual data
if isinstance(knowledge_data, str) and knowledge_data.endswith('.json'):
    with open(knowledge_data, 'r') as f:
        knowledge_articles = json.load(f)
elif isinstance(knowledge_data, list):
    knowledge_articles = knowledge_data
else:
    knowledge_articles = []

# Look for knowledge articles about policy, SLA, agent behavior
policy_keywords = ['policy', 'sla', 'agreement', 'breach', 'violation', 'agent behavior', 'response time']
matching_articles = []

for article in knowledge_articles:
    title = article.get('title', '').lower()
    answer = article.get('faq_answer__c', '').lower()
    summary = article.get('summary', '').lower()
    
    content = title + ' ' + answer + ' ' + summary
    
    if any(keyword in content for keyword in policy_keywords):
        # Store full article for inspection
        matching_articles.append(article)

print(f"Found {len(matching_articles)} potential policy-related articles")
if matching_articles:
    for article in matching_articles:
        print(f"ID: {article['id']}, Title: {article['title']}")"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_functions.query_db:5': [], 'var_functions.query_db:7': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'id': 'a04Wt00000535bOIAQ', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Owner Assignment'}]}

exec(code, env_args)
