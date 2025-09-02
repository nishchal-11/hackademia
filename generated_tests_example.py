# Example of Generated Test Cases from Stage 4
# These are the types of tests the TestGeneratorAgent creates

import pytest

def test_calculate_average_normal_case():
    """Test calculate_average with a normal list of numbers"""
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0

def test_calculate_average_empty_list():
    """Test calculate_average with empty list - should handle gracefully"""
    assert calculate_average([]) is None

def test_calculate_average_one_element():
    """Test calculate_average with single element"""
    assert calculate_average([5]) == 5.0

def test_calculate_average_mixed_numbers():
    """Test calculate_average with integers and floats"""
    assert calculate_average([1, 2.5, 3, 4.5, 5]) == 3.2

def test_calculate_average_non_numeric_element():
    """Test calculate_average with invalid input - should raise TypeError"""
    with pytest.raises(TypeError):
        calculate_average([1, 2, 'a', 4, 5])

def test_safe_division_normal_case():
    """Test safe_division with normal inputs"""
    assert safe_division(10, 2) == 5.0

def test_safe_division_zero_denominator():
    """Test safe_division with zero denominator - should raise ZeroDivisionError"""
    with pytest.raises(ZeroDivisionError):
        safe_division(10, 0)

def test_safe_division_non_numeric_inputs():
    """Test safe_division with invalid input types"""
    with pytest.raises(TypeError):
        safe_division('a', 2)
    with pytest.raises(TypeError):
        safe_division(10, 'b')

def test_user_creation_normal_case():
    """Test User class creation with valid inputs"""
    user = User("Alice", 30)
    assert user.name == "Alice"
    assert user.age == 30

def test_user_creation_invalid_name():
    """Test User class with invalid name type"""
    with pytest.raises(TypeError):
        User(123, 30)

def test_user_creation_negative_age():
    """Test User class with negative age"""
    with pytest.raises(ValueError):
        User("Charlie", -1)

def test_user_get_info():
    """Test User.get_info method"""
    user = User("David", 25)
    assert user.get_info() == "Name: David, Age: 25"
