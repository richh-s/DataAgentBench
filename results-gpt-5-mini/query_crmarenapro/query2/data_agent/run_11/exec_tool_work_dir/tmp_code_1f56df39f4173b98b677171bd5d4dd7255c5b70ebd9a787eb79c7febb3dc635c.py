code = """import json
import math

# Load data from previous tool calls
quotes = var_call_4o9qXXPwgcpMZxjgs5ZnSU2u
qli = var_call_mY1OwHkwTLTdhzlKidMp1fqJ
pbe = var_call_oziNgmNQ3XsVXcYghhAkLJK3

# Load large query results from files if necessary
def load_if_path(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

kav_discount_results = load_if_path(var_call_fEoqEFeWetfGQ9IuqOvqlCNz)
kav_setup_results = load_if_path(var_call_bKWhnWkG1eUQdANssPVT2lOF)

# Find the specific knowledge articles by title
discount_article = None
install_article = None
for art in kav_discount_results:
    title = (art.get('title') or '').strip()
    if 'Volume-Based Discounts' in title:
        discount_article = art
        break
for art in kav_setup_results:
    title = (art.get('title') or '').strip()
    if 'Volume-Based Installation Timeline Policy' in title:
        install_article = art
        break

# Compute totals
def to_float(v):
    try:
        return float(v)
    except:
        return 0.0

pre_discount_total = 0.0
total_quantity = 0.0
line_discounts = []
for line in qli:
    qty = to_float(line.get('Quantity'))
    up = to_float(line.get('UnitPrice'))
    disc = to_float(line.get('Discount'))
    pre_discount_total += qty * up
    total_quantity += qty
    line_discounts.append(disc)

# Determine expected discount per Volume-Based Discounts policy
expected_discount = 0.0
if pre_discount_total > 20:
    expected_discount = 15.0
elif pre_discount_total > 10:
    expected_discount = 10.0
elif pre_discount_total > 5:
    expected_discount = 5.0
else:
    expected_discount = 0.0

# Check compliance: all line discounts should equal expected_discount
violation = None
if discount_article is not None:
    # allow small tolerance
    for d in line_discounts:
        if not math.isclose(d, expected_discount, rel_tol=1e-6, abs_tol=1e-6):
            violation = discount_article.get('id')
            break

# If no violation found from discounts, check installation timeline policy only if quote includes setup timeline info
# However Quote table has no setup timeline fields; so we cannot verify setup compliance. Therefore only discount check applies here.

result = violation if violation is not None else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4o9qXXPwgcpMZxjgs5ZnSU2u': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_mY1OwHkwTLTdhzlKidMp1fqJ': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_bvTpgQi2B6gCKzsBeG46gIDe': [], 'var_call_oziNgmNQ3XsVXcYghhAkLJK3': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_fEoqEFeWetfGQ9IuqOvqlCNz': 'file_storage/call_fEoqEFeWetfGQ9IuqOvqlCNz.json', 'var_call_bKWhnWkG1eUQdANssPVT2lOF': 'file_storage/call_bKWhnWkG1eUQdANssPVT2lOF.json'}

exec(code, env_args)
