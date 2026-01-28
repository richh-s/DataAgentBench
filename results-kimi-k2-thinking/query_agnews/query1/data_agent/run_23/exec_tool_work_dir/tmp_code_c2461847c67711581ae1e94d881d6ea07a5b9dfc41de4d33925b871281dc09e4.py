code = """import json
import re

# Load the full result from the file path stored in variable var_functions.query_db:5
file_path = var_functions.query_db:5

# Read the JSON file
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define sports keywords (case-insensitive)
sports_keywords = [
    'sport', 'sports', 'football', 'soccer', 'basketball', 'baseball',
    'tennis', 'golf', 'cricket', 'rugby', 'hockey', 'NFL', 'NBA', 'MLB', 'NHL',
    'Olympics', 'Olympic', 'World Cup', 'champion', 'race', 'racing',
    'marathon', 'athlete', 'athletes', 'team', 'league', 'cup', 'final',
    'semi-final', 'quarter-final'
]

# Compile a regex for word boundaries for each keyword
# Use case-insensitive matching
regex = re.compile(r'\b(' + '|'.join(re.escape(k) for k in sports_keywords) + r')\b', re.IGNORECASE)

# Filter sports articles
sports_articles = []
for article in articles:
    title = article.get('title', '')
    description = article.get('description', '')
    text = f"{title} {description}"
    if regex.search(text):
        sports_articles.append(article)

# Compute description length for each sports article
max_len = -1
best_title = None
best_article = None
for article in sports_articles:
    desc = article.get('description', '')
    length = len(desc)
    if length > max_len:
        max_len = length
        best_title = article.get('title')
        best_article = article

# Prepare result dictionary
result = {
    'sports_articles_count': len(sports_articles),
    'best_title': best_title,
    'best_description_length': max_len,
    'best_article': best_article
}

# Print as required
print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969718be0a121f2e78a5337', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969718be0a121f2e78a5338', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969718be0a121f2e78a5339', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969718be0a121f2e78a533a', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969718be0a121f2e78a533b', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
