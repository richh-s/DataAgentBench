code = """import json
import pandas as pd

# Get the results from previous queries
# Access via locals() dictionary
locals_dict = locals()
opportunity_key = 'var_functions.query_db:5'
order_key = 'var_functions.query_db:7'

if opportunity_key in locals_dict:
    opportunity_data = locals_dict[opportunity_key]
else:
    opportunity_data = []

if order_key in locals_dict:
    order_data = locals_dict[order_key]
else:
    order_data = []

# Check if data exists
if not opportunity_data or not order_data:
    result = {"error": "Missing required data"}
else:
    # Parse opportunity data (handle both dict and string formats)
    if isinstance(opportunity_data, str):
        try:
            with open(opportunity_data, 'r') as f:
                opportunity_data = json.load(f)
        except:
            pass
    
    if isinstance(order_data, str):
        try:
            with open(order_data, 'r') as f:
                order_data = json.load(f)
        except:
            pass
    
    # Convert to DataFrames
    df_opportunity = pd.DataFrame(opportunity_data)
    df_orders = pd.DataFrame(order_data)
    
    # Clean data - remove leading # from IDs and convert numeric fields
    df_opportunity['OwnerId'] = df_opportunity['OwnerId'].astype(str).str.replace('#', '', regex=False)
    df_opportunity['TotalPrice'] = pd.to_numeric(df_opportunity['TotalPrice'], errors='coerce')
    
    # Calculate sales by agent from opportunities
    agent_sales_opportunity = df_opportunity.groupby('OwnerId')['TotalPrice'].sum().dropna().reset_index()
    
    # Process order data
    df_orders['OwnerId'] = df_orders['OwnerId'].astype(str).str.replace('#', '', regex=False)
    df_orders['Quantity'] = pd.to_numeric(df_orders['Quantity'], errors='coerce')
    df_orders['UnitPrice'] = pd.to_numeric(df_orders['UnitPrice'], errors='coerce')
    
    # Calculate sales from orders (Quantity * UnitPrice)
    df_orders['SalesAmount'] = df_orders['Quantity'] * df_orders['UnitPrice']
    agent_sales_orders = df_orders.groupby('OwnerId')['SalesAmount'].sum().dropna().reset_index()
    
    # Combine results
    combined_sales = {}
    
    # Add opportunity sales
    for _, row in agent_sales_opportunity.iterrows():
        if pd.notna(row['TotalPrice']) and row['TotalPrice'] > 0:
            owner_id = str(row['OwnerId']).strip()
            combined_sales[owner_id] = combined_sales.get(owner_id, 0) + float(row['TotalPrice'])
    
    # Add order sales
    for _, row in agent_sales_orders.iterrows():
        if pd.notna(row['SalesAmount']) and row['SalesAmount'] > 0:
            owner_id = str(row['OwnerId']).strip()
            combined_sales[owner_id] = combined_sales.get(owner_id, 0) + float(row['SalesAmount'])
    
    # Find top agent
    if combined_sales:
        top_agent = max(combined_sales.items(), key=lambda x: x[1])
        result = {"top_agent_id": top_agent[0]}
    else:
        result = {"error": "No sales data found"}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [{'ContractId': '800Wt00000DDe3OIAT', 'CompanySignedDate': '2022-09-20', 'OpportunityId': '#006Wt000007B5bTIAS', 'OwnerId': '005Wt000003NJ53IAG', 'AccountId': '001Wt00000PGYx5IAH'}, {'ContractId': '800Wt00000DE2vLIAT', 'CompanySignedDate': '2022-06-29', 'OpportunityId': '006Wt000007B6u8IAC', 'OwnerId': '005Wt000003NEa3IAG', 'AccountId': '001Wt00000PGovMIAT'}, {'ContractId': '800Wt00000DE0FHIA1', 'CompanySignedDate': '2022-08-02', 'OpportunityId': '006Wt000007B8PgIAK', 'OwnerId': '005Wt000003NBp4IAG', 'AccountId': '#001Wt00000PGZZoIAP'}, {'ContractId': '800Wt00000DE0TiIAL', 'CompanySignedDate': '2022-09-10', 'OpportunityId': '006Wt000007BAY1IAO', 'OwnerId': '005Wt000003NJmbIAG', 'AccountId': '001Wt00000PGZmfIAH'}, {'ContractId': '800Wt00000DDNlnIAH', 'CompanySignedDate': '2022-09-02', 'OpportunityId': '006Wt000007BBqXIAW', 'OwnerId': '005Wt000003NCegIAG', 'AccountId': '001Wt00000PGtdJIAT'}, {'ContractId': '800Wt00000DE98oIAD', 'CompanySignedDate': '2022-11-10', 'OpportunityId': '006Wt000007BBs9IAG', 'OwnerId': '005Wt000003NGwoIAG', 'AccountId': '001Wt00000PGtdJIAT'}, {'ContractId': '800Wt00000DE9GrIAL', 'CompanySignedDate': '2022-06-30', 'OpportunityId': '006Wt000007BCLCIA4', 'OwnerId': '005Wt000003NGFHIA4', 'AccountId': '001Wt00000PGRnYIAX'}, {'ContractId': '800Wt00000DE9YbIAL', 'CompanySignedDate': '2022-11-22', 'OpportunityId': '#006Wt000007BEgMIAW', 'OwnerId': '005Wt000003NJmcIAG', 'AccountId': '001Wt00000PHRTfIAP'}, {'ContractId': '800Wt00000DDzZLIA1', 'CompanySignedDate': '2022-10-26', 'OpportunityId': '#006Wt000007BFaoIAG', 'OwnerId': '005Wt000003NDEBIA4', 'AccountId': '001Wt00000PHVqdIAH'}, {'ContractId': '800Wt00000DE9qLIAT', 'CompanySignedDate': '2022-09-01', 'OpportunityId': '006Wt000007BHBBIA4', 'OwnerId': '005Wt000003NBp4IAG', 'AccountId': '#001Wt00000PGzSaIAL'}, {'ContractId': '800Wt00000DDeg6IAD', 'CompanySignedDate': '2022-07-18', 'OpportunityId': '006Wt000007BHCpIAO', 'OwnerId': '005Wt000003NJkzIAG', 'AccountId': '001Wt00000PHVtpIAH'}, {'ContractId': '800Wt00000DE9rxIAD', 'CompanySignedDate': '2022-09-19', 'OpportunityId': '#006Wt000007BHJFIA4', 'OwnerId': '005Wt000003NHzJIAW', 'AccountId': '001Wt00000PHVtpIAH'}], 'var_functions.execute_python:2': {'error': "name 'var_functions' is not defined"}, 'var_functions.query_db:5': [{'OpportunityId': '006Wt000007BHCpIAO', 'OwnerId': '005Wt000003NJkzIAG', 'Quantity': '8.0', 'TotalPrice': '4559.924'}, {'OpportunityId': '006Wt000007BBs9IAG', 'OwnerId': '005Wt000003NGwoIAG', 'Quantity': '10.0', 'TotalPrice': '5399.91'}, {'OpportunityId': '006Wt000007BAY1IAO', 'OwnerId': '005Wt000003NJmbIAG', 'Quantity': '7.0', 'TotalPrice': '3524.4335'}, {'OpportunityId': '006Wt000007B8PgIAK', 'OwnerId': '005Wt000003NBp4IAG', 'Quantity': '2.0', 'TotalPrice': '1059.98'}, {'OpportunityId': '006Wt000007B8PgIAK', 'OwnerId': '005Wt000003NBp4IAG', 'Quantity': '3.0', 'TotalPrice': '1799.97'}, {'OpportunityId': '006Wt000007BBqXIAW', 'OwnerId': '005Wt000003NCegIAG', 'Quantity': '8.0', 'TotalPrice': '4559.924'}, {'OpportunityId': '006Wt000007BBs9IAG', 'OwnerId': '005Wt000003NGwoIAG', 'Quantity': '8.0', 'TotalPrice': '4179.924'}, {'OpportunityId': '006Wt000007BBqXIAW', 'OwnerId': '005Wt000003NCegIAG', 'Quantity': '10.0', 'TotalPrice': '4499.91'}, {'OpportunityId': '006Wt000007BBqXIAW', 'OwnerId': '005Wt000003NCegIAG', 'Quantity': '12.0', 'TotalPrice': '5723.892'}, {'OpportunityId': '006Wt000007BCLCIA4', 'OwnerId': '005Wt000003NGFHIA4', 'Quantity': '10.0', 'TotalPrice': '5399.91'}, {'OpportunityId': '006Wt000007B8PgIAK', 'OwnerId': '005Wt000003NBp4IAG', 'Quantity': '4.0', 'TotalPrice': '1599.96'}, {'OpportunityId': '006Wt000007BCLCIA4', 'OwnerId': '005Wt000003NGFHIA4', 'Quantity': '15.0', 'TotalPrice': '5399.865'}, {'OpportunityId': '006Wt000007BCLCIA4', 'OwnerId': '005Wt000003NGFHIA4', 'Quantity': '8.0', 'TotalPrice': '3603.932'}, {'OpportunityId': '006Wt000007B6u8IAC', 'OwnerId': '005Wt000003NEa3IAG', 'Quantity': '20.0', 'TotalPrice': '7819.83'}, {'OpportunityId': '006Wt000007B6u8IAC', 'OwnerId': '005Wt000003NEa3IAG', 'Quantity': '50.0', 'TotalPrice': '22524.575'}, {'OpportunityId': '006Wt000007B6u8IAC', 'OwnerId': '005Wt000003NEa3IAG', 'Quantity': '30.0', 'TotalPrice': '16574.745'}, {'OpportunityId': '006Wt000007BHBBIA4', 'OwnerId': '005Wt000003NBp4IAG', 'Quantity': '10.0', 'TotalPrice': '3599.91'}, {'OpportunityId': '006Wt000007BHCpIAO', 'OwnerId': '005Wt000003NJkzIAG', 'Quantity': '12.0', 'TotalPrice': '3779.892'}, {'OpportunityId': '006Wt000007B8PgIAK', 'OwnerId': '005Wt000003NBp4IAG', 'Quantity': '3.0', 'TotalPrice': '1649.97'}, {'OpportunityId': '#006Wt000007BEgMIAW', 'OwnerId': '005Wt000003NJmcIAG', 'Quantity': '6.0', 'TotalPrice': '3020.943'}, {'OpportunityId': '#006Wt000007BFaoIAG', 'OwnerId': '005Wt000003NDEBIA4', 'Quantity': '8.0', 'TotalPrice': '4559.924'}, {'OpportunityId': '006Wt000007BAY1IAO', 'OwnerId': '005Wt000003NJmbIAG', 'Quantity': '3.0', 'TotalPrice': '1709.9715'}, {'OpportunityId': '006Wt000007BHBBIA4', 'OwnerId': '005Wt000003NBp4IAG', 'Quantity': '9.0', 'TotalPrice': '4702.4145'}, {'OpportunityId': '006Wt000007BHCpIAO', 'OwnerId': '005Wt000003NJkzIAG', 'Quantity': '15.0', 'TotalPrice': '5399.865'}, {'OpportunityId': '#006Wt000007BFaoIAG', 'OwnerId': '005Wt000003NDEBIA4', 'Quantity': '10.0', 'TotalPrice': '4769.91'}], 'var_functions.query_db:7': [{'OrderId': '#801Wt00000PFt7UIAT', 'Quantity': '10.0', 'UnitPrice': '359.991', 'EffectiveDate': '2022-09-15', 'AccountId': '001Wt00000PGzSaIAL', 'OwnerId': '005Wt000003NIiUIAW'}, {'OrderId': '#801Wt00000PFt7UIAT', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-09-15', 'AccountId': '001Wt00000PGzSaIAL', 'OwnerId': '005Wt000003NIiUIAW'}, {'OrderId': '801Wt00000PFyITIA1', 'Quantity': '15.0', 'UnitPrice': '359.991', 'EffectiveDate': '2022-07-10', 'AccountId': '001Wt00000PGRnYIAX', 'OwnerId': '005Wt000003NDJ0IAO'}, {'OrderId': '801Wt00000PFyITIA1', 'Quantity': '8.0', 'UnitPrice': '503.4905', 'EffectiveDate': '2022-07-10', 'AccountId': '001Wt00000PGRnYIAX', 'OwnerId': '005Wt000003NDJ0IAO'}, {'OrderId': '801Wt00000PGGhBIAX', 'Quantity': '10.0', 'UnitPrice': '359.991', 'EffectiveDate': '2022-10-01', 'AccountId': '001Wt00000PHVtpIAH', 'OwnerId': '005Wt000003NIaRIAW'}, {'OrderId': '801Wt00000PGGhBIAX', 'Quantity': '14.0', 'UnitPrice': '476.991', 'EffectiveDate': '2022-10-01', 'AccountId': '001Wt00000PHVtpIAH', 'OwnerId': '005Wt000003NIaRIAW'}, {'OrderId': '801Wt00000PGGhBIAX', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-10-01', 'AccountId': '001Wt00000PHVtpIAH', 'OwnerId': '005Wt000003NIaRIAW'}, {'OrderId': '#801Wt00000PGbdMIAT', 'Quantity': '20.0', 'UnitPrice': '450.4915', 'EffectiveDate': '2022-07-01', 'AccountId': '#001Wt00000PGZgHIAX', 'OwnerId': '#005Wt000003NGtcIAG'}, {'OrderId': '#801Wt00000PGbdMIAT', 'Quantity': '30.0', 'UnitPrice': '390.9915', 'EffectiveDate': '2022-07-01', 'AccountId': '#001Wt00000PGZgHIAX', 'OwnerId': '#005Wt000003NGtcIAG'}, {'OrderId': '801Wt00000PH4FMIA1', 'Quantity': '10.0', 'UnitPrice': '476.991', 'EffectiveDate': '2022-09-15', 'AccountId': '#001Wt00000PGZmfIAH', 'OwnerId': '#005Wt000003NJmbIAG'}, {'OrderId': '801Wt00000PH8yvIAD', 'Quantity': '20.0', 'UnitPrice': '390.9915', 'EffectiveDate': '2022-07-01', 'AccountId': '001Wt00000PGovMIAT', 'OwnerId': '005Wt000003NIXCIA4'}, {'OrderId': '801Wt00000PH8yvIAD', 'Quantity': '30.0', 'UnitPrice': '552.4915', 'EffectiveDate': '2022-07-01', 'AccountId': '001Wt00000PGovMIAT', 'OwnerId': '005Wt000003NIXCIA4'}, {'OrderId': '801Wt00000PH8yvIAD', 'Quantity': '50.0', 'UnitPrice': '450.4915', 'EffectiveDate': '2022-07-01', 'AccountId': '001Wt00000PGovMIAT', 'OwnerId': '005Wt000003NIXCIA4'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '1.0', 'UnitPrice': '399.99', 'EffectiveDate': '2022-07-01', 'AccountId': '001Wt00000PFsjOIAT', 'OwnerId': '005Wt000003NJ9uIAG'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '3.0', 'UnitPrice': '499.99', 'EffectiveDate': '2022-07-01', 'AccountId': '001Wt00000PFsjOIAT', 'OwnerId': '005Wt000003NJ9uIAG'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '5.0', 'UnitPrice': '427.4905', 'EffectiveDate': '2022-07-01', 'AccountId': '001Wt00000PFsjOIAT', 'OwnerId': '005Wt000003NJ9uIAG'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '7.0', 'UnitPrice': '455.9905', 'EffectiveDate': '2022-07-01', 'AccountId': '001Wt00000PFsjOIAT', 'OwnerId': '005Wt000003NJ9uIAG'}, {'OrderId': '801Wt00000PHHhDIAX', 'Quantity': '12.0', 'UnitPrice': '314.991', 'EffectiveDate': '2022-08-01', 'AccountId': '#001Wt00000PHVtpIAH', 'OwnerId': '#005Wt000003NITxIAO'}, {'OrderId': '801Wt00000PHLzNIAX', 'Quantity': '10.0', 'UnitPrice': '449.991', 'EffectiveDate': '2022-09-15', 'AccountId': '001Wt00000PGtdJIAT', 'OwnerId': '005Wt000003NEoYIAW'}, {'OrderId': '801Wt00000PHLzNIAX', 'Quantity': '12.0', 'UnitPrice': '476.991', 'EffectiveDate': '2022-09-15', 'AccountId': '001Wt00000PGtdJIAT', 'OwnerId': '005Wt000003NEoYIAW'}, {'OrderId': '801Wt00000PHLzNIAX', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-09-15', 'AccountId': '001Wt00000PGtdJIAT', 'OwnerId': '005Wt000003NEoYIAW'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '16.0', 'UnitPrice': '440.991', 'EffectiveDate': '2022-07-01', 'AccountId': '001Wt00000PGdwiIAD', 'OwnerId': '#005Wt000003NIx1IAG'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '5.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-07-01', 'AccountId': '001Wt00000PGdwiIAD', 'OwnerId': '#005Wt000003NIx1IAG'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '7.0', 'UnitPrice': '379.9905', 'EffectiveDate': '2022-07-01', 'AccountId': '001Wt00000PGdwiIAD', 'OwnerId': '#005Wt000003NIx1IAG'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-07-01', 'AccountId': '001Wt00000PGdwiIAD', 'OwnerId': '#005Wt000003NIx1IAG'}, {'OrderId': '#801Wt00000PHVkDIAX', 'Quantity': '3.0', 'UnitPrice': '599.99', 'EffectiveDate': '2022-08-15', 'AccountId': '001Wt00000PGZZoIAP', 'OwnerId': '005Wt000003NJt3IAG'}, {'OrderId': '801Wt00000PHVqfIAH', 'Quantity': '10.0', 'UnitPrice': '539.991', 'EffectiveDate': '2022-09-20', 'AccountId': '#001Wt00000PGzM9IAL', 'OwnerId': '005Wt000003NDEBIA4'}, {'OrderId': '#801Wt00000PHWptIAH', 'Quantity': '2.0', 'UnitPrice': '339.99', 'EffectiveDate': '2022-09-25', 'AccountId': '#001Wt00000PGYx5IAH', 'OwnerId': '005Wt000003NJ0EIAW'}, {'OrderId': '#801Wt00000PHWptIAH', 'Quantity': '3.0', 'UnitPrice': '529.99', 'EffectiveDate': '2022-09-25', 'AccountId': '#001Wt00000PGYx5IAH', 'OwnerId': '005Wt000003NJ0EIAW'}]}

exec(code, env_args)
