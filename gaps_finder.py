import re
from typing import Iterable, List, Sequence, Tuple, Union

Interval = Tuple[int, int]
ParsedResult = Tuple[List[Interval], int, float, int]


def _parse_input(input_data: Union[str, Sequence[Union[str, int]]]) -> List[int]:
    """Extract numeric values from a string or sequence of values."""
    if isinstance(input_data, str):
        return [int(value) for value in re.findall(r"\d+", input_data)]

    values: List[int] = []
    for item in input_data:
        if isinstance(item, str):
            values.extend(int(value) for value in re.findall(r"\d+", item))
        else:
            values.append(int(item))

    return values


def _build_intervals(numbers: List[int]) -> List[Interval]:
    """Build a list of (start, end) pairs from consecutive numeric values."""
    intervals: List[Interval] = []
    for index in range(0, len(numbers), 2):
        if index + 1 < len(numbers):
            intervals.append((numbers[index], numbers[index + 1]))
    return intervals


def _merge_intervals(intervals: List[Interval]) -> List[Interval]:
    """Merge overlapping or adjacent intervals into non-overlapping regions."""
    if not intervals:
        return []

    sorted_intervals = sorted(intervals)
    merged: List[Interval] = [sorted_intervals[0]]

    for start, end in sorted_intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def gaps_finder(input_data: Union[str, Sequence[Union[str, int]]], sequence_length: int) -> ParsedResult:
    """Return gaps and coverage metrics for a given sequence length.

    input_data may be:
    - a single string containing numeric ranges, or
    - a list of strings or integers that represent start/end pairs.

    Returns a tuple of:
    - gaps: list of missing intervals as (start, end)
    - total_missing_bases: number of bases missing in all gaps
    - match_percentage: coverage of the sequence in percent
    - gaps_count: number of gap intervals found
    """
    numbers = _parse_input(input_data)
    intervals = _build_intervals(numbers)
    merged_intervals = _merge_intervals(intervals)

    if sequence_length <= 0:
        return [], 0, 100.0, 0

    if not merged_intervals:
        return [(0, sequence_length)], sequence_length, 0.0, 1

    gaps: List[Interval] = []
    cursor = 0
    for start, end in merged_intervals:
        if cursor < start:
            gaps.append((cursor, start))
        cursor = max(cursor, end)

    if cursor < sequence_length:
        gaps.append((cursor, sequence_length))

    gaps = [(start, end) for start, end in gaps if end > start]
    total_missing_bases = sum(end - start for start, end in gaps)
    gaps_count = len(gaps)
    match_percentage = ((sequence_length - total_missing_bases) / sequence_length) * 100

    return gaps, total_missing_bases, match_percentage, gaps_count
