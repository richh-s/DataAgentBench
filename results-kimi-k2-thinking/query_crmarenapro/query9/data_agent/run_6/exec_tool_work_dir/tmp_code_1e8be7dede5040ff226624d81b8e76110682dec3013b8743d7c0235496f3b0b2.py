code = """import json
import pandas as pd
from datetime import datetime

# Load the data
support_cases = locals()['var_functions.query_db:2']
accounts = locals()['var_functions.query_db:4']

# Convert to DataFrames
df_cases = pd.DataFrame(support_cases)
df_accounts = pd.DataFrame(accounts)

# Print basic info about the data
print('Cases shape:', df_cases.shape)
print('Accounts shape:', df_accounts.shape)

# Show sample data
print('\nSample cases:')
print(df_cases.head())
print('\nSample accounts:')
print(df_accounts.head())

# Convert date strings to datetime
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'])
df_cases['closeddate'] = pd.to_datetime(df_cases['closeddate'])

# Calculate case closure time in hours
df_cases['closure_hours'] = (df_cases['closeddate'] - df_cases['createddate']).dt.total_seconds() / 3600

print('\nSample with closure hours:')
print(df_cases[['id', 'createddate', 'closeddate', 'closure_hours']].head())

# Clean account IDs (remove leading # if present)
df_accounts['Id_clean'] = df_accounts['Id'].str.replace('^#', '', regex=True)
df_cases['accountid_clean'] = df_cases['accountid'].str.replace('^#', '', regex=True)

# Clean ShippingState (remove trailing whitespace)
df_accounts['ShippingState_clean'] = df_accounts['ShippingState'].str.strip()

# Merge cases with accounts to get states
df_merged = df_cases.merge(
    df_accounts[['Id_clean', 'ShippingState_clean']], 
    left_on='accountid_clean', 
    right_on='Id_clean', 
    how='left'
)

print('\nMerged data shape:', df_merged.shape)
print('\nSample merged data:')
print(df_merged[['id', 'accountid', 'ShippingState_clean', 'closure_hours']].head())

# Group by state and calculate average closure time
df_state_stats = df_merged.groupby('ShippingState_clean').agg({
    'closure_hours': ['mean', 'count'],
    'id': 'count'
}).round(2)

# Flatten column names
df_state_stats.columns = ['avg_closure_hours', 'closure_hours_count', 'case_count']
df_state_stats = df_state_stats.reset_index()

# Filter states with at least 2 cases to ensure meaningful averages
df_state_stats_filtered = df_state_stats[df_state_stats['case_count'] >= 2]

# Sort by average closure time (ascending)
df_state_stats_sorted = df_state_stats_filtered.sort_values('avg_closure_hours')

print('\nState statistics (top 10 fastest):')
print(df_state_stats_sorted.head(10).to_string(index=False))

# Get the state with quickest closure time
if not df_state_stats_sorted.empty:
    quickest_state = df_state_stats_sorted.iloc[0]
    state_abbr = quickest_state['ShippingState_clean']
    avg_hours = quickest_state['avg_closure_hours']
    case_count = quickest_state['case_count']
    
    result = state_abbr
    print(f"\nQuickest state: {state_abbr} with average closure time of {avg_hours:.2f} hours ({case_count} cases)")
else:
    result = "No data available"
    print("No data available after filtering")

# Print result in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:2': [{'id': '#500Wt00000DDTERIA5', 'accountid': '001Wt00000PGzSaIAL', 'createddate': '2022-03-10T09:30:00.000+0000', 'closeddate': '2022-03-13T09:45:27.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDYdwIAH', 'accountid': '001Wt00000PFj4zIAD', 'createddate': '2022-02-03T14:30:00.000+0000', 'closeddate': '2022-02-03T14:46:56.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDYpHIAX', 'accountid': '#001Wt00000PHHXXIA5', 'createddate': '2022-09-05T11:15:00.000+0000', 'closeddate': '2022-09-05T11:42:09.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDet1IAD', 'accountid': '001Wt00000PGzSbIAL', 'createddate': '2021-09-07T23:48:00.000+0000', 'closeddate': '2021-09-08T03:11:32.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDg1yIAD', 'accountid': '#001Wt00000PHVnNIAX', 'createddate': '2022-02-08T06:22:00.000+0000', 'closeddate': '2022-02-08T06:43:35.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDg1zIAD', 'accountid': '001Wt00000PGdzxIAD', 'createddate': '2022-04-17T14:20:00.000+0000', 'closeddate': '2022-04-17T14:37:58.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDg8RIAT', 'accountid': '001Wt00000PGZZoIAP', 'createddate': '2022-05-10T11:30:00.000+0000', 'closeddate': '2022-05-10T17:02:48.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDgLLIA1', 'accountid': '#001Wt00000PGZZoIAP', 'createddate': '2022-05-12T14:45:00.000+0000', 'closeddate': '2022-05-12T14:54:10.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDsKuIAL', 'accountid': '#001Wt00000PHVvRIAX', 'createddate': '2022-07-23T07:37:00.000+0000', 'closeddate': '2022-07-23T07:47:37.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDxVqIAL', 'accountid': '001Wt00000PHVvRIAX', 'createddate': '2021-09-15T09:10:00.000+0000', 'closeddate': '2021-09-15T09:50:35.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDxZ4IAL', 'accountid': '001Wt00000PGtmwIAD', 'createddate': '2021-06-19T21:19:00.000+0000', 'closeddate': '2021-06-19T21:32:46.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDzZFIA1', 'accountid': '001Wt00000PGoAaIAL', 'createddate': '2021-07-15T10:30:00.000+0000', 'closeddate': '2021-07-15T13:32:47.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzarIAD', 'accountid': '#001Wt00000PGoAaIAL', 'createddate': '2021-10-08T08:07:00.000+0000', 'closeddate': '2021-10-08T08:43:11.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzcTIAT', 'accountid': '001Wt00000PGRnYIAX', 'createddate': '2022-08-01T10:15:00.000+0000', 'closeddate': '2022-08-01T14:45:37.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzfhIAD', 'accountid': '001Wt00000PGzM9IAL', 'createddate': '2022-03-04T09:45:00.000+0000', 'closeddate': '2022-03-05T10:25:32.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DE08jIAD', 'accountid': '001Wt00000PGSwYIAX', 'createddate': '2021-09-16T11:00:00.000+0000', 'closeddate': '2021-09-16T11:14:27.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE0FCIA1', 'accountid': '001Wt00000PHVvRIAX', 'createddate': '2021-09-05T11:15:00.000+0000', 'closeddate': '2021-09-05T11:25:45.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DE0IPIA1', 'accountid': '001Wt00000PHVtpIAH', 'createddate': '2022-08-10T09:30:00.000+0000', 'closeddate': '2022-08-10T13:59:01.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DE0QTIA1', 'accountid': '001Wt00000PFt7TIAT', 'createddate': '2022-02-02T15:30:45.000+0000', 'closeddate': '2022-02-03T10:17:46.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DE0S5IAL', 'accountid': '001Wt00000PFt7TIAT', 'createddate': '2022-03-05T11:20:30.000+0000', 'closeddate': '2022-03-05T11:34:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE0ThIAL', 'accountid': '#001Wt00000PGXrLIAX', 'createddate': '2021-10-02T10:30:00.000+0000', 'closeddate': '2021-10-03T13:27:49.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DE0YXIA1', 'accountid': '#001Wt00000PGaZDIA1', 'createddate': '2022-02-24T19:20:00.000+0000', 'closeddate': '2022-02-25T04:35:46.000+0000', 'status': 'Closed'}], 'var_functions.query_db:4': [{'Id': '001Wt00000PFj4zIAD', 'Name': 'NaviCorp Tech ', 'ShippingState': 'FL'}, {'Id': '001Wt00000PFj50IAD', 'Name': 'FusionTech Systems', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PFluoIAD', 'Name': 'BlueSky Aerospace', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PFlupIAD', 'Name': 'NeuralWave Technologies', 'ShippingState': 'CA'}, {'Id': '001Wt00000PFrk1IAD', 'Name': 'SkyNet Technologies', 'ShippingState': 'MO'}, {'Id': '001Wt00000PFsjMIAT', 'Name': 'EvoTrend Systems', 'ShippingState': 'OH'}, {'Id': '001Wt00000PFsjOIAT', 'Name': 'QuantumLeap Computing', 'ShippingState': 'NY'}, {'Id': '001Wt00000PFsmZIAT', 'Name': 'EcoVision Engineering', 'ShippingState': 'CO'}, {'Id': '001Wt00000PFsmaIAD', 'Name': 'EcoLite Innovations   ', 'ShippingState': 'MI'}, {'Id': '001Wt00000PFsmbIAD', 'Name': 'Innovative Robotics', 'ShippingState': 'NV'}, {'Id': '#001Wt00000PFsmcIAD', 'Name': 'Nordic HealthTech', 'ShippingState': 'MN'}, {'Id': '001Wt00000PFsmdIAD', 'Name': 'NexGen Biotech', 'ShippingState': 'MA'}, {'Id': '001Wt00000PFt7TIAT', 'Name': 'TerraForm Engineering  ', 'ShippingState': 'CO'}, {'Id': '#001Wt00000PFttwIAD', 'Name': 'Digital Horizon Media', 'ShippingState': 'CA'}, {'Id': '001Wt00000PGGTtIAP', 'Name': 'SecureWise Solutions', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGGTuIAP', 'Name': 'Horizon Tech Integrations  ', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGHsyIAH', 'Name': 'Circuit Dynamics Inc.', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGQzcIAH', 'Name': 'UrbanEDGE Innovation', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGR63IAH', 'Name': 'Pioneer Envisions', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGRnYIAX', 'Name': 'AgroSmart Innovations', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGRqjIAH', 'Name': 'DataWave Analytics', 'ShippingState': 'CA'}, {'Id': '001Wt00000PGSwYIAX', 'Name': 'GreenLeaf Engineering  ', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGSwZIAX', 'Name': 'Insight Analytics Group', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PGXrKIAX', 'Name': 'InnovateX Solutions', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGXrLIAX', 'Name': 'DataGuard Insights', 'ShippingState': 'NY'}, {'Id': '001Wt00000PGXrMIAX', 'Name': 'Innovatech Group', 'ShippingState': 'NY'}, {'Id': '001Wt00000PGXrNIAX', 'Name': 'FutureTech Innovations', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGYgxIAH', 'Name': 'EcoShield Technologies', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGYx4IAH', 'Name': 'UrbanSmart Inc.', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PGYx5IAH', 'Name': 'Quantum Designs', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGZZnIAP', 'Name': 'SolarWind Innovations', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGZZoIAP', 'Name': 'EnviroTech Solutions', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGZgHIAX', 'Name': 'TechGrove Systems', 'ShippingState': 'UT'}, {'Id': '#001Wt00000PGZmeIAH', 'Name': 'AlphaWave Networks', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGZmfIAH', 'Name': 'Quantum Dynamics LLC', 'ShippingState': 'MI'}, {'Id': '001Wt00000PGaHIIA1', 'Name': 'MetroGrid Networks', 'ShippingState': 'NV'}, {'Id': '001Wt00000PGaNjIAL', 'Name': 'MetaData Analytics', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGaNkIAL', 'Name': 'Horizon Dynamics', 'ShippingState': 'VA'}, {'Id': '#001Wt00000PGaZCIA1', 'Name': 'GreenStar Electronics  ', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGaZDIA1', 'Name': 'Oceanic Innovation Labs  ', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGb5MIAT', 'Name': 'InnoBuild Constructors', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PGb5NIAT', 'Name': 'SkyLink Communications', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGb5OIAT', 'Name': 'UrbanTech Developments', 'ShippingState': 'IL'}, {'Id': '#001Wt00000PGcFxIAL', 'Name': 'GreenWave Circuits   ', 'ShippingState': 'MI'}, {'Id': '001Wt00000PGccRIAT', 'Name': 'CyberWave Security', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGcpMIAT', 'Name': 'TechBridge Systems', 'ShippingState': 'MO'}, {'Id': '#001Wt00000PGdBuIAL', 'Name': 'TechSavvy Innovations', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGdwiIAD', 'Name': 'EcoTech Manufacturing', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGdzxIAD', 'Name': 'AquaSys Controls', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGeJIIA1', 'Name': 'InnoSphere Labs', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGoAaIAL', 'Name': 'TrueNorth Technologies', 'ShippingState': 'NJ'}, {'Id': '#001Wt00000PGovMIAT', 'Name': 'ClearSky Data Solutions', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGtdJIAT', 'Name': 'Quantum Innovations Inc.', 'ShippingState': 'IL'}, {'Id': '001Wt00000PGtdKIAT', 'Name': 'CyberPulse Security', 'ShippingState': 'VA'}, {'Id': '001Wt00000PGtmwIAD', 'Name': 'InfiLink Solutions', 'ShippingState': 'IL'}, {'Id': '001Wt00000PGtmxIAD', 'Name': 'Titan Robotics Group', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGyTIIA1', 'Name': 'GreenTech Dynamics', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGyv0IAD', 'Name': 'Future Innovations LLC   ', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGz2nIAD', 'Name': 'GreenEnergy Solutions', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGzM9IAL', 'Name': 'MediLux Solutions', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGzSaIAL', 'Name': 'TechFusion Inc.', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGzSbIAL', 'Name': 'AquaGuard Solutions   ', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGzVpIAL', 'Name': 'EcoEnergy Solutions', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGzsMIAT', 'Name': 'PrimeEdge Technology   ', 'ShippingState': 'CA'}, {'Id': '001Wt00000PH90cIAD', 'Name': 'InspireTech Consulting', 'ShippingState': 'MA'}, {'Id': '#001Wt00000PH9DRIA1', 'Name': 'SkyLevel Systems ', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PH9ITIA1', 'Name': 'DigitalWave Solutions', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PHHXXIA5', 'Name': 'Innovate Sphere', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHR75IAH', 'Name': 'RenewSys Corp', 'ShippingState': 'OR'}, {'Id': '#001Wt00000PHR8gIAH', 'Name': 'SkyTech Ventures', 'ShippingState': 'AZ'}, {'Id': '001Wt00000PHRF8IAP', 'Name': 'EcoWave Solutions', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHRF9IAP', 'Name': 'Green Circuitry LLC', 'ShippingState': 'WA'}, {'Id': '001Wt00000PHRTeIAP', 'Name': 'Metro Security Systems', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PHRTfIAP', 'Name': 'Vertex Engineering Corp', 'ShippingState': 'FL'}, {'Id': '001Wt00000PHRVGIA5', 'Name': 'AlphaTech Productions', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHRVHIA5', 'Name': 'InnovateGrid Systems', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHRVIIA5', 'Name': 'SkyVista Technologies', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHRbiIAH', 'Name': 'PowerGrid Innovations   ', 'ShippingState': 'GA'}, {'Id': '001Wt00000PHVaUIAX', 'Name': 'TerraSync Solutions', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVaVIAX', 'Name': 'Precision Circuit Systems', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PHVdhIAH', 'Name': 'NeonTech Industries', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PHVfJIAX', 'Name': 'BrightTech Systems', 'ShippingState': 'MN'}, {'Id': '001Wt00000PHVgvIAH', 'Name': 'Skyline Robotics   ', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHViXIAX', 'Name': 'Nova Healthcare Tech ', 'ShippingState': 'NC'}, {'Id': '001Wt00000PHViYIAX', 'Name': 'BioPulse MedTech', 'ShippingState': 'MD'}, {'Id': '#001Wt00000PHViZIAX', 'Name': 'OmegaDesign Labs', 'ShippingState': 'PA'}, {'Id': '001Wt00000PHViaIAH', 'Name': 'InnovateVibes LLC', 'ShippingState': 'CO'}, {'Id': '001Wt00000PHVk9IAH', 'Name': 'LiftTech Elevations', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PHVkAIAX', 'Name': 'SecureLink Technologies  ', 'ShippingState': 'VA'}, {'Id': '001Wt00000PHVllIAH', 'Name': 'SafetyNet Inc.', 'ShippingState': 'FL'}, {'Id': '001Wt00000PHVnNIAX', 'Name': 'BrightField Ventures', 'ShippingState': 'SC'}, {'Id': '001Wt00000PHVnOIAX', 'Name': 'CraftTech Electronics', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVozIAH', 'Name': 'TechSphere Design', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHVqbIAH', 'Name': 'Onyx Security Systems', 'ShippingState': 'GA'}, {'Id': '001Wt00000PHVqdIAH', 'Name': 'TechWave Innovations', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVsDIAX', 'Name': 'NeoGreen Enterprises', 'ShippingState': 'OR'}, {'Id': '001Wt00000PHVtpIAH', 'Name': 'EnergyNova Corp', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVvRIAX', 'Name': 'AeroFusion Systems', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVx3IAH', 'Name': 'Altai Innovations', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PHVyfIAH', 'Name': 'MedTech Advances', 'ShippingState': 'NC'}, {'Id': '001Wt00000PHW0HIAX', 'Name': 'DataStream Analytics', 'ShippingState': 'NY'}]}

exec(code, env_args)
