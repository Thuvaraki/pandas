import pandas as pd
import numpy as np

df = pd.read_csv("d18.2.csv")

# replace -99999 with NaN
new_df = df.replace('[A-Za-z]','',regex=True)
print(new_df)

#           day temperature windspeed event
# 0  01/01/2017         32         6
# 1  01/02/2017      -99999        9
# 2  01/03/2017          28    -99999
# 3  01/04/2017      -99999         7
# 4  01/05/2017         32     -99999
# 5  01/06/2017          31         2
# 6  01/06/2017          34         5

# here all the content in the event column will  br replaced with empty string bcz it contain alphabet
# so we could use dictionaries

new_df = df.replace({'temperature':'[A-Za-z]',
                               'windspeed':'[A-Za-z]'},'',regex=True)
print(new_df)

#           day temperature windspeed     event
# 0  01/01/2017         32         6       Rain
# 1  01/02/2017      -99999        9      Sunny
# 2  01/03/2017          28    -99999      Snow
# 3  01/04/2017      -99999         7  No Event
# 4  01/05/2017         32     -99999      Rain
# 5  01/06/2017          31         2     Sunny
# 6  01/06/2017          34         5  No Event