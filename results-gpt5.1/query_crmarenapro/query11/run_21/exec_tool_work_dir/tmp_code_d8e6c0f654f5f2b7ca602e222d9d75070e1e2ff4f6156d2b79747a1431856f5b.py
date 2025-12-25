code = """import json, pandas as pd
opps = pd.DataFrame(var_call_B9cLlKmkYBLQfwvhsy3oXsNK)
cutoff = '2021-06-15'
rel = opps[opps['CloseDate']>=cutoff].copy()
rel['CloseDate']=pd.to_datetime(rel['CloseDate'])
rel = rel.sort_values('CloseDate').iloc[0]
opp_id = rel['Id'].replace('#','')
oli_path = var_call_nwVT1syf4Uy2vwxEJR3GXQ3b
olis = pd.read_json(oli_path)
olis['OpportunityId_clean']=olis['OpportunityId'].str.replace('#','')
match = olis[olis['OpportunityId_clean']==opp_id].head(1)
prod_id = None
if not match.empty:
    prod_id = match.iloc[0]['Product2Id']
    if isinstance(prod_id,str):
        prod_id = prod_id.replace('#','')
result = json.dumps(prod_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_B9cLlKmkYBLQfwvhsy3oXsNK': [{'Id': '#006Wt000007BIjxIAG', 'ContactId': '#003Wt00000Jqy8SIAR', 'CloseDate': '2023-12-15'}, {'Id': '006Wt000007BInBIAW', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2022-06-20'}, {'Id': '006Wt000007BBx1IAG', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-11-01'}, {'Id': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'Id': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}], 'var_call_xymCIbe222PMTvXEgxGhfPeZ': [], 'var_call_GUwlfkMnWxecWirVcDw9kXH6': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_nwVT1syf4Uy2vwxEJR3GXQ3b': 'file_storage/call_nwVT1syf4Uy2vwxEJR3GXQ3b.json'}

exec(code, env_args)
