code = """import json
import re

# Load metadata
with open(locals()['var_function-call-9790443739614513755'], 'r') as f:
    metadata_list = json.load(f)

article_year_map = {}
for item in metadata_list:
    aid = int(item['article_id'])
    year = int(item['publication_date'].split('-')[0])
    article_year_map[aid] = year

# Load articles
with open(locals()['var_function-call-13176827165821674892'], 'r') as f:
    articles_list = json.load(f)

# Keywords
single_keywords = {
    "market", "markets", "stock", "stocks", "trade", "trading", "economy", "economies", "economic", 
    "business", "businesses", "financial", "finance", "investor", "investors", "investment", "investments", 
    "bank", "banks", "banking", "profit", "profits", "loss", "losses", "dollar", "dollars", "euro", "euros", 
    "currency", "currencies", "oil", "price", "prices", "rate", "rates", "inflation", "fed", "treasury", 
    "corporate", "company", "companies", "merger", "mergers", "acquisition", "acquisitions", "deal", "deals", 
    "sale", "sales", "revenue", "revenues", "ipo", "ipos", "nasdaq", "dow", "ceo", "cfo", "bankrupt", 
    "bankruptcy", "debt", "debts", "loan", "loans", "credit", "fund", "funds", "commodity", "commodities", 
    "crude", "opec", "wto", "imf", "gdp", "recession", "employment", "jobless", "jobs", "retail", "consumer", 
    "spending", "budget", "tax", "taxes", "deficit", "share", "shares", "dividend", "dividends", "earnings", 
    "quarterly", "bond", "bonds", "asset", "assets", "yen", "yuan"
}

multi_keywords = [
    "wall street", "wall st", "stock market", "central bank", "federal reserve", "interest rate", 
    "interest rates", "mutual fund", "hedge fund", "private equity", "fiscal cliff", "trade war"
]

classified_samples = []
count = 0

for article in articles_list:
    try:
        aid = int(article.get('article_id'))
    except:
        continue
        
    if aid in article_year_map:
        year = article_year_map[aid]
        if not (2010 <= year <= 2020):
            continue
            
        title = article.get('title', '')
        desc = article.get('description', '')
        text = (title + " " + desc).lower()
        
        tokens = set(re.findall(r'[a-z]+', text))
        
        match = False
        matched_kw = []
        if not tokens.isdisjoint(single_keywords):
            match = True
            matched_kw = list(tokens.intersection(single_keywords))
        else:
            for mk in multi_keywords:
                if mk in text:
                    match = True
                    matched_kw = [mk]
                    break
        
        if match:
            classified_samples.append({"title": title, "matched": matched_kw})
            count += 1
            if count >= 20:
                break

print("__RESULT__:")
print(json.dumps(classified_samples))"""

