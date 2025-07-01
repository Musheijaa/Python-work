# Student Name:Musheija Abraham
# Student ID: 23/U/12139/EVE
# Student Number: 2300712139
# Assignment: Create an AI agent that automates tasks of creating posts on social media platforms
# Course: AI/Machine Learning
# Date: 1/7/2025

import random
import time
from datetime import datetime

class SocialMediaBot:
    def __init__(self):
        self.posts = []
        self.platforms = ["Twitter", "LinkedIn", "Telegram", "Pinterest"]
        
    def generate_post_content(self, topic):
        # Simple content templates for different topics
        templates = [
            f"Just learned something new about {topic}! Really interesting stuff.",
            f"Working on a project related to {topic}. Any tips?",
            f"Quick thoughts on {topic} - what do you think?",
            f"Found a great article about {topic}. Worth reading!",
            f"Today I explored {topic}. Here's what I discovered..."
        ]
        return random.choice(templates)
    
    def create_post(self, topic, platform):
        content = self.generate_post_content(topic)
        post = {
            'content': content,
            'platform': platform,
            'topic': topic,
            'time_created': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'status': 'created'
        }
        self.posts.append(post)
        print(f"Created post for {platform}: {content}")
        return post
    
    def post_to_twitter(self, content):
        # Simulate posting to Twitter
        print(f"Posting to Twitter: {content}")
        time.sleep(1)  # Simulate API delay
        return True
    
    def post_to_linkedin(self, content):
        # Simulate posting to LinkedIn
        print(f"Posting to LinkedIn: {content}")
        time.sleep(1)
        return True
    
    def post_to_telegram(self, content):
        # Simulate posting to Telegram
        print(f"Posting to Telegram: {content}")
        time.sleep(1)
        return True
    
    def post_to_pinterest(self, content):
        # Simulate posting to Pinterest
        print(f"Posting to Pinterest: {content}")
        time.sleep(1)
        return True
    
    def publish_post(self, post):
        platform = post['platform']
        content = post['content']
        
        try:
            if platform == "Twitter":
                success = self.post_to_twitter(content)
            elif platform == "LinkedIn":
                success = self.post_to_linkedin(content)
            elif platform == "Telegram":
                success = self.post_to_telegram(content)
            elif platform == "Pinterest":
                success = self.post_to_pinterest(content)
            else:
                print(f"Platform {platform} not supported")
                return False
            
            if success:
                post['status'] = 'published'
                print(f"Successfully published to {platform}")
                return True
            else:
                post['status'] = 'failed'
                print(f"Failed to publish to {platform}")
                return False
                
        except Exception as e:
            print(f"Error publishing to {platform}: {e}")
            post['status'] = 'failed'
            return False
    
    def create_and_publish(self, topic, platform):
        # Create a post and immediately publish it
        post = self.create_post(topic, platform)
        self.publish_post(post)
        return post
    
    def bulk_create_posts(self, topics, platforms):
        # Create multiple posts for multiple platforms
        created_posts = []
        for topic in topics:
            for platform in platforms:
                post = self.create_post(topic, platform)
                created_posts.append(post)
        return created_posts
    
    def publish_all_pending(self):
        # Publish all posts that haven't been published yet
        pending_posts = [p for p in self.posts if p['status'] == 'created']
        print(f"Publishing {len(pending_posts)} pending posts...")
        
        for post in pending_posts:
            self.publish_post(post)
            time.sleep(2)  # Wait between posts
    
    def show_stats(self):
        # Show simple statistics about posts
        total = len(self.posts)
        published = len([p for p in self.posts if p['status'] == 'published'])
        failed = len([p for p in self.posts if p['status'] == 'failed'])
        pending = len([p for p in self.posts if p['status'] == 'created'])
        
        print("\n--- Post Statistics ---")
        print(f"Total posts: {total}")
        print(f"Published: {published}")
        print(f"Failed: {failed}")
        print(f"Pending: {pending}")
        
        # Show posts by platform
        platform_counts = {}
        for post in self.posts:
            platform = post['platform']
            if platform in platform_counts:
                platform_counts[platform] += 1
            else:
                platform_counts[platform] = 1
        
        print("\nPosts by platform:")
        for platform, count in platform_counts.items():
            print(f"{platform}: {count}")
    
    def list_all_posts(self):
        # Display all posts
        print("\n--- All Posts ---")
        for i, post in enumerate(self.posts, 1):
            print(f"{i}. Platform: {post['platform']}")
            print(f"   Content: {post['content']}")
            print(f"   Status: {post['status']}")
            print(f"   Created: {post['time_created']}")
            print()

