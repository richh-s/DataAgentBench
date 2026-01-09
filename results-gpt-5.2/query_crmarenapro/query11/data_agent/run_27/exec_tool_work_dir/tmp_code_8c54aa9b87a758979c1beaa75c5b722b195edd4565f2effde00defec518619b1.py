code = """import json, pandas as pd

df = pd.DataFrame(var_call_51umr2IGOmTTwLri0JvjYwE8)
prod = pd.DataFrame(var_call_DOUEAvKJ2iWOAhPYNQJdP9h3)

df['Product2Id_clean'] = df['Product2Id'].astype(str).str.replace('#','', regex=False).str.strip()
prod['ProductId_clean'] = prod['ProductId'].astype(str).str.replace('#','', regex=False).str.strip()

m = df.merge(prod, left_on='Product2Id_clean', right_on='ProductId_clean', how='left')
# pick product matching AI processing unit intent: contains 'ai' in name/desc
m['text'] = (m['ProductName'].fillna('') + ' ' + m['Description'].fillna('')).str.lower()
ai = m[m['text'].str.contains('ai')]
# choose first deterministic by Product2Id_clean
ans = None
if len(ai)>0:
    ans = ai.sort_values(['CloseDate','OpportunityId','Product2Id_clean']).iloc[0]['Product2Id_clean']

print('__RESULT__:')
print(json.dumps({'product_id': ans}))"""

env_args = {'var_call_xfXJk0DpEO0CM5B7yYy2ba0A': [], 'var_call_51umr2IGOmTTwLri0JvjYwE8': [{'Product2Id': '#01tWt000006hV8LIAU', 'CloseDate': '2021-06-15', 'OpportunityId': '006Wt000007B0g2IAC'}, {'Product2Id': '#01tWt000006hV58IAE', 'CloseDate': '2021-06-15', 'OpportunityId': '006Wt000007B0g2IAC'}, {'Product2Id': '01tWt000006hTUkIAM', 'CloseDate': '2021-06-15', 'OpportunityId': '006Wt000007B7TcIAK'}, {'Product2Id': '01tWt000006hV8LIAU', 'CloseDate': '2021-06-15', 'OpportunityId': '006Wt000007B7TcIAK'}, {'Product2Id': '01tWt000006hV9xIAE', 'CloseDate': '2021-06-15', 'OpportunityId': '006Wt000007B0g2IAC'}, {'Product2Id': '01tWt000006hVczIAE', 'CloseDate': '2021-06-15', 'OpportunityId': '006Wt000007B0g2IAC'}], 'var_call_DOUEAvKJ2iWOAhPYNQJdP9h3': [{'ProductId': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer', 'Description': 'Cloud-based design collaboration tool enhancing team productivity across global projects.'}, {'ProductId': '#01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite', 'Description': 'Comprehensive security and compliance modules with integrated data protection features.'}, {'ProductId': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.'}, {'ProductId': '#01tWt000006hV9xIAE', 'ProductName': 'OptiPower Manager', 'Description': 'Enhanced power optimization tools for sustainable electronics development.'}, {'ProductId': '01tWt000006hVczIAE', 'ProductName': 'CollabDesign Studio', 'Description': 'Enhanced design collaboration platform offering real-time editing and feedback.'}]}

exec(code, env_args)
