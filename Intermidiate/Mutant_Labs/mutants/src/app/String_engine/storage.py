# TODO: Use numpy to store it as an individual array

import numpy as np

from .validators import DNARange


def store_segment_in_array(sequence: str, start_pos: int, length: int) -> np.ndarray:
    dna = DNARange(sequence=sequence, start_pos=start_pos, length=length)
    segment = dna.get_segment()

    segment_array = np.array(list(segment))
    return segment_array


if __name__ == "__main__":
    result = store_segment_in_array(sequence="atgcgtaac", start_pos=3, length=4)
    print(f"Segment array: {result}")
    print(f"Array shape: {result.shape}")
