import picamera

initialized = False

class Camera:
	camera = None
	def __init__(self):
		self.camera = picamera.PiCamera()
	
	def take_photo(self, filepath):
		self.camera.capture(filepath)

	def get_pi_camera(self):
		return self.camera
