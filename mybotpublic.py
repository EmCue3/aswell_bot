#Done with the assistance of a generous redditor

import praw
import time
import os

REPLY_MESSAGE = "> aswell \n\n Did you mean as well? \n\n-------------------------------------- \nI am a bot account."

 
def authenticate():
    print('Authenticating...')
    reddit = praw.Reddit('<bot_name>', user_agent='Test bot /u/<account_name>')
    print('Authenticated as {}'.format(reddit.user.me()))
    return reddit
 
 
def run_bot(reddit, comments_replied_to):
    print('Obtaining comments...')
 
    for comment in reddit.subreddit('all').comments(limit=2500000):
        trigger_string = comment.body
        trigger_string = trigger_string.lower()
 
        if "aswell " in trigger_string and comment.id not in comments_replied_to and not comment.author == reddit.user.me() or "aswell." in trigger_string and comment.id not in comments_replied_to and not comment.author == reddit.user.me() or "aswell," in trigger_string and comment.id not in comments_replied_to and not comment.author == reddit.user.me():
            print('String found. id = {}'.format(comment.id))
            comment.reply(REPLY_MESSAGE)
            print('Replied to comment {}'.format(comment.id))
 
            comments_replied_to.append(comment.id)
            with open('comments_replied_to.txt', 'a') as f:
                f.write(comment.id + '\n')
 
    print('Sleeping for 5 seconds')
    time.sleep(5)
 
 
def get_saved_comments():
    if not os.path.isfile('comments_replied_to.txt'):
        comments_replied_to = []
    else:
        with open('comments_replied_to.txt', 'r') as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split('\n')
        return comments_replied_to
 
 
 
def main():
    try:
        reddit = authenticate()
        comments_replied_to = get_saved_comments()
        while True:
            run_bot(reddit, comments_replied_to)
    except Exception as e:
        print(str(e))
        print('Waiting for 20 seconds')
        time.sleep(20)
        main()
 
if __name__ == '__main__':
    main()




