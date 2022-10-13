#Assignment: Convert temperatures p56

def converts_to_C(far):
    return (far - 32) * 5/9

def converts_to_F(cel):
    return cel * 9/5 + 32

print(converts_to_F(37))
print(converts_to_C(72))
