code = """import json
import pandas as pd

# Load previous tool results from storage variables
metadata_path = var_call_j3FSFf3NaDh9P3rUdbvC77K1
with open(metadata_path, 'r') as f:
    metadata = json.load(f)
articles = var_call_rFEqCPCfyDZhO118dvWSs1D4

# Create DataFrames
df_meta = pd.DataFrame(metadata)
df_articles = pd.DataFrame(articles)

# Ensure article_id are strings
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge metadata for 2015 with article content
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Classification keywords
world_kw = [
    'president','election','elections','government','minister','foreign','diplomat','diplomacy',
    'united nations','un ','un.', 'refugee','war','attack','bomb','killed','clash','protest','protests',
    'crisis','ceasefire','isis','al qaeda','rebels','soldier','military','border','sanctions','summit',
    'china','russia','iraq','syria','afghanistan','country','countries','international','world','global'
]

sports_kw = ['win','wins','beat','defeat','defeated','match','goal','scored','season','tournament','championship','fifa','nba','mlb','soccer','football','rugby','cricket']

business_kw = ['stock','stocks','market','economy','economies','shares','company','companies','firm','investment','investors','ipo','merger','bank','oil','business','earnings']

tech_kw = ['technology','tech','scientist','research','nasa','space','robot','software','computer','internet','study','scientific','ai']

# Lowercase text for matching
def classify(row):
    text = ''
    if pd.notnull(row.get('title')):
        text += str(row['title']).lower() + ' '
    if pd.notnull(row.get('description')):
        text += str(row['description']).lower()
    # check categories in priority: Sports, Business, Science/Technology, World
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in business_kw:
        if kw in text:
            return 'Business'
    for kw in tech_kw:
        if kw in text:
            return 'Science/Technology'
    for kw in world_kw:
        if kw in text:
            return 'World'
    # fallback: World
    return 'World'

# Apply classification
df['category'] = df.apply(classify, axis=1)

# Filter to World articles
df_world = df[df['category'] == 'World']

# Count by region
counts = df_world.groupby('region').size().to_dict()

if counts:
    # find max
    max_count = max(counts.values())
    top_regions = [r for r,c in counts.items() if c == max_count]
    # If single, return string, else list
    region_result = top_regions[0] if len(top_regions)==1 else top_regions
else:
    max_count = 0
    region_result = None

result = {'region': region_result, 'count': int(max_count), 'counts_by_region': counts}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GYWg58yjXKSEJU7oy1tqxXeD': ['articles'], 'var_call_pvGQK9Bf2t4dJdPaChWjzW21': ['authors', 'article_metadata'], 'var_call_j3FSFf3NaDh9P3rUdbvC77K1': 'file_storage/call_j3FSFf3NaDh9P3rUdbvC77K1.json', 'var_call_rFEqCPCfyDZhO118dvWSs1D4': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
