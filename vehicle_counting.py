import cv2
import os
import glob
density=0
from vehicle_detector import VehicleDetector
# Load Veichle Detector
vd = VehicleDetector()
time_allocated = 0

def counting(density, densities):
        densities = sorted(densities)
        density = densities[-1:]
# Load the first four images from the folder
for i in range (4,1,-1):
    images_folder = sorted(glob.glob("images/*.jpg"))[:i]
    count = []
    densities = []
# Allocate time based on density
    time_allocated = 0
    if density >= 5:
            time_allocated = 20 + 2 * (density - 5)
            if time_allocated < 20:
                time_allocated = 20
    elif density < 5:
        time_allocated = 10
        print("Allocated time based on highest density:", time_allocated)

for img_path in images_folder:
    vehicles_folder_count=0
    print("Img path", img_path)
    img = cv2.imread(img_path)
    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)

    # Update total count
    vehicles_folder_count += vehicle_count

    density = vehicle_count
    densities.append(density)
    #print("hello")
    counting(density, densities)

    for box in vehicle_boxes:
        x, y, w, h = box

        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

        cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)
    print("Vehicles count in image: ", vehicle_count)

    cv2.imshow("Cars", img)
    cv2.waitKey(1)

    # # Sort densities list in ascending order
    # densities = sorted(densities)
    densities.sort()
    # Remove the highest density and corresponding image if necessary
    if len(densities) > 0 and densities[0] == density:
        densities.pop(0)
        if os.path.exists(img_path):
            os.remove(img_path)

    print("Total current count", vehicles_folder_count)
print(densities)
densities.pop(0)

# import cv2
# import os
# import glob
# from vehicle_detector import VehicleDetector

# # Load Veichle Detector
# vd = VehicleDetector()
# time_allocated = 0

# # Load images from a folder
# images_folder = glob.glob("images/*.jpg")
# count = []
# densities = []


# def counting(density, densities):
#     densities = sorted(densities)
#     density = densities[-1:][0]

#     # Allocate time based on density
#     time_allocated = 0
#     if density >= 5:
#         time_allocated = 20 + 2 * (density - 5)
#         if time_allocated < 20:
#             time_allocated = 20
#     elif density < 5:
#         time_allocated = 10
#     print("Allocated time based on highest density:", time_allocated)

# for img_path in images_folder:
#     print("Img path", img_path)
#     img = cv2.imread(img_path)
#     vehicle_boxes = vd.detect_vehicles(img)
#     vehicle_count = len(vehicle_boxes)

#     # Update total count
#     vehicles_folder_count += vehicle_count

#     density = vehicle_folder_count
#     densities.append(density)
#     counting(density, densities)

#     for box in vehicle_boxes:
#         x, y, w, h = box

#         cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

#         cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)
#     print("Vehicles count in image: ", vehicle_count)

#     cv2.imshow("Cars", img)
#     cv2.waitKey(1)

#     # # Sort densities list in ascending order
#     densities = sorted(densities)

#     # Remove the highest density and corresponding image if necessary
#     if len(densities) > 0 and densities[0] == density:
#         densities.pop(0)
#         if os.path.exists(img_path):
#             os.remove(img_path)

# print("Total current count", vehicles_folder_count)
# print(densities)
# densities.pop(0)

# import cv2
# import glob
# from vehicle_detector import VehicleDetector
# # Load Veichle Detector
# vd = VehicleDetector()

# # Load images from a folder
# images_folder = glob.glob("images/*.jpg")
# # count=[]
# # # def counting(count):
# #     count.append(vehicle_count)
# #     count=sorted(count)
# #     print(count)
# vehicles_folder_count = 0
# n=3
# i=0
# densities = []
# for img_path in images_folder:
#     print("Img path", img_path)
#     img = cv2.imread(img_path)
#     vehicle_boxes = vd.detect_vehicles(img)
#     vehicle_count = len(vehicle_boxes)

#     # Update total count
#     vehicles_folder_count += vehicle_count
#     # height, width, channels = img.shape
#     # image_area = height * width

#     density = vehicle_count 
#     densities.append(density)

#     for box in vehicle_boxes:
#         x, y, w, h = box

#         cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

#         cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)
#     print("Vehicles count in image: ", vehicle_count)
#     # counting(count)    
#     cv2.imshow("Cars", img)
#     cv2.waitKey(1)

#     # # Sort densities list in ascending order
    
#         def counting(density,densities):
#             densities = sorted(densities)
#             density=densities[-1:][0]

#             # Allocate time based on density
#             time_allocated=0
#             if density>=5:
#                 time_allocated = 20 + 2 * (density - 5)
#                 if time_allocated < 20:
#                     time_allocated = 20
#                 elif density<5:
#                     time_allocated=10
#             print("Allocated time based on highest density:", time_allocated)
#             print(densities)
#             densities.pop(0)
#     counting(density,densities) 

