import pathlib
import sys
src_path = pathlib.Path(__file__).parent.parent.resolve()
sys.path.append(str(src_path))
import os

from timeit import default_timer
import numpy as np
from PIL import Image
from termcolor import colored
from src.cryptonets_python_sdk.factor import FaceFactor


def image_path_to_array(image_path: str) -> np.ndarray:
    """Convert image path to numpy array."""
    image = Image.open(image_path).convert('RGB')
    return np.array(image)


def test_get_embeddings(face_factor, image_path):
    """Test the get_embeddings function."""
    print(colored("get_embeddings\n" + "=" * 25, "green"))
    start_time = default_timer()
    handle = face_factor.get_embedding(image_path=image_path)
    print(f"Duration: {default_timer() - start_time}\n")
    print(f"Status: {handle.status}\nResult: {handle.embedding}\nMessage: {handle.message}")
    return handle.embedding


def test_get_distance(face_factor, embedding_one, embedding_two):
    """Test the get_distance function."""
    print(colored("get_distance\n" + "=" * 25, "green"))
    start_time = default_timer()
    handle = face_factor.get_distance(embedding_one, embedding_two)
    print(f"Duration: {default_timer() - start_time}\n")
    print(f"Status: {handle.status}\nResult: {handle.distance}\nMessage: {handle.message}")


def build_sample_image_path(image_filename=None):
    """Build the path for the sample image."""
    images_files_path = pathlib.Path(__file__).parent.joinpath("example/test_images/").resolve()
    return images_files_path.joinpath(image_filename)


def setup_test(image_filename=None):
    """Setup the test environment."""
    image_file_path = build_sample_image_path(image_filename)
    face_factor = FaceFactor()
    return face_factor, image_file_path

def test_compare(face_factor, image_path_1, image_path_2):
    """Test the compare function."""
    print(colored("compare\n" + "=" * 25, "green"))
    start_time = default_timer()
    print(image_path_1,image_path_2)
    result = face_factor.compare(image_path_1=image_path_1, image_path_2=image_path_2)
    print(f"Duration: {default_timer() - start_time}\n")
    print(f"Status: {result.status}\nResult: {result.is_similar}\nMessage: {result.message}")

if __name__ == "__main__":
    os.environ['PI_SERVER_URL'] = 'https://api.devel.cryptonets.ai/node'
    os.environ['PI_API_KEY'] = '00000000000000001962'
    face_factor, image_path_1 = setup_test("8.png")
    _, image_path_2 = setup_test("8.png") 
 
    emb = test_get_embeddings(face_factor, image_path_1)
    test_get_distance(face_factor, emb, emb)
    test_compare(face_factor, image_path_1, image_path_2)
    print("Done")