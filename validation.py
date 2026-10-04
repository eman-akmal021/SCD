def validate_mark(mark: float) -> bool:
    """Returns True if mark is within valid range (0-100), otherwise False."""
    return 0 <= mark <= 100