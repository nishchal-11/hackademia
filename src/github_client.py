import os
import requests
import json

class GitHubClient:
    """
    Client for interacting with GitHub API to fetch PR data and post comments.
    """
    
    def __init__(self):
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.repo_owner = os.getenv("GITHUB_REPOSITORY_OWNER", "nishchal-11")
        self.repo_name = os.getenv("GITHUB_REPOSITORY", "hackademia").split("/")[-1]
        self.pr_number = os.getenv("GITHUB_PR_NUMBER")
        
        if not self.github_token:
            raise ValueError("GITHUB_TOKEN not found in environment variables")
    
    def get_pr_files(self):
        """
        Fetch the files changed in the current PR.
        For testing, returns sample code.
        """
        # In a real implementation, this would fetch from:
        # GET /repos/{owner}/{repo}/pulls/{pull_number}/files
        
        # For now, return sample code for testing
        return {
            "sample_module.py": """
def calculate_average(numbers):
    total = 0
    for i in numbers:
        total += i
    return total / len(numbers)

def divide_numbers(a, b):
    return a / b

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"
"""
        }
    
    def post_comment(self, comment_body: str):
        """
        Post a comment on the current PR.
        
        Args:
            comment_body: The markdown content to post as a comment
        """
        if not self.pr_number:
            print("No PR number found - would post comment in real scenario")
            print("Comment content:")
            print("-" * 50)
            print(comment_body)
            return
        
        url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/issues/{self.pr_number}/comments"
        
        headers = {
            "Authorization": f"token {self.github_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        data = {
            "body": comment_body
        }
        
        try:
            response = requests.post(url, headers=headers, json=data)
            
            if response.status_code == 201:
                print("✅ Successfully posted comment to PR")
            else:
                print(f"❌ Failed to post comment: {response.status_code}")
                print(response.text)
                
        except Exception as e:
            print(f"Error posting comment: {str(e)}")
