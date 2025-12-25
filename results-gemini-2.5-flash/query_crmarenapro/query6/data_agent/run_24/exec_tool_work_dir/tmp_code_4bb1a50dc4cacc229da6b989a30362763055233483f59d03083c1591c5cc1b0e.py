code = """import json
import pandas as pd

with open(locals()['var_function-call-18017907217083951603'], 'r') as f:
    knowledge_articles = json.load(f)

df_articles = pd.DataFrame(knowledge_articles)

# Search for keywords related to 'invalid config', 'price', 'quantity', 'discount', 'regulation', 'policy'
relevant_articles = df_articles[df_articles['faq_answer__c'].str.contains('invalid|regulation|policy|price|quantity|discount', case=False, na=False) | 
                                df_articles['summary'].str.contains('invalid|regulation|policy|price|quantity|discount', case=False, na=False)]

# Look for articles related to discounts, specifically if there is a discount value of 15.0 in the quote line item and if there are policies regarding discount rates.
discount_articles = relevant_articles[relevant_articles['faq_answer__c'].str.contains('discount', case=False, na=False) | 
                                      relevant_articles['summary'].str.contains('discount', case=False, na=False)]

if not discount_articles.empty:
    # If articles related to discount are found, check if they mention specific discount percentages or conditions
    # For now, let's assume we are looking for a general discount policy violation.
    # If there are multiple, we might need more specific criteria to pick one.
    # Let's return the ID of the first relevant article for now.
    result_id = discount_articles['id'].iloc[0]
else:
    # If no specific discount articles, look for general invalid config/policy articles.
    if not relevant_articles.empty:
        result_id = relevant_articles['id'].iloc[0]
    else:
        result_id = "No relevant article found."

print('__RESULT__:')
print(json.dumps(result_id))"""

env_args = {'var_function-call-10813265146709863551': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-13563332919546654427': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-18017907217083951603': 'file_storage/function-call-18017907217083951603.json'}

exec(code, env_args)
