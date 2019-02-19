# Tagup Data Visualization Expert Challenge

## Overview
We are fortunate to work with some truly amazing and very large data sets. One of our most important business challenges is to visualize this data and analytics derived from the data effectively.

## Project Description
To see how you think about large-scale data set visualizations, we have a brief technical challenge detailed here. You are provided with a simulated data set of 2100 assets around New York. Data about the assets include an identifier, physical location, metadata, and a hazard (effectively, a failure probability).

Your goal is to visualize this information effectively. You are free to do this however you like. For context, the user is an asset manager who is responsible for maximizing the uptime of their equipment fleet.

## Data Format
Data is provided in a CSV file. Columns include:
- reference
- longitude
- latitude
- probability_of_faillure_at_timestamps_1
- probability_of_faillure_at_timestamps_2
- ...
- probability_of_faillure_at_timestamps_n

For example, table representation will look like:

|reference  |longitude      |latitude       |timestamp_1            |...    |timestamp_n            |
|--         |--             |--             |--                     |--     |--                     |
|asset_n    |-71.10285830   |42.38180399    |hazard at timestamp_1  |--     |hazard at timestamp_n  |

## Deliverable
You are welcome to provide the final visualization in any reasonable format (PNG, PDF, etc.). Please also provide source files. 

Bonus point for industrializable solutions
