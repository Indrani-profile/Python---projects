def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def main():
    print("Celsius\tFahrenheit")

    for celsius in range(1, 101):
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}\t{fahrenheit:.1f}")

if __name__ == "__main__":
    main()