# Gaps Finder
When analysing biological data such as BLAST results, it's very hard to see if the results are as good as it seems. So this project helps to identify missing intervals (gaps) in a sequence and reports coverage statistics respecting your query lenght.

## What it does

- Reads start/end ranges from text input
- Merges overlapping intervals
- Computes missing segments for a sequence of fixed length
- Returns total missing bases and coverage percentage

## Files

- `gaps_finder.py`: module with the main logic
- `main.py`: example script that runs the analysis
- `examples/sample_input.txt`: example input data

## How to use

1. Put your input in the dedicacted line in main.py
2. Run the script from the project folder:

```bash
python main.py
```

3. The script prints gap statistics and coverage percentage.

## Input format

The input can be a text block containing numeric pairs.
Each pair is interpreted as a start and end position.
Pairs could be ordained or not, and could overlap. 

Example:

```
1 122, 4953 5048, 200 300
```

This means three intervals, (1, 122), (4953, 5048), (100, 300)
