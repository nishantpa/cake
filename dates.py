# << Swami Shreeji >>
# 28 Dec 2017
# A function that formats the date from DD-MM-YYYY to YYYY-MM-DD

def reformatDate(dates):
    answer = []
    for elem in dates:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        temp = str.split(elem)
        
        # Find day
        day = temp[0].replace(' ', '')[:-2]
        if len(day) < 2:
            day = "0" + day
        
        # Find month
        preMonth = temp[1]
        defMonth = 0
        if preMonth in months:
            defMonth = months.index(preMonth) + 1
            defMonth = str(defMonth)
            if len(defMonth) < 2:
                defMonth = "0" + defMonth
        
        # Find year
        year = temp[2]
        
        # Return answer
        ansArray = year + "-" + str(defMonth) + "-" + day
        answer.append(ansArray)
    return answer
