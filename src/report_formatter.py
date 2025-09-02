def format_report(analysis: str, corrected_code: str, generated_tests: str, original_code: str) -> str:
    """
    Format the results from all agents into a comprehensive Markdown report.
    
    Args:
        analysis: Analysis report from AnalysisAgent
        corrected_code: Corrected code from CorrectionAgent  
        generated_tests: Test code from TestGeneratorAgent
        original_code: Original code that was analyzed
        
    Returns:
        Formatted Markdown report
    """
    
    report = f"""# 🤖 Hackademia AI Code Review Report

## 📊 Summary
This pull request has been automatically analyzed by our AI-powered CI/CD pipeline. Below are the findings and recommendations.

---

## 🔍 Code Analysis
{analysis}

---

## 🛠️ Proposed Code Corrections

### Original Code:
```python
{original_code.strip()}
```

### Corrected Code:
```python
{corrected_code.strip()}
```

---

## 🧪 Generated Unit Tests

The following pytest tests have been automatically generated to ensure code quality:

```python
{generated_tests.strip()}
```

---

## 🎯 Next Steps
1. **Review the analysis** and consider the identified issues
2. **Apply the corrections** if they align with your requirements
3. **Add the generated tests** to your test suite
4. **Run the tests** to verify functionality

---

*This report was generated automatically by the Hackademia AI pipeline using LangChain and Google Gemini.*
"""
    
    return report


def extract_code_from_response(response: str) -> str:
    """
    Extract clean code from AI response that might contain markdown formatting.
    
    Args:
        response: Raw response from AI agent
        
    Returns:
        Clean code string
    """
    # Remove markdown code blocks if present
    if "```python" in response:
        start = response.find("```python") + 9
        end = response.find("```", start)
        if end != -1:
            return response[start:end].strip()
    
    # Remove any other markdown formatting
    lines = response.split('\n')
    clean_lines = []
    
    for line in lines:
        # Skip markdown headers and formatting
        if not line.startswith('#') and not line.startswith('*') and line.strip():
            clean_lines.append(line)
    
    return '\n'.join(clean_lines)


def truncate_text(text: str, max_length: int = 60000) -> str:
    """
    Truncate text to fit within GitHub comment limits.
    
    Args:
        text: Text to truncate
        max_length: Maximum allowed length
        
    Returns:
        Truncated text with notice if truncated
    """
    if len(text) <= max_length:
        return text
    
    truncated = text[:max_length - 100]
    return truncated + "\n\n... (Report truncated due to length limits)"
