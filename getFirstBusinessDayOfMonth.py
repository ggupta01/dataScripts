import pandas as pd
from pandas.tseries.offsets import BMonthBegin
from datetime import date
from datetime import datetime
#d = date.today()
#offset = BMonthBegin()
#offset.rollforward(d)
#offset.rollback(d)
offset = BMonthBegin()
def getFirstDay(d):
        day = datetime.strptime(str(d),'%Y%m%d').date()
        fd = offset.rollforward(day)
        return fd

df = pd.read_csv("newticker.csv")
df['new'] = df['Month'].apply(lambda x: getFirstDay(x))
df.to_csv("NewFile.csv")
