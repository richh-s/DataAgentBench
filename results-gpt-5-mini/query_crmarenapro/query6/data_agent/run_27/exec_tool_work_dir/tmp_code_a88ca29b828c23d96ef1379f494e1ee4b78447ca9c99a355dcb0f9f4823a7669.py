code = """import json
res = var_call_oin2GPR9tVx0NVzS6TuURww2
# Determine which knowledge article specifically addresses 'Discount > 10% or Quantity > 30'
# Based on titles, look for ones about 'Volume-Based Discounts' or 'Product Quantity Limits'
candidates = []
for art in res['matching_knowledge_articles']:
    title = (art['title'] or '').lower()
    if 'volume' in title or 'quantity' in title or 'product quantity' in title or 'discount' in title:
        candidates.append(art)

# Prefer explicit policy like 'Product Quantity Limits' or 'Volume-Based Discounts'
chosen = None
for art in candidates:
    t = (art['title'] or '').lower()
    if 'product quantity limits' in t or 'volume-based discounts' in t:
        chosen = art
        break

# If id contains leading #, remove? User asked to return only Id of knowledge article that the invalid config violates.
# We'll return the id as-is
if chosen is None and candidates:
    chosen = candidates[0]

out = chosen['id'] if chosen else None
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_bMDlLquwdVYFwmVoOvAeV8eE': [], 'var_call_CcS0WbIuEos0jxEIVKL95Dga': 'file_storage/call_CcS0WbIuEos0jxEIVKL95Dga.json', 'var_call_2YdGIHKZW0bprh7mnpDTqHoP': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_nGygwU6SNc7Y5E4RH0grYgRb': 'file_storage/call_nGygwU6SNc7Y5E4RH0grYgRb.json', 'var_call_oin2GPR9tVx0NVzS6TuURww2': {'quote_id': '0Q0Wt000001WRAzKAO', 'flagged_line_items': [{'Id': '#0QLWt0000022oAvOAI', 'Quantity': 35.0, 'UnitPrice': 399.99, 'Discount': 15.0}], 'matching_knowledge_articles': [{'id': 'ka0Wt000000EowFIAS', 'title': 'Competitor: Adaptive Design Solutions', 'keyword': 'pricing'}, {'id': '#ka0Wt000000EqRlIAK', 'title': 'Competitor: NanoDesign Systems   ', 'keyword': 'pricing'}, {'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'keyword': 'discount'}, {'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy', 'keyword': 'quantity'}, {'id': '#ka0Wt000000EnwvIAC', 'title': 'Product Quantity Limits   ', 'keyword': 'quantity'}, {'id': 'ka0Wt000000EnyXIAS', 'title': 'TechPulse Solutions: Defining Values that Drive Innovation and Success', 'keyword': 'pricing'}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'keyword': 'discount'}]}}

exec(code, env_args)
