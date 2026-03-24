#!/usr/bin/env python3
"""
Update README with latest YouTube videos
Automatically fetches and updates the YouTube videos section
"""

import os
import re
import requests
from datetime import datetime, timedelta

def get_youtube_videos(api_key, channel_id):
    """
    Fetch latest YouTube videos from a channel
    """
    try:
        # YouTube Data API endpoint
        url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            'key': api_key,
            'channelId': channel_id,
            'part': 'snippet',
            'type': 'video',
            'maxResults': 6,
            'order': 'date',
            'publishedAfter': (datetime.now() - timedelta(days=90)).isoformat() + 'Z'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        videos = []
        for item in data.get('items', []):
            video_id = item['id']['videoId']
            title = item['snippet']['title']
            published_at = item['snippet']['publishedAt']
            
            # Get video stats
            stats_url = "https://www.googleapis.com/youtube/v3/videos"
            stats_params = {
                'key': api_key,
                'id': video_id,
                'part': 'statistics,contentDetails'
            }
            
            stats_response = requests.get(stats_url, params=stats_params)
            stats_data = stats_response.json()
            
            if stats_data['items']:
                stats = stats_data['items'][0]
                view_count = stats['statistics'].get('viewCount', '0')
                
                videos.append({
                    'id': video_id,
                    'title': title,
                    'views': int(view_count),
                    'published': published_at,
                    'thumbnail': f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
                })
        
        return videos
        
    except Exception as e:
        print(f"Error fetching YouTube videos: {e}")
        return []

def format_video_card(video):
    """
    Format a single video as a markdown card
    """
    views = video['views']
    if views >= 1000000:
        views_str = f"{views/1000000:.1f}M"
    elif views >= 1000:
        views_str = f"{views/1000:.1f}K"
    else:
        views_str = str(views)
    
    # Parse date
    published = datetime.fromisoformat(video['published'].replace('Z', '+00:00'))
    date_str = published.strftime('%b %d, %Y')
    
    return f"""[![{video['title']}]({video['thumbnail']})](https://youtu.be/{video['id']})
**[{video['title']}](https://youtu.be/{video['id']})**  
{views_str} views • {date_str}"""

def update_readme(videos):
    """
    Update README with video cards
    """
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Format video section
    if videos:
        video_cards = []
        for video in videos[:6]:  # Show only 6 videos
            video_cards.append(format_video_card(video))
        
        videos_section = '\n\n'.join(video_cards)
    else:
        videos_section = "Check out my latest videos on [YouTube](https://youtube.com)!"
    
    # Replace the YouTube section
    pattern = r'<!-- BEGIN YOUTUBE-CARDS -->.*?<!-- END YOUTUBE-CARDS -->'
    replacement = f'''<!-- BEGIN YOUTUBE-CARDS -->
{videos_section}
<!-- END YOUTUBE-CARDS -->'''
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ README updated successfully!")

def main():
    """
    Main function
    """
    api_key = os.environ.get('YOUTUBE_API_KEY')
    channel_id = os.environ.get('YOUTUBE_CHANNEL_ID')
    
    if not api_key or not channel_id:
        print("⚠️ YouTube API key or Channel ID not set in secrets")
        print("Please set YOUTUBE_API_KEY and YOUTUBE_CHANNEL_ID in GitHub secrets")
        return
    
    print(f"📺 Fetching videos from channel: {channel_id}")
    videos = get_youtube_videos(api_key, channel_id)
    
    if videos:
        print(f"✅ Found {len(videos)} videos")
        update_readme(videos)
    else:
        print("⚠️ No videos found")

if __name__ == '__main__':
    main()
