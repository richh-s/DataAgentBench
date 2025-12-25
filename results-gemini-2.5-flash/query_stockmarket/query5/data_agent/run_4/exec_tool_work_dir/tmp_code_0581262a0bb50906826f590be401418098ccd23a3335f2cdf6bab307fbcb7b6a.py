code = """import pandas as pd
import json

with open(locals()['var_function-call-8084294124488648582'], 'r') as f:
    nasdaq_capital_market_companies = json.load(f)

# Filter out test issues and non-financially normal companies, as per best practice (though not explicitly asked for here)
# For this query, the criteria for "financially troubled" are not explicitly asked, so I will skip this step for now.

company_data = []
for company in nasdaq_capital_market_companies:
    company_data.append({'Symbol': company['Symbol'], 'Company Description': company['Company Description']})

df_companies = pd.DataFrame(company_data)
# Print only symbols and names to keep the output concise, as the full list is too large
print('__RESULT__:')
print(df_companies.to_json(orient='records'))"""

env_args = {'var_function-call-8084294124488648582': 'file_storage/function-call-8084294124488648582.json'}

exec(code, env_args)
