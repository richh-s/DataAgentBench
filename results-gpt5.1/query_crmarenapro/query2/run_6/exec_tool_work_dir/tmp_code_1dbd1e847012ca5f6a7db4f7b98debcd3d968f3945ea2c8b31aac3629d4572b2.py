code = """import json, pandas as pd, os
kp = var_call_7axxrKHfclt9rlTFaoAfMcdi
data = json.load(open(kp)) if isinstance(kp, str) and os.path.exists(kp) else var_call_7axxrKHfclt9rlTFaoAfMcdi
df = pd.DataFrame(data)
mask = df['title'].str.contains('Quote Approval Policy', case=False, na=False) | df['summary'].str.contains('quote', case=False, na=False) | df['summary'].str.contains('discount', case=False, na=False) | df['summary'].str.contains('pricing', case=False, na=False)
relevant = df[mask][['id','title','summary']]
result = relevant.to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jRfpS3Cu7FR4uVof7NfwltGv': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_cmXwdK12qvZ82ErybBUTlQUm': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_7axxrKHfclt9rlTFaoAfMcdi': 'file_storage/call_7axxrKHfclt9rlTFaoAfMcdi.json'}

exec(code, env_args)