env_args = {'var_function-call-9790443739614513755': 'file_storage/function-call-9790443739614513755.json', 'var_function-call-3385916558167782532': 'file_storage/function-call-3385916558167782532.json', 'var_function-call-16581665091431742479': 14860, 'var_function-call-13176827165821674892': 'file_storage/function-call-13176827165821674892.json', 'var_function-call-8099412520408383884': {'business_counts_per_year': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}, 'total_business': 0, 'average': 0.0, 'filtered_articles': 5762}, 'var_function-call-4496362446234829779': ['Iraq Halts Oil Exports from Main Southern Pipeline (Reuters) - Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.', "Wall St. Bears Claw Back Into the Black -  NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again.", "Google IPO Auction Off to Rocky Start -  WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators.", "Dollar Falls Broadly on Record Trade Gap -  NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap.", 'Eurozone economy keeps growing - Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.', 'HP shares tumble on profit news - Hewlett-Packard shares fall after disappointing third-quarter profits, while the firm warns the final quarter will also fall short of expectations.', 'Grant to aid Lynn Central Square - Central Square in Lynn should be looking a bit brighter. New sidewalks, curbs, fences, lights, landscaping, and road improvements are planned for the Gateway Artisan Block, a key area of the square, with \\$830,000 in state grant money given to Lynn last week.', 'Oldsmobile: The final parking lot - Why General Motors dropped the Oldsmobile. The four brand  paradoxes GM had to face - the name, the product, image re-positioning, and the consumer - all added up to a brand that had little hope of rebranding.', "Downhome Pinoy Blues, Intersecting Life Paths, and Heartbreak Songs - The Blues is alive and well in the Philippines, as evidenced by this appreciation of the Pinoy Blues band 'Lampano Alley', penned by columnist Clarence Henderson as a counterpoint to his usual economics, business, and culture fare.", 'The Real Time Modern Manila Blues: Bill Monroe Meets Muddy Waters in the Orient - Globalization does strange things to people. A day in the life of a Manila Philippines based business consultant - proving that you really CAN talk about Muddy Walters, bluegrass and work all on the same page...', "Best Asian Tourism Destinations - The new APMF survey of the best Asian tourism destinations has just kicked off, but it's crowded at the top, with Chiang Mai in Thailand just leading from perennial favourites Hong Kong, Bangkok and Phuket in Thailand, and Bali in  Indonesia. Be one of the first to vote and let us know your reasons.", 'IT alligator tales - I grew up in New York, where giant alligators -- sometimes more ornately described as albino alligators -- were rumored to roam the citys sewer systems. According to legend, vacationers picked up the tiny crocodilians in Florida, brought them home to New York, and eventually flushed the little buggers when they grew too big for the local concrete jungle.', '\'Madden,\' \'ESPN\' Football Score in Different Ways (Reuters) - Reuters - Was absenteeism a little high\\on Tuesday among the guys at the office? EA Sports would like\\to think it was because "Madden NFL 2005" came out that day,\\and some fans of the football simulation are rabid enough to\\take a sick day to play it.', 'Space Science Pioneer Van Allen Questions Human Spaceflight (SPACE.com) - SPACE.com - A leading space scientist has called to question the validity of human spaceflight, suggesting that sending astronauts outward from Earth is outdated, too costly, and the science returned is trivial.', 'Nevada Ponders Superfund Status for Mine (AP) - AP - Pressured by a ranking senator from Nevada and the Environmental Protection Agency, Gov. Kenny Guinn says he might reconsider his opposition to a federal Superfund cleanup declaration for a huge abandoned mine contaminated with toxic waste and uranium.', 'Southeast Coast Sees Fewer Turtle Nests (AP) - AP - About half the usual number of loggerhead turtles have nested between North Carolina and Florida this season, and scientists have no explanation for the drop.', "Company Said to Be Ready to Clone Pets (AP) - AP - A company that unveiled the world's first cloned cat nearly three years ago now says it is ready to start filling orders for cloned pets, a newspaper reported Thursday.", 'Deep-Sea Vessel Puts Ocean Floor in Reach (AP) - AP - A new deep-sea research vessel will be able to carry people to 99 percent of the ocean floor, diving deeper than the famed Alvin that pioneered the study of seafloor vents, plate tectonics and deep ocean creatures over the past 40 years.', 'Pacific May Be Seeing New El Nino (AP) - AP - Warming water temperatures in the central equatorial Pacific last month may indicate the start of a new El Nino.', "Experts Downplay Texas Shark Attacks (AP) - AP - Three shark attacks off the Texas coast in the past two months are unusual but don't mean there are more sharks than normal along the beach or that they are getting bolder, marine biologists and other experts say."], 'var_function-call-17997540539097556608': {'business_counts_per_year': {'2010': 154, '2011': 170, '2012': 168, '2013': 186, '2014': 172, '2015': 186, '2016': 179, '2017': 189, '2018': 186, '2019': 183, '2020': 186}, 'total_business': 1959, 'average': 178.0909090909091, 'matches': 1959}}

exec(code, env_args)
