def comfort_level(temperature: int, humidity: int, people: int) -> float:
    return 72 - (temperature - 70)**2 - 2*(humidity - 40)**2 + 5*people

def findFirstOneToOptimiseComfort(temperature: int, humidity: int, people: int) -> str:
    ## partial derivatives
    dC_dT = -2 * (temperature - 70)
    dC_dH = -4 * (humidity - 40)
    dC_dO = 5

    if abs(dC_dT) >= abs(dC_dH) and abs(dC_dT) >= abs(dC_dO):
        return 'temperature, increase' if dC_dT > 0 else 'temperature, decrease'
    elif abs(dC_dH) >= abs(dC_dO):
        return 'humidity, increase' if dC_dH > 0 else 'humidity, decrease'
    else:
        return 'occupancy, increase'

def main():
    inputs = [
        (74, 45, 2),
        (0, 50, 2),
        (500, 50, 2)
    ]

    for temperature, humidity, people in inputs:
        print(findFirstOneToOptimiseComfort(temperature, humidity, people))

main()