"""
You are given two APIs: one that provides real-time stock prices and another that provides historical stock prices. Develop a system that validates the incoming real-time prices against historical data to detect anomalies or significant deviations.

Write a program to fetch data from both APIs, process and compare the prices, and identify outliers. Implement a mechanism to flag or log the anomalies in real time.

𝐇𝐢𝐧𝐭:
-> Use statistical methods like z-score or standard deviation to determine significant deviations.
-> Consider edge cases such as missing data or API failures.
-> Use multi-threading or asynchronous calls to handle real-time data efficiently.
"""