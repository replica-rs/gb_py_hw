values = [
[0,0,0],
[0,0,1],
[0,1,0],
[0,1,1],
[1,0,0],
[1,0,1],
[1,1,0],
[1,1,1]
]

for i in range(8):
    out1 = not(values[i][0] and values[i][1] and values[i][2])
    out2 = not(values[i][0]) and not(values[i][1]) and not(values[i][2])
    print(f"x = {values[i][0]}, y = {values[i][1]}, z = {values[i][2]}.")
    print(f"¬(X ⋁ Y ⋁ Z) - {out1 == out2}")
    print(f"¬X ⋀ ¬Y ⋀ ¬Z - {out1 == out2}")
    print(f"¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - {out1 == out2}")
    print()
