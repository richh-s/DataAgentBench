code = """import json
# load the QuoteLineItems stored earlier
qli = var_call_i25sxslZHda6XTnRwj17GXYS
# Convert numeric strings to numbers and compute checks
issues = []
# Load pricebook entries
pbe = var_call_GRYq4ciMS62cvPigp4QNxtom
pbe_map = {x['Id'].strip('#'): x for x in pbe}
# PricebookEntry 01uWt0000027P8bIAE was missing from query; handle
for item in qli:
    # clean ids
    pbe_id = item['PricebookEntryId'].lstrip('#')
    unit_price = float(item['UnitPrice'])
    qty = float(item['Quantity'])
    discount = float(item['Discount'])
    total_price = float(item['TotalPrice'])
    # Check discounts and large quantities
    if discount > 0:
        issues.append({'lineId': item['Id'], 'issue': 'Discount applied', 'discount': discount})
    # Compare unit price to pricebook entry if available
    pbe_entry = pbe_map.get(pbe_id)
    if pbe_entry:
        pbe_price = float(pbe_entry['UnitPrice'])
        if abs(pbe_price - unit_price) > 0.01:
            issues.append({'lineId': item['Id'], 'issue': 'Unit price mismatch', 'quote_unit': unit_price, 'pb_unit': pbe_price})
    else:
        issues.append({'lineId': item['Id'], 'issue': 'PricebookEntry missing or not found', 'PricebookEntryId': item['PricebookEntryId']})
    # Quantity limits: flag quantities > 10
    if qty > 10:
        issues.append({'lineId': item['Id'], 'issue': 'Quantity exceeds limit', 'quantity': qty})
    # Validate total price
    calc_total = round((unit_price * qty) * (1 - discount/100), 4)
    if abs(calc_total - total_price) > 0.01:
        issues.append({'lineId': item['Id'], 'issue': 'Total price mismatch', 'calc_total': calc_total, 'reported_total': total_price})

print('__RESULT__:')
print(json.dumps(issues))"""

env_args = {'var_call_i25sxslZHda6XTnRwj17GXYS': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_UBSEwzhCruvwIkjx6sEEhiRR': 'file_storage/call_UBSEwzhCruvwIkjx6sEEhiRR.json', 'var_call_UELP4a6Hx3N0cCOry9kYDBPf': 'file_storage/call_UELP4a6Hx3N0cCOry9kYDBPf.json', 'var_call_GRYq4ciMS62cvPigp4QNxtom': [{'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}], 'var_call_mo85EFalNkRNgZyOaiabqjY8': [{'Id': '01sWt000000imiTIAQ', 'Name': 'Standard Price Book', 'IsActive': '1'}], 'var_call_DS6Bk9VrCM47JZcz60HMFIAH': [], 'var_call_5zlxi95sCYynBT56J04w9h5t': {'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'faq_answer__c': "Volume-based discounts are a strategic tool for fostering customer loyalty and encouraging bulk purchases. At TechPulse Solution, we aim to provide value-added benefits to our customers, and volume-based discounts are integral to this mission. Here is a detailed overview of the volume-based discounts currently available:\n\n1. **5% Discount for Purchases Over $5**: This entry-level discount is designed for customers making modest but regular purchases. If your transaction totals $5 or more, you automatically become eligible for a 5% discount on your total purchase. This incentive is perfect for small businesses or individuals looking to maximize their purchasing power without committing to large upfront investments.\n\n2. **10% Discount for Purchases Over $10**: By increasing your purchase to $10, you can enjoy a more substantial 10% discount. This tier is targeted at growing businesses or tech enthusiasts planning for larger projects. Whether you're a startup needing essential tech solutions or an established entity upgrading current systems, this level of discount allows you to save significant amounts while meeting your needs.\n\n3. **15% Discount for Purchases Over $20**: The highest discount tier is designed for customers planning substantial investments in tech solutions. With a purchase of $20 or more, you can benefit from a generous 15% discount. This is particularly advantageous for businesses engaged in major scaling projects or for those who require extensive tech solutions for operational expansion.\n\nThese volume-based discounts are designed to reward you as you invest more in our innovative solutions, ensuring that you receive the best possible value. They are automatically applied at checkout, simplifying the purchasing process and enabling you to focus on selecting the best technology for your needs.\n\nIncorporating these discounts into your purchasing strategy can significantly reduce costs while allowing access to premium technology and support from TechPulse Solution. Whether you are a small business making selective purchases or a large company procuring extensive solutions, our discount structure provides a tailored approach to meet varying budgetary needs.\n\nOptimize your purchasing strategy and operational efficiency with our volume-based discounts, designed to bring you closer to innovative technology that can drive your success. At TechPulse Solution, your needs are at the forefront, and these carefully crafted discounts provide a pathway to affordable excellence.", 'summary': 'Volume-Based Discounts', 'urlname': '1745269013-mq1zw'}, 'var_call_uM1MgID7Zh5QwNF3M4ehzcet': 'file_storage/call_uM1MgID7Zh5QwNF3M4ehzcet.json', 'var_call_vr11zgr40FB8stTWlToRXeBH': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'summary': 'Volume-Based Discounts'}, {'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy', 'summary': 'TechPulse Solution Volume-Based Installation Timeline Policy'}, {'id': '#ka0Wt000000EnwvIAC', 'title': 'Product Quantity Limits   ', 'summary': 'Product Quantity Limits'}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'summary': 'Policy for price adjustments based on competing offers'}]}

exec(code, env_args)
