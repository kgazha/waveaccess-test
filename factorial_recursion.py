def compute_factorial(number):
    if number < 0:
        raise 'Factorial can only be computed for non-negative integers!'

    def _compute(n):
        if n == 1 or n == 0:
            return 1
        return n * _compute(n-1)

    return _compute(number)
