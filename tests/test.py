import pathlib
import sys
from timeit import default_timer
import numpy as np
from PIL import Image
from termcolor import colored

src_path = pathlib.Path(__file__).parent.parent.resolve()
sys.path.append(str(src_path))
from tango_python_sdk.factor import FaceFactor


def image_path_to_array(image_path: str) -> np.ndarray:
    """Convert image path to numpy array."""
    image = Image.open(image_path).convert('RGB')
    return np.array(image)


def test_get_embeddings(face_factor: FaceFactor, image_path: str) -> np.ndarray:
    """Test the get_embeddings function."""
    print(colored("get_embeddings\n" + "=" * 25, "green"))
    start_time = default_timer()
    handle = face_factor.get_embedding(image_path=image_path)
    print(f"Duration: {default_timer() - start_time}\n")
    print(f"Status: {handle.status}\nResult: {handle.embedding}\nMessage: {handle.message}")
    return handle.embedding


def test_get_distance(face_factor: FaceFactor, embedding_one: np.ndarray, embedding_two: np.ndarray) -> None:
    """Test the get_distance function."""
    print(colored("get_distance\n" + "=" * 25, "green"))
    start_time = default_timer()
    handle = face_factor.get_distance(embedding_one, embedding_two)
    print(f"Duration: {default_timer() - start_time}\n")
    print(f"Status: {handle.status}\nResult: {handle.distance}\nMessage: {handle.message}")


def build_sample_image_path(image_filename: str) -> pathlib.Path:
    """Build the path for the sample image."""
    images_files_path = pathlib.Path(__file__).parent.joinpath("example/test_images/").resolve()
    return images_files_path.joinpath(image_filename)


def setup_test(image_filename: str) -> (FaceFactor, pathlib.Path):
    """Setup the test environment."""
    image_file_path = build_sample_image_path(image_filename)
    face_factor = FaceFactor()
    return face_factor, image_file_path



def test_compare(face_factor: FaceFactor, image_path_1: str, image_path_2: str) -> None:
    """Test the compare function."""
    print(colored(f"Comparing: {image_path_1} and {image_path_2}", "yellow"))
    print(colored("compare\n" + "=" * 25, "green"))
    start_time = default_timer()
    result = face_factor.compare(image_path_1=image_path_1, image_path_2=image_path_2)
    print(f"Duration: {default_timer() - start_time}\n")
    print(f"Status: {result.status}\nResult: {result.is_similar}\nMessage: {result.message}")


def generate_comparison_pairs(images: list) -> list:
    """Generate all possible pairs for comparison."""
    pairs = []
    for i in range(len(images)):
        for j in range(i, len(images)):
            if images[i] != images[j]:  # Avoid comparing the same image with itself
                pairs.append((images[i], images[j]))
    return pairs

if __name__ == "__main__":
    images = [
        "tom_hanks_1.jpg",
        "tom_hanks_2.png",
        "johnny_depp_1.jpg",
        "johnny_depp_2.jpeg"
    ]

    comparison_pairs = generate_comparison_pairs(images)

    for image_1, image_2 in comparison_pairs:
        face_factor, image_path_1 = setup_test(image_1)
        _, image_path_2 = setup_test(image_2)

        # emb_1 = test_get_embeddings(face_factor, image_path_1)
        # emb_2 = test_get_embeddings(face_factor, image_path_2)
        # test_get_distance(face_factor, emb_1, emb_2)
        test_compare(face_factor, image_path_1, image_path_2)