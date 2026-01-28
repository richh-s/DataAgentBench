code = """import json

# Access the stored variables
scalability_result = locals()['var_functions.query_db:8']
policy_result = locals()['var_functions.query_db:16']

# Load the scalability articles
if isinstance(scalability_result, str) and scalability_result.endswith('.json'):
    with open(scalability_result, 'r') as f:
        scalability_articles = json.load(f)
else:
    scalability_articles = scalability_result

# Load the policy articles
if isinstance(policy_result, str) and policy_result.endswith('.json'):
    with open(policy_result, 'r') as f:
        policy_articles = json.load(f)
else:
    policy_articles = policy_result

print(f"Found {len(scalability_articles)} scalability-related articles")
print(f"Found {len(policy_articles)} policy/procedure-related articles")

# Look for articles about case handling, SLA, or documentation requirements
agent_policy_map = {}
for article in policy_articles:
    article_id = article.get('id')
    title = article.get('title', '').lower()
    content = article.get('faq_answer__c', '').lower()
    summary = article.get('summary', '').lower()
    
    # Check if this is about agent policies, case handling, SLA, or documentation
    keywords = ['agent', 'case handling', 'support process', 'sla', 'documentation', 'response time', 'escalation']
    if any(keyword in title or keyword in content or keyword in summary for keyword in keywords):
        agent_policy_map[article_id] = article

print(f"Found {len(agent_policy_map)} potential agent policy articles")

# Check case details
case_info = locals()['var_functions.query_db:2'][0]
print(f"\nCase Status: {case_info.get('status')}")
print(f"Subject: {case_info.get('subject')}")

# Check if case is waiting on customer
if case_info.get('status') == 'Waiting on Customer':
    print("\nCase is in 'Waiting on Customer' status")
    
    # Look for policy about responding to customers vs closing cases
    for article_id, article in agent_policy_map.items():
        title = article.get('title', '').lower()
        if 'waiting' in title or 'customer' in title or 'response' in title:
            print(f"\nPotential policy article: {article_id}")
            print(f"Title: {article.get('title')}")

__RESULT__:
json.dumps(list(agent_policy_map.keys()))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_functions.query_db:5': [], 'var_functions.query_db:7': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [], 'var_functions.query_db:12': [], 'var_functions.query_db:14': [], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
