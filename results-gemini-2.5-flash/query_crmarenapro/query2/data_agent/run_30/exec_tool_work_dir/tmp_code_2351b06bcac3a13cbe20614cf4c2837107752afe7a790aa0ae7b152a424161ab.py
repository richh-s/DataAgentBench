code = """import pandas as pd
import json

knowledge_articles_path = locals()['var_function-call-13050873656842667550']
with open(knowledge_articles_path, 'r') as f:
    knowledge_articles = json.load(f)

df_articles = pd.DataFrame(knowledge_articles)

# Keywords to look for in knowledge articles related to quote compliance
keywords = ['policy', 'approval', 'discount', 'pricing', 'cost', 'setup', 'compliance']

conflicting_articles = []

for index, row in df_articles.iterrows():
    content = str(row['faq_answer__c']) + " " + str(row['summary'])
    content = content.lower()
    
    if any(keyword in content for keyword in keywords):
        conflicting_articles.append(row['id'])

if conflicting_articles:
    # Filter for unique IDs and clean them if necessary (e.g., remove '#')
    cleaned_articles = [article.replace('#', '') for article in set(conflicting_articles)]
    print('__RESULT__:')
    print(json.dumps(cleaned_articles[0] if cleaned_articles else None))
else:
    print('__RESULT__:')
    print(json.dumps(None))"""

env_args = {'var_function-call-4228969629798834237': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-5067393010194402960': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_function-call-1776677460422211927': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-13050873656842667550': 'file_storage/function-call-13050873656842667550.json'}

exec(code, env_args)
