code = """import sqlite3
import json

# Connect to products_orders database
conn = sqlite3.connect('products_orders.db')
cursor = conn.cursor()

# Query for all OrderItems with the product ID
cursor.execute("""
    SELECT Id, Product2Id 
    FROM OrderItem 
    WHERE Product2Id = '01tWt000006hV8LIAU'
""")

order_items = cursor.fetchall()
order_item_ids = [row[0] for row in order_items]

# Handle potential corruption (leading #)
clean_order_item_ids = []
for oid in order_item_ids:
    clean_id = oid.lstrip('#').strip()
    clean_order_item_ids.append(clean_id)

print("__RESULT__:")
print(json.dumps({
    "original_order_items": order_items,
    "order_item_ids": order_item_ids,
    "clean_order_item_ids": clean_order_item_ids,
    "count": len(order_items)
}))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'Id': '802Wt0000078wz5IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078xAAIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt0000078yXiIAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt00000790WEIAY', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000792gDIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000792zTIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '#802Wt0000079315IAA', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000793sTIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794F3IAI', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '802Wt00000794F4IAI', 'Product2Id': '01tWt000006hV8LIAU'}], 'var_functions.list_db:4': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript']}

exec(code, env_args)
