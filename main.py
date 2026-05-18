from gaps_finder import gaps_finder


def main() -> None:
    
    # Replace the contents of this string with your input data.
    input_data = """
    1 122, 4953 5048
    """
    sequence_length = 5120

    gaps, total_missing, match_pct, gaps_count = gaps_finder(input_data, sequence_length)

    print(f"Match %: {match_pct:.2f}%")
    print(f"Total missing bases: {total_missing}")
    print(f"Number of gaps: {gaps_count}")
    print(f"Gaps: {gaps}")


if __name__ == "__main__":
    main()