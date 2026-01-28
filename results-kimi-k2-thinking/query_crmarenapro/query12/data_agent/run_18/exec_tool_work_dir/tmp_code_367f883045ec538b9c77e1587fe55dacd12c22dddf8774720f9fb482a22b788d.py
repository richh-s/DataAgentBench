code = """import json
import pandas as pd

# Get the query result
query_result = locals()['var_functions.query_db:8']

# Load data if it's a file path
if isinstance(query_result, str) and query_result.endswith('.json'):
    with open(query_result, 'r') as f:
        data = json.load(f)
else:
    data = query_result

# Print debug info
print("Number of records: {}".format(len(data)))

if len(data) == 0:
    result = None
else:
    print("First few records: {}".format(data[:5]))
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Handle date parsing - remove timezone info for consistent calculation
    df['OpportunityCreatedDate'] = pd.to_datetime(df['OpportunityCreatedDate']).dt.tz_localize(None)
    df['CompanySignedDate'] = pd.to_datetime(df['CompanySignedDate'])
    
    # Calculate sales cycle days
    df['SalesCycleDays'] = (df['CompanySignedDate'] - df['OpportunityCreatedDate']).dt.days
    
    # Print sales cycle days for debugging
    print("Sales cycle days calculated: {}".format(df[['OwnerId', 'SalesCycleDays']].to_dict('records')))
    
    # Group by OwnerId and calculate average
    avg_sales_cycle = df.groupby('OwnerId')['SalesCycleDays'].mean().reset_index()
    
    # Sort by average to find quickest (minimum)
    avg_sales_cycle = avg_sales_cycle.sort_values('SalesCycleDays')
    
    print("Average sales cycle by agent:")
    print(avg_sales_cycle.to_string())
    
    # Get the agent with the quickest average
    if not avg_sales_cycle.empty:
        quickest_agent = avg_sales_cycle.iloc[0]['OwnerId']
        print("Quickest agent: {}".format(quickest_agent))
        result = quickest_agent
    else:
        result = None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'OwnerId': '005Wt000003NDEBIA4', 'OpportunityCreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15'}], 'var_functions.query_db:8': [{'OwnerId': '005Wt000003NDEBIA4', 'OpportunityCreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15'}]}

exec(code, env_args)
