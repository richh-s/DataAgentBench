code = """import json
import pandas as pd
import re
import random

# Load data (assuming previous variables are still available in this session context? No, `execute_python` is stateless except for storage keys?
# No, the prompt says "All previous tool results are available as variables". But the *local variables* from previous `execute_python` calls are NOT persisted.
# I must reload the data or use the storage keys again.
# Wait, I didn't save the merged dataframe. I have to redo the loading and merging.

meta_path = locals()['var_function-call-230048583216778633']
with open(meta_path, 'r') as f:
    metadata_records = json.load(f)
df_meta = pd.DataFrame(metadata_records)
df_meta['article_id'] = df_meta['article_id'].astype(int)

articles_path = locals()['var_function-call-2198657140293455711']
with open(articles_path, 'r') as f:
    articles_records = json.load(f)
df_articles = pd.DataFrame(articles_records)
df_articles['article_id'] = df_articles['article_id'].astype(int)

df = pd.merge(df_meta, df_articles, on='article_id', how='inner')

def classify(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    keywords = {
        'World': [
            "war", "peace", "government", "president", "minister", "military", "bomb", "kill", "attack", "treaty", "un", "united nations", 
            "country", "international", "foreign", "policy", "iraq", "syria", "iran", "israel", "palestine", "russia", "china", "europe", 
            "africa", "asia", "rebel", "crisis", "refugee", "election", "parliament", "leader", "official", "troops", "police", "protest", 
            "court", "law", "nuclear", "blast", "disaster", "storm", "hurricane", "earthquake", "rescue", "aid", "hostage", "terror", "vote", 
            "party", "talks", "agreement", "summit", "border", "nation", "state", "region", "global", "nato", "gaza", "afghanistan", "pakistan",
            "baghdad", "kabul", "tehran", "jerusalem", "beijing", "moscow", "london", "paris", "berlin", "tokyo", "washington", "prime minister",
            "senate", "congress", "diplomat", "embassy", "suicide", "explosion", "crash"
        ],
        'Business': [
            "market", "stock", "dow", "nasdaq", "wall street", "dollar", "euro", "yen", "economy", "finance", "bank", "fed", "rate", 
            "inflation", "deficit", "budget", "profit", "earnings", "revenue", "loss", "sales", "trade", "company", "firm", "business", 
            "industry", "oil", "gas", "price", "cost", "deal", "merger", "acquisition", "bid", "share", "investor", "ceo", "executive", 
            "manager", "job", "unemployment", "labor", "work", "corp", "inc", "ltd", "airline", "boeing", "airbus", "ford", "gm", "toyota", 
            "microsoft", "google", "apple", "intel", "ibm", "oracle", "wal-mart", "retail", "store"
        ],
        'Sports': [
            "game", "match", "score", "win", "loss", "team", "player", "coach", "cup", "league", "season", "champion", "olympic", "medal", 
            "stadium", "club", "ball", "sport", "race", "f1", "tennis", "football", "soccer", "basketball", "baseball", "cricket", "hockey", 
            "golf", "rugby", "boxing", "athlete", "tournament", "round", "final", "semi", "quarter", "playoff", "nba", "nfl", "nhl", "mlb", 
            "fifa", "uefa", "olympics", "gold", "silver", "bronze", "record", "world cup"
        ],
        'Sci/Tech': [
            "technology", "science", "research", "study", "space", "nasa", "launch", "computer", "software", "internet", "web", "phone", 
            "mobile", "virus", "discovery", "drug", "health", "hospital", "patient", "disease", "treatment", "doctor", "biology", "physics", 
            "chemistry", "chip", "server", "linux", "windows", "browser", "search engine", "online", "digital", "network", "satellite", 
            "telescope", "mars", "moon", "orbit", "robot", "gadget", "device", "screen", "monitor", "keyboard", "mouse", "hacker", "spam",
            "security", "patch", "update", "version", "release", "beta"
        ]
    }
    scores = {cat: 0 for cat in keywords}
    tokens = re.findall(r'\w+', text)
    for token in tokens:
        for cat, kws in keywords.items():
            if token in kws:
                scores[cat] += 1
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return "Unknown"
    return best_cat

df['category'] = df.apply(classify, axis=1)

world_sample = df[df['category'] == 'World'].sample(5)[['title', 'description']].to_dict(orient='records')
business_sample = df[df['category'] == 'Business'].sample(5)[['title', 'description']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps({"World": world_sample, "Business": business_sample}))"""

env_args = {'var_function-call-230048583216778633': 'file_storage/function-call-230048583216778633.json', 'var_function-call-8260068931381035711': {'count': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97], 'regions': ['Europe', 'South America', 'Africa', 'Asia', 'North America']}, 'var_function-call-7380412333144670889': {'min_id': 13, 'max_id': 127570, 'count': 6696}, 'var_function-call-7005320274688524134': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13531593010111911559': {'count': 5, 'sample': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}, 'var_function-call-864367092588596787': [], 'var_function-call-2764836307452452932': [{'_id': '69451f0991224f9718080b40', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_function-call-2198657140293455711': 'file_storage/function-call-2198657140293455711.json', 'var_function-call-5208470535368002308': {'Africa': 439, 'South America': 431, 'Europe': 429, 'Asia': 426, 'North America': 420}}

exec(code, env_args)
