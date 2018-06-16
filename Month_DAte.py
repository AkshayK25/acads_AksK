from datetime import *

months = ['Months hai ye ->',
          "January",
          "Febuary",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"]

now = (datetime.now())
year = (now.year)
month = (months[now.month])
print(month)