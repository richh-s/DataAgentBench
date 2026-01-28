code = """import json

# Read the knowledge articles
try:
    with open(locals()['var_functions.query_db:4'], 'r') as f:
        knowledge_articles = json.load(f)
except:
    knowledge_articles = locals().get('var_functions.query_db:4', [])

# Look for policy-related articles
policy_related = []
for article in knowledge_articles:
    title = article.get('title', '').lower()
    summary = article.get('summary', '').lower()
    faq = article.get('faq_answer__c', '').lower()
    
    # Check for policy-related keywords
    keywords = ['policy', 'breach', 'violation', 'competitor', 'confidential', 'disclosure', 'acceptable use', 'security policy']
    if any(keyword in title or keyword in summary or keyword in faq for keyword in keywords):
        policy_related.append({
            'id': article.get('id'),
            'title': article.get('title'),
            'summary': article.get('summary')[:200] + '...' if article.get('summary') else ''
        })

print("__RESULT__:")
print(json.dumps(policy_related[:20]))  # Return first 20 matches"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_functions.execute_python:10': {'case_description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'issue_description': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.', 'knowledge_articles_count': 194}}

exec(code, env_args)