# print("Total current count", vehicles_folder_count)





    
# import cv2
# import glob
# from vehicle_detector import VehicleDetector
# density=0
# # Load Veichle Detector
# vd = VehicleDetector()

# # Load images from a folder
# images_folder = glob.glob("images/*.jpg")
# count=[]
# def counting():
#     count.append(vehicle_count)
#     print(count)
# vehicles_folder_count = 0
# for img_path in images_folder:
#     print("Img path", img_path)
#     img = cv2.imread(img_path)

#     vehicle_boxes = vd.detect_vehicles(img)
#     vehicle_count = len(vehicle_boxes)

#     # Update total count
#     vehicles_folder_count += vehicle_count

#     # height, width, channels = img.shape
#     # image_area = height * width

#     density = vehicle_count 

#     # Allocate time based on density
#     if density<=5:
#         time_allocated = 20
#     else:
#         while density >=5 :
#             time_allocated +=2
#         density= density/2
    
#     for box in vehicle_boxes:
#         x, y, w, h = box

#         cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

#     cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)
#     print("Vehicles count in image: ", vehicle_count)
#     counting()    
#     print("Time allocated: ", time_allocated)
#     cv2.imshow("Cars", img)
#     cv2.waitKey(1)

# print("Total current count", vehicles_folder_count)

# import cv2
# import glob
# from vehicle_detector import VehicleDetector
# density=0
# # Load Veichle Detector
# vd = VehicleDetector()

# # Load images from a folder
# images_folder = glob.glob("images/*.jpg")
# count=[]
# def counting():
#     count.append(vehicle_count)
#     print(count)
# vehicles_folder_count = 0
# for img_path in images_folder:
#     print("Img path", img_path)
#     img = cv2.imread(img_path)

#     vehicle_boxes = vd.detect_vehicles(img)
#     vehicle_count = len(vehicle_boxes)

#     # Update total count
#     vehicles_folder_count += vehicle_count

#     # height, width, channels = img.shape
#     # image_area = height * width

#     density = vehicle_count 

#     # Allocate time based on density
#     if density<=5:
#         time_allocated = 20
#     else:
#         while density >=5 :
#             time_allocated +=2
#         density= density/2
    
#     for box in vehicle_boxes:
#         x, y, w, h = box

#         cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

#     cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)
#     print("Vehicles count in image: ", vehicle_count)
#     counting()    
#     print("Time allocated: ", time_allocated)
#     cv2.imshow("Cars", img)
#     cv2.waitKey(1)

# print("Total current count", vehicles_folder_count)

# for img_path in images_folder:
#     print("Img path", img_path)
#     img = cv2.imread(img_path)

#     vehicle_boxes = vd.detect_vehicles(img)
#     vehicle_count = len(vehicle_boxes)

#     # Update total count
#     vehicles_folder_count += vehicle_count

#     height, width, channels = img.shape
#     #image_area = height * width

#     density = vehicle_count 

#    # Allocate time based on density
#     if density < 20:
# #         time_allocated = 10
# #     elif density >= 20 :
# #         time_allocated = 20
# #     else:
# #         time_allocated = 30

#     for box in vehicle_boxes:
#         x, y, w, h = box

#         cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

#     cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)
#     print("Vehicles count in image: ", vehicle_count)
#     print("Time allocated: ", time_allocated)
#     cv2.imshow("Cars", img)
#     cv2.waitKey(1)

# print("Total current count", vehicles_folder_count)

# for img_path in images_folder:
#     print("Img path", img_path)
#     img = cv2.imread(img_path)

#     vehicle_boxes = vd.detect_vehicles(img)
#     vehicle_count = len(vehicle_boxes)

#     # Update total count
#     vehicles_folder_count += vehicle_count

#     for box in vehicle_boxes:
#         x, y, w, h = box

#         cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

#     cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)
#     print("Vehicles count in image: ", vehicle_count)
#     cv2.imshow("Cars", img)
#     cv2.waitKey(1)

# print("Total current count", vehicles_folder_count)


# Loop through all the images
# for img_path in images_folder:
#     print("Img path", img_path)
#     img = cv2.imread(img_path)

#     vehicle_boxes = vd.detect_vehicles(img)
#     vehicle_count = len(vehicle_boxes)

#     # Update total count
#     vehicles_folder_count += vehicle_count

#     for box in vehicle_boxes:
#         x, y, w, h = box

#         cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

#         cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

#     cv2.imshow("Cars", img)
#     cv2.waitKey(1)

# print("Total current count", vehicles_folder_count)