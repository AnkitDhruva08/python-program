from googleapiclient.discovery import build

api_key = 'you you tube api key'

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

# Enter video ID
video_id = "Uv1kkNL88lA"  # Use the video ID only, not the full URL

# Call the function and store the result
comments_data = video_comments(video_id)

# Print the comments and their replies
for comment_data in comments_data:
    print("Comment:", comment_data['comment'])
    print("Replies:", comment_data['replies'])
    print("\n")
