code = """import json

# Access stored variables by reading from the actual variable names
# The variables are stored as locals()['var_functions.query_db:8'] etc.

# For the scalability articles
scalability_key = 'var_functions.query_db:8'
scalability_result = locals()[scalability_key] if scalability_key in locals() else []

# For the policy/procedure articles
policy_key = 'var_functions.query_db:16'
policy_result = locals()[policy_key] if policy_key in locals() else []

# Load scalability articles
if isinstance(scalability_result, str) and scalability_result.endswith('.json'):
    with open(scalability_result, 'r') as f:
        scalability_articles = json.load(f)
else:
    scalability_articles = scalability_result if isinstance(scalability_result, list) else []

# Load policy articles
if isinstance(policy_result, str) and policy_result.endswith('.json'):
    with open(policy_result, 'r') as f:
        policy_articles = json.load(f)
else:
    policy_articles = policy_result if isinstance(policy_result, list) else []

# Get case info
case_key = 'var_functions.query_db:2'
case_result = locals()[case_key] if case_key in locals() else []
case_info = case_result[0] if case_result else None

# Analyze relevant policy articles
relevant_policies = []
if case_info and case_info.get('status') == 'Waiting on Customer':
    # Case is waiting on customer - check if agent should have responded or closed
    for article in policy_articles:
        article_id = article.get('id', '')
        title = article.get('title', '').lower()
        content = article.get('faq_answer__c', '').lower()
        
        # Look for policies about case handling, SLA, waiting on customer, case closure
        policy_keywords = ['case handling', 'support process', 'sla', 'response time', 'case closure', 'waiting on customer', 'escalation']
        if any(keyword in title or keyword in content for keyword in policy_keywords):
            relevant_policies.append(article_id)

# Return result
policy_id = relevant_policies[0] if relevant_policies else None

print('__RESULT__:')
print(json.dumps(policy_id))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_functions.query_db:5': [], 'var_functions.query_db:7': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [], 'var_functions.query_db:12': [], 'var_functions.query_db:14': [], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
