code = """import json
import pandas as pd

# Load metadata results from the stored JSON file path
metadata_path = var_call_PuI7iPprQ9NBMj6kaNMHLErf
with open(metadata_path, 'r') as f:
    metadata = json.load(f)

articles = var_call_zijDf7GOXeIv4G4Uhu9hmaty

# Create DataFrames
df_meta = pd.DataFrame(metadata)
df_articles = pd.DataFrame(articles)

# Ensure article_id types match
# They appear to be strings in both datasets; if not, convert to string
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge metadata with articles
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Classification keywords
sports_kw = [
    'football','soccer','world cup','match','goal','olympic','olympics','nba','mlb','nfl',
    'cricket','tennis','golf','fifa','goalkeeper','score','hat-trick','final','semi-final'
]
business_kw = [
    'stock','stocks','market','markets','economy','economic','bank','banks','investment',
    'investor','investors','billion','million','company','companies','business','trade',
    'oil prices','oil','merger','acquisition','revenue','dow','nasdaq','s&p','profit'
]
sci_kw = [
    'technology','tech','scientist','research','nasa','space','scientists','software','computer',
    'ai','artificial intelligence','robot','google','facebook','iphone','android','device','laboratory',
    'scientific','study','researchers'
]

def classify(row):
    text = ''
    if pd.notna(row.get('title')):
        text += row['title'] + ' '
    if pd.notna(row.get('description')):
        text += row['description']
    text = text.lower()
    # If no text, return None to indicate unknown
    if not text.strip():
        return None
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in business_kw:
        if kw in text:
            return 'Business'
    for kw in sci_kw:
        if kw in text:
            return 'Science/Technology'
    return 'World'

# Classify articles
df['category'] = df.apply(classify, axis=1)

# Filter to 2015 just in case
df['year'] = pd.to_datetime(df['publication_date'], errors='coerce').dt.year
df2015 = df[df['year'] == 2015]

# Consider only classified articles (exclude None)
df2015_class = df2015[df2015['category'].notna()]

# Count World articles by region
world_counts = df2015_class[df2015_class['category'] == 'World'].groupby('region').size().reset_index(name='count')

if world_counts.empty:
    result = {"top_regions": [], "count": 0, "answer": "No classified World articles found for 2015."}
else:
    max_count = int(world_counts['count'].max())
    top_regions = world_counts[world_counts['count'] == max_count]['region'].tolist()
    answer_text = f"{', '.join(top_regions)} published the largest number of World articles in 2015 with {max_count} articles."
    result = {"top_regions": top_regions, "count": max_count, "answer": answer_text}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_PuI7iPprQ9NBMj6kaNMHLErf': 'file_storage/call_PuI7iPprQ9NBMj6kaNMHLErf.json', 'var_call_zijDf7GOXeIv4G4Uhu9hmaty': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
