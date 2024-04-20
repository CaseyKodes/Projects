from myhdl import Signal, block, always_comb, instances
@block
def combo_D(a,b,c,D):
    and_out = Signal(bool(0))
    xor_out = Signal(bool(0))
    mux_out = Signal(bool(0))

    u1 = AND2(and_out, b,c)
    u2 = XOR2(xor_out, b,c)
    u3 = MUX2(mux_out, a, xor_out, and_out)

    D.next = mux_out

    return instances