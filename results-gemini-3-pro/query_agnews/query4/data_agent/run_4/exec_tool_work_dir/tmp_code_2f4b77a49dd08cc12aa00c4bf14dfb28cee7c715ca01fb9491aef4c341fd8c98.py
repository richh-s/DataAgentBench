code = """import json
import collections

with open(locals()['var_function-call-9481774673941223282'], 'r') as f:
    sqlite_data = json.load(f)

with open(locals()['var_function-call-17773819078785154740'], 'r') as f:
    mongo_data = json.load(f)

mongo_lookup = {item['article_id']: (item.get('title', ''), item.get('description', '')) for item in mongo_data}

keywords = {
    'World': set([
        "government", "president", "minister", "police", "military", "war", "iraq", "israel", "palestinian", 
        "bomb", "killed", "united nations", "country", "peace", "official", "state", "election", "protest", 
        "china", "russia", "iran", "afghanistan", "attack", "force", "security", "nuclear", "syria", "korea", 
        "yemen", "egypt", "lebanon", "pakistan", "india", "baghdad", "gaza", "troops", "soldiers", "rebel", 
        "blast", "suicide", "politics", "parliament", "senate", "vote", "party", "leader", "crisis", "talks", 
        "treaty", "diplomat", "foreign", "international", "putin", "beijing", "africa", "sudan", "darfur", 
        "zimbabwe", "kabul", "kashmir", "indonesia", "earthquake", "tsunami", "storm", "hurricane", "typhoon", 
        "collision", "crash", "hostage", "terror", "al qaeda", "bin laden", "prime minister", "premier",
        "sharon", "arafat", "blair", "bush", "kerry", "clinton", "obama", "isis", "islamic state", "refugee", 
        "migrant", "eu", "european union", "greece", "greek", "ukraine", "kiev", "crimea", "nepal", "kathmandu",
        "yemen", "saudi", "arabia", "turkey", "erdogan", "merkel", "hollande", "cameron", "modi", "xi jinping",
        "boko haram", "nigeria", "kenya", "somalia", "libya", "venezuela", "brazil", "argentina", "colombia",
        "mexico", "chile", "peru", "thailand", "bangkok", "myanmar", "rohingya", "malaysia", "flight", "mh370",
        "ebola", "virus" # Ebola was big in World news
    ]),
    'Sports': set([
        "game", "team", "win", "season", "score", "cup", "league", "player", "coach", "olympic", "champion", 
        "football", "baseball", "basketball", "soccer", "tennis", "hockey", "gold", "medal", "sport", "f1", 
        "racing", "athlete", "tournament", "match", "victory", "defeat", "club", "nfl", "nba", "mlb", "nhl", 
        "fifa", "uefa", "wimbledon", "open", "grand slam", "ball", "run", "goal", "touchdown", "points", 
        "sox", "yankees", "mets", "giants", "patriots", "jets", "knicks", "rangers", "bulls", "lakers", 
        "barcelona", "real madrid", "messi", "ronaldo", "world cup", "super bowl"
    ]),
    'Business': set([
        "company", "stock", "market", "profit", "loss", "percent", "dollar", "bank", "economy", "trade", 
        "corp", "inc", "shares", "price", "invest", "sale", "ceo", "oil", "gas", "energy", "finance", 
        "money", "deal", "merger", "acquisition", "buy", "sell", "ipo", "revenue", "earnings", "quarter", 
        "wall st", "dow", "nasdaq", "fed", "rates", "interest", "bond", "currency", "euro", "yen", "manager", 
        "business", "industry", "airline", "boeing", "airbus", "ford", "gm", "toyota", "sales", "gdp", 
        "inflation", "deflation", "central bank", "imf", "ecb"
    ]),
    'Sci/Tech': set([
        "technology", "computer", "software", "internet", "google", "microsoft", "apple", "space", "nasa", 
        "science", "research", "study", "phone", "chip", "web", "online", "virus", "launch", "linux", 
        "windows", "browser", "search", "engine", "network", "wireless", "mobile", "server", "digital", 
        "device", "gadget", "screen", "pixel", "memory", "storage", "data", "robot", "orbit", "moon", "mars", 
        "galaxy", "astronomy", "physics", "biology", "health", "disease", "cancer", "medical", "drug", 
        "fda", "study", "scientists", "users", "facebook", "twitter", "amazon", "uber"
    ])
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in keywords}
    
    for cat, kws in keywords.items():
        for kw in kws:
            if kw in text:
                 # Simple substring match
                 scores[cat] += 1
    
    # Weight adjustments
    if "oil" in text and ("prices" in text or "barrel" in text):
        scores['Business'] += 2
    if "iraq" in text or "syria" in text:
        scores['World'] += 2
    if "olympic" in text:
        scores['Sports'] += 5
    if "apple" in text and "ipod" in text:
        scores['Sci/Tech'] += 2
    
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return None
    return best_cat

region_counts = collections.defaultdict(int)

for record in sqlite_data:
    aid = record['article_id']
    region = record['region']
    
    if aid in mongo_lookup:
        title, desc = mongo_lookup[aid]
        full_text = f"{title} {desc}"
        category = classify(full_text)
        
        if category == 'World':
            region_counts[region] += 1

print("__RESULT__:")
print(json.dumps(region_counts))"""

env_args = {'var_function-call-5603379809440090295': ['authors', 'article_metadata'], 'var_function-call-5603379809440088388': ['articles'], 'var_function-call-7811902432841330022': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-7811902432841330007': [{'_id': '6944ece6af7b411e49d540f7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944ece6af7b411e49d540f8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944ece6af7b411e49d540f9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944ece6af7b411e49d540fa', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944ece6af7b411e49d540fb', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-2005858685656178700': [{'count(*)': '6696'}], 'var_function-call-7188942272774877746': [{'_id': '6944ece6af7b411e49d540f7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944ece6af7b411e49d540f8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944ece6af7b411e49d540f9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944ece6af7b411e49d540fa', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944ece6af7b411e49d540fb', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9481774673941223282': 'file_storage/function-call-9481774673941223282.json', 'var_function-call-14567244081031398768': [{'_id': '6944ece6af7b411e49d540f7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944ece6af7b411e49d540f8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944ece6af7b411e49d540f9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944ece6af7b411e49d540fa', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944ece6af7b411e49d540fb', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17773819078785154740': 'file_storage/function-call-17773819078785154740.json', 'var_function-call-13901013144232453965': {'Asia': 460, 'South America': 464, 'North America': 439, 'Europe': 445, 'Africa': 453}}

exec(code, env_args)
