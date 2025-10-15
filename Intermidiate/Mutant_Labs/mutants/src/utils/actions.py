"""Core sequence manipulation functions for genetic sequence operations.

This module provides fundamental operations for manipulating genetic sequences,
including insertion, deletion, and reversal operations commonly used in
mutant analysis and genetic research.
"""

# TODO: Core functionalities like insertion, deletion

# Insertion or addition of segments to base segment


def insert_segment(seq: str, position: int, insert_seq: str) -> str:
    """Insert a sequence segment at a specified position.

    Inserts a new sequence at the given position (1-based indexing)
    within the original sequence.

    Args:
        seq (str): The original DNA/RNA sequence
        position (int): The position where to insert (1-based index)
        insert_seq (str): The sequence to be inserted

    Returns:
        str: The modified sequence with the inserted segment

    Example:
        >>> insert_segment("ATGC", 3, "GTA")
        'ATGTACG'
    """
    return seq[: position - 1] + insert_seq + seq[position - 1 :]


def delete_segment(seq: str, start_pos: int, length: int) -> str:
    """Delete a segment of specified length from a sequence.

    Removes a segment starting at the given position with the specified
    length from the original sequence.

    Args:
        seq (str): The original DNA/RNA sequence
        start_pos (int): The starting position for deletion (1-based index)
        length (int): The number of characters to delete

    Returns:
        str: The modified sequence with the segment removed

    Example:
        >>> delete_segment("ATGCGTAAC", 4, 3)
        'ATGAAC'
    """
    return seq[: start_pos - 1] + seq[start_pos - 1 + length :]


def reverse_segment(seq: str) -> str:
    """Reverse the order of nucleotides in a sequence.

    Creates a reversed copy of the input sequence, which is useful
    for analyzing reverse complement operations or strand orientation.

    Args:
        seq (str): The DNA/RNA sequence to reverse

    Returns:
        str: The reversed sequence

    Example:
        >>> reverse_segment("ATGC")
        'CGTA'
    """
    return seq[::-1]


if __name__ == "__main__":
    # Demonstration of the sequence manipulation functions
    # Test deletion: remove 3 characters starting at position 4 from "ATGCGTAAC"
    Del = delete_segment("ATGCGTAAC", 4, 3)  # Expected result: "ATGAAC"

    # Test reversal: reverse the entire sequence "ATGCGTAAC"
    Rev = reverse_segment("ATGCGTAAC")  # Expected result: "CAATGCGTA"

    Ins = insert_segment("ATGCGTAAC", 4, "CC")
