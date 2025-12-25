code = """import json, pandas as pd, os, textwrap

path = var_call_LCEjiC9uEuT5bNnYvpc8SU2q
with open(path, 'r') as f:
    articles = json.load(f)

ka_df = pd.DataFrame(articles)

quote_lines = pd.DataFrame(var_call_Cjpc7rNiGM6ghn3aQsnJZ13p)
quote_lines['Quantity'] = quote_lines['Quantity'].astype(float)
quote_lines['UnitPrice'] = quote_lines['UnitPrice'].astype(float)

violated = []

for _, row in quote_lines.iterrows():
    if row['Quantity'] > 30:
        cand = ka_df[ka_df['title'].str.contains('quantity', case=False, na=False)]
        if not cand.empty:
            violated.append(cand.iloc[0]['id'])
    if row['UnitPrice'] > 400:
        cand = ka_df[ka_df['title'].str.contains('pricing|discount|price', case=False, na=False)]
        if not cand.empty:
            violated.append(cand.iloc[0]['id'])

violated = list(dict.fromkeys(violated))
result = violated[0] if violated else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Cjpc7rNiGM6ghn3aQsnJZ13p': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_2P2vcgqg4McEZlcMPrec0oc8': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_vDEqzknefPewZ05XWWNi8lsw': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_LCEjiC9uEuT5bNnYvpc8SU2q': 'file_storage/call_LCEjiC9uEuT5bNnYvpc8SU2q.json'}

exec(code, env_args)
