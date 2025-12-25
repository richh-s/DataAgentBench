code = """import json
import pandas as pd
import re

# Metadata file path
path_meta = locals()['var_function-call-2680107260476408076']
# Articles file path
path_articles = locals()['var_function-call-1953247370218847689']

# Load Metadata
with open(path_meta, 'r') as f:
    meta_data = json.load(f)

# Load Articles
with open(path_articles, 'r') as f:
    articles_data = json.load(f)

# Create DataFrames
df_meta = pd.DataFrame(meta_data)
df_articles = pd.DataFrame(articles_data)

# Normalize article_id to string
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='inner')

# Add Year
df['year'] = pd.to_datetime(df['publication_date']).dt.year

# Fill NaNs
df['title'] = df['title'].fillna('')
df['description'] = df['description'].fillna('')

# Define Keywords
keywords = {
    'Business': [
        'business', 'economy', 'economic', 'financial', 'finance', 'market', 'markets', 'stock', 'stocks', 'trade', 
        'investment', 'investor', 'investors', 'bank', 'banks', 'banking', 'corporate', 'company', 'companies', 'firm', 'firms', 'industry', 
        'profit', 'profits', 'loss', 'losses', 'revenue', 'oil', 'energy', 'price', 'prices', 'dollar', 'euro', 'currency', 'tax', 
        'jobs', 'unemployment', 'recession', 'growth', 'deal', 'merger', 'acquisition', 'ipo', 
        'ceo', 'cfo', 'fed', 'federal reserve', 'rates', 'loan', 'credit', 'bond', 'bonds', 'debt', 'crisis', 
        'budget', 'consumer', 'spending', 'retail', 'sales', 'earnings', 'forecast', 'nasdaq', 
        'dow', 's&p', 'wall st', 'wall street', 'imf', 'wto', 'treasury', 'mortgage', 'assets', 'funds', 'insurance'
    ],
    'SciTech': [
        'science', 'technology', 'tech', 'computer', 'software', 'hardware', 'internet', 'web', 
        'online', 'space', 'nasa', 'launch', 'orbit', 'moon', 'mars', 'galaxy', 'universe', 
        'biology', 'physics', 'chemistry', 'research', 'study', 'scientist', 'discovery', 
        'innovation', 'mobile', 'phone', 'app', 'google', 'microsoft', 'apple', 'facebook', 
        'amazon', 'intel', 'chip', 'processor', 'server', 'network', 'wireless', 'broadband', 
        'virus', 'hacker', 'security', 'robot', 'ai', 'artificial intelligence', 'genetics', 
        'dna', 'stem cell', 'climate', 'global warming', 'environment', 'browser', 'search engine',
        'videogame', 'gaming', 'console'
    ],
    'Sports': [
        'sport', 'sports', 'game', 'games', 'match', 'matches', 'team', 'teams', 'player', 'players', 'coach', 'win', 'lose', 'draw', 'score', 
        'goal', 'goals', 'point', 'points', 'cup', 'league', 'championship', 'tournament', 'olympic', 'olympics', 'medal', 
        'race', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'cricket', 
        'rugby', 'hockey', 'stadium', 'athlete', 'f1', 'formula one', 'nfl', 'nba', 'mlb'
    ],
    'World': [
        'world', 'war', 'peace', 'conflict', 'military', 'army', 'troops', 'soldier', 'soldiers', 'police', 
        'attack', 'attacks', 'bomb', 'blast', 'kill', 'killed', 'die', 'died', 'dead', 'injure', 'injured', 'wound', 'wounded', 'crash', 'disaster', 
        'earthquake', 'flood', 'storm', 'fire', 'politics', 'political', 'government', 'president', 
        'minister', 'leader', 'election', 'vote', 'poll', 'campaign', 'party', 'democrat', 
        'republican', 'senate', 'congress', 'parliament', 'law', 'court', 'trial', 'judge', 
        'prison', 'jail', 'crime', 'murder', 'kidnap', 'hostage', 'terror', 'iraq', 'iran', 
        'afghanistan', 'syria', 'israel', 'palestine', 'china', 'russia', 'eu', 'un', 
        'united nations', 'nato', 'treaty', 'diplomat'
    ]
}

regex_map = {}
for cat, words in keywords.items():
    # Use lookbehind/lookahead for word boundaries
    # Note: re.escape escapes space to '\ ', which is fine.
    # But we want to allow spaces in multi-word keywords.
    # pattern = (?<!\w)(word1|word2)(?!\w)
    pattern = r'(?<!\w)(' + '|'.join(map(re.escape, words)) + r')(?!\w)'
    regex_map[cat] = re.compile(pattern, re.IGNORECASE)

def classify(row):
    text = (str(row['title']) + " " + str(row['description']))
    scores = {}
    for cat, regex in regex_map.items():
        scores[cat] = len(regex.findall(text))
    
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return 'Unknown'
    return best_cat

df['category'] = df.apply(classify, axis=1)

business_df = df[df['category'] == 'Business']

# Group by Year
yearly_counts = business_df.groupby('year').size()

# Years range 2010-2020
all_years = range(2010, 2021)
yearly_counts = yearly_counts.reindex(all_years, fill_value=0)

avg = yearly_counts.mean()

print("__RESULT__:")
print(json.dumps({
    "average": avg,
    "yearly_counts": yearly_counts.to_dict(),
    "count_business": len(business_df),
    "count_total": len(df)
}))"""

