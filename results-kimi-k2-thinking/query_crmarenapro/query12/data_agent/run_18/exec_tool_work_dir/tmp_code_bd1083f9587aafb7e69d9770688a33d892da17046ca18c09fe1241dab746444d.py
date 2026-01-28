code = """import json
import pandas as pd
from datetime import datetime

# Get the query result
query_result = var_functions.query_db:2

# If the result is a string path to a JSON file, read it
if isinstance(query_result, str):
    with open(query_result, 'r') as f:
        data = json.load(f)
else:
    data = query_result

print(f"Number of records: {len(data)}")
print(f"First few records: {data[:5]}")

# Convert to DataFrame to process
df = pd.DataFrame(data)

if not df.empty:
    # Calculate sales cycle days for each opportunity
    df['OpportunityCreatedDate'] = pd.to_datetime(df['OpportunityCreatedDate'])
    df['CompanySignedDate'] = pd.to_datetime(df['CompanySignedDate'])
    df['SalesCycleDays'] = (df['CompanySignedDate'] - df['OpportunityCreatedDate']).dt.days
    
    # Group by OwnerId and calculate average sales cycle
    avg_sales_cycle = df.groupby('OwnerId')['SalesCycleDays'].mean().reset_index()
    
    # Sort by average sales cycle to find the quickest
    avg_sales_cycle = avg_sales_cycle.sort_values('SalesCycleDays')
    
    print(f"Average sales cycle by agent:")
    print(avg_sales_cycle)
    
    # Get the agent with the quickest average
    if not avg_sales_cycle.empty:
        quickest_agent = avg_sales_cycle.iloc[0]['OwnerId']
        print(f"Quickest agent: {quickest_agent}")
        
        # Prepare the result
        result = quickest_agent
    else:
        result = None
else:
    result = None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'OwnerId': '005Wt000003NDEBIA4', 'OpportunityCreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15'}]}

exec(code, env_args)
