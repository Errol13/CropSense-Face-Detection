import os
confidence_level = 0.5

# Output cropped resolution (pixel)
output_res = 1080
preview_output_res = 256
preview_debug_max_res = 640

# Minimum face bounding box size (pixel)
min_face_res = 96
min_upperbody_res = 64
min_fullbody_res = 32

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(BASE_DIR, "input")

# Make all output folders relative to the script location for portability
output_upperbody_folder = os.path.join(BASE_DIR, "output", "upperbody_cropped")
debug_upperbody_folder = os.path.join(BASE_DIR, "output", "upperbody_debug")
output_face_folder = os.path.join(BASE_DIR, "output", "face_cropped")
debug_face_folder = os.path.join(BASE_DIR, "output", "face_debug")
output_fullbody_folder = os.path.join(BASE_DIR, "output", "fullbody_cropped")
debug_fullbody_folder = os.path.join(BASE_DIR, "output", "fullbody_debug")
error_folder = os.path.join(BASE_DIR, "output", "error_images")

# All output folders are now relative to BASE_DIR, so the code works from any working directory.