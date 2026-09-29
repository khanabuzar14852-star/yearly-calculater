"""
Leap Year & Time Explorer
-------------------------
A friendly tool to check whether any given year is a leap year
and calculate the total days, hours, minutes, and seconds in that year.
"""

def is_leap_year(year: int) -> tuple[bool, str]:
    """
    Determines if a year is a leap year and explains why in plain language.
    
    Rules:
    1. A year divisible by 4 is a leap year, UNLESS:
    2. It is divisible by 100, in which case it is NOT a leap year, UNLESS:
    3. It is also divisible by 400, in which case it IS a leap year.
    """
    if year % 400 == 0:
        return True, f"{year} is divisible by 400 (century leap year exception)."
    elif year % 100 == 0:
        return False, f"{year} is divisible by 100 but not by 400 (century rule)."
    elif year % 4 == 0:
        return True, f"{year} is divisible by 4 and not a century year."
    else:
        return False, f"{year} is not divisible by 4."


def display_year_breakdown(year: int) -> None:
    """Calculates and prints time metrics in a human-friendly format."""
    leap, reason = is_leap_year(year)
    
    # Calculate time units
    days = 366 if leap else 365
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    status = "a LEAP YEAR 🎉" if leap else "NOT a leap year (regular year) 📅"

    print("\n" + "=" * 50)
    print(f"       Year Breakdown for: {year}")
    print("=" * 50)
    print(f"• Verdict: {year} is {status}")
    print(f"• Reason:  {reason}")
    print("-" * 50)
    print("Time Summary:")
    print(f"  • Total Days:    {days:>12,} days")
    print(f"  • Total Hours:   {hours:>12,} hours")
    print(f"  • Total Minutes: {minutes:>12,} minutes")
    print(f"  • Total Seconds: {seconds:>12,} seconds")
    print("=" * 50 + "\n")


def main():
    print("👋 Welcome to the Year & Time Explorer!")
    print("Enter any year (e.g., 2024, 2025, 2000) or type 'exit' to quit.\n")

    while True:
        user_input = input("Enter a year: ").strip()

        if user_input.lower() in ("exit", "quit", "q"):
            print("Thanks for stopping by! Have a wonderful day! 👋")
            break

        if not user_input.isdigit() or int(user_input) <= 0:
            print("⚠️  Please enter a valid positive whole number for the year.\n")
            continue

        year = int(user_input)
        display_year_breakdown(year)


if __name__ == "__main__":
    main()
