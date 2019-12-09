import sys

HEIGHT = 6
WIDTH = 25

def main():
    encoded_image = list([x for x in sys.stdin.readline().strip()])
    image = []

    num_layers = len(encoded_image) // (WIDTH*HEIGHT)
    layers = []

    for l in range(num_layers):
        
        start = l * WIDTH * HEIGHT
        end = start + WIDTH * HEIGHT
        layers.append(encoded_image[start:end])

    for i in range(WIDTH*HEIGHT):

        layer_num = 0

        while layers[layer_num][i] == '2':
            layer_num += 1

        x = layers[layer_num][i]
        image.append(x) if x == '1' else image.append(" ") 

    for l in range(HEIGHT):
        start = l * WIDTH
        end = start + WIDTH
        print(''.join(image[start:end]))


if __name__ == "__main__":
    main()
