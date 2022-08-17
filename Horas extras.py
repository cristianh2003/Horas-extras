def Pago(a, b):
    if b <= 40:
        Total = a * b
    else:
        b = b - 40
        Total = (a * 40) + (a * b * 1.5)
    return float(Total)

print("Pago: Q", Pago(15, 45))    