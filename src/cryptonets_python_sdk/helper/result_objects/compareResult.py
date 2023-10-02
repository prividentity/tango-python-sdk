class CompareResult:
    CALL_STATUS_SUCCESS = 0
    CALL_STATUS_ERROR = -1

    def __init__(self, is_similar=None, status=CALL_STATUS_ERROR, message=""):
        """Result handler for compare."""
        self._status = status
        self._is_similar = is_similar
        self._message = message

    @property
    def status(self) -> int:
        """
        Returns the status of the operation.

        0 - If successfully obtained result from server.
        -1 - In case of error.
        """
        return self._status

    @property
    def is_similar(self) -> bool:
        """
        Returns the comparison result of the operation.
        True if the images are similar, False otherwise.
        """
        return self._is_similar

    @property
    def message(self) -> str:
        """
        Returns the message of the operation.
        """
        return self._message

    @status.setter
    def status(self, value):
        self._status = value

    @is_similar.setter
    def is_similar(self, value):
        self._is_similar = value

    @message.setter
    def message(self, value):
        self._message = value
