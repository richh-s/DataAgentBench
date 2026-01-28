code = """import json
from datetime import datetime, timedelta

# Extract OrderItem IDs for SecureAnalytics Pro
order_items = [
 {"Id": "#802Wt0000078yuGIAQ", "OrderId": "801Wt00000PGdVHIA1", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "8.0"},
 {"Id": "802Wt00000790mOIAQ", "OrderId": "#801Wt00000PHQuGIAX", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "30.0"},
 {"Id": "802Wt00000790zGIAQ", "OrderId": "#801Wt00000PGc9QIAT", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "6.0"},
 {"Id": "802Wt00000794F2IAI", "OrderId": "801Wt00000PHLzOIAX", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "2.0"},
 {"Id": "802Wt000007968eIAA", "OrderId": "801Wt00000PH4FLIA1", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "2.0"},
 {"Id": "802Wt00000796bfIAA", "OrderId": "801Wt00000PGRh3IAH", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "3.0"},
 {"Id": "802Wt00000796qFIAQ", "OrderId": "801Wt00000PHRdKIAX", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "7.0"},
 {"Id": "802Wt0000079734IAA", "OrderId": "#801Wt00000PGu6KIAT", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "1.0"},
 {"Id": "802Wt00000797W5IAI", "OrderId": "801Wt00000PHWZlIAP", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "20.0"},
 {"Id": "802Wt00000797awIAA", "OrderId": "801Wt00000PGdVGIA1", "Product2Id": "#01tWt000006hVJdIAM", "Quantity": "10.0"},
 {"Id": "802Wt00000797z7IAA", "OrderId": "801Wt00000PGos9IAD", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "1.0"},
 {"Id": "#802Wt00000798VPIAY", "OrderId": "#801Wt00000PGdjoIAD", "Product2Id": "#01tWt000006hVJdIAM", "Quantity": "10.0"},
 {"Id": "802Wt00000798YdIAI", "OrderId": "801Wt00000PH8yvIAD", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "30.0"},
 {"Id": "802Wt00000798okIAA", "OrderId": "#801Wt00000PGVJJIA5", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "1.0"},
 {"Id": "#802Wt00000799o1IAA", "OrderId": "#801Wt00000PGoc0IAD", "Product2Id": "#01tWt000006hVJdIAM", "Quantity": "19.0"},
 {"Id": "802Wt0000079A2bIAE", "OrderId": "801Wt00000PGe00IAD", "Product2Id": "#01tWt000006hVJdIAM", "Quantity": "12.0"},
 {"Id": "802Wt0000079ACGIA2", "OrderId": "#801Wt00000PGSYIIA5", "Product2Id": "#01tWt000006hVJdIAM", "Quantity": "20.0"},
 {"Id": "802Wt0000079B0EIAU", "OrderId": "801Wt00000PHHMIIA5", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "6.0"},
 {"Id": "802Wt0000079B6gIAE", "OrderId": "#801Wt00000PHQz1IAH", "Product2Id": "#01tWt000006hVJdIAM", "Quantity": "4.0"}
]

# Extract all unique order item IDs (both with and without # prefix)
order_item_ids = []
for item in order_items:
    order_item_ids.append(item["Id"])
    # Also add version without prefix if it has one, and vice versa
    clean_id = item["Id"].replace("#", "")
    with_prefix = "#" + clean_id if "#" not in item["Id"] else clean_id
    if clean_id not in order_item_ids:
        order_item_ids.append(clean_id)
    if with_prefix not in order_item_ids and with_prefix != clean_id:
        order_item_ids.append(with_prefix)

# Create a WHERE clause for order_item_id__c
order_item_list = "'" + "','".join(order_item_ids) + "'"
print('__RESULT__:')
print(json.dumps({"order_item_ids": order_item_ids[:5], "total": len(order_item_ids), "format_example": order_item_list[:100]}))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro', 'Description': 'Data analytics platform with enhanced focus on security and compliance.'}], 'var_functions.list_db:8': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:10': [{'id': '#500Wt00000DDDfwIAH', 'subject': 'Feature Update Notifications Lack', 'createddate': '2023-07-02T11:00:00.000+0000', 'orderitemid__c': '802Wt00000797r4IAA'}, {'id': '500Wt00000DDDtTIAX', 'subject': 'Missing Feature Update Alerts', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDNYoIAP', 'subject': 'Delayed Support Response ', 'createddate': '2023-09-30T11:30:00.000+0000', 'orderitemid__c': '802Wt00000792tiIAA'}, {'id': '500Wt00000DDPIsIAP', 'subject': 'AI Feature Malfunction', 'createddate': '2022-08-05T14:30:00.000+0000', 'orderitemid__c': '802Wt00000797r3IAA'}, {'id': '500Wt00000DDPM6IAP', 'subject': 'Access Issues with Training Module', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDPSZIA5', 'subject': 'Slow Reply from Support Team', 'createddate': '2023-10-02T14:15:00.000+0000', 'orderitemid__c': '802Wt00000792tiIAA'}, {'id': '500Wt00000DDPZ0IAP', 'subject': 'Scaling Difficulties ', 'createddate': '2022-04-18T10:30:00.000+0000', 'orderitemid__c': '802Wt0000078xAFIAY'}, {'id': '500Wt00000DDPsOIAX', 'subject': 'EcoPCB Data Integration Error', 'createddate': '2021-07-06T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079ATyIAM'}, {'id': '500Wt00000DDPsPIAX', 'subject': 'Customization Issue', 'createddate': '2023-04-05T17:51:00.000+0000', 'orderitemid__c': '802Wt00000794bXIAQ'}, {'id': '500Wt00000DDQRsIAP', 'subject': 'Scalability Issue', 'createddate': '2023-03-08T06:49:00.000+0000', 'orderitemid__c': '802Wt00000796yFIAQ'}], 'var_functions.execute_python:12': {'start_date': '2020-06-10T00:00:00', 'end_date': '2021-04-10T00:00:00'}, 'var_functions.list_db:14': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:16': [{'Id': '#802Wt0000078yuGIAQ', 'OrderId': '801Wt00000PGdVHIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '8.0'}, {'Id': '802Wt00000790mOIAQ', 'OrderId': '#801Wt00000PHQuGIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '30.0'}, {'Id': '802Wt00000790zGIAQ', 'OrderId': '#801Wt00000PGc9QIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '6.0'}, {'Id': '802Wt00000794F2IAI', 'OrderId': '801Wt00000PHLzOIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0'}, {'Id': '802Wt000007968eIAA', 'OrderId': '801Wt00000PH4FLIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0'}, {'Id': '802Wt00000796bfIAA', 'OrderId': '801Wt00000PGRh3IAH', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '3.0'}, {'Id': '802Wt00000796qFIAQ', 'OrderId': '801Wt00000PHRdKIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '7.0'}, {'Id': '802Wt0000079734IAA', 'OrderId': '#801Wt00000PGu6KIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0'}, {'Id': '802Wt00000797W5IAI', 'OrderId': '801Wt00000PHWZlIAP', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '20.0'}, {'Id': '802Wt00000797awIAA', 'OrderId': '801Wt00000PGdVGIA1', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '10.0'}, {'Id': '802Wt00000797z7IAA', 'OrderId': '801Wt00000PGos9IAD', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0'}, {'Id': '#802Wt00000798VPIAY', 'OrderId': '#801Wt00000PGdjoIAD', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '10.0'}, {'Id': '802Wt00000798YdIAI', 'OrderId': '801Wt00000PH8yvIAD', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '30.0'}, {'Id': '802Wt00000798okIAA', 'OrderId': '#801Wt00000PGVJJIA5', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0'}, {'Id': '#802Wt00000799o1IAA', 'OrderId': '#801Wt00000PGoc0IAD', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '19.0'}, {'Id': '802Wt0000079A2bIAE', 'OrderId': '801Wt00000PGe00IAD', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '12.0'}, {'Id': '802Wt0000079ACGIA2', 'OrderId': '#801Wt00000PGSYIIA5', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '20.0'}, {'Id': '802Wt0000079B0EIAU', 'OrderId': '801Wt00000PHHMIIA5', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '6.0'}, {'Id': '802Wt0000079B6gIAE', 'OrderId': '#801Wt00000PHQz1IAH', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '4.0'}]}

exec(code, env_args)
