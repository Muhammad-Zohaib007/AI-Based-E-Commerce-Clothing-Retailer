import numpy as np
import matplotlib.pyplot as plt
import struct

# Replace with the actual path to your file
file_path = "G:\\Machine Learning Scientist\\Datacamp Course Project\\AI-Based E-commerce clothing retailer\\Data\\data\\FashionMNIST\\raw\\t10k-images-idx3-ubyte"

# Load the file into a numpy array
def load_idx_file(file_path):
    with open(file_path, 'rb') as f:
        magic, num, rows, cols = struct.unpack('>IIII', f.read(16))
        data = np.frombuffer(f.read(), dtype=np.uint8).reshape(num, rows, cols)
    return data

images = load_idx_file(file_path)

# Display the first image in the set
plt.imshow(images[0], cmap='gray')
plt.title("Label: Digit from MNIST")
plt.show()