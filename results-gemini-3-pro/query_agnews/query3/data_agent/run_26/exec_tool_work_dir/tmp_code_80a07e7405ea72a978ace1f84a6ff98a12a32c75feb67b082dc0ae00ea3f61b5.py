code = """import json

# Load the result from the previous query
with open('var_function-call-8881788724553702350', 'r') as f:
    articles_metadata = json.load(f)

# Extract article IDs and create a mapping of ID to year
article_ids = []
id_to_year = {}

for item in articles_metadata:
    # article_id comes as string in the preview but the DB description says int. 
    # The preview shows "3", "9". Let's handle both just in case, but probably should be int for Mongo query if description is right.
    # However, description says "article_id (int)" for Mongo too.
    # But preview shows strings. Let's convert to int.
    try:
        aid = int(item['article_id'])
        article_ids.append(aid)
        id_to_year[aid] = int(item['publication_date'][:4])
    except ValueError:
        pass

# Prepare the list for the next step
print("__RESULT__:")
print(json.dumps({"article_ids": article_ids, "id_to_year": id_to_year}))"""

env_args = {'var_function-call-12051989784931741793': ['authors', 'article_metadata'], 'var_function-call-8881788724553702350': 'file_storage/function-call-8881788724553702350.json'}

exec(code, env_args)
