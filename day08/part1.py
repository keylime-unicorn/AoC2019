import sys

HEIGHT = 6
WIDTH = 25

def main():
    image = list([x for x in sys.stdin.readline().strip()])

    num_layers = len(image) // (WIDTH*HEIGHT)
    layers = []
    min_zeroes = float('inf')
    min_layer = []

    for l in range(num_layers):
        start = l * WIDTH * HEIGHT
        end = start + WIDTH * HEIGHT
        layers.append(image[start:end])

    for layer in layers:
        zeroes = len(list([x for x in layer if x == '0']))
        if zeroes < min_zeroes:
            min_zeroes = zeroes
            min_layer = layer

    ones = len(list([x for x in min_layer if x == '1']))
    twos = len(list([x for x in min_layer if x == '2']))

    print(ones*twos)


if __name__ == "__main__":
    main()
