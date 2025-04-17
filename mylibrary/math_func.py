def my_sum(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.

    This method takes two integer values, adds them together, and returns the result as an integer.

    :param a: The first integer value.
    :type a: int
    :param b: The second integer value.
    :type b: int
    :return: The sum of `a` and `b`.
    :rtype: int

    :raises ValueError: If any of the inputs is not an integer.

    Example:
    >>> add(2, 3)
    5
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both parameters must be integers.")
    return a + b
