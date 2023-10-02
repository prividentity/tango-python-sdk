"""Factor implements the functionalities of each factors to generate and verify Private IDs .
"""
import os

import platform
import sys
import traceback

import numpy as np

from .factor_modules.FaceModule import Face
from .helper.decorators import Singleton
from .helper.messages import Message

from .helper.result_objects.GetEmbeddingResult import GetEmbeddingResult
from .helper.result_objects.compareResult import CompareResult
from .helper.result_objects.GetDistanceResult import GetDistanceResult
from .helper.utils import image_path_to_array
from .settings.supportedPlatforms import SupportedPlatforms


class FaceFactor(metaclass=Singleton):
    """
        Parameters
        ----------
        api_key : str
            The API key for using the FaceFactor server.

        server_url : str
            The URL of the FaceFactor server.

        Returns
        -------
        FaceFactor
            Instance of the FaceFactor class.

        Methods
        -------
        get_embedding
        get_distance
    
    """

    def __init__(self, api_key: str = None, server_url: str = None):

        try:
            if platform.system() not in SupportedPlatforms.supportedOS.value:
                raise OSError("Invalid OS")
            if server_url is None and (os.environ.get('PI_SERVER_URL') is None or len(
                    os.environ.get('PI_SERVER_URL')) <= 0):
                raise ValueError("Server URL has to be configured")
            if api_key is None and (os.environ.get('PI_API_KEY') is None or len(
                    os.environ.get('PI_API_KEY')) <= 0):
                raise ValueError("API Key is required.")

            if server_url is None:
                self._server_url = os.environ.get('PI_SERVER_URL')
            else:
                self._server_url = server_url
            if api_key is None:
                self._api_key = os.environ.get('PI_API_KEY')
            else:
                self._api_key = api_key
                
            self.face_factor = Face(api_key=self._api_key, server_url=self._server_url)
            self.message = Message()
        except ValueError as exp:
            print("Initialization Failed: {}\n".format(exp))
            print("Please refer to the usage documentation for setting up "
                  "Factor:: \nhttps://docs.private.id/cryptonets-python-sdk/usage.html")
            sys.exit(1)
        except OSError as exp:
            print("Initialization Failed: {}\n".format(exp))
            print("Please refer to the usage documentation for setting up "
                  "Factor:: \nhttps://docs.private.id/cryptonets-python-sdk/usage.html")
            sys.exit(1)



    def get_embedding(self, image_path: str = None, image_data: np.array = None) -> GetEmbeddingResult:
        """
        Obtain the embedding for a given image. The image can be provided either via a path or as numpy data.

        Parameters
        ----------
        image_path : str, optional
            Directory path to the image file. Either `image_path` or `image_data` should be provided, not both.
        
        image_data : np.array, optional
            Image data in numpy RGB format. Either `image_path` or `image_data` should be provided, not both.

        Returns
        -------
        GetEmbeddingResult
            - status: int [0 if successful, -1 if any error]
            - message: str [Message from the operation]
            - embedding: list [Embedding of the image]

        Raises
        ------
        Exception
            If there's any error during the operation.
        """
        
        try:
            if (image_path is not None and image_data is not None) or (image_path is None and image_data is None):
                return GetEmbeddingResult(message="Specify either image_path or image_data, not both or none.")

            if image_data:
                if not isinstance(image_data, np.ndarray):
                    return GetEmbeddingResult(message="Required numpy array in RGB/RGBA/BGR format")
                img_data = image_data

            if image_path:
                if not os.path.exists(image_path):
                    return GetEmbeddingResult(message="Image path does not exist.")
                img_data = image_path_to_array(image_path, input_format="rgb")

            if img_data is None:
                return GetEmbeddingResult(message="Failed to load image data.")

            return self.face_factor.get_embedding(image_data=img_data)

        except Exception as e:
            print(f"Oops: {e}\nTrace: {traceback.format_exc()}")
            print("Issue Tracker:: \nhttps://github.com/prividentity/cryptonets-python-sdk/issues")
            return GetEmbeddingResult(message="Error occurred while getting embedding.")
    def get_distance(self, embedding_one: list, embedding_two: list) -> GetDistanceResult:
        """
        Compute the distance between two embeddings.

        Parameters
        ----------
        embedding_one : list
            The first embedding vector.
        
        embedding_two : list
            The second embedding vector.

        Returns
        -------
        GetDistanceResult
            - status: int [0 if successful, -1 if any error]
            - message: str [Message from the operation]
            - distance: float [Distance between the two embeddings]

        Raises
        ------
        Exception
            If there's any error during the operation.
        """


        """
        
        """
        try:
            if not embedding_one or not embedding_two:
                return GetDistanceResult(message="Both embeddings must be provided and non-empty.")

            distance_obj = self.face_factor.get_distance(embedding_one, embedding_two)

            if distance_obj is None:
                return GetDistanceResult(message="Failed to compute distance between embeddings.")
            return GetDistanceResult(distance=distance_obj.distance, status=GetDistanceResult.CALL_STATUS_SUCCESS, message="OK")

        except Exception as e:
            print(f"Oops: {e}\nTrace: {traceback.format_exc()}")
            print("Issue Tracker:: \nhttps://github.com/prividentity/cryptonets-python-sdk/issues")
            return GetDistanceResult(message="Error occurred while computing distance.")
    
    def compare(self, image_path_1: str = None, image_data_1: np.array = None, 
                image_path_2: str = None, image_data_2: np.array = None) -> CompareResult:
        """
        Compare two images to determine if they are similar.

        Parameters
        ----------
        image_path_1 : str, optional
            Directory path to the first image file. Either `image_path_1` or `image_data_1` should be provided, not both.
        
        image_data_1 : np.array, optional
            Image data of the first image in numpy RGB format. Either `image_path_1` or `image_data_1` should be provided, not both.

        image_path_2 : str, optional
            Directory path to the second image file. Either `image_path_2` or `image_data_2` should be provided, not both.
        
        image_data_2 : np.array, optional
            Image data of the second image in numpy RGB format. Either `image_path_2` or `image_data_2` should be provided, not both.

        Returns
        -------
        CompareResult
            A result object containing the comparison result, status, and message.
        """
    
        try:
        
            
            input_format = "rgb"
            if (image_path_1 is not None and image_path_2 is not None and
                image_data_1 is not None and image_data_2 is not None) or (
                    image_path_1 is None and image_path_2 is None and image_data_1 is None and image_data_2 is None):
                return CompareResult(message="Specify either image_path or image_data")
            img_data_1, img_data_2 = None, None
            if image_data_1 is not None and image_data_2 is not None:
                if not isinstance(image_data_1, np.ndarray) or not isinstance(image_data_2, np.ndarray):
                    return CompareResult(message="Required numpy array in RGB/RGBA/BGR format")
                img_data_1 = image_data_1
                img_data_2 = image_data_2
            if image_path_1 or image_path_2:
                if not os.path.exists(image_path_1) or not os.path.exists(image_path_2):
                    return CompareResult(message=self.message.get_message(101))
                img_data_1 = image_path_to_array(image_path_1, input_format=input_format)
                img_data_2 = image_path_to_array(image_path_2, input_format=input_format)
                if img_data_1 is None or img_data_2 is None:
                    return CompareResult(message=self.message.EXCEPTION_ERROR_COMPARE)
            return self.face_factor.compare(image_data_1=img_data_1, image_data_2=img_data_2)
        except Exception as e:
            print("Oops: {}\nTrace: {}".format(e, traceback.format_exc()))
            print("Issue Tracker:: \nhttps://github.com/prividentity/cryptonets-python-sdk/issues")
            return CompareResult(message=self.message.EXCEPTION_ERROR_COMPARE)
        


    @property
    def api_key(self) -> str:
        return self._api_key

    @property
    def server_url(self) -> str:
        return self._server_url

if __name__ == "__main__":
    pass
