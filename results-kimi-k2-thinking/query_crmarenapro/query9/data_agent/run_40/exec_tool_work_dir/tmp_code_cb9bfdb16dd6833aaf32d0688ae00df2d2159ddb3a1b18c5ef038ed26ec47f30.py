code = """import json
import pandas as pd

# Load the full case data from file
case_data_file = locals()['var_functions.query_db:10']
with open(case_data_file, 'r') as f:
    cases = json.load(f)

# Load account data directly
accounts = locals()['var_functions.query_db:12']

# Convert to DataFrames
df_cases = pd.DataFrame(cases)
df_accounts = pd.DataFrame(accounts)

# Clean up the data - remove leading # from IDs and trim whitespace
df_cases['accountid'] = df_cases['accountid'].astype(str).str.replace('#', '').str.strip()
df_accounts['Id'] = df_accounts['Id'].astype(str).str.replace('#', '').str.strip()
df_accounts['ShippingState'] = df_accounts['ShippingState'].astype(str).str.strip()

# Merge cases with accounts to get state information
df_merged = pd.merge(df_cases, df_accounts, how='left', left_on='accountid', right_on='Id')

# Convert date strings to datetime and remove timezone for easier comparison
df_merged['createddate'] = pd.to_datetime(df_merged['createddate']).dt.tz_localize(None)
df_merged['closeddate'] = pd.to_datetime(df_merged['closeddate']).dt.tz_localize(None)

# Calculate closure time in hours
df_merged['closure_hours'] = (df_merged['closeddate'] - df_merged['createddate']).dt.total_seconds() / 3600

# Filter for past 6 quarters (from 2021-04-26 onwards, since today is 2022-10-26)
start_date = pd.to_datetime('2021-04-26')
df_filtered = df_merged[df_merged['createddate'] >= start_date].copy()

# Group by state and calculate average closure time
state_stats = df_filtered.groupby('ShippingState').agg({
    'closure_hours': ['mean', 'count']
}).round(2)

state_stats.columns = ['avg_closure_hours', 'case_count']
state_stats = state_stats.reset_index()

# Sort by average closure time (quickest first)
state_stats_sorted = state_stats.sort_values('avg_closure_hours')

# Show results for debugging
print('Number of cases:', len(df_filtered))
print('States found:', len(state_stats_sorted))
print('Top 5 fastest states:')
print(state_stats_sorted.head(5))

# Get the top state with quickest closure time
top_state = state_stats_sorted.head(1)
if not top_state.empty:
    result = top_state['ShippingState'].iloc[0]
else:
    result = None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '#500Wt00000DDDfwIAH', 'accountid': '001Wt00000PFttwIAD', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDNYoIAP', 'accountid': '001Wt00000PGZZoIAP', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDPIsIAP', 'accountid': '#001Wt00000PGRnYIAX', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'status': 'Closed '}, {'id': '500Wt00000DDPSZIA5', 'accountid': '#001Wt00000PGZZoIAP', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDPZ0IAP', 'accountid': '001Wt00000PGdzxIAD', 'createddate': '2022-04-18T10:30:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDPsOIAX', 'accountid': '001Wt00000PHRF9IAP', 'createddate': '2021-07-06T14:30:00.000+0000', 'closeddate': 'None', 'status': 'Working'}, {'id': '500Wt00000DDPsPIAX', 'accountid': '#001Wt00000PGHsyIAH', 'createddate': '2023-04-05T17:51:00.000+0000', 'closeddate': '2023-04-06T11:30:54.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDQRsIAP', 'accountid': '001Wt00000PGzM9IAL', 'createddate': '2023-03-08T06:49:00.000+0000', 'closeddate': '2023-03-08T07:07:30.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDQoUIAX', 'accountid': '#001Wt00000PGzM9IAL', 'createddate': '2021-09-15T10:00:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDRW0IAP', 'accountid': '001Wt00000PGZZoIAP', 'createddate': '2021-06-03T14:30:00.000+0000', 'closeddate': 'None', 'status': 'Working'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'Id': '001Wt00000PFj4zIAD', 'Name': 'NaviCorp Tech ', 'Phone': '000-111-2222', 'Industry': 'Navigation Technology', 'Description': 'NaviCorp Tech excels in developing advanced navigation technologies, with a focus on precision and power efficiency. Utilizing CircuitAI Innovator alongside OptiPower Manager, they deliver solutions that redefine navigation systems, enhancing accuracy and operational excellence.', 'NumberOfEmployees': '800.0', 'ShippingState': 'FL'}, {'Id': '001Wt00000PFj50IAD', 'Name': 'FusionTech Systems', 'Phone': '333-987-6543', 'Industry': 'Technology Manufacturing', 'Description': 'FusionTech Systems stands out in technology manufacturing by integrating AI and cloud-based solutions. With products like AI Cirku-Tech and CloudLink Designer, they commit to providing innovative manufacturing processes. Their dedication to tech-driven manufacturing ensures high-quality, reliable outputs.', 'NumberOfEmployees': '760.0', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PFluoIAD', 'Name': 'BlueSky Aerospace', 'Phone': '839-393-9393', 'Industry': 'Aerospace Engineering', 'Description': "BlueSky Aerospace excels in aerospace engineering through innovative simulation and circuit design tools. With QuantumPCB Modeler and SimuFlow Xtreme, they develop precise and advanced aerospace components. Their continuous pursuit of innovation drives aerospace technology's evolution.", 'NumberOfEmployees': '980.0', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PFlupIAD', 'Name': 'NeuralWave Technologies', 'Phone': '444-333-4444', 'Industry': 'Artificial Intelligence', 'Description': 'NeuralWave Technologies leads advancements in AI-driven solutions for various applications. Using products like AI Cirku-Tech and Workflow Genius, they optimize design processes and enhance power management in AI systems. Focused on innovation, they continue to push the boundaries of artificial intelligence capabilities.', 'NumberOfEmployees': '950.0', 'ShippingState': 'CA'}, {'Id': '001Wt00000PFrk1IAD', 'Name': 'SkyNet Technologies', 'Phone': '111-222-3334', 'Industry': 'Drones & Aviation', 'Description': 'SkyNet Technologies pioneers in drone development and aviation technology, combining precision design with advanced cloud capabilities. Through QuantumPCB Modeler and CloudLink Designer, they produce innovative and efficient aviation systems. Their contributions set standards in the modernization of aerial technology.', 'NumberOfEmployees': '700.0', 'ShippingState': 'MO'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'Id': '001Wt00000PFj4zIAD', 'ShippingState': 'FL'}, {'Id': '001Wt00000PFj50IAD', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PFluoIAD', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PFlupIAD', 'ShippingState': 'CA'}, {'Id': '001Wt00000PFrk1IAD', 'ShippingState': 'MO'}, {'Id': '001Wt00000PFsjMIAT', 'ShippingState': 'OH'}, {'Id': '001Wt00000PFsjOIAT', 'ShippingState': 'NY'}, {'Id': '001Wt00000PFsmZIAT', 'ShippingState': 'CO'}, {'Id': '001Wt00000PFsmaIAD', 'ShippingState': 'MI'}, {'Id': '001Wt00000PFsmbIAD', 'ShippingState': 'NV'}, {'Id': '#001Wt00000PFsmcIAD', 'ShippingState': 'MN'}, {'Id': '001Wt00000PFsmdIAD', 'ShippingState': 'MA'}, {'Id': '001Wt00000PFt7TIAT', 'ShippingState': 'CO'}, {'Id': '#001Wt00000PFttwIAD', 'ShippingState': 'CA'}, {'Id': '001Wt00000PGGTtIAP', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGGTuIAP', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGHsyIAH', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGQzcIAH', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGR63IAH', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGRnYIAX', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGRqjIAH', 'ShippingState': 'CA'}, {'Id': '001Wt00000PGSwYIAX', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGSwZIAX', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PGXrKIAX', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGXrLIAX', 'ShippingState': 'NY'}, {'Id': '001Wt00000PGXrMIAX', 'ShippingState': 'NY'}, {'Id': '001Wt00000PGXrNIAX', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGYgxIAH', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGYx4IAH', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PGYx5IAH', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGZZnIAP', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGZZoIAP', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGZgHIAX', 'ShippingState': 'UT'}, {'Id': '#001Wt00000PGZmeIAH', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGZmfIAH', 'ShippingState': 'MI'}, {'Id': '001Wt00000PGaHIIA1', 'ShippingState': 'NV'}, {'Id': '001Wt00000PGaNjIAL', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGaNkIAL', 'ShippingState': 'VA'}, {'Id': '#001Wt00000PGaZCIA1', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGaZDIA1', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGb5MIAT', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PGb5NIAT', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGb5OIAT', 'ShippingState': 'IL'}, {'Id': '#001Wt00000PGcFxIAL', 'ShippingState': 'MI'}, {'Id': '001Wt00000PGccRIAT', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGcpMIAT', 'ShippingState': 'MO'}, {'Id': '#001Wt00000PGdBuIAL', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGdwiIAD', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGdzxIAD', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGeJIIA1', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGoAaIAL', 'ShippingState': 'NJ'}, {'Id': '#001Wt00000PGovMIAT', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGtdJIAT', 'ShippingState': 'IL'}, {'Id': '001Wt00000PGtdKIAT', 'ShippingState': 'VA'}, {'Id': '001Wt00000PGtmwIAD', 'ShippingState': 'IL'}, {'Id': '001Wt00000PGtmxIAD', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGyTIIA1', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGyv0IAD', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGz2nIAD', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGzM9IAL', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGzSaIAL', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGzSbIAL', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGzVpIAL', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGzsMIAT', 'ShippingState': 'CA'}, {'Id': '001Wt00000PH90cIAD', 'ShippingState': 'MA'}, {'Id': '#001Wt00000PH9DRIA1', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PH9ITIA1', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PHHXXIA5', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHR75IAH', 'ShippingState': 'OR'}, {'Id': '#001Wt00000PHR8gIAH', 'ShippingState': 'AZ'}, {'Id': '001Wt00000PHRF8IAP', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHRF9IAP', 'ShippingState': 'WA'}, {'Id': '001Wt00000PHRTeIAP', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PHRTfIAP', 'ShippingState': 'FL'}, {'Id': '001Wt00000PHRVGIA5', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHRVHIA5', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHRVIIA5', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHRbiIAH', 'ShippingState': 'GA'}, {'Id': '001Wt00000PHVaUIAX', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVaVIAX', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PHVdhIAH', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PHVfJIAX', 'ShippingState': 'MN'}, {'Id': '001Wt00000PHVgvIAH', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHViXIAX', 'ShippingState': 'NC'}, {'Id': '001Wt00000PHViYIAX', 'ShippingState': 'MD'}, {'Id': '#001Wt00000PHViZIAX', 'ShippingState': 'PA'}, {'Id': '001Wt00000PHViaIAH', 'ShippingState': 'CO'}, {'Id': '001Wt00000PHVk9IAH', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PHVkAIAX', 'ShippingState': 'VA'}, {'Id': '001Wt00000PHVllIAH', 'ShippingState': 'FL'}, {'Id': '001Wt00000PHVnNIAX', 'ShippingState': 'SC'}, {'Id': '001Wt00000PHVnOIAX', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVozIAH', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHVqbIAH', 'ShippingState': 'GA'}, {'Id': '001Wt00000PHVqdIAH', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVsDIAX', 'ShippingState': 'OR'}, {'Id': '001Wt00000PHVtpIAH', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVvRIAX', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVx3IAH', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PHVyfIAH', 'ShippingState': 'NC'}, {'Id': '001Wt00000PHW0HIAX', 'ShippingState': 'NY'}]}

exec(code, env_args)
