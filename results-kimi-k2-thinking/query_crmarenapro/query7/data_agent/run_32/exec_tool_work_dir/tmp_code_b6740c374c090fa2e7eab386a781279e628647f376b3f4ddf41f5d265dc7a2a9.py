code = """import json

# Load the knowledge articles result
knowledge_result_path = var_functions.query_db_8
with open(knowledge_result_path, 'r') as f:
    knowledge_articles = json.load(f)

# The case is about QuantumPCB Modeler scalability issues
# Looking for knowledge articles that discuss policy violations related to:
# 1. Scalability issues
# 2. QuantumPCB or similar products
# 3. Policy violations

relevant_articles = []
for article in knowledge_articles:
    # Check if article contains policy-related content
    content = (article.get('title', '') + ' ' + 
               article.get('summary', '') + ' ' + 
               article.get('faq_answer__c', '')).lower()
    
    # Look for scalability mentions combined with policy/constraint/violation language
    if 'scalability' in content:
        # Check if it's about limitations or policy constraints
        if any(keyword in content for keyword in ['limitation', 'constraint', 'violation', 'policy', 'breach']):
            relevant_articles.append(article)
        # Also check if it's about competitor comparisons that might mention policy
        elif 'competitor' in article.get('title', '').lower():
            relevant_articles.append(article)

print(f"Found {len(relevant_articles)} relevant articles")
for article in relevant_articles:
    print(f"- {article['id']}: {article['title']}")"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [], 'var_functions.query_db:12': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_functions.query_db:14': [{'id': 'a04Wt00000535bOIAQ', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Owner Assignment'}]}

exec(code, env_args)
