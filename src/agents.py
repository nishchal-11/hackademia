import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, SystemMessage

class AnalysisAgent:
    """
    AI Agent that analyzes Python code for errors, security issues, and best practices.
    """
    
    def __init__(self):
        # Initialize the Gemini model
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
            
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=api_key,
            temperature=0.1  # Low temperature for consistent analysis
        )
    
    def analyze_code(self, code: str) -> str:
        """
        Analyze the provided Python code for issues.
        
        Args:
            code: Python code string to analyze
            
        Returns:
            Analysis report as a string
        """
        system_prompt = """You are an expert Python code reviewer and security analyst. 
        Analyze the provided Python code and identify:

        1. **Bugs and Logic Errors**: Look for potential runtime errors, logical mistakes, or edge cases
        2. **Security Vulnerabilities**: Identify potential security issues like SQL injection, unsafe operations
        3. **Code Quality Issues**: Check for PEP 8 violations, poor naming, code smells
        4. **Best Practices**: Suggest improvements for readability, maintainability, and performance
        5. **Missing Error Handling**: Identify places where exceptions should be caught

        Format your response as:
        ## Analysis Summary
        [Brief overview of findings]

        ## Issues Found
        ### 🐛 Bugs and Logic Errors
        [List specific issues with line references]

        ### 🔒 Security Concerns
        [List security issues]

        ### 📏 Code Quality
        [List style and quality issues]

        ### 💡 Recommendations
        [Suggest improvements]

        Be specific, provide line numbers when possible, and explain the impact of each issue."""

        human_prompt = f"""Please analyze this Python code:

```python
{code}
```"""

        try:
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=human_prompt)
            ]
            
            response = self.llm.invoke(messages)
            return response.content
            
        except Exception as e:
            return f"Error during analysis: {str(e)}"


class CorrectionAgent:
    """
    AI Agent that proposes and applies code corrections based on analysis.
    """
    
    def __init__(self):
        # Initialize the Gemini model
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
            
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=api_key,
            temperature=0.1  # Low temperature for consistent corrections
        )
    
    def correct_code(self, original_code: str, analysis_report: str) -> str:
        """
        Generate corrected code based on the analysis report.
        
        Args:
            original_code: The original Python code
            analysis_report: The analysis report from AnalysisAgent
            
        Returns:
            Corrected code as a string
        """
        system_prompt = """You are an expert Python developer specializing in code correction and improvement.
        
        Your task is to fix the issues identified in the analysis report by rewriting the problematic code sections.
        
        Guidelines:
        1. Fix all bugs and logic errors
        2. Add proper error handling (try-catch blocks, input validation)
        3. Follow PEP 8 coding standards
        4. Improve code readability and maintainability
        5. Add docstrings where missing
        6. Handle edge cases (e.g., division by zero, empty lists)
        
        Return ONLY the corrected Python code, properly formatted and ready to use.
        Do not include explanations or markdown formatting - just the clean Python code."""

        human_prompt = f"""Original Code:
```python
{original_code}
```

Analysis Report:
{analysis_report}

Please provide the corrected version of this code that addresses all the issues mentioned in the analysis."""

        try:
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=human_prompt)
            ]
            
            response = self.llm.invoke(messages)
            return response.content
            
        except Exception as e:
            return f"Error during correction: {str(e)}"
