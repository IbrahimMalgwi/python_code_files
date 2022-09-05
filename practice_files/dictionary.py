month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Spe": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(month_conversions["Mar"])
print(month_conversions.get("Jan"))
print(month_conversions.get("Jam", "Not a valid key"))
