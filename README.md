# Beijing Air Quality Dataset and Time Series Forecasting

## Overview
This repository contains the **Beijing Multi-Site Air Quality Dataset**, which includes hourly air pollutant data from 12 monitoring sites in Beijing, China, collected between March 1, 2013, and February 28, 2017. The dataset is sourced from the Beijing Municipal Environmental Monitoring Center and paired with meteorological data from the China Meteorological Administration. This project also includes sample code for exploring and forecasting air quality using Python.

The goal of this repository is to provide a resource for learning time series forecasting techniques, such as ARIMA or machine learning models, applied to real-world air quality data.

## Dataset Description
- **Source**: Beijing Municipal Environmental Monitoring Center and China Meteorological Administration
- **Time Period**: March 1, 2013 - February 28, 2017
- **Frequency**: Hourly
- **Features**:
  - `No`: Row number
  - `year`, `month`, `day`, `hour`: Date and time of measurement
  - `PM2.5`: Particulate matter (2.5 µm) concentration (µg/m³)
  - `PM10`: Particulate matter (10 µm) concentration (µg/m³)
  - `SO2`: Sulfur dioxide concentration (µg/m³)
  - `NO2`: Nitrogen dioxide concentration (µg/m³)
  - `CO`: Carbon monoxide concentration (µg/m³)
  - `O3`: Ozone concentration (µg/m³)
  - `TEMP`: Temperature (°C)
  - `PRES`: Pressure (hPa)
  - `DEWP`: Dew point temperature (°C)
  - `RAIN`: Precipitation (mm)
  - `wd`: Wind direction
  - `WSPM`: Wind speed (m/s)
  - `station`: Name of the monitoring site (e.g., Aotizhongxin, Changping)
- **Size**: ~420,000 rows across 12 CSV files (one per station)
- **Missing Data**: Denoted as `NA`

## Repository Structure
