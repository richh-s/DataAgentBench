code = """import pandas as pd
import json

# Load OrderItems (using the variable from storage)
with open(locals()['var_function-call-16912545030574088445']) as f:
    order_items = json.load(f)

# Load Cases (using the variable from storage)
with open(locals()['var_function-call-5257925918374328330']) as f:
    cases = json.load(f)

target_product_id = '01tWt000006hVJdIAM'

# Process OrderItems
valid_order_item_ids = set()
for item in order_items:
    pid = item.get('Product2Id')
    oid = item.get('Id')
    if pid and oid:
        # Clean
        pid_clean = pid.strip().lstrip('#')
        oid_clean = oid.strip().lstrip('#')
        
        if pid_clean == target_product_id:
            valid_order_item_ids.add(oid_clean)

# Process Cases
case_dates = []
for c in cases:
    oid = c.get('orderitemid__c')
    cdate = c.get('createddate')
    if oid and cdate:
        oid_clean = oid.strip().lstrip('#')
        if oid_clean in valid_order_item_ids:
            case_dates.append(cdate)

# Create DataFrame
if not case_dates:
    print("__RESULT__:")
    print(json.dumps("No cases found for this product."))
else:
    df = pd.DataFrame({'date': pd.to_datetime(case_dates, utc=True)})

    # Filter by date range
    # Today: 2021-04-10
    ref_date = pd.Timestamp('2021-04-10', tz='UTC')
    # Past 10 months implies looking back 10 months.
    # Start date approx: 2020-06-10.
    start_date = ref_date - pd.DateOffset(months=10)

    mask = (df['date'] >= start_date) & (df['date'] <= ref_date)
    df_filtered = df[mask].copy()

    # Aggregate by Month
    # We want to see if one month significantly exceeds others.
    # Format: Year-Month first to sort
    df_filtered['month_year'] = df_filtered['date'].dt.to_period('M')
    
    counts = df_filtered.groupby('month_year').size().sort_index()
    
    # Convert to string for printing
    counts_dict = {str(k): int(v) for k, v in counts.items()}
    
    print("__RESULT__:")
    print(json.dumps(counts_dict))"""

env_args = {'var_function-call-16912545030574088445': 'file_storage/function-call-16912545030574088445.json', 'var_function-call-5257925918374328330': 'file_storage/function-call-5257925918374328330.json'}

exec(code, env_args)
