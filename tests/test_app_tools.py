"""Tests for app tools."""
import pytest

def test_app_name_validation():
    """Test app name validation logic."""
    def validate_name(name: str) -> bool:
        return name.replace("_", "").replace("-", "").isalnum()

    assert validate_name("library_management") == True
    assert validate_name("my_app_123") == True
    assert validate_name("my-app") == True
    assert validate_name("invalid name") == False
    assert validate_name("invalid@name") == False

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
