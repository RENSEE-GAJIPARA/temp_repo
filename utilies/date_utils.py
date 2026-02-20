from datetime import datetime as d
def days(d1, d2):
    d1 = d.strptime(d1, "%Y-%m-%d")
    d2 = d.strptime(d2, "%Y-%m-%d")

    diff = abs((d2 - d1).days)
    print(f"Total days : {diff}")