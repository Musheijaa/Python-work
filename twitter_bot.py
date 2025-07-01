# Student Name:Musheija Abraham
# Student ID: 23/U/12139/EVE
# Student Number: 2300712139
# Assignment: Create an AI agent that automates tasks of creating posts on social media platforms
# Course: AI/Machine Learning
# Date: 1/7/2025

import os
import tweepy
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

class TwitterReader:
    def __init__(self):
        # Get API credentials
        api_key = os.getenv('TWITTER_API_KEY')
        api_secret = os.getenv('TWITTER_API_SECRET')
        access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        
        if not all([api_key, api_secret, bearer_token]):
            print("❌ Missing API credentials in .env file!")
            self.client = None
            return
        
        try:
            # Use Twitter API v2 client (works with free tier)
            self.client = tweepy.Client(
                bearer_token=bearer_token,
                consumer_key=api_key,
                consumer_secret=api_secret,
                access_token=access_token,
                access_token_secret=access_token_secret
            )
            
            # Test connection by getting your own user info
            me = self.client.get_me()
            if me.data:
                print(f"✅ Connected to Twitter successfully!")
                print(f"👤 Your account: @{me.data.username}")
                print(f"📝 Display name: {me.data.name}")
                self.user_id = me.data.id
                self.username = me.data.username
            else:
                print("❌ Could not get user info")
                self.client = None
                
        except Exception as e:
            print(f"❌ Failed to connect: {e}")
            self.client = None
    
    def read_my_tweets(self, count=10):
        """Read your own recent tweets"""
        if not self.client:
            print("❌ No Twitter connection")
            return
        
        try:
            print(f"📖 Reading your last {count} tweets...\n")
            
            # Get your tweets
            tweets = self.client.get_users_tweets(
                id=self.user_id,
                max_results=count,
                tweet_fields=['created_at', 'public_metrics', 'text']
            )
            
            if not tweets.data:
                print("📭 No tweets found on your account!")
                return
            
            print(f"📊 Found {len(tweets.data)} tweets:\n")
            
            for i, tweet in enumerate(tweets.data, 1):
                # Format the date
                created_at = tweet.created_at.strftime("%Y-%m-%d %H:%M")
                
                # Get metrics
                metrics = tweet.public_metrics
                likes = metrics['like_count']
                retweets = metrics['retweet_count']
                replies = metrics['reply_count']
                
                print(f"🐦 Tweet {i}:")
                print(f"📅 Date: {created_at}")
                print(f"📝 Content: {tweet.text}")
                print(f"📊 Stats: {likes} likes, {retweets} retweets, {replies} replies")
                print(f"🔗 URL: https://twitter.com/{self.username}/status/{tweet.id}")
                print("-" * 60)
            
        except Exception as e:
            print(f"❌ Error reading tweets: {e}")
    
    def search_my_tweets(self, keyword):
        """Search for specific words in your tweets"""
        if not self.client:
            print("❌ No Twitter connection")
            return
        
        try:
            print(f"🔍 Searching your tweets for '{keyword}'...\n")
            
            # Search your tweets
            query = f"from:{self.username} {keyword}"
            tweets = self.client.search_recent_tweets(
                query=query,
                max_results=10,
                tweet_fields=['created_at', 'public_metrics']
            )
            
            if not tweets.data:
                print(f"🔍 No tweets found containing '{keyword}'")
                return
            
            print(f"📊 Found {len(tweets.data)} tweets with '{keyword}':\n")
            
            for i, tweet in enumerate(tweets.data, 1):
                created_at = tweet.created_at.strftime("%Y-%m-%d %H:%M")
                metrics = tweet.public_metrics
                
                print(f"🐦 Match {i}:")
                print(f"📅 Date: {created_at}")
                print(f"📝 Content: {tweet.text}")
                print(f"❤️ Likes: {metrics['like_count']}")
                print("-" * 50)
                
        except Exception as e:
            print(f"❌ Error searching tweets: {e}")
    
    def get_account_stats(self):
        """Get your account statistics"""
        if not self.client:
            print("❌ No Twitter connection")
            return
        
        try:
            # Get your user info with metrics
            user = self.client.get_user(
                username=self.username,
                user_fields=['public_metrics', 'created_at', 'description']
            )
            
            if user.data:
                metrics = user.data.public_metrics
                created_at = user.data.created_at.strftime("%Y-%m-%d")
                
                print(f"📊 YOUR TWITTER ACCOUNT STATS:")
                print(f"👤 Username: @{user.data.username}")
                print(f"📝 Display Name: {user.data.name}")
                print(f"📅 Account Created: {created_at}")
                print(f"📝 Bio: {user.data.description or 'No bio'}")
                print(f"👥 Followers: {metrics['followers_count']:,}")
                print(f"👤 Following: {metrics['following_count']:,}")
                print(f"🐦 Total Tweets: {metrics['tweet_count']:,}")
                print(f"📋 Listed: {metrics['listed_count']:,}")
                
        except Exception as e:
            print(f"❌ Error getting stats: {e}")

def main():
    print("🐦 REAL TWITTER READER")
    print("Reads from your actual X/Twitter account")
    print("=" * 45)
    
    # Create reader
    reader = TwitterReader()
    
    if not reader.client:
        print("Cannot continue without Twitter connection.")
        return
    
    while True:
        print("\nWhat do you want to do?")
        print("1. Read my recent tweets")
        print("2. Search my tweets")
        print("3. Show my account stats")
        print("4. Exit")
        
        choice = input("\nChoose (1-4): ")
        
        if choice == "1":
            try:
                count = int(input("How many tweets to read? (1-100): "))
                if 1 <= count <= 100:
                    reader.read_my_tweets(count)
                else:
                    print("Please enter a number between 1 and 100")
            except ValueError:
                print("Please enter a valid number")
        
        elif choice == "2":
            keyword = input("Enter word to search for: ")
            if keyword.strip():
                reader.search_my_tweets(keyword.strip())
            else:
                print("Please enter a search term")
        
        elif choice == "3":
            reader.get_account_stats()
        
        elif choice == "4":
            print("👋 Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try 1-4.")

if __name__ == "__main__":
    main()
