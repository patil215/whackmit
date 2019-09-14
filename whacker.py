import time
import click
from servo import Striker
from camera import Camera
from faces import FaceClassifier

@click.command()
@click.option('--interval', default=4, help='Seconds between taking camera photo for whacking')
@click.option('--image-filepath', default='image.jpg', help='Location to save camera captures')
def run_whacker(interval, image_filepath):
    camera = Camera()
    striker = Striker()
    face_classifier = FaceClassifier()
    
    while True:
        time.sleep(interval)
        camera.take_photo(image_filepath)
        if face_classifier.is_anger_photo(image_filepath):
            striker.strike()
            striker.reset()

if __name__ == '__main__':
    run_whacker()