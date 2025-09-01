import os
import sys
from dotenv import load_dotenv
from agents import AnalysisAgent

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
    print("Stage 2: Analysis Agent - Starting...")
    
    # Get sample code (simulating PR code)
    code_to_analyze = get_sample_code()
    print(f"\nCode to analyze:\n{code_to_analyze}")
    
    # Initialize and run the Analysis Agent
    try:
        analysis_agent = AnalysisAgent()
        analysis_result = analysis_agent.analyze_code(code_to_analyze)
        
        print("\n" + "="*50)
        print("ANALYSIS RESULTS:")
        print("="*50)
        print(analysis_result)
        
    except Exception as e:
        print(f"Error in analysis: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
