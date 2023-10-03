# Tango-python-sdk

The `tango-python-sdk` provides a Python interface for generating embeddings from images, getting distances and comparing the images. 

## Table of Contents
- [Installation](#installation)
- [Quick Start](#quick-start)
- [API Documentation](#api-documentation)

## Installation

### Prerequisites
- Python 3.6 or newer
- Required libraries: Numpy, Pillow

### Steps:

1. **Download the SDK**: Fetch the `tango_python_sdk-1.0.0-py3-none-any.whl` file from the provided [link](https://tango-python-sdk.s3.amazonaws.com/tango_python_sdk-1.0.0-py3-none-any.whl).
2. **Install the SDK**: Navigate to the directory containing the `.whl` file and execute:
   ```bash
   pip install tango_python_sdk-1.0.0-py3-none-any.whl
   ```

## Quick Start

### 1. Extract Embeddings:

Obtain the embedding of the image. Embedding will be a Fully-Encrypted 1-Way Homomorphic Encryption (FHE) representation of the provided image. A `FloatArray` represents the face embedding. If no face is detected in the image, an empty FloatArray is returned.

```python
from tango_python_sdk.factor import FaceFactor

face_factor = FaceFactor()
embedding = face_factor.get_embedding(image_path="path_to_image.jpg")
print(embedding.embedding)  # Outputs the embedding of the image
```

### 2. Compute Distance Between Embeddings:

Gives back the distance between the two images. Calculated by using the Euclidean distance between the two FHE representations of the images.

```python
embedding_one = face_factor.get_embedding(image_path="path_to_image1.jpg").embedding
embedding_two = face_factor.get_embedding(image_path="path_to_image2.jpg").embedding

distance_result = face_factor.get_distance(embedding_one, embedding_two)
print(distance_result.distance)  # Outputs the distance between the two embeddings
```

### 3. Compare Two Images:

Compares two images and outputs the result. `True` means the images belong to the same person. `False` means the images do not match.

```python
image_path_1 = "path_to_image1.jpg"
image_path_2 = "path_to_image2.jpg"

compare_result = face_factor.compare(image_path_1=image_path_1, image_path_2=image_path_2)
print(compare_result.is_similar)  # Outputs True if the images are similar, otherwise False
```

## API Documentation

The `FaceFactor` class in the SDK offers face embeddings and comparison functionalities. Here's a detailed breakdown:

### get_embedding

Obtain the embedding of an image.

**Parameters:**
- `image_path`: Directory path to the image. Either `image_path` or `image_data` should be provided, not both.
- `image_data`: Image data in numpy RGB format. Either `image_path` or `image_data` should be provided, not both.

**Returns:**
- `GetEmbeddingResult` object with attributes:
  - `status`: 0 for success, -1 for errors.
  - `message`: Descriptive message from the operation.
  - `embedding`: Image's embedding.

### get_distance

Compute the distance between two face embeddings.

**Parameters:**
- `embedding_one`: First embedding vector.
- `embedding_two`: Second embedding vector.

**Returns:**
- `GetDistanceResult` object with attributes:
  - `status`: 0 for success, -1 for errors.
  - `message`: Descriptive message from the operation.
  - `distance`: Distance between the embeddings.

### compare

Compare two images to determine their similarity.

**Parameters:**
- `image_path_1`: Directory path to the first image. Either `image_path_1` or `image_data_1` should be provided, not both.
- `image_data_1`: Image data of the first image in numpy RGB format. Either `image_path_1` or `image_data_1` should be provided, not both.
- `image_path_2`: Directory path to the second image. Either `image_path_2` or `image_data_2` should be provided, not both.
- `image_data_2`: Image data of the second image in numpy RGB format. Either `image_path_2` or `image_data_2` should be provided, not both.

**Returns:**
- `CompareResult` object with attributes:
  - `status`: 0 for success, -1 for errors.
  - `message`: Descriptive message from the operation.
  - `is_similar`: Boolean indicating if the images are similar.

