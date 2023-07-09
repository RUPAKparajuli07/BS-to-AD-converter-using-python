## BS to AD / AD to BS Converter

This program provides a graphical user interface (GUI) for converting dates between the Bikram Sambat (BS) and Gregorian (AD) calendars. It utilizes the `tkinter` library for creating the GUI components and the `tkcalendar` library for the date picker functionality.

### Prerequisites

Before running the program, make sure you have the following libraries installed:

- `tkinter`
- `tkcalendar`

You can install these libraries using the package manager `pip` by running the following command:

```
pip install tkinter tkcalendar
```

### Usage

To use the BS to AD / AD to BS converter, follow these steps:

1. Import the necessary libraries:

```python
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
```

2. Define the conversion functions:

```python
def bs_to_ad():
    """
    Convert Bikram Sambat (BS) date to Gregorian (AD) date.
    """
    ...

def ad_to_bs():
    """
    Convert Gregorian (AD) date to Bikram Sambat (BS) date.
    """
    ...
```

3. Implement the conversion logic:

```python
def convert_bs_to_ad(bs_date):
    """
    Convert Bikram Sambat (BS) date to Gregorian (AD) date.
    """
    ...

def convert_ad_to_bs(ad_date):
    """
    Convert Gregorian (AD) date to Bikram Sambat (BS) date.
    """
    ...
```

4. Create the main window and configure its properties:

```python
window = tk.Tk()
window.title("BS to AD / AD to BS Converter")
window.geometry("900x400")
window.configure(bg="black")
```

5. Define the font style for labels and entry fields:

```python
font_style = ("Times New Roman", 20)
```

6. Create labels to display "BS" and "AD" headers:

```python
bs_label = tk.Label(window, text="Bikram Sambat (BS)", fg="red", bg="black", font=font_style)
bs_label.grid(row=0, column=0, padx=10, pady=5)

ad_label = tk.Label(window, text="Gregorian (AD)", fg="red", bg="black", font=font_style)
ad_label.grid(row=0, column=2, padx=10, pady=5)
```

7. Create calendar pickers for selecting dates:

```python
bs_cal = DateEntry(window, width=12, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd', font=font_style)
bs_cal.grid(row=1, column=1, padx=10, pady=5)

ad_cal = DateEntry(window, width=12, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd', font=font_style)
ad_cal.grid(row=1, column=3, padx=10, pady=5)
```

8. Create entry fields for displaying and editing BS date:

```python
bs_year_entry = tk.Entry(window, width=10, bg="black", fg="red", font=font_style)
bs_year_entry.grid(row=2, column=1, padx=10, pady=5)

bs_month_entry = tk.Entry(window, width=10, bg="black", fg="red", font=font_style)
bs_month_entry.grid(row=3, column=1, padx=10, pady=5)

bs_day_entry = tk.Entry(window, width=10, bg="black", fg="red", font=font_style)
bs_day_entry.grid(row=4, column=1, padx=10, pady=5)
```

9. Create entry fields for displaying and editing AD date:

```python
ad_year_entry = tk.Entry(window, width=10, bg="black", fg="red", font=font_style)
ad_year_entry.grid(row=2, column=3, padx=10, pady=5)

ad_month_entry = tk.Entry(window, width=10, bg="black", fg="red", font=font_style)
ad_month_entry.grid(row=3, column=3, padx=10, pady=5)

ad_day_entry = tk.Entry(window, width=10, bg="black", fg="red", font=font_style)
ad_day_entry.grid(row=4, column=3, padx=10, pady=5)
```

10. Create buttons for initiating the date conversion:

```python
bs_to_ad_button = tk.Button(window, text="BS to AD", command=bs_to_ad, bg="black", fg="red", font=font_style)
bs_to_ad_button.grid(row=5, column=1, padx=10, pady=5)

ad_to_bs_button = tk.Button(window, text="AD to BS", command=ad_to_bs, bg="black", fg="red", font=font_style)
ad_to_bs_button.grid(row=5, column=3, padx=10, pady=5)
```

11. Run the main window loop:

```python
window.mainloop()
```

### Functionality

The program provides the following functionality:

- Date conversion from Bikram Sambat (BS) to Gregorian (AD) and vice versa.
- Date validation and error handling for invalid dates.
- Displaying the selected BS date in the corresponding BS date entry fields.
- Displaying the selected AD date in the corresponding AD date entry fields.

-   <h2 id="contributing">Contributing</h2>
  <p>Contributions are welcome! If you find any issues or would like to suggest enhancements, please feel free to submit a pull request or open an issue.</p>

  <h2 id="license">License</h2>
  <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
</body>
</html>

### Limitations

The program assumes the validity of dates within the supported range of the conversion algorithms. If an invalid date is entered, an error message will be displayed.

### Conclusion

With the BS to AD / AD to BS Converter, you can easily convert dates between the Bikram Sambat and Gregorian calendars using a user-friendly GUI.
