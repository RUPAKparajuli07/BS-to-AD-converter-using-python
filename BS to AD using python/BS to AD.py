import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

def bs_to_ad():
    """
    Convert Bikram Sambat (BS) date to Gregorian (AD) date.
    """
    bs_date = bs_cal.get_date()

    try:
        ad_date = convert_bs_to_ad(bs_date)
        ad_cal.set_date(ad_date)
    except ValueError:
        messagebox.showerror("Error", "Invalid BS date.")

    # Display selected BS date in BS date section
    bs_year_entry.delete(0, tk.END)
    bs_year_entry.insert(tk.END, str(bs_date.year))
    bs_month_entry.delete(0, tk.END)
    bs_month_entry.insert(tk.END, str(bs_date.month))
    bs_day_entry.delete(0, tk.END)
    bs_day_entry.insert(tk.END, str(bs_date.day))

def ad_to_bs():
    """
    Convert Gregorian (AD) date to Bikram Sambat (BS) date.
    """
    ad_date = ad_cal.get_date()

    try:
        bs_date = convert_ad_to_bs(ad_date)
        bs_cal.set_date(bs_date)
    except ValueError:
        messagebox.showerror("Error", "Invalid AD date.")

    # Display selected AD date in AD date section
    ad_year_entry.delete(0, tk.END)
    ad_year_entry.insert(tk.END, str(ad_date.year))
    ad_month_entry.delete(0, tk.END)
    ad_month_entry.insert(tk.END, str(ad_date.month))
    ad_day_entry.delete(0, tk.END)
    ad_day_entry.insert(tk.END, str(ad_date.day))

def convert_bs_to_ad(bs_date):
    ad_year = bs_date.year + 57

    if bs_date.month > 12 or bs_date.month < 1:
        raise ValueError("Invalid BS month")

    if bs_date.day > 32 or bs_date.day < 1:
        raise ValueError("Invalid BS day")

    if bs_date.month <= 9:
        ad_year -= 1
        month = bs_date.month + 3
    else:
        month = bs_date.month - 9

    return bs_date.replace(year=ad_year, month=month)

def convert_ad_to_bs(ad_date):
    bs_year = ad_date.year - 57

    if ad_date.month > 12 or ad_date.month < 1:
        raise ValueError("Invalid AD month")

    if ad_date.day > 31 or ad_date.day < 1:
        raise ValueError("Invalid AD day")

    if ad_date.month >= 4:
        bs_year += 1
        month = ad_date.month - 3
    else:
        month = ad_date.month + 9

    return ad_date.replace(year=bs_year, month=month)

# Create the main window
window = tk.Tk()
window.title("BS to AD / AD to BS Converter")
window.geometry("900x400")
window.configure(bg="black")

# Define font style
font_style = ("Times New Roman", 20)

# Create labels
bs_label = tk.Label(window, text="Bikram Sambat (BS)", fg="red", bg="black", font=font_style)
bs_label.grid(row=0, column=0, padx=10, pady=5)
ad_label = tk.Label(window, text="Gregorian (AD)", fg="red", bg="black", font=font_style)
ad_label.grid(row=0, column=2, padx=10, pady=5)

# Create calendar pickers
bs_cal = DateEntry(window, width=12, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd', font=font_style)
bs_cal.grid(row=1, column=1, padx=10, pady=5)

ad_cal = DateEntry(window, width=12, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd', font=font_style)
ad_cal.grid(row=1, column=3, padx=10, pady=5)

# Create entry fields for BS date
bs_year_entry = tk.Entry(window, width=10, bg="black", fg="red", font=font_style)
bs_year_entry.grid(row=2, column=1, padx=10, pady=5)
bs_month_entry = tk.Entry(window, width=10, bg="black", fg="red", font=font_style)
bs_month_entry.grid(row=3, column=1, padx=10, pady=5)
bs_day_entry = tk.Entry(window, width=10, bg="black", fg="red", font=font_style)
bs_day_entry.grid(row=4, column=1, padx=10, pady=5)

# Create entry fields for AD date
ad_year_entry = tk.Entry(window, width=10, bg="black", fg="red", font=font_style)
ad_year_entry.grid(row=2, column=3, padx=10, pady=5)
ad_month_entry = tk.Entry(window, width=10, bg="black", fg="red", font=font_style)
ad_month_entry.grid(row=3, column=3, padx=10, pady=5)
ad_day_entry = tk.Entry(window, width=10, bg="black", fg="red", font=font_style)
ad_day_entry.grid(row=4, column=3, padx=10, pady=5)

# Create buttons
bs_to_ad_button = tk.Button(window, text="BS to AD", command=bs_to_ad, bg="black", fg="red", font=font_style)
bs_to_ad_button.grid(row=5, column=1, padx=10, pady=5)

ad_to_bs_button = tk.Button(window, text="AD to BS", command=ad_to_bs, bg="black", fg="red", font=font_style)
ad_to_bs_button.grid(row=5, column=3, padx=10, pady=5)

# Run the main window loop
window.mainloop()
