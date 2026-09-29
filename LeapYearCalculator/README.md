#  Leap Year & Time Breakdown Utility

A friendly, humanized Python command-line utility to determine whether a given year is a leap year and calculate its total time breakdown into days, hours, minutes, and seconds.

---

##  Features

- **Accurate Leap Year Logic:** Implements the official Gregorian calendar rules (handling divisible by 4, century non-leap years, and 400-year exceptions).
- **Human-Friendly Explanations:** Explains *why* a year is or isn't a leap year in plain language.
- **Complete Time Breakdown:**
  - Total days (365 or 366)
  - Total hours
  - Total minutes
  - Total seconds
- **Formatted Readability:** Uses digit grouping commas (e.g., `31,622,400 seconds`) so large numbers are effortless to read.
- **Interactive Command Line Interface:** Allows checking multiple years continuously with input validation.

---

##  Project Structure

```text
LeapYearCalculator/
├── leap_year_info.py    # Main Python script
├── README.md            # Project overview and usage guide
└── STATEMENT.md         # Detailed statement of use, purpose, and construction
```

---

## ⚙️ Requirements

- **Python 3.7+** (No external libraries required; uses standard built-in functions).

---

##  How to Run

1. Open your terminal (PowerShell, Command Prompt, or Terminal).
2. Navigate to the folder where the files are located:
   ```powershell
   cd "$HOME\Desktop\LeapYearCalculator"
   ```
3. Run the Python script:
   ```powershell
   python leap_year_info.py
   ```
4. Enter any year (such as `2024`, `2025`, or `2000`). Type `exit` to quit.

---

##  Sample Run & Output

```text
 Welcome to the Year & Time Explorer!
Enter any year (e.g., 2024, 2025, 2000) or type 'exit' to quit.

Enter a year: 2024

==================================================
       Year Breakdown for: 2024
==================================================
• Verdict: 2024 is a LEAP YEAR 
• Reason:  2024 is divisible by 4 and not a century year.
--------------------------------------------------
Time Summary:
  • Total Days:             366 days
  • Total Hours:          8,784 hours
  • Total Minutes:      527,040 minutes
  • Total Seconds:   31,622,400 seconds
==================================================

Enter a year: 2025

==================================================
       Year Breakdown for: 2025
==================================================
• Verdict: 2025 is NOT a leap year (regular year) 
• Reason:  2025 is not divisible by 4.
--------------------------------------------------
Time Summary:
  • Total Days:             365 days
  • Total Hours:          8,760 hours
  • Total Minutes:      525,600 minutes
  • Total Seconds:   31,536,000 seconds
==================================================
```

---

##  Further Reading

For a deeper dive into the origin, mathematical theory, and structural implementation of this project, read [STATEMENT.md](STATEMENT.md).
