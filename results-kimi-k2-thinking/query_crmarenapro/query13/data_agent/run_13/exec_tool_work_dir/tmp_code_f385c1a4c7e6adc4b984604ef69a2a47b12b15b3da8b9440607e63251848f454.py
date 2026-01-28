code = """from calendar import monthrange
from datetime import datetime, timedelta
import json

# Calculate date range: past 5 months from 2022-11-25
today = datetime(2022, 11, 25)
# Go back 5 months
if today.month > 5:
    start_date = datetime(today.year, today.month - 5, 1)
else:
    year = today.year - 1
    month = today.month + 7  # 12 - 5 + month
    start_date = datetime(year, month, 1)

end_date = today
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')

print('__RESULT__:')
print(json.dumps(f"{start_date_str} to {end_date_str}"))"""

env_args = {'var_functions.list_db:0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:2': [{'Id': '801Wt00000PFsjPIAT', 'OwnerId': '005Wt000003NJ0EIAW', 'EffectiveDate': '2023-06-25'}, {'Id': '801Wt00000PFsjQIAT', 'OwnerId': '005Wt000003NGjwIAG', 'EffectiveDate': '2021-09-30'}, {'Id': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'EffectiveDate': '2022-09-15'}, {'Id': '801Wt00000PFtAmIAL', 'OwnerId': '005Wt000003NIljIAG', 'EffectiveDate': '2020-09-01'}, {'Id': '801Wt00000PFtAnIAL', 'OwnerId': '005Wt000003NEdJIAW', 'EffectiveDate': '2023-06-01'}, {'Id': '801Wt00000PFyISIA1', 'OwnerId': '005Wt000003NIljIAG', 'EffectiveDate': '2022-01-15'}, {'Id': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO', 'EffectiveDate': '2022-07-10'}, {'Id': '801Wt00000PFyIUIA1', 'OwnerId': '005Wt000003NJ53IAG', 'EffectiveDate': '2024-09-20'}, {'Id': '801Wt00000PFyIVIA1', 'OwnerId': '005Wt000003NJmcIAG', 'EffectiveDate': '2020-09-15'}, {'Id': '801Wt00000PFyIWIA1', 'OwnerId': '005Wt000003NJY5IAO', 'EffectiveDate': '2021-12-01'}], 'var_functions.query_db:5': [{'Id': '#800Wt00000DD0SZIA1', 'CompanySignedDate': '2021-07-16'}, {'Id': '800Wt00000DD0SaIAL', 'CompanySignedDate': '2021-09-28'}, {'Id': '#800Wt00000DD0SbIAL', 'CompanySignedDate': '2023-07-12'}, {'Id': '800Wt00000DDDuRIAX', 'CompanySignedDate': '2024-04-16'}, {'Id': '800Wt00000DDNFUIA5', 'CompanySignedDate': '2023-07-02'}, {'Id': '800Wt00000DDNFVIA5', 'CompanySignedDate': '2021-06-26'}, {'Id': '800Wt00000DDNlnIAH', 'CompanySignedDate': '2022-09-02'}, {'Id': '800Wt00000DDPXRIA5', 'CompanySignedDate': '2022-04-22'}, {'Id': '800Wt00000DDPXSIA5', 'CompanySignedDate': '2023-02-25'}, {'Id': '800Wt00000DDPXTIA5', 'CompanySignedDate': '2023-10-13'}], 'var_functions.query_db:6': [{'Id': '802Wt0000078wz3IAA', 'OrderId': '801Wt00000PGSYIIA5', 'Product2Id': '#01tWt000006hVTJIA2', 'Quantity': '15.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027Pa1IAE'}, {'Id': '802Wt0000078wz4IAA', 'OrderId': '801Wt00000PHVkDIAX', 'Product2Id': '01tWt000006hVDBIA2', 'Quantity': '3.0', 'UnitPrice': '549.99', 'PriceBookEntryId': '01uWt0000027PF3IAM'}, {'Id': '802Wt0000078wz5IAA', 'OrderId': '801Wt00000PHQuFIAX', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '9.0', 'UnitPrice': '503.4905', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '802Wt0000078xAAIAY', 'OrderId': '801Wt00000PGHg7IAH', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '10.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '#802Wt0000078xABIAY', 'OrderId': '801Wt00000PHVicIAH', 'Product2Id': '01tWt000006hVMrIAM', 'Quantity': '1.0', 'UnitPrice': '299.99', 'PriceBookEntryId': '01uWt0000027POjIAM'}], 'var_functions.list_db:8': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem']}

exec(code, env_args)
