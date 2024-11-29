import csv
from googleapiclient.discovery import build
import re
import time

api_key = 'AIzaSyADB7U5e-kjykuAsXsMX9A2QEvgu1bGj2w'

def extract_video_id(url):
    """
    Extract the video ID from a YouTube URL.
    Supports URLs like:
    https://www.youtube.com/watch?v=VIDEO_ID
    https://youtube.com/watch?v=VIDEO_ID
    https://www.youtube.com/v/VIDEO_ID
    """
    video_id = None
    youtube_url_pattern = r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]+)'

    match = re.match(youtube_url_pattern, url)
    if match:
        video_id = match.group(1)  # Extract the video ID from the URL
    else:
        print("Invalid YouTube URL format.")
    
    return video_id

def video_comments(video_id):
    # List to store comments and replies
    comments_and_replies = []

    # Creating youtube resource object
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Retrieve youtube video results
    video_response = youtube.commentThreads().list(
        part='snippet,replies',
        videoId=video_id
    ).execute()

    # Iterate video response
    while video_response:
        # Extracting required info from each result object
        for item in video_response['items']:
            # Extracting comments
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']

            # Counting the number of replies
            reply_count = item['snippet']['totalReplyCount']

            # List to store replies for the current comment
            replies = []

            # If replies are present
            if reply_count > 0:
                # Iterate through all replies
                for reply in item['replies']['comments']:
                    # Extract reply
                    reply_text = reply['snippet']['textDisplay']
                    # Store reply in list
                    replies.append(reply_text)

            # Store the comment and its replies in the comments_and_replies list
            comments_and_replies.append({
                'comment': comment,
                'replies': replies
            })

        # If there are more comments, get the next page of results
        if 'nextPageToken' in video_response:
            video_response = youtube.commentThreads().list(
                part='snippet,replies',
                videoId=video_id,
                pageToken=video_response['nextPageToken']
            ).execute()
        else:
            break

    return comments_and_replies

# Input: YouTube URL
url = input('Enter UoyTube url')  # Example URL

# Extract video ID from URL
video_id = extract_video_id(url)

if video_id:
    # Call the function to get the comments
    comments_data = video_comments(video_id)

    # Get only the last 10 comments (if there are that many)
    last_10_comments = comments_data[-10:]

    # Define the CSV file name dynamically
    csv_filename = f"youtube_comments_{int(time.time())}.csv"  # Creates a unique file name based on current timestamp

    # Writing to CSV
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['Comment', 'Replies'])

        # Write each comment and its replies
        for comment_data in last_10_comments:
            # Join replies into a single string if there are any
            replies_text = " | ".join(comment_data['replies']) if comment_data['replies'] else "No replies"
            writer.writerow([comment_data['comment'], replies_text])

    print(f"Data has been written to {csv_filename}")
