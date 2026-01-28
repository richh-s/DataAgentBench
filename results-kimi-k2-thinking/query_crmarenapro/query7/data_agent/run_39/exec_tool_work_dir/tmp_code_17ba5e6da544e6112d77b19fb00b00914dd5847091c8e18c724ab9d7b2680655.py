code = """import json
import os

# Read the scalability-related knowledge articles
scalability_file = var_functions.query_db:8
if isinstance(scalability_file, str) and scalability_file.endswith('.json'):
    with open(scalability_file, 'r') as f:
        scalability_articles = json.load(f)
else:
    scalability_articles = var_functions.query_db:8

# Read the agent/policy/procedure-related knowledge articles  
policy_file = var_functions.query_db:16
if isinstance(policy_file, str) and policy_file.endswith('.json'):
    with open(policy_file, 'r') as f:
        policy_articles = json.load(f)
else:
    policy_articles = var_functions.query_db:16

print(f"Found {len(scalability_articles)} scalability articles")
print(f"Found {len(policy_articles)} policy/procedure articles")

# Look for articles about agent behavior, case handling, SLA, or documentation requirements
agent_policy_articles = []
for article in policy_articles:
    title = article.get('title', '').lower()
    content = article.get('faq_answer__c', '').lower()
    summary = article.get('summary', '').lower()
    
    # Check if this is about agent policies, procedures, case handling, SLA, or documentation
    if any(keyword in title or keyword in content or keyword in summary 
           for keyword in ['agent', 'procedure', 'policy', 'sla', 'documentation', 'case handling', 'support process']):
        agent_policy_articles.append(article)

print(f"Found {len(agent_policy_articles)} potential agent policy articles")

# Display relevant articles
for article in agent_policy_articles[:5]:
    print(f"\nArticle ID: {article.get('id')}")
    print(f"Title: {article.get('title')}")
    print(f"Summary: {article.get('summary', '')[:200]}...")"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_functions.query_db:5': [], 'var_functions.query_db:7': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [], 'var_functions.query_db:12': [], 'var_functions.query_db:14': [], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
