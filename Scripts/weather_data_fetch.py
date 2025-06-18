# Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

# Set time period
start = datetime(2016, 1, 1)
end = datetime(2024, 12, 31)

# Create Point for Vancouver, BC
faisalabad = Point(31.418, 73.079, 183)

# Get daily data for 2018
data = Daily(faisalabad, start, end)
df = data.fetch()
df = df.reset_index()
# # Plot line chart including average, minimum and maximum temperature
# df.plot(y=['tavg', 'tmin', 'tmax'])
# plt.show()

df.to_csv("Time Series Project/TimeSeries Dataset/faisalabad_daily_2016-2024.csv",index=False)