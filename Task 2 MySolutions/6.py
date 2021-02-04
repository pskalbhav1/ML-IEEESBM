import pandas as pd
mydata={
    'Training Hours': [1,2,1,1,1.5,1.5,1.5],
    'Truth': [True,False,True,True,True,True,False]
}
myvar=pd.DataFrame(mydata, index=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
print(myvar)