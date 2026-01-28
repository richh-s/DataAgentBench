code = """# Access the file path variable
print('Available variables:', list(locals().keys()))

# Try to find the correct variable name for the knowledge articles
file_path = None
for key in locals().keys():
    if 'query_db' in key and '8' in key:
        file_path = locals()[key]
        print(f'Found variable {key} with value: {file_path}')
        break

if file_path is None:
    print('Could not find the file path variable')
else:
    import json
    
    try:
        with open(file_path, 'r') as f:
            knowledge_articles = json.load(f)
        
        print(f'Loaded {len(knowledge_articles)} articles')
        
        # Look for articles specifically about scalability policies or guidelines
        # for TechPulse/QuantumPCB
        relevant_articles = []
        
        for article in knowledge_articles:
            article_id = article.get('id', '').replace('#', '')
            title = article.get('title', '').lower()
            summary = article.get('summary', '').lower()
            faq = article.get('faq_answer__c', '').lower()
            
            # Check for scalability-related policy violations
            # The case mentions "QuantumPCB Modeler" and TechPulse Solutions
            if any(keyword in title for keyword in ['policy', 'guideline', 'violation', 'breach']):
                if any(keyword in summary or keyword in faq for keyword in ['scalability', 'performance']):
                    relevant_articles.append(article_id)
            elif any(keyword in title for keyword in ['quantumpcb', 'techpulse']):
                if any(keyword in summary or keyword in faq for keyword in ['scalability', 'performance']):
                    relevant_articles.append(article_id)
        
        print('Relevant articles:', relevant_articles)
        print('__RESULT__:')
        print(json.dumps(relevant_articles))
        
    except Exception as e:
        print(f'Error: {e}')
        print('__RESULT__:')
        print(json.dumps([]))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'id': '#500Wt00000DDyznIAD', 'priority': 'High', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt000007928FIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'id': 'a04Wt00000535bOIAQ', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537V8IAI', 'caseid__c': '500Wt00000DDyznIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'field__c': 'Owner Assignment'}]}

exec(code, env_args)
