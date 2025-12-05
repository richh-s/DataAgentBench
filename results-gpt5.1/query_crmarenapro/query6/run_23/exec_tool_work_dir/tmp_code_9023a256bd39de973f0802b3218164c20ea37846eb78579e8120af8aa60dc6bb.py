code = """import json
import pandas as pd

qli = pd.DataFrame(var_call_nMxkWCr8vXuXIVja4DhihPVa)
products_path = var_call_NfqcyFsnhJFLl7k4sxyetmx2
with open(products_path, 'r') as f:
    products = json.load(f)
prod_df = pd.DataFrame(products)

qli['Product2Id_clean'] = qli['Product2Id'].str.replace('#','', regex=False)
prod_df['Id_clean'] = prod_df['Id'].str.replace('#','', regex=False)
merged = qli.merge(prod_df, left_on='Product2Id_clean', right_on='Id_clean', how='left')

ka_path = var_call_ZqCoX3MaP70iublfwNtRy6bb
with open(ka_path, 'r') as f:
    kas = json.load(f)
ka_df = pd.DataFrame(kas)

text = '\n'.join(ka_df['title'].fillna('') + ' ' + ka_df['summary'].fillna('') + ' ' + ka_df['faq_answer__c'].fillna(''))

invalid = []
for _, row in merged.iterrows():
    qty = float(row['Quantity'])
    price = float(row['UnitPrice'])
    name = str(row['Name']).strip() if 'Name' in row else ''
    prodname = str(row['Name_y']).strip() if 'Name_y' in row else ''
    if qty > 30 or price < 300:
        invalid.append({'Product2Id': row['Product2Id_clean'], 'Quantity': qty, 'UnitPrice': price})

# naive rule: assume there is an article mentioning volume discounts or minimum price per unit
ka_df['blob'] = (ka_df['title'].fillna('') + ' ' + ka_df['summary'].fillna('') + ' ' + ka_df['faq_answer__c'].fillna('')).str.lower()

candidates = ka_df[ka_df['blob'].str.contains('discount') | ka_df['blob'].str.contains('volume pricing') | ka_df['blob'].str.contains('minimum unit price')]

result_id = None
if not candidates.empty and invalid:
    result_id = candidates.iloc[0]['id']

if result_id is None:
    result_id = ''

out = json.dumps(result_id)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_nMxkWCr8vXuXIVja4DhihPVa': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_HXPLgIvaThiuB22pMoV44jrm': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_ZqCoX3MaP70iublfwNtRy6bb': 'file_storage/call_ZqCoX3MaP70iublfwNtRy6bb.json', 'var_call_NfqcyFsnhJFLl7k4sxyetmx2': 'file_storage/call_NfqcyFsnhJFLl7k4sxyetmx2.json'}

exec(code, env_args)
