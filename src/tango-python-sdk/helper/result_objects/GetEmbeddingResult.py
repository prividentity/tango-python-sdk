class GetEmbeddingResult:
    CALL_STATUS_SUCCESS = 0
    CALL_STATUS_ERROR = -1

    def __init__(self, embedding=None, status=CALL_STATUS_ERROR, message=""):
        """Result handler for get_embedding"""
        self._status = status
        self._embedding = embedding
        self._message = message

    @property
    def status(self) -> int:
        """
        Returns the status of the operation

        0 - If successfully obtained result from server

        -1 - In case of error

        """
        return self._status

    @property
    def embedding(self) -> list:
        """
        Returns the embedding obtained from the operation
        """
        return self._embedding

    @property
    def message(self) -> str:
        """
        Returns the message of the operation
        """
        return self._message

    @status.setter
    def status(self, value):
        self._status = value

    @embedding.setter
    def embedding(self, value):
        self._embedding = value

    @message.setter
    def message(self, value):
        self._message = value
