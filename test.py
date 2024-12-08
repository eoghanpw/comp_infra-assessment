# Import the modules.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import AutoMinorLocator

# Import the weather data to a pandas dataframe.
json_file = "./data/weather/20241029_190617.json"
df = pd.read_json(json_file)

# Let's look at the data.
df

# Let's check the dtypes of the columns.
df.info()

# Let's update the windSpeed to numeric dype and replace any NaN with 0.
# References:
# https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html
df["windSpeed"] = pd.to_numeric(df["windSpeed"],
                                errors="coerce"
                                ).fillna(value=0)

# Let's combine the date and reportTime columns.
# References:
# https://www.statology.org/pandas-combine-date-and-time-columns/
df["dateTime"] = pd.to_datetime(df["date"].astype(str) + df["reportTime"],
                                format="%Y-%m-%d%H:%M")

# Let's plot the temperature.
fig, ax = plt.subplots()

# x variable.
time = df["dateTime"]
# y variable.
temp = df["temperature"]

# Format the datetime x axis.
# References:
# https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter
# https://matplotlib.org/stable/gallery/showcase/anatomy.html#anatomy-of-a-figure
# https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.autofmt_xdate.html
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_minor_locator(AutoMinorLocator(2))
fig.autofmt_xdate()

# Set title, axis labels and legend.
ax.set_title("Athenry Hourly Temperature")
ax.set_xlabel("Time")
ax.set_ylabel("Temperature (C)")

# Plot.
# References:
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_between_alpha.html
ax.fill_between(time, temp.min(), temp, color="orange", alpha=0.5)

# Add text box for descriptive statistics.
# References:
# https://matplotlib.org/stable/gallery/specialty_plots/anscombe.html
text = (f"max temp: {temp.max()} C\n"
        f"min temp: {temp.min()} C\n"
        f"mean temp: {temp.mean():.2f} C")
bbox = dict(boxstyle="round", fc=("orange", 0.1), ec=("orange", 0.5))
x_loc = df["dateTime"].iloc[:1]
y_loc = 12.5
ax.text(x_loc, y_loc, text, bbox=bbox)

# Let's plot the windspeed.
fig, ax = plt.subplots()

# x variable.
time = df["dateTime"]
# y variable.
wind = df["windSpeed"]

# Format the datetime x axis.
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_minor_locator(AutoMinorLocator(2))
fig.autofmt_xdate()

# Set title and axis labels.
ax.set_title("Athenry Hourly Windspeed")
ax.set_xlabel("Time")
ax.set_ylabel("Windspeed (kt)")

# Plot.
ax.fill_between(time, wind.min(), wind, alpha=0.5)

# Add text box for descriptive stats.
text = (f"max windspeed: {wind.max():.0f} kt\n"
        f"min windspeed: {wind.min():.0f} kt\n"
        f"mean windspeed: {wind.mean():.2f} kt")
bbox = dict(boxstyle='round', fc=("tab:blue", 0.1), ec=("tab:blue", 0.5))
x_loc = df["dateTime"].iloc[:1]
y_loc = 7
ax.text(x_loc, y_loc, text, bbox=bbox)

# Let's update the windSpeed to numeric dype and replace any NaN with 0.
# References:
# https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html
df["windSpeed"] = pd.to_numeric(df["windSpeed"], downcast="integer",
                                errors="coerce"
                                ).fillna(value=0)

# Let's replace blanks in cardinalWindDirection with NaN.
# References:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html
df["cardinalWindDirection"] = df["cardinalWindDirection"].replace("", np.nan)

# Let's plot the wind direction.
fig, ax = plt.subplots()

wind_direction = df["cardinalWindDirection"].value_counts()
labels = wind_direction.index

ax.pie(wind_direction, shadow=True, explode=(0.1, 0, 0))

ax.set_title("Athenry Wind Direction")
ax.legend(loc="upper left", labels=labels)
