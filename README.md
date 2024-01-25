# EOVSA-spectraDB

A sqlite database for long-term EOVSA dynamic spectrum.

## Data Structure

`stmp` is the unix time stamp of the time slot of the data,

each entry have 17 attr, for flux of 17 frequency.

| Name | Data Type | Note |
|------|-----------|------|
| stmp | INTEGER   | Primary key |
| ch1  | REAL      | 1.5GHz   |
| ch2  | REAL      | 2.5GHz   |
| ch3  | REAL      | 3.5GHz   |
| ch4  | REAL      | 4.5GHz   |
| ch5  | REAL      | 5.5GHz   |
| ch6  | REAL      | 6.5GHz   |
| ch7  | REAL      | 7.5GHz   |
| ch8  | REAL      | 8.5GHz   |
| ch9  | REAL      | 9.5GHz   |
| ch10 | REAL      | 10.5GHz  |
| ch11 | REAL      | 11.5GHz  |
| ch12 | REAL      | 12.5GHz  |
| ch13 | REAL      | 13.5GHz  |
| ch14 | REAL      | 14.5GHz  |
| ch15 | REAL      | 15.5GHz  |
| ch16 | REAL      | 16.5GHz  |
| ch17 | REAL      | 17.5GHz  |

Check out the demo.ipynb to see an example of query and plot.