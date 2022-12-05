#25 pixels wide and 6 pixels tall
# find the layer with the fewest zeros
infile = "input8.txt"

w = 25
h = 6
chunk = w * h
f = open(infile)
line = f.readline()
pixels = [int(c) for c in line]

max_layer = -1
max_zeros = 0
n_layers = len(pixels) // chunk    
print(n_layers, len(pixels))

min_zeros = 1000000000000000000
layer_idx = -1
answer = 0
result_chunk = pixels[0:chunk]
for i in range(n_layers):
    start_i = i*chunk
    layer = pixels[start_i:start_i+chunk]
    zeros_per_layer = sum(1 for item in layer if item == 0)

    for i, p in enumerate(layer):
        if result_chunk[i] != 2:
            # 2 is transparent
            continue
        result_chunk[i] = p

    if (zeros_per_layer < min_zeros):
        layer_idx = i
        min_zeros = zeros_per_layer
        ones_per_layer = sum(1 for item in layer if item == 1)
        twos_per_layer = sum(1 for item in layer if item == 2)
        answer = ones_per_layer * twos_per_layer

print(f"layer is {layer_idx}")
print(f"answer is {answer} num zeros is {min_zeros}")

for row in range(h):
    print(result_chunk[row * w:(row + 1) * w])