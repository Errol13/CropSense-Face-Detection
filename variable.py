confidence_level = 0.5

# Output cropped resolution (pixel)
output_res = 1080
preview_output_res = 256
preview_debug_max_res = 640

# Minimum face bounding box size (pixel)
min_face_res = 96
min_upperbody_res = 64
min_fullbody_res = 32

input_folder = "input"
output_upperbody_folder = "output/upperbody_cropped"
debug_upperbody_folder = "output/upperbody_debug"
output_face_folder = "output/face_cropped"
debug_face_folder = "output/face_debug"
output_fullbody_folder = "output/fullbody_cropped"
debug_fullbody_folder = "output/fullbody_debug"
error_folder = "output/error_images"

# No deprecated NumPy types (np.int, np.float, etc.) or OpenCV constants used in this file.
# All major NumPy/OpenCV compatibility changes are handled in image_processing.py.