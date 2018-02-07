# Swami Shreeji
# 7 Feb 2018

# Write a function that reformats the date from DD-MM-YYYY to Mon-DD-YYYY. Return as array

def dates(cases):
	months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
	answer = []

	for elem in cases:
		days = elem[0:2]
		mon = months[int(elem[3:5]) - 1]
		year = elem[-4:]

		soln = mon + "-" + days + "-" + year
		answer.append(soln)

	return answer

# Date strings serving as cases
cases = ["25-12-2017", "07-02-2018", "14-05-1933"]

finalAns = dates(cases)
print finalAns
