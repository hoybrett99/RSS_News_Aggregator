import feedparser
import csv

# Define the RSS feeds
RSS_FEEDS = {
    # 'Daily Nations Zambia: Local News': 'https://dailynationzambia.com/category/local/feed/',
    # 'Daily Nations Zambia: Business': 'https://dailynationzambia.com/category/biz-corporate/feed/',
    # 'Daily Nations Zambia: Lifestyle': 'https://dailynationzambia.com/category/lifestyle/feed/',
    # 'Daily Nations Zambia: Sports': 'https://dailynationzambia.com/category/sports/',
    # 'ZNBC: Sports': 'https://znbc.co.zm/news/category/sport/feed/',
    # 'ZNBC: Agriculture': 'https://znbc.co.zm/news/category/agriculture/feed/',
    # 'ZNBC: Entertainment': 'https://znbc.co.zm/news/category/intertainment-life-style/feed/',
    # 'ZNBC: Education': 'https://znbc.co.zm/news/category/education/feed/',
    # 'ZNBC: International': 'https://znbc.co.zm/news/category/foreign_news/feed/',
    # 'ZNBC: Tourism and Arts': 'https://znbc.co.zm/news/category/tourism-arts-culture/feed/',
    # 'Zambia Diggers': 'https://diggers.news/rss/',
    'Kitwe News': 'https://kitweonline.com/feed',
    # 'Daily Nations Zambia': 'https://dailynationzambia.com/feed/',
    # 'Kitwe City Council': 'https://www.kitwecouncil.gov.zm/?feed=rss2',
    # 'Lusaka Times: Economy': 'https://www.lusakatimes.com/economy/feed/'
}

# Function to handle paginated feed entries
def get_feed_entries(feed_url, pages=8):
    all_entries = []
    for page in range(1, pages + 1):
        paged_url = f"{feed_url}?paged={page}"
        parsed_feed = feedparser.parse(paged_url)
        entries = parsed_feed.entries
        if not entries:
            break  # Exit if there are no more entries
        all_entries.extend(entries)
    return all_entries

# CSV file path
csv_file_path = 'C:/Users/hoybr/sessionworkspace/Kitwe/News Collector/rss_feed_data.csv'

# Open the CSV file for writing
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(['Source', 'Link', 'Date', 'Sub-category'])
    
    # Loop through each RSS feed
    for source_name, feed_url in RSS_FEEDS.items():
        # Get paginated entries for the feed
        entries = get_feed_entries(feed_url, pages=8)
        
        # Process each entry and write to CSV
        for entry in entries:
            link = entry.link
            date = entry.published if 'published' in entry else 'N/A'
            category = entry.tags[0].term if 'tags' in entry and entry.tags else 'N/A'
            
            # Write the entry data to the CSV file
            writer.writerow([source_name, link, date, category])

print(f"Data has been saved to {csv_file_path}")






