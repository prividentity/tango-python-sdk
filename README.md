# Tango-python-sdk

This repository contains the `tango-python-sdk` class and an example application that demonstrates its usage.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Example App](#example-app)
  - [Installation](#example-app-installation)

## Installation
We recommend using the latest version of Python. This SDK supports Python 3.6 and newer.

### Prerequisites
- Python 3.6+
- Numpy 
- Pillow

### Instructions:

1. **Download the SDK**: Download the `tango_python_sdk-1-0-0.whl` file from this [link](#provide-the-link-here).
2. **Install the SDK**: Navigate to the directory where the `.whl` file is located and run:
   ```bash
   pip install tango_python_sdk-1-0-0.whl
   ```
## Usage

Here's how to use the SDK's `get_embedding` function:

```python
from tango_python_sdk import FaceFactor

face_factor = FaceFactor()
embedding = face_factor.get_embedding(image_path="path_to_image.jpg")
```

## API Documentation

The `FaceFactor` class provides a set of functionalities to work with face embeddings and comparisons. Below are the methods available in the SDK:

### get_embedding

```python
get_embedding(image_path: str = None, image_data: np.array = None) -> GetEmbeddingResult
```

This method takes an image either via a path or as numpy data and returns its face embedding.

**Parameters:**

- `image_path`: Directory path to the image file. Either `image_path` or `image_data` should be provided, not both.
- `image_data`: Image data in numpy RGB format. Either `image_path` or `image_data` should be provided, not both.

**Returns:**

- `GetEmbeddingResult` object containing:
  - `status`: 0 if successful, -1 if any error.
  - `message`: Message from the operation.
  - `embedding`: Embedding of the image.

**Example:**

```python
face_factor = FaceFactor()
embedding_result = face_factor.get_embedding(image_path="path_to_image.jpg")
if embedding_result.status == 0:
    print("Embedding:", embedding_result.embedding)
else:
    print("Error:", embedding_result.message)
```

### get_distance

```python
get_distance(embedding_one: list, embedding_two: list) -> GetDistanceResult
```

This method takes two face embeddings and computes the distance between them.

**Parameters:**

- `embedding_one`: The first embedding vector.
- `embedding_two`: The second embedding vector.

**Returns:**

- `GetDistanceResult` object containing:
  - `status`: 0 if successful, -1 if any error.
  - `message`: Message from the operation.
  - `distance`: Distance between the two embeddings.

### compare

```python
compare(image_path_1: str = None, image_data_1: np.array = None, image_path_2: str = None, image_data_2: np.array = None) -> CompareResult
```

This method compares two images to determine if they are similar.

**Parameters:**

- `image_path_1`: Directory path to the first image file. Either `image_path_1` or `image_data_1` should be provided, not both.
- `image_data_1`: Image data of the first image in numpy RGB format. Either `image_path_1` or `image_data_1` should be provided, not both.
- `image_path_2`: Directory path to the second image file. Either `image_path_2` or `image_data_2` should be provided, not both.
- `image_data_2`: Image data of the second image in numpy RGB format. Either `image_path_2` or `image_data_2` should be provided, not both.

**Returns:**

- `CompareResult` object containing the comparison result, status, and message.