env_args = {'var_function-call-2680107260476408076': 'file_storage/function-call-2680107260476408076.json', 'var_function-call-13397356953059300154': 'file_storage/function-call-13397356953059300154.json', 'var_function-call-1670274316384238860': 14860, 'var_function-call-1875156488519907562': {'min': 3, 'max': 127583}, 'var_function-call-1443102593717289086': [{'_id': '6944cdeaa22edcf3f63727c7', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944cdeaa22edcf3f63727cd', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '6944cdeaa22edcf3f63727d1', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6944cdeaa22edcf3f63727d2', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '6944cdeaa22edcf3f63727d9', 'article_id': '21', 'title': 'Eurozone economy keeps growing', 'description': 'Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.'}], 'var_function-call-18301044853391582882': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7109915908133143421': {'meta_type': "<class 'str'>", 'articles_type': "<class 'list'>", 'meta_val_preview': 'file_storage/function-call-2680107260476408076.json', 'articles_val_preview': '[{\'article_id\': \'0\', \'title\': \'Wall St. Bears Claw Back Into the Black (Reuters)\', \'description\': "R'}, 'var_function-call-1953247370218847689': 'file_storage/function-call-1953247370218847689.json', 'var_function-call-10705749776945302881': {'average': 0.0, 'yearly_counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}, 'count_business': 0, 'count_total': 14860}, 'var_function-call-10508084062561316541': [{'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.', 'scores': {'Business': 0}}, {'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again.", 'scores': {'Business': 0}}, {'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators.", 'scores': {'Business': 0}}, {'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap.", 'scores': {'Business': 0}}, {'title': 'Eurozone economy keeps growing', 'description': 'Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.', 'scores': {'Business': 0}}], 'var_function-call-3792131773513156295': {'text': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'pattern': '\x08(oil)\x08', 'matches': [], 'count': 0}, 'var_function-call-14851872805890418549': {'raw_matches': [], 'no_raw_matches': [], 'simple_matches': ['Oil']}, 'var_function-call-16956484020735252992': {'pattern': '(?:^|\\W)(oil)(?:$|\\W)', 'matches': ['Oil']}, 'var_function-call-16712277931458078396': {'pattern': '(?<!\\w)(oil)(?!\\w)', 'matches': ['Oil']}}

exec(code, env_args)
