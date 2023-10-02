import sys
import platform
import pathlib
import ctypes
import numpy as np

from ctypes import POINTER, c_uint8, c_int, c_float, c_bool, byref


class NativeMethods:
    def __init__(self, api_key: str, server_url: str):
        try:
            self._library_path = pathlib.Path(__file__).parent.joinpath("lib")

            if platform.system() == "Linux":
                self._load_dependencies_for_linux()

            self._initialize_attributes(api_key, server_url)
            self._face_setup()
        except Exception as e:
            raise RuntimeError(f"Failed to initialize NativeMethods: {e}")

    def _load_dependencies_for_linux(self):
        """Load necessary shared libraries for Linux."""
        ctypes.CDLL(self._library_path.joinpath("libopencv_core.so").resolve())
        ctypes.CDLL(self._library_path.joinpath("libopencv_imgproc.so").resolve())
        ctypes.CDLL(self._library_path.joinpath("libtensorflowlite.so").resolve())
        self._load_library(self._library_path.joinpath("libtango.so"))

    def _load_library(self, path):
        """Load the main library."""
        self._libtango = ctypes.CDLL(str(path.resolve()))

    def _initialize_attributes(self, api_key, server_url):
        """Initialize basic attributes."""
        self._api_key = api_key
        self._server_url = server_url

    def _face_setup(self):
       
        self._libtango.tango_get_embedding.argtypes = [POINTER(c_uint8),  # const uint8_t* image_bytes
        c_int,             # const int image_width
        c_int,             # const int image_height
        POINTER(POINTER(c_float)),  # float** embedding_buffer_out
        POINTER(c_int) ]    # int* embedding_buffer_length_out
        self._libtango.tango_get_embedding.restype = c_bool

        self._libtango.tango_free_embedding.argtypes = [POINTER(c_float)]  # const float* embedding_buffer
        self._libtango.tango_free_embedding.restype = None

        self._libtango.tango_get_embeddings_distance.argtypes = [
        POINTER(c_float),  # const uint8_t* image_one_bytes
        c_int,             # const int image_one_width
        POINTER(c_float),  # const uint8_t* image_two_bytes
        c_int,             # const int image_two_width          
    ]
        self._libtango.tango_get_embeddings_distance.restype = c_float

    def get_embedding(self,image: np.array):
        # Ensure the image is in uint8 format
        if image.dtype != np.uint8:
            raise ValueError("Image should be of dtype uint8")

        # Flatten the image array and get its dimensions
        image_bytes = image.ctypes.data_as(POINTER(c_uint8))
        image_height, image_width = image.shape[:2]

        embedding_buffer_out = POINTER(c_float)()
        embedding_buffer_length_out = c_int()

        result = self._libtango.tango_get_embedding(
            image_bytes, image_width, image_height,
            byref(embedding_buffer_out), byref(embedding_buffer_length_out)
        )

        if result:
            embedding_list = [embedding_buffer_out[i] for i in range(embedding_buffer_length_out.value)]
            self._libtango.tango_free_embedding(embedding_buffer_out)
            return embedding_list
        else:
            return None
        
    def get_distance(self, embedding_one: list, embedding_two: list) -> float:
        array_type_one = c_float * len(embedding_one)
        array_type_two = c_float * len(embedding_two)

        embedding_one_array = array_type_one(*embedding_one)
        embedding_two_array = array_type_two(*embedding_two)

        distance = self._libtango.tango_get_embeddings_distance(
            embedding_one_array, len(embedding_one),
            embedding_two_array, len(embedding_two)
        )



        return distance