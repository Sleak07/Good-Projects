# TODO: Core functionalities like insertion, deletion

# Insertion or addition of seqments to base seqment


def insert_segment(seq: str, position: int, insert_seq: str) -> str:
    return seq[: position - 1] + insert_seq + seq[position - 1 :]

def delete_segment(seq:str,position:int,length:int) -> str:
    # return
    # return seq[]
