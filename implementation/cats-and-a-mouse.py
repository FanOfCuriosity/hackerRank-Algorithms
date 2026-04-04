def catAndMouse(x: int, y: int, z: int) -> str:
    catARange = abs(z - x)
    catBRange = abs(z - y)
    whoGetMouse = ''
    if catARange < catBRange:
        whoGetMouse = 'Cat A'
    elif catBRange < catARange:
        whoGetMouse = 'Cat B'
    else:
        whoGetMouse = 'Mouse C'
    return whoGetMouse

print(catAndMouse(x=2, y=5, z=4))
