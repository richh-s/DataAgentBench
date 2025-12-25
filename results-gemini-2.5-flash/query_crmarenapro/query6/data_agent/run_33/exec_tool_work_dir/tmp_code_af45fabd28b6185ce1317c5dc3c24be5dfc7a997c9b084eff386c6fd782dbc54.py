code = """import json
import pandas as pd

# Load the full knowledge article data from the file
with open(locals()['var_function-call-1169451631084900939'], 'r') as f:
    knowledge_articles = json.load(f)

df_articles = pd.DataFrame(knowledge_articles)

# Keywords to search for in knowledge article content
keywords = ['invalid config', 'quantity regulation', 'price regulation', 'discount regulation', 'pricing rules', 'configuration error', 'pricing policy', 'minimum quantity', 'maximum quantity', 'price limit', 'discount limit', 'violation']

# Search for keywords in 'faq_answer__c' and 'summary' fields
matching_articles = []
for index, row in df_articles.iterrows():
    content = str(row['faq_answer__c']) + ' ' + str(row['summary'])
    if any(keyword in content.lower() for keyword in keywords):
        matching_articles.append(row['id'])

# Remove duplicates and print the result
result = list(set(matching_articles))

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-4198281158085155910': [{'Id': '0QLWt0000022j3GOAQ', 'Product2Id': '#01tWt000006hV6jIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'Product2Id': '#01tWt000006hPffIAE', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'Product2Id': '01tWt000006hVczIAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-1169451631084900939': 'file_storage/function-call-1169451631084900939.json'}

exec(code, env_args)
