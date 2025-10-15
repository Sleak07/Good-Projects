from typing import Annotated

from pydantic import BaseModel, Field, field_validator, model_validator
from pydantic.types import StringConstraints

# Constraints for valid DNA sequencing
DNAString = Annotated[
    str,
    StringConstraints(
        pattern=r"^[ATGC]+$",
        min_length=3,
        max_length=100,
    ),
]


class DNARange(BaseModel):
    """DNA sequence with a specified range for operations.

    Note: Uses 1-based indexing (start_pos=1 is the first nucleotide).
    """

    sequence: DNAString = Field(..., description="DNA sequence: [A,T,G,C] only")
    start_pos: Annotated[
        int, Field(ge=1, description="Start position (1-based indexing)")
    ]
    length: Annotated[int, Field(ge=1, le=100, description="Length of segment")]

    @field_validator("sequence", mode="before")
    @classmethod
    def normalize_sequence(cls, v: str) -> str:
        """Strip whitespace and convert to uppercase before validation."""
        if isinstance(v, str):
            return v.strip().upper()
        return v

    @model_validator(mode="after")
    def check_range_within_sequence(self) -> "DNARange":
        """Validate that the specified range falls within sequence boundaries."""
        seq_len = len(self.sequence)
        end_pos = self.start_pos + self.length - 1

        if end_pos > seq_len:
            raise ValueError(
                f"Segment (start={self.start_pos}, end={end_pos}) "
                f"extends beyond sequence boundary (length={seq_len})."
            )
        return self

    def get_segment(self) -> str:
        """Extract the DNA segment defined by start_pos and length."""
        start_idx = self.start_pos - 1
        end_idx = start_idx + self.length
        return self.sequence[start_idx:end_idx]


if __name__ == "__main__":
    dna = DNARange(sequence=" atgcgtaac ", start_pos=3, length=4)
    print(f"Sequence: {dna.sequence}")
    print(f"Segment: {dna.get_segment()}")