# Simple AI content generator
class ContentGenerator:
    def __init__(self):
        self.hashtags = {
            'technology': ['#tech', '#innovation', '#AI', '#coding'],
            'education': ['#learning', '#education', '#study', '#knowledge'],
            'business': ['#business', '#entrepreneurship', '#startup', '#success'],
            'lifestyle': ['#lifestyle', '#wellness', '#motivation', '#inspiration']
        }
    
    def add_hashtags(self, content, topic):
        # Add relevant hashtags to content
        topic_lower = topic.lower()
        relevant_hashtags = []
        
        for category, tags in self.hashtags.items():
            if category in topic_lower:
                relevant_hashtags = tags
                break
        
        if not relevant_hashtags:
            relevant_hashtags = ['#general', '#interesting']
        
        # Add 2-3 hashtags
        selected_tags = random.sample(relevant_hashtags, min(2, len(relevant_hashtags)))
        return content + " " + " ".join(selected_tags)

# Main function to demonstrate the bot
def main():
    print("Social Media AI Agent - Student Assignment")
    print("=" * 50)
    
    # Create the bot
    bot = SocialMediaBot()
    content_gen = ContentGenerator()
    
    # Test 1: Create single posts
    print("Test 1: Creating individual posts...")
    post1 = bot.create_and_publish("Machine Learning", "Twitter")
    post2 = bot.create_and_publish("Web Development", "LinkedIn")
    
    # Test 2: Bulk create posts
    print("\nTest 2: Bulk creating posts...")
    topics = ["Artificial Intelligence", "Data Science", "Programming"]
    platforms = ["Twitter", "LinkedIn"]
    bulk_posts = bot.bulk_create_posts(topics, platforms)
    
    print(f"Created {len(bulk_posts)} posts in bulk")
    
    # Test 3: Publish all pending posts
    print("\nTest 3: Publishing all pending posts...")
    bot.publish_all_pending()
    
    # Test 4: Enhanced content with hashtags
    print("\nTest 4: Creating posts with hashtags...")
    for topic in ["Technology Trends", "Education Innovation"]:
        content = bot.generate_post_content(topic)
        enhanced_content = content_gen.add_hashtags(content, topic)
        post = {
            'content': enhanced_content,
            'platform': 'Twitter',
            'topic': topic,
            'time_created': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'status': 'created'
        }
        bot.posts.append(post)
        bot.publish_post(post)
    
    # Show final statistics
    bot.show_stats()
    
    # List all posts
    bot.list_all_posts()
    
    print("\nAssignment completed successfully!")

# Additional helper functions for the assignment
def demo_custom_scenarios():
    """Demonstrate different usage scenarios"""
    bot = SocialMediaBot()
    
    print("Scenario 1: Tech company social media campaign")
    tech_topics = ["AI Revolution", "Cloud Computing", "Cybersecurity", "Mobile Apps"]
    for topic in tech_topics:
        bot.create_and_publish(topic, "LinkedIn")
        bot.create_and_publish(topic, "Twitter")
    
    print("\nScenario 2: Educational content series")
    edu_topics = ["Python Basics", "Data Structures", "Algorithms", "Database Design"]
    for topic in edu_topics:
        bot.create_post(topic, "Telegram")
    
    bot.publish_all_pending()
    bot.show_stats()

if __name__ == "__main__":
    main()
    
    print("\n" + "=" * 50)
    print("Running additional demo scenarios...")
    demo_custom_scenarios()