import os
import datetime
import random
import json

class GitHubCommitBot:
    def __init__(self):
        self.commit_data = []
        
    def make_commits(self, days: int):
        """Create commit history for specified days"""
        if days < 1:
            return True
            
        commit_date = datetime.datetime.now() - datetime.timedelta(days=days)
        date_str = commit_date.strftime('%Y-%m-%d %H:%M:%S')
        
        # Different commit patterns
        commit_patterns = [
            self.code_improvement_commit,
            self.documentation_commit,
            self.bug_fix_commit,
            self.feature_commit
        ]
        
        # Make 1-3 commits per day for natural look
        commits_today = random.randint(1, 3)
        for _ in range(commits_today):
            commit_func = random.choice(commit_patterns)
            commit_func(date_str)
        
        print(f"Created {commits_today} commits for {date_str}")
        return self.make_commits(days - 1)
    
    def code_improvement_commit(self, date_str):
        """Create a code improvement commit"""
        messages = [
            "Refactor code for better performance",
            "Optimize algorithm efficiency",
            "Improve code readability",
            "Clean up unused imports",
            "Update code formatting"
        ]
        self._create_commit(random.choice(messages), date_str, "src/main.py")
    
    def documentation_commit(self, date_str):
        """Create a documentation commit"""
        messages = [
            "Update README with new features",
            "Add code comments for clarity",
            "Improve documentation structure",
            "Fix typos in documentation",
            "Add API documentation"
        ]
        self._create_commit(random.choice(messages), date_str, "docs/README.md")
    
    def bug_fix_commit(self, date_str):
        """Create a bug fix commit"""
        messages = [
            "Fix critical bug in main module",
            "Resolve edge case handling",
            "Patch security vulnerability",
            "Fix memory leak issue",
            "Resolve compatibility bug"
        ]
        self._create_commit(random.choice(messages), date_str, "src/bug_fixes.py")
    
    def feature_commit(self, date_str):
        """Create a feature implementation commit"""
        messages = [
            "Implement new user feature",
            "Add API endpoint for new functionality",
            "Create new utility functions",
            "Add support for additional file formats",
            "Implement authentication system"
        ]
        self._create_commit(random.choice(messages), date_str, "src/features.py")
    
    def _create_commit(self, message, date_str, filename):
        """Helper function to create a commit"""
        # Ensure directory exists
        os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
        
        # Create or update file
        with open(filename, 'a') as f:
            f.write(f"# Update on {date_str}\n")
            f.write(f"# {message}\n\n")
        
        # Add and commit
        os.system(f'git add {filename}')
        os.system(f'git commit --date="{date_str}" -m "{message}"')
        
        # Store commit data
        self.commit_data.append({
            'date': date_str,
            'message': message,
            'file': filename
        })
    
    def save_commit_log(self):
        """Save commit history to JSON file"""
        with open('commit_history.json', 'w') as f:
            json.dump(self.commit_data, f, indent=2)

def main():
    bot = GitHubCommitBot()
    
    # Create commits for past 7 days (adjust as needed)
    print("Starting automated commit process...")
    success = bot.make_commits(7)
    
    if success:
        bot.save_commit_log()
        print("Commit process completed successfully!")
    else:
        print("Commit process failed!")

if __name__ == "__main__":
    main()
