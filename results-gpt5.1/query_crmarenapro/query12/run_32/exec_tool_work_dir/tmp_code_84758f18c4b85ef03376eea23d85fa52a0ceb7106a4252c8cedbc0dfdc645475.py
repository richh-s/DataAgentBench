code = """import pandas as pd, json
opps = pd.DataFrame(var_call_pf8jOqfoLfNR92SaRdgTTKkY)
if opps.empty:
    result = None
else:
    opps['OppCreatedDate'] = pd.to_datetime(opps['OppCreatedDate'])
    opps['CompanySignedDate'] = pd.to_datetime(opps['CompanySignedDate'])
    opps['cycle_days'] = (opps['CompanySignedDate'] - opps['OppCreatedDate']).dt.days
    opps['AgentId_clean'] = opps['AgentId'].str.replace('#','', regex=False)
    grouped = opps.groupby('AgentId_clean')['cycle_days'].mean().reset_index()
    fastest = grouped.sort_values('cycle_days').iloc[0]['AgentId_clean']
    result = fastest
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_pf8jOqfoLfNR92SaRdgTTKkY': [{'AgentId': '005Wt000003NJgAIAW', 'OpportunityId': '#006Wt000007BChmIAG', 'OppCreatedDate': '2023-04-25T10:45:30.000+0000', 'CompanySignedDate': '2023-06-13'}, {'AgentId': '005Wt000003NISMIA4', 'OpportunityId': '006Wt000007BDApIAO', 'OppCreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'AgentId': '#005Wt000003NEa3IAG', 'OpportunityId': '006Wt000007BHPhIAO', 'OppCreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}], 'var_call_mPFRsAYF4dXkguAIfY7ChFgE': [{'AgentId': '005Wt000003NJBVIA4'}, {'AgentId': '#005Wt000003NBcBIAW'}, {'AgentId': '005Wt000003NInKIAW'}, {'AgentId': '005Wt000003NDEBIA4'}, {'AgentId': '005Wt000003NIovIAG'}, {'AgentId': '#005Wt000003NEdJIAW'}, {'AgentId': '#005Wt000003NJjNIAW'}, {'AgentId': '005Wt000003NHpdIAG'}, {'AgentId': '005Wt000003NJ1pIAG'}, {'AgentId': '005Wt000003NJgAIAW'}, {'AgentId': '005Wt000003NIaPIAW'}, {'AgentId': '005Wt000003NIqXIAW'}, {'AgentId': '#005Wt000003NEa3IAG'}, {'AgentId': '#005Wt000003NJMnIAO'}, {'AgentId': '#005Wt000003NFhPIAW'}, {'AgentId': '005Wt000003NIdeIAG'}, {'AgentId': '#005Wt000003NBylIAG'}, {'AgentId': '005Wt000003NJZhIAO'}, {'AgentId': '005Wt000003NISMIA4'}, {'AgentId': '005Wt000003NJxtIAG'}, {'AgentId': '005Wt000003NJ0EIAW'}, {'AgentId': '005Wt000003NFRKIA4'}, {'AgentId': '005Wt000003NIfGIAW'}, {'AgentId': '005Wt000003NEtPIAW'}, {'AgentId': '005Wt000003NIAbIAO'}, {'AgentId': '005Wt000003NIs9IAG'}, {'AgentId': '005Wt000003NF9WIAW'}, {'AgentId': '005Wt000003NBcBIAW'}]}

exec(code, env_args)
