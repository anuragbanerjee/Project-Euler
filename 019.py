# Problem 19
# https://projecteuler.net/problem=19
# Question: How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# Answer: 171
#
# Approach: Find the day of the year (a unique integer) for each predicate individually (is a Sunday, is first day) and determine the cardinality of their intersection. Repeat for each year in interval.

def main():
  february_on_leap = lambda year: 29 if is_leap_year(year) else 28

  months = [31, february_on_leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  print count_first_sundays(months)

# Determines if a given year is a leap year. If it is a century and it's divisible by 400, then it is a leap year. If it's not a century and it's divisible by 4, then it is a leap year.
def is_leap_year(year):
  return (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

# Finds the day of the year for the first days of each month.
def find_xth_day_of_month(xth, months, current_year):
  total = 0
  xth_days = [0 for x in range(12)]
  for month_number, days in enumerate(months):
    if month_number == 1:
      days = days(current_year)
    xth_days[month_number] = total + xth
    total += days
  return set(xth_days)

# Finds the day of the year for each Sunday.
def find_sundays(first, year, offset):
  candidate = first + offset
  while candidate < 1:
    candidate += 7

  is_leap = is_leap_year(year)
  sundays = set([candidate])

  for week in range(1, 53):
    new_sunday = candidate + (7 * week)
    if 0 < new_sunday <= (366 if is_leap else 365):
      sundays.add(new_sunday)

  offset -= (2 if is_leap else 1)
  return sundays, offset

# Finds the number of Sundays that are the first of the month in the 20th century.
def count_first_sundays(months):
  starting_year = current_year = 1900
  first_sunday = 6
  offset = 0

  total = 0

  while current_year <= 2000:
    firsts = find_xth_day_of_month(1, months, current_year)
    sundays_raw = find_sundays(first_sunday, current_year, offset)
    sundays, offset = sundays_raw[0], sundays_raw[1]

    if current_year != 1900:
      total += len(sundays & firsts)

    current_year += 1

  return total

if __name__ == '__main__':
  main()