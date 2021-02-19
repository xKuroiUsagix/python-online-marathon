def check_odd_even(number: int) -> None:
    try:
        return f"Entered number is {'even' if not number % 2 else 'odd'}"
    except TypeError:
        return 'You entered not a number.'