# Unit Converter

A menu-based unit converter I built in Python using Thonny. It converts kilometres, miles, Celsius, Fahrenheit and kilograms, and it doesn't crash if you type something that isn't a number.

## Screenshot

<img width="609" height="718" alt="image" src="https://github.com/user-attachments/assets/3702c7b9-7121-44a3-b565-d85378a23b7d" />


## Features

- Text menu with 4 conversions, and you can keep converting until you quit
- Handles bad input: type "banana" instead of a number and it asks again
- Rounds answers so they're easy to read
- Each conversion is its own function, so the code is tidy and easy to extend

## Conversions

| Option | Conversion | Formula |
|--------|------------|---------|
| 1 | Kilometres to miles | km × 0.621371 |
| 2 | Celsius to Fahrenheit | C × 9 ÷ 5 + 32 |
| 3 | Kilograms to pounds | kg × 2.20462 |
| 4 | Miles to kilometres | miles × 1.60934 |

## Example

```
--- Unit Converter ---
1. Kilometres to miles
2. Celsius to Fahrenheit
3. Kilograms to pounds
4. Miles to kilometres
q. Quit
Choose an option: 4
Enter miles: 10
10.0 miles is 16.09 km
```

## How to run

1. Install Python 3 from [python.org](https://www.python.org/downloads/)
2. Download `unit_converter.py` from this repository
3. Open a terminal in the folder where you saved it and run:

```
python3 unit_converter.py
```

(On Windows, use `python` instead of `python3`.)

You can also open the file in [Thonny](https://thonny.org) and click the green Run button.

## How it works

- **Functions** (`km_to_miles`, `celsius_to_fahrenheit`, `kg_to_pounds`, `miles_to_kilometres`) each do one conversion
- **`get_number()`** keeps asking until the user types a real number, using `try` and `except`
- A **`while True` loop** keeps showing the menu until the user types `q`
- **`if / elif / else`** decides which conversion to run

## What I learned

- Writing and calling functions, and using `return`
- Using `while` loops and `break`
- Handling errors with `try` and `except` so the program doesn't crash
- Turning text from `input()` into numbers with `float()`
- Fixing bugs like indentation mistakes and mismatched function names

## Ideas for the future

- Add more conversions (Fahrenheit to Celsius, pounds to kilograms)
- Add a pocket money calculator
- Add a "convert another?" prompt
