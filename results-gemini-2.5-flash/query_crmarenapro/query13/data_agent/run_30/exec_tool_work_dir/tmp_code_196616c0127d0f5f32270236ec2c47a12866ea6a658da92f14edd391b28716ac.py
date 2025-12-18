code = """import json

pricebook_entry_ids_data = locals()['var_function-call-7477208485156344770']['results']
pricebook_entry_ids = [item['PricebookEntryId'] for item in pricebook_entry_ids_data]

# Prepare the list of IDs for the SQL IN clause
ids_tuple = tuple(pricebook_entry_ids)

# The tuple needs to be a string to be passed into the SQL query.
# If it is a single element, it should be represented as ('id',)
# If it is multiple elements, it should be represented as ('id1', 'id2')
# If it is empty, this query should not be executed
if not ids_tuple:
    pricebook_entry_ids_sql = "('')"
elif len(ids_tuple) == 1:
    pricebook_entry_ids_sql = f"('{ids_tuple[0]}')"
else:
    pricebook_entry_ids_sql = str(ids_tuple)

query = f"""
    SELECT
        REPLACE(TRIM(oi.OrderId), '#', '') AS OrderId,
        REPLACE(TRIM(o.OwnerId), '#', '') AS OwnerId,
        oi.Quantity,
        oi.UnitPrice
    FROM OrderItem oi
    JOIN "Order" o ON REPLACE(TRIM(oi.OrderId), '#', '') = REPLACE(TRIM(o.Id), '#', '')
    WHERE REPLACE(TRIM(oi.PriceBookEntryId), '#', '') IN {pricebook_entry_ids_sql};
"""

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-7477208485156344770': [{'PricebookEntryId': '01uWt0000027PDRIA2'}, {'PricebookEntryId': '01uWt0000027P8cIAE'}, {'PricebookEntryId': '01uWt0000027Q34IAE'}, {'PricebookEntryId': '01uWt0000027PjhIAE'}, {'PricebookEntryId': '01uWt0000027PJtIAM'}, {'PricebookEntryId': '01uWt0000027PIIIA2'}, {'PricebookEntryId': '01uWt0000027P5NIAU'}, {'PricebookEntryId': '01uWt0000027PIHIA2'}, {'PricebookEntryId': '01uWt0000027PtOIAU'}, {'PricebookEntryId': '01uWt0000027P8bIAE'}, {'PricebookEntryId': '01uWt0000027PLVIA2'}, {'PricebookEntryId': '01uWt0000027PBpIAM'}, {'PricebookEntryId': '01uWt0000027PGfIAM'}, {'PricebookEntryId': '01uWt0000027P3lIAE'}, {'PricebookEntryId': '01uWt0000027PTZIA2'}, {'PricebookEntryId': '01uWt0000027PVBIA2'}, {'PricebookEntryId': '01uWt0000027PF3IAM'}, {'PricebookEntryId': '01uWt0000027PADIA2'}, {'PricebookEntryId': '01uWt0000027P6zIAE'}, {'PricebookEntryId': '01uWt0000027POjIAM'}]}

exec(code, env_args)
