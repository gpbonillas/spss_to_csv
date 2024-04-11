# Convert SPSS File to CSV

Convert a SPSS file (.SAV) to CSV file using and Python

## Dependencies
- pyreadstat

## Dataset file
The dataset is [American Trends Panel Wave 64](https://www.pewresearch.org/social-trends/dataset/covid-19-late-march-2020/), about most americans say Coronavirus Outbreak has impacted their lives. 

*Nearly nine-in-ten U.S. adults say their life has changed at least a little as a result of the COVID-19 outbreak, including 44% who say their life has changed in a major way.*


## Warning

```message
The script when execute display this warning message to console. However it still works to generate the CSV file:

*FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!*
**You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:**

`df["col"][row_indexer] = value`

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

*See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy*

  `for df, meta in reader:`

```
