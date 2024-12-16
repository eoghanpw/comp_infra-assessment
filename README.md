# Computer Infrastructure - Assessment

This repository contains the assessment for the Computer Infrastructure module.

---

## Overview

### 1. [`weather.ipynb`](./weather.ipynb)
This notebook summarises the various computational tasks I completed in the command line interface environment including:

- Directory Management: 
   - Create and navigate through directories and subdirectories.

- Timestamp Generation: 
   - Utilise commands to generate and handle timestamps.

- Weather Data Retrieval: 
   - Develop a script to download weather data from a URL.

- Data Analysis and Visualisation:
   - Leverage Python libraries such as `pandas` and `matplotlib` to analyse and visualise the retrieved [weather data](data/weather/20241029_190617.json).

### 2. [`weather.sh`](./weather.sh)
Bash script to download weather data from a [Met Eireann URL](https://prodapi.metweb.ie/observations/athenry/today) and save a timestamped file to the [`data/weather`](data/weather/) directory.

### 3. [`weather-data.yml`](.github/workflows/weather-data.yml)
YAML workflow file that automates the `weather.sh` bash script with the help of [GitHub Actions](https://docs.github.com/en/actions/about-github-actions/understanding-github-actions).


---

## Getting Started

The notebook can be run online instantly using [GitHub Codespaces](https://github.com/features/codespaces) or on your local machine using [Visual Studio Code](https://code.visualstudio.com/) and [Anaconda](https://www.anaconda.com/download/success).

### Prerequisites for running locally.
- Ensure [Git](https://git-scm.com/), Visual Studio Code and Anaconda are installed on your machine if running locally.

### Installation

1. Clone Repository
   ```bash
   git clone https://github.com/eoghanpw/comp_infra-assessment.git
   cd comp_infra-assessment
   ```

2. Launch Visual Studio Code

3. Run the Jupyter notebook
   - Open the repository folder in VS Code.
   - Select the desired notebook and click Run All to generate the visualisations.

---

## Usage Example

The code snippet below is extracted from the [`weather.ipynb`](./weather.ipynb) notebook and demonstrates how to visualise windspeed data using `matplotlib`.

```python
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

# Fill between plot.
ax.fill_between(time, wind.min(), wind, alpha=0.5)

# Add text box for descriptive stats.
text = (f"max windspeed: {wind.max():.0f} kt\n"
        f"min windspeed: {wind.min():.0f} kt\n"
        f"mean windspeed: {wind.mean():.2f} kt")
bbox = dict(boxstyle='round', fc=("tab:blue", 0.1), ec=("tab:blue", 0.5))
x_loc = df["dateTime"].iloc[:1]
y_loc = 7
ax.text(x_loc, y_loc, text, bbox=bbox)

# Show plot
plt.show()
```
![windspeed plot](img/windspeed%20plot.png)

---

## Acknowledgments

- [pandas documentation](https://pandas.pydata.org/docs/)
- [matplotlib documentation](https://matplotlib.org/stable/index.html)
- [numpy documentation](https://numpy.org/doc/stable/)
- [seaborn](https://seaborn.pydata.org/tutorial.html)
- [Bash cheat sheet](https://github.com/RehanSaeed/Bash-Cheat-Sheet)
- [Cron](https://crontab.guru/examples.html)
- [GitHub READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [GitHub Actions](https://docs.github.com/en/actions/about-github-actions/understanding-github-actions)
- [ChatGPT](https://chatgpt.com/)

---

## Author
Eoghan Walsh