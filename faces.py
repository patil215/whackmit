# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

import io
import os

class FaceClassifier:

    def __init__(self):
        # Instantiates a client
        self.client = vision.ImageAnnotatorClient()

    def is_anger_photo(self, image_path):
        # Loads the image into memory
        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()
            image = vision.types.Image(content=content)

            response = self.client.face_detection(image=image)
            print(response)

            # Names of likelihood from google.cloud.vision.enums
            likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                    'LIKELY', 'VERY_LIKELY')
            
            rating = likelihood_name[face.anger_likelihood]
            if rating == 'POSSIBLE' or rating == 'LIKELY' or rating == 'VERY_LIKELY':
                return True
            
            return False
