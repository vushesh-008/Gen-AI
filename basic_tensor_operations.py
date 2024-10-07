# Import PyTorch
import torch
import numpy as np

# Main program
if __name__ == "__main__":
    list_a = [1, 2, 3, 4]

    # Create a tensor from list_a
    tensor_a = torch.tensor(list_a, device="mps", dtype=torch.float32)

    # Display the tensor device and data type
    print(tensor_a.device, tensor_a.dtype)

    array_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Create a 2D array
    array_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])  # Create another 2D array

    # Create a tensor from array_a
    tensor_a = torch.tensor(array_a)
    tensor_b = torch.tensor(array_b)

    tensor_c = tensor_a + tensor_b  # Add tensor_a and tensor_b
    tensor_d = tensor_a * tensor_b  # Multiply tensor_a and tensor_b

    # Add tensor_c to tensor_d
    tensor_e = tensor_c + tensor_d

    # Display tensor_e
    print(tensor_e)
