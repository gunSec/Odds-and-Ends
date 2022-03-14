import os

years = ["2022", "2023"]
months = ["1 JAN", "2 FEB", "3 MAR", "4 APR", "5 MAY", "6 JUN", "7 JUL", "8 AUG", "9 SEP", "10 OCT", "11 NOV", "12 DEC"]

for year in years:
    PWD = "/mnt/c/Users/Gunnar/Desktop/Incidents/"
    folder = os.path.join(PWD, year)
    try:
        os.mkdir(folder)
        PWD = "/mnt/c/Users/Gunnar/Desktop/Incidents/" + year
        for month in months:
            folder = os.path.join(PWD, month)
            try:
                os.mkdir(folder)
            except:
                continue
    except:
        PWD = "/mnt/c/Users/Gunnar/Desktop/Incidents/" + year
        for month in months:
            folder = os.path.join(PWD, month)
            try:
                os.mkdir(folder)
            except:
                continue
