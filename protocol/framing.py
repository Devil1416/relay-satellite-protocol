"""HDLC-inspired byte-stuffing framer for satellite relay links."""

FLAG = 0x7E
ESC  = 0x7D
ESC_XOR = 0x20

def stuff(data: bytes) -> bytes:
    """Apply byte stuffing."""
    out = []
    for b in data:
        if b in (FLAG, ESC):
            out.append(ESC)
            out.append(b ^ ESC_XOR)
        else:
            out.append(b)
    return bytes(out)

def unstuff(data: bytes) -> bytes:
    """Remove byte stuffing."""
    out = []
    esc_next = False
    for b in data:
        if esc_next:
            out.append(b ^ ESC_XOR)
            esc_next = False
        elif b == ESC:
            esc_next = True
        else:
            out.append(b)
    return bytes(out)

def wrap_frame(data: bytes) -> bytes:
    return bytes([FLAG]) + stuff(data) + bytes([FLAG])

def unwrap_frame(frame: bytes) -> bytes:
    if frame[0] != FLAG or frame[-1] != FLAG:
        raise ValueError("Missing frame delimiters")
    return unstuff(frame[1:-1])
