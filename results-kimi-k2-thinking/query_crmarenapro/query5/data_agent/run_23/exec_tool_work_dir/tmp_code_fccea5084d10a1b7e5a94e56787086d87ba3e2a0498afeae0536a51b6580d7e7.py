code = """from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Today is 2023-01-16
today = datetime(2023, 1, 16)

# Calculate 5 months ago
five_months_ago = today - relativedelta(months=5)
print('__RESULT__:')
print(five_months_ago.strftime('%Y-%m-%d'))"""

env_args = {'var_functions.list_db:0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.list_db:2': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:5': [{'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.'}]}

exec(code, env_args)
