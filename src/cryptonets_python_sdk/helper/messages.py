class Message:
    def __init__(self):
        self.EXCEPTION_ERROR_COMPARE= "Something went wrong while doing compare operation"
        self.EXCEPTION_ERROR_GET_DISTANCE = "Something went wrong while getting distance."
        self.EXCEPTION_ERROR_GET_EMB = "Something went wrong while getting embeddings."

        self.APP_MESSAGES = {
            0: "Valid Image",
            1: "Error Description: Face is an image of an image (spoof). Please only provide live facial image(s).",
            2: "Error Description: Face is an image of a video (spoof). Please only provide live facial image(s).",
            3: "Error Description: Face in image is too close to the camera. Please move away from the camera.",
            4: "Error Description: Face in image is too far away.",
            5: "Error Description: Face in image is too far to the right.",
            6: "Error Description: Face in image is too far to the left.",
            7: "Error Description: Face in image is too high.",
            8: "Error Description: Face in image is too low.",
            9: "Error Description: Face in image is too blurry.",
            10: "Error Description: Please remove eyeglasses during registration.",
            11: "Error Description:  Please remove face mask  during registration. ",
            12: "Head in image turned too far toward the left/right. Please face the camera",
            13: "Head in image turned too far toward the up/down. Please face the camera",
            14: "UNUSED ERROR CODE",
            15: "UNUSED ERROR CODE",
            16: "Error Description: No face found in image.",
            17: "Error Description: API Error",
            18:	"Error Description: Local Storage Error",
            19: "Error Description: Memory Error",
            100: "Successfully registered",
            101: "Error Description: Image file does not exist.",
            102: "Error Description: Input image quality is low.",
            103: "Error Description: There is an error in endpoint.",
            104: "Factor object successfully created.",
            105: "Error Description: Something went wrong while initializing.",
            107: self.EXCEPTION_ERROR_GET_DISTANCE,
            108: self.EXCEPTION_ERROR_GET_EMB,
            109: "Error Description: Incorrect Usage."
        }

    def get_message(self, code):
        return self.APP_MESSAGES[code]
