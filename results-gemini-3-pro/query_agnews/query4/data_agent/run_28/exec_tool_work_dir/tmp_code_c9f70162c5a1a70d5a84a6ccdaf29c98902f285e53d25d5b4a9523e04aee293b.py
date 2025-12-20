code = """import json
import collections

# Load Metadata
with open(locals()['var_function-call-13685975547188021313'], 'r') as f:
    metadata_list = json.load(f)

# Create a map of article_id -> region for 2015 articles
# Also keep track of relevant IDs
metadata_map = {} # article_id (str) -> region
for item in metadata_list:
    metadata_map[str(item['article_id'])] = item['region']

# Load Articles
with open(locals()['var_function-call-4632820292160960647'], 'r') as f:
    articles_list = json.load(f)

# Keywords
keywords_world = [
    "president", "minister", "parliament", "congress", "senate", "lawmaker", "governor",
    "election", "vote", "poll", "campaign",
    "war", "military", "army", "troops", "soldier", "police", "attack", "bomb", "blast", "explosion", "kill", "death", "dead", "injured", "casualty", "crash",
    "terror", "rebel", "insurgent", "militia", "guerrilla", "hostage", "kidnap",
    "peace", "treaty", "ceasefire", "negotiation", "talks", "summit", "meeting", "diplomat", "envoy", "ambassador",
    "government", "official", "authority", "state", "federal", "national",
    "united nations", "un ", "nato", "eu ", "european union", "au ", "african union",
    "court", "judge", "trial", "prison", "jail", "sentence",
    "protest", "demonstration", "strike", "riot",
    "disaster", "storm", "hurricane", "typhoon", "earthquake", "flood", "tsunami", "fire",
    "iraq", "iran", "afghanistan", "israel", "palestin", "syria", "lebanon", "egypt", "libya", "sudan", "darfur", "congo", "zimbabwe", "nigeria", "kenya", "somalia", "pakistan", "india", "kashmir", "sri lanka", "nepal", "china", "japan", "korea", "indonesia", "thailand", "philippines", "russia", "ukraine", "georgia", "chechnya", "turkey", "cyprus", "greece", "spain", "france", "germany", "britain", "uk ", "ireland", "italy", "vatican", "pope", "poland", "usa", "america", "bush", "kerry", "clinton", "obama", "putin", "blair", "chirac", "schroeder", "berlusconi", "sharon", "arafat", "abbas", "hamas", "hezbollah", "qaeda"
]

keywords_business = [
    "market", "stock", "dow jones", "nasdaq", "s&p", "ftse", "nikkei", "hang seng",
    "price", "rate", "currency", "dollar", "euro", "yen", "yuan",
    "oil", "gas", "gold", "silver", "metal", "commodity", "crude", "barrel",
    "company", "corp", "inc", "ltd", "firm", "business", "industry", "sector",
    "bank", "financial", "finance", "investment", "investor", "fund", "equity", "bond", "loan", "debt", "credit", "mortgage",
    "profit", "loss", "earning", "revenue", "sale", "income", "dividend",
    "deal", "merger", "acquisition", "buyout", "bid", "offer", "stake", "share",
    "economy", "economic", "growth", "recession", "inflation", "deflation", "gdp", "job", "employment", "unemployment", "labor", "strike", "union",
    "fed ", "federal reserve", "greenspan", "bernanke", "ecb", "central bank", "imf", "world bank", "wto",
    "ceo", "cfo", "chairman", "executive", "manager", "boss",
    "google", "microsoft", "yahoo", "apple", "ibm", "intel", "hp", "dell", "cisco", "oracle", "sony", "nokia", "motorola", "samsung", "toyota", "honda", "gm", "ford", "daimler", "chrysler", "vw", "boeing", "airbus", "wal-mart", "mcdonald", "coke", "pepsi", "pfizer", "merck"
]

keywords_tech = [
    "computer", "software", "hardware", "internet", "web", "online", "net ", "cyber", "digital",
    "technology", "tech ", "hitech", "electronics", "gadget", "device",
    "phone", "mobile", "cell", "wireless", "wifi", "bluetooth", "broadband", "dsl",
    "chip", "processor", "semiconductor",
    "server", "network", "router", "database", "data",
    "virus", "worm", "trojan", "spyware", "spam", "hacker", "security", "patch", "bug",
    "microsoft", "windows", "linux", "unix", "mac os", "apple", "ipod", "itunes", "google", "search engine", "yahoo", "amazon", "ebay",
    "space", "nasa", "shuttle", "rocket", "satellite", "orbit", "planet", "mars", "moon", "sun", "star", "galaxy", "universe", "astronomy",
    "science", "scientific", "physic", "chemist", "biolog", "genetic", "dna", "cell", "stem cell", "clone", "medical", "medicine", "drug", "cancer", "aids", "hiv", "disease", "health", "hospital", "doctor", "research", "study", "experiment", "lab "
]

keywords_sports = [
    "sport", "game", "match", "team", "player", "coach", "manager", "referee", "umpire",
    "win", "won", "winner", "victory", "beat", "defeat", "loss", "lost", "lose", "draw", "tie",
    "score", "point", "goal", "touchdown", "run", "basket",
    "cup", "trophy", "medal", "title", "championship", "tournament", "league", "season", "playoff", "final",
    "olympic", "athens", "beijing", "world cup", "euro 2004",
    "football", "soccer", "basketball", "nba", "baseball", "mlb", "hockey", "nhl", "nfl", "rugby", "cricket", "tennis", "golf", "pga", "racing", "f1", "formula one", "nascar", "cycling", "tour de france", "boxing", "swimming", "track and field", "athletics", "marathon"
]

region_counts = collections.defaultdict(int)

for article in articles_list:
    aid = str(article['article_id'])
    if aid in metadata_map:
        region = metadata_map[aid]
        
        text = (article.get('title', '') + " " + article.get('description', '')).lower()
        
        scores = {'World': 0, 'Business': 0, 'Sci/Tech': 0, 'Sports': 0}
        
        for kw in keywords_world:
            if kw in text: scores['World'] += 1
        for kw in keywords_business:
            if kw in text: scores['Business'] += 1
        for kw in keywords_tech:
            if kw in text: scores['Sci/Tech'] += 1
        for kw in keywords_sports:
            if kw in text: scores['Sports'] += 1
            
        # Determine Category
        # Logic: If max > 0, pick max. Ties: Business > Tech > Sports > World (Arbitrary, need a rule)
        # Actually, let's look at counts.
        # If no keywords, skip or default?
        
        if max(scores.values()) == 0:
            category = 'Unknown'
        else:
            category = max(scores, key=scores.get)
            # Tie breaking is handled by max (first occurrence if equal). Keys insertion order?
            # 'World' is inserted first.
            
        if category == 'World':
            region_counts[region] += 1

print("__RESULT__:")
print(json.dumps(region_counts))"""

env_args = {'var_function-call-13685975547188021313': 'file_storage/function-call-13685975547188021313.json', 'var_function-call-3836964039147778648': 6696, 'var_function-call-11235517214380394953': [{'_id': '69450b0f81b0966b2ba88161', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69450b0f81b0966b2ba88162', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69450b0f81b0966b2ba88163', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69450b0f81b0966b2ba88164', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69450b0f81b0966b2ba88165', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8836096259464870655': 127570, 'var_function-call-4632820292160960647': [{'_id': '69450b0f81b0966b2ba88161', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69450b0f81b0966b2ba88162', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69450b0f81b0966b2ba88163', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69450b0f81b0966b2ba88164', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69450b0f81b0966b2ba88165', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
