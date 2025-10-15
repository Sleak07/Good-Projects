# TODO: Validation system

from typing import Annotated

from pydantic import BaseModel, Field, model_validator
from pydantic.types import StringConstraints

# constraints for valid sequencing
DNAString = Annotated[
str,
StringConstraints(
    strip_whitespace=True,
    to_upper=True,
    pattern=r"^[ATGC]+$",
    min_length=3,
    max_length=100,
),
]


class DNARange(BaseModel):
    sequence: DNAString = Field(..., description="[A,T,G,C] only acceptable")
    start_pos: Annotated[int, Field(ge=1, description="Start position of segment")]
    length: Annotated[
    int, Field(ge=1, le=100, description="Length for operations to happen")
]

    @model_validator(mode="after")
    def check_range_within_sequence(self) -> "DNARange":
        seq_len = len(self.sequence)
        end_pos = self.start_pos + self.length - 1

        if end_pos > seq_len:
            raise ValueError(
                f"Segment (start={self.start_pos}, end={end_pos}) "
                    f"extends beyond sequence boundary (length={seq_len}). "
                    f"Maximum length for this start position: {seq_len - self.start_pos + 1}"
            )
        return self

    def get_segment(self) -> str:
        """Extract the DNA segment defined by start_pos and length.

        Returns:
            The DNA substring from start_pos for length nucleotides.
        """
        # Convert 1-based to 0-based indexing
        start_idx = self.start_pos - 1
        end_idx = start_idx + self.length
        return self.sequence[start_idx:end_idx]


if __name__ == "__main__":
    dna = DNARange(sequence=" atgcgtaac ", start_pos=3, length=4)
    print(f"Sequence: {dna.sequence}")
    print(f"Segment: {dna.get_segment()}")
