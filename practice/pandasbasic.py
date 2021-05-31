import pandas

mydataset={
    'Name':["Sam","wendy"],
    'DOB':["0219","1013"],
    'SEX':["boy","girl"]
}

myvar=pandas.DataFrame(mydataset)
print(myvar)
