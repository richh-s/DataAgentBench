code = """import json, pandas as pd
oli = pd.DataFrame(var_call_tUEvAeA1m7pgK59zOwP7iLqo)
prod = pd.DataFrame(var_call_kXkU17gNSQgmvzllR1C8jJ7a)
oli['Product2Id_clean']=oli['Product2Id'].str.replace('#','', regex=False)
prod['Id_clean']=prod['Id'].str.replace('#','', regex=False)
merged=oli.merge(prod, left_on='Product2Id_clean', right_on='Id_clean', how='left')
# choose AI processing unit: interpret as AI product among purchased; pick one with AI in name/description
merged['is_ai']=merged['Name'].str.contains('AI', case=False, na=False) | merged['Description'].str.contains('AI', case=False, na=False)
ai=merged[merged['is_ai']].copy()
# pick first unique product id
pid = None
if len(ai)>0:
    pid = ai.iloc[0]['Product2Id_clean']
result = json.dumps(pid)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_3FCKXnnG1w2grGblYJkUdZDr': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'CreatedDate': '2021-03-01T10:15:30.000+0000'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'CreatedDate': '2021-03-15T10:27:45.000+0000'}, {'Id': '006Wt000007BBx1IAG', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-11-01', 'CreatedDate': '2021-03-05T09:47:23.000+0000'}, {'Id': '#006Wt000007BIjxIAG', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '#003Wt00000Jqy8SIAR', 'CloseDate': '2023-12-15', 'CreatedDate': '2021-04-10T11:15:45.000+0000'}, {'Id': '006Wt000007BInBIAW', 'AccountId': '#001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2022-06-20', 'CreatedDate': '2021-04-15T14:22:35.000+0000'}], 'var_call_tUEvAeA1m7pgK59zOwP7iLqo': [{'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '01tWt000006hV9xIAE'}], 'var_call_6VxeraQUSxgIDT6IvtO3AVmd': [], 'var_call_kXkU17gNSQgmvzllR1C8jJ7a': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift', 'Description': 'Dynamic AI-powered design tool shifting paradigms in circuit creation.'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager', 'Description': 'Enhanced power optimization tools for sustainable electronics development.'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision', 'Description': 'AI-powered optical design tool for developing efficient light-based components.'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite', 'Description': 'Robust training platform for mastering EDA tools with hands-on labs.'}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro', 'Description': 'AI-enhanced design tool for seamless circuit synchronization and development.'}, {'Id': '#01tWt000006hVY9IAM', 'Name': 'EduFlow Academy', 'Description': 'All-inclusive training platform for EDA tools with interactive learning modules.'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator', 'Description': 'AI-enhanced circuit design tool for innovative electronic development.'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub', 'Description': 'Innovative training platform offering advanced EDA courses and certifications.'}, {'Id': '01tWt000006hVmfIAE', 'Name': 'EduTech Advance', 'Description': 'Advanced educational platform providing expert training in modern EDA tools.'}, {'Id': '01tWt000006hVt7IAE', 'Name': 'PCB EcoModel  ', 'Description': 'Eco-conscious PCB design platform focusing on sustainable materials.'}]}

exec(code, env_args)
