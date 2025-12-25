code = """import pandas as pd
import json

# Read the full articles data from the file
with open(locals()['var_function-call-6209549211058515819'], 'r') as f:
    articles_data = json.load(f)

df_articles = pd.DataFrame(articles_data)

# Convert article_id to int for consistent merging
df_articles['article_id'] = df_articles['article_id'].astype(int)

# Define keywords for the "World" category (case-insensitive)
world_keywords = ['world', 'global', 'international', 'foreign affairs', 'countries', 'nations', 'peace', 'war', 'conflict', 'diplomacy', 'un', 'eu', 'nato', 'africa', 'asia', 'europe', 'america', 'middle east']

# Function to check if an article belongs to the "World" category
def is_world_article(title, description):
    text = (str(title) + " " + str(description)).lower()
    for keyword in world_keywords:
        if keyword in text:
            return True
    return False

# Filter articles into the "World" category
df_world_articles = df_articles[df_articles.apply(lambda row: is_world_article(row['title'], row['description']), axis=1)]

# Select only the article_id for world articles
world_article_ids = df_world_articles['article_id'].tolist()

print("__RESULT__:")
print(json.dumps(world_article_ids))"""

env_args = {'var_function-call-6209549211058515819': 'file_storage/function-call-6209549211058515819.json'}

exec(code, env_args)
