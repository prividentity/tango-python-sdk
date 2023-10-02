class GetDistanceResult:
    CALL_STATUS_SUCCESS = 0
    CALL_STATUS_ERROR = -1

    def __init__(self, distance=None, status=CALL_STATUS_ERROR, message=""):
        """Result handler for get_distance"""
        self._status = status
        self._distance = distance
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
    def distance(self) -> float:
        """
        Returns the distance obtained from the operation
        """
        return self._distance

    @property
    def message(self) -> str:
        """
        Returns the message of the operation
        """
        return self._message

    @status.setter
    def status(self, value):
        self._status = value

    @distance.setter
    def distance(self, value):
        self._distance = value

    @message.setter
    def message(self, value):
        self._message = value
