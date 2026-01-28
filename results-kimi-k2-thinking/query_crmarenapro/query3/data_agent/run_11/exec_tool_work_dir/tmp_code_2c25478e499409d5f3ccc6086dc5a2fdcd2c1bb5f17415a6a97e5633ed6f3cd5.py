code = """import pandas as pd
import json

# Load the data from previous queries
db_results = {}
for i in range(4):
    key = f'var_functions.query_db:{i}'
    db_results[i] = locals().get(key, [])

# Display what we found
print("Opportunity Data:")
print(json.dumps(db_results[0], indent=2))

print("\nQuotes Data:")
print(json.dumps(db_results[1], indent=2))

print("\nContracts Data:")
print(json.dumps(db_results[2], indent=2))

print("\nOpportunity Line Items Data:")
print(json.dumps(db_results[3], indent=2))

# Analysis
opportunity = db_results[0][0] if db_results[0] else None
quotes = db_results[1]
contracts = db_results[2]
line_items = db_results[3]

if opportunity:
    stage_name = opportunity.get('StageName')
    probability = float(opportunity.get('Probability', 0))
    close_date = opportunity.get('CloseDate')
    
    print(f"\n=== ANALYSIS ===")
    print(f"Current Stage: {stage_name}")
    print(f"Probability: {probability}%")
    print(f"Close Date: {close_date}")
    print(f"Has Line Items: {len(line_items) > 0}")
    print(f"Has Quotes: {len(quotes) > 0}")
    print(f"Has Contracts: {len(contracts) > 0}")
    
    # Determine correct stage based on CRM best practices
    # High probability (85%) and past close date suggests this should be Closed
    # But let's check if there are any activities to confirm

print("__RESULT__:")
print(json.dumps({"current_stage": stage_name, "probability": probability, "close_date": close_date, "has_quotes": len(quotes) > 0, "has_contracts": len(contracts) > 0}))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Amount': '61666.225', 'Probability': '85.0', 'CloseDate': '2022-02-20'}], 'var_functions.query_db:2': [], 'var_functions.query_db:3': [], 'var_functions.query_db:4': [{'Id': '00kWt000002HJTPIA4', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HUdKIAW', 'Product2Id': '01tWt000006hVhpIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}]}

exec(code, env_args)
