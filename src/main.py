import os
import sys
from dotenv import load_dotenv
from agents import AnalysisAgent, CorrectionAgent, TestGeneratorAgent
from github_client import GitHubClient
from report_formatter import format_report, extract_code_from_response, truncate_text

# Load environment variables
load_dotenv()

def get_sample_code():
    """
    For testing purposes, we'll use sample code.
    In a real PR, this would come from GitHub API.
    """
    return """
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

def main():
    print("Hello, Hackademia!")
    print("Stage 5: Complete AI Pipeline with GitHub Integration - Starting...")
    
    try:
        # Initialize GitHub client
        github_client = GitHubClient()
        
        # Get code from PR (or sample for testing)
        pr_files = github_client.get_pr_files()
        
        for filename, code_content in pr_files.items():
            print(f"\n📄 Processing file: {filename}")
            print(f"Original Code:\n{code_content}")
            
            # Step 1: Analysis Agent
            print("\n" + "="*60)
            print("STEP 1: ANALYZING CODE...")
            print("="*60)
            
            analysis_agent = AnalysisAgent()
            analysis_result = analysis_agent.analyze_code(code_content)
            print(analysis_result)
            
            # Step 2: Correction Agent
            print("\n" + "="*60)
            print("STEP 2: GENERATING CORRECTIONS...")
            print("="*60)
            
            correction_agent = CorrectionAgent()
            corrected_code = correction_agent.correct_code(code_content, analysis_result)
            
            print("CORRECTED CODE:")
            print("-" * 40)
            print(corrected_code)
            
            # Step 3: Test Generation Agent
            print("\n" + "="*60)
            print("STEP 3: GENERATING UNIT TESTS...")
            print("="*60)
            
            test_agent = TestGeneratorAgent()
            generated_tests = test_agent.generate_tests(corrected_code)
            
            print("GENERATED PYTEST TESTS:")
            print("-" * 40)
            print(generated_tests)
            
            # Step 4: Format and Post Report
            print("\n" + "="*60)
            print("STEP 4: FORMATTING AND POSTING REPORT...")
            print("="*60)
            
            # Clean up the AI responses
            clean_corrected_code = extract_code_from_response(corrected_code)
            clean_generated_tests = extract_code_from_response(generated_tests)
            
            # Format the comprehensive report
            report = format_report(
                analysis=analysis_result,
                corrected_code=clean_corrected_code,
                generated_tests=clean_generated_tests,
                original_code=code_content
            )
            
            # Truncate if too long for GitHub
            final_report = truncate_text(report)
            
            # Post to GitHub PR
            github_client.post_comment(final_report)
            
        print("\n" + "="*60)
        print("🎉 STAGE 5 COMPLETE: Full AI Pipeline with GitHub Integration")
        print("Analysis ✅ | Correction ✅ | Test Generation ✅ | GitHub Reporting ✅")
        print("="*60)
        
    except Exception as e:
        print(f"Error in pipeline: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
