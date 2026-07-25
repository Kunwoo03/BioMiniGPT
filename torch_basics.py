import torch
#importing pytorch

matrix = torch.tensor([[1,2,3], [4,5,6]]);
print("Matrix")
print(matrix)
print(f"Shape: {matrix.shape}")
print(f"Dimensions: {matrix.ndim}")
print(f"Data Type: {matrix.dtype}")
print(f"Device: {matrix.device}")

print("\nMatrix indexing")
print(f"First Row: {matrix[0]}")
print(f"Second Row: {matrix[1]}")
print(f"First Row, third value: {matrix[0,2]}")
print(f"First Column: {matrix[:,0]}")
#:means selecting every value in the axis
print(f"Second Column: {matrix[:,1]}")

print("\nMatrix slicing")
print(f"First two columns: {matrix[:,0:2]}")
#0:2 means from 0~1 (2 is excluded)

token_ids = torch.tensor([0,1,2,3,1], dtype=torch.long)
inputs = token_ids[:-1]
#from 0 to 3 (before last element)
targets = token_ids[1:]
#from 1 to 1 (including last element)
print("\nLanguage Model Data")
print(f"All tokens: {token_ids}")
print(f"Inputs: {inputs}")
print(f"Targets: {targets}")
#We train the model by comparing inputs and targets, which is a ground truth data set.

sequences = torch.tensor([[0,1,2,3,1],[3,2,1,0,2]],dtype = torch.long)
print("\nSequence Batch")
print(sequences)
print(f"Shape: {sequences.shape}")
batch_inputs = sequences[:,:-1]
batch_targets = sequences[:,1:]
print(f"Batch inputs: \n{batch_inputs}")
print(f"Batch targets: \n{batch_targets}")
print(f"Input shape: {batch_inputs.shape}")
print(f"Target shape: {batch_targets.shape}")