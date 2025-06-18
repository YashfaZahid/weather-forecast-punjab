# weather-forecast-punjab
__Average Temperature Forecasting with Facebook Prophet & Streamlit__

This project forecasts average daily temperature (Tavg) for the Punjab region using Facebook Prophet, with minimum (Tmin) and maximum (Tmax) temperatures as additional regressors. Historical weather data was collected using the Meteostat library, saved to a SQL Server database, and visualized through a Streamlit app.


__Features__



•	Predicts Tavg using Prophet time series forecasting.

•	Uses tmin and tmax as external regressors.

•	Saves and retrieves data from SQL Server.

•	Interactive Streamlit web app for user-friendly forecasting.



__Technologies Used__



•	Python

•	Facebook Prophet

•	Streamlit

•	Meteostat (for weather data)

•	Pandas & NumPy

•	SQL Server (data storage)

•	pyodbc / sqlalchemy (for database connectivity)



__Methodology__



__Data Collection:__
Fetched historical weather data (tavg, tmin, tmax) for Punjab using the meteostat library.

__Data Storage:__
Cleaned and saved the data to SQL Server using pyodbc.

__Modeling:__
Trained Facebook Prophet using tmin and tmax as regressors to forecast tavg.

__Evaluation:__
Achieved MAPE = 3.77%, indicating accurate forecasting.

__Visualization:__
Built a Streamlit app to display forecasts interactively with database integration.
