import os
import sys
from dotenv import load_dotenv
from agents import AnalysisAgent, CorrectionAgent

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
    print("Stage 3: Analysis + Correction Agents - Starting...")
    
    # Get sample code (simulating PR code)
    code_to_analyze = get_sample_code()
    print(f"\nOriginal Code:\n{code_to_analyze}")
    
    try:
        # Step 1: Analysis Agent
        print("\n" + "="*50)
        print("STEP 1: ANALYZING CODE...")
        print("="*50)
        
        analysis_agent = AnalysisAgent()
        analysis_result = analysis_agent.analyze_code(code_to_analyze)
        print(analysis_result)
        
        # Step 2: Correction Agent
        print("\n" + "="*50)
        print("STEP 2: GENERATING CORRECTIONS...")
        print("="*50)
        
        correction_agent = CorrectionAgent()
        corrected_code = correction_agent.correct_code(code_to_analyze, analysis_result)
        
        print("CORRECTED CODE:")
        print("-" * 30)
        print(corrected_code)
        
        print("\n" + "="*50)
        print("STAGE 3 COMPLETE: Analysis + Correction")
        print("="*50)
        
    except Exception as e:
        print(f"Error in pipeline: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
