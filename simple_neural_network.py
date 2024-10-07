import torch
import torch.nn as nn


def simple_neural_network(input_tensor: torch.Tensor) -> None:
    # Implement a small neural network with exactly 1 linear layers
    model = nn.Sequential(nn.Linear(8, 1))
    print(model(input_tensor))

    # Implement a small neural network with exactly two linear layers
    model = nn.Sequential(nn.Linear(8, 3), nn.Linear(3, 1))

    output = model(input_tensor)
    print(output)


if __name__ == "__main__":
    input_tensor = torch.randn(1, 8)
    simple_neural_network(input_tensor)
