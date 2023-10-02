import traceback
import logging
import numpy as np

from ..handler.nativeMethods import NativeMethods
from ..helper.decorators import Singleton
from ..helper.messages import Message
from ..helper.result_objects.compareResult import CompareResult
from ..helper.result_objects.GetEmbeddingResult import GetEmbeddingResult
from ..helper.result_objects.GetDistanceResult import GetDistanceResult

# Set up logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class Face(metaclass=Singleton):

    def __init__(self, api_key: str, server_url: str):
        self.message = Message()
        self.COMPARE_THRESHOLD=1.01
        self.face_factor_processor = NativeMethods(api_key=api_key, server_url=server_url)

    def _handle_error(self, e, message):
        logger.error(f"Exception: {e}, Traceback: {traceback.format_exc()}")
        return message

    def get_embedding(self, image_data: np.array) -> GetEmbeddingResult:
        try:
            embeddings = self.face_factor_processor.get_embedding(image_data)
            if not embeddings:
                return GetEmbeddingResult(message=self.message.EXCEPTION_ERROR_GET_EMB)
            return GetEmbeddingResult(embedding=embeddings,
                                      status=GetEmbeddingResult.CALL_STATUS_SUCCESS, 
                                      message="OK")
        except Exception as e:
            return self._handle_error(e, GetEmbeddingResult(message=self.message.EXCEPTION_ERROR_GET_EMB))

    def get_distance(self, embedding_one: list, embedding_two: list) -> GetDistanceResult:
        try:
            distance = self.face_factor_processor.get_distance(embedding_one, embedding_two)
            if distance is None:
                return GetDistanceResult(message=self.message.EXCEPTION_ERROR_GET_DISTANCE)
            return GetDistanceResult(distance=distance,
                                     status=GetDistanceResult.CALL_STATUS_SUCCESS, 
                                     message="OK")
        except Exception as e:
            return self._handle_error(e, GetDistanceResult(message=self.message.EXCEPTION_ERROR_GET_DISTANCE))
    def compare(self, image_data_1: np.array = None, image_data_2: np.array = None) -> CompareResult:
        """
        Compare two images to determine if they are similar.

        Parameters
        ----------
        
        image_data_1 : np.array, optional
            Image data of the first image in numpy RGB format. Either `image_path_1` or `image_data_1` should be provided, not both.

        image_data_2 : np.array, optional
            Image data of the second image in numpy RGB format. Either `image_path_2` or `image_data_2` should be provided, not both.

        Returns
        -------
        CompareResult
            A result object containing the comparison result, status, and message.
        """
        embedding_1 = self.get_embedding( image_data=image_data_1)
        embedding_2 = self.get_embedding( image_data=image_data_2)

        if embedding_1.status != 0 or embedding_2.status != 0:
            return CompareResult(is_similar=False, status=CompareResult.CALL_STATUS_ERROR, message="Failed to get embeddings for one or both images.")

        distance_result = self.get_distance(embedding_1.embedding, embedding_2.embedding)

        if distance_result.status != 0:
            return CompareResult(is_similar=False, status=CompareResult.CALL_STATUS_ERROR, message="Failed to compute distance between embeddings.")

        is_similar = distance_result.distance < self.COMPARE_THRESHOLD
        return CompareResult(is_similar=is_similar, status=CompareResult.CALL_STATUS_SUCCESS, message="Comparison successful.")
