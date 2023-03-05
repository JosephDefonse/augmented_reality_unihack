
import cv2
import numpy as np
import os
import math
from objloader_simple import *

"""
References:
(1) https://github.com/mafda/augmented_reality_101
(2) https://docs.opencv.org/3.4/
"""

DEFAULT_COLOR = (0, 0, 0)
MIN_MATCHES = 10
RECTANGLE_COLOR = (0, 255, 0)  # Green color for the rectangle

def render(img, obj, projection, model, color=False):
    """
    Render a loaded obj model into the current video frame
    """
    vertices = obj.vertices
    scale_matrix = np.eye(3) * 14
    # scale_matrix = np.eye(3) * 8
    h, w = model.shape

    for face in obj.faces:
        face_vertices = face[0]
        points = np.array([vertices[vertex - 1] for vertex in face_vertices])
        points = np.dot(points, scale_matrix)

        # render model in the middle of the reference surface. To do so,
        # model points must be displaced
        points = np.array([[p[0] + w / 2, p[1] + h / 2, p[2]] for p in points])
        dst = cv2.perspectiveTransform(points.reshape(-1, 1, 3), projection)
        imgpts = np.int32(dst)
        if color is False:
            cv2.fillConvexPoly(img, imgpts, DEFAULT_COLOR)
        else:
            cv2.fillConvexPoly(img, imgpts, (50, 50, 50))

    return img

def projection_matrix(camera_parameters, homography):
    """
    From the camera calibration matrix and the estimated homography
    compute the 3D projection matrix
    """

    # Compute rotation along the x and y axis as well as the translation
    homography = homography * (-1)
    rot_and_transl = np.dot(np.linalg.inv(camera_parameters), homography)
    col_1 = rot_and_transl[:, 0]
    col_2 = rot_and_transl[:, 1]
    col_3 = rot_and_transl[:, 2]

    # normalise vectors
    l = math.sqrt(np.linalg.norm(col_1, 2) * np.linalg.norm(col_2, 2))
    rot_1 = col_1 / l
    rot_2 = col_2 / l
    translation = col_3 / l

    # compute the orthonormal basis
    c = rot_1 + rot_2
    p = np.cross(rot_1, rot_2)
    d = np.cross(c, p)
    rot_1 = np.dot(c / np.linalg.norm(c, 2) + d / np.linalg.norm(d, 2), 1 / math.sqrt(2))
    rot_2 = np.dot(c / np.linalg.norm(c, 2) - d / np.linalg.norm(d, 2), 1 / math.sqrt(2))
    rot_3 = np.cross(rot_1, rot_2)

    # finally, compute the 3D projection matrix from the model to the current frame
    projection = np.stack((rot_1, rot_2, rot_3, translation)).T
    return np.dot(camera_parameters, projection)

def hex_to_rgb(hex_color):
    """
    Helper function to convert hex strings to RGB
    """
    hex_color = hex_color.lstrip('#')
    h_len = len(hex_color)
    return tuple(int(hex_color[i:i + h_len // 3], 16) for i in range(0, h_len, h_len // 3))



# Load reference image (image that we are trying to find in the camera)
dir_name = os.getcwd()
directory = os.path.join(dir_name, 'reference/file.jpg')
model = cv2.imread(directory)

# Initialising the SIFT keypoint detector and FLANN matcher
sift = cv2.xfeatures2d.SIFT_create()
FLANN_INDEX_KDTREE = 1
flann_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
matcher = cv2.FlannBasedMatcher(flann_params, {})

# Compute keypoints and descriptors for reference image using SIFT keypoint detector
kp_model, des_model = sift.detectAndCompute(model, None)

# initialising the .obj model
obj = OBJ(os.path.join(dir_name, 'models/pizza.obj'), swapyz=True)

camera_parameters = np.array([[1600, 0, 640], [0, 1600, 480], [0, 0, 1]])

# Open live camera stream
cap = cv2.VideoCapture(0)

# Continuously read frames from camera
while True:

    # Read frame from camera
    ret, frame = cap.read()
    if not ret:
        break

    # Convert camera frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Compute keypoints and descriptors for current frame
    kp_frame, des_frame = sift.detectAndCompute(gray, None)

    # Use FLANN matcher to find matches
    matches = matcher.knnMatch(des_model, des_frame, k=2)

    # Ratio test to get good matches
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    # Check if there are enough matches
    if len(good_matches) > MIN_MATCHES:
        # Identify the model in the frame
        src_pts = np.float32([kp_model[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp_frame[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

        homography, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

        if homography is not None:
            try:

                # Get the corners of the model image
                h, w = model.shape
                pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
                dst = cv2.perspectiveTransform(pts, homography)

                # Draw a rectangle around the identified model image
                frame = cv2.polylines(frame, [np.int32(dst)], True, RECTANGLE_COLOR, 3, cv2.LINE_AA)

                # obtain 3D projection matrix from homography matrix and camera parameters
                projection = projection_matrix(camera_parameters, homography)

                # project obj model
                frame = render(frame, obj, projection, model, True)
            except:
                pass

        # Show result
        cv2.imshow('frame', frame)
        cv2.waitKey(1)
    else:
        # Display error message
        cv2.imshow('matches', np.zeros((480, 640), dtype=np.uint8))
        print("Not enough matches have been found - %d/%d" % (len(good_matches), MIN_MATCHES))

    # Check for user input to quit program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close all windows
cap.release()
cv2.destroyAllWindows()





