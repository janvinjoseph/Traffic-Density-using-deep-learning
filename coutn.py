import cv2
import os
import glob
from vehicle_detector import VehicleDetector


vd = VehicleDetector()                                                                  
time_allocated = 0


images_folder = sorted(glob.glob("images/*.jpg"))
count = []
densities = []
density = 0
def delete(densities):
    if density == densities[-1]:
        print("Deleting image with high density:", img_path)
        os.remove(img_path)

def counting(density, densities, img_path):
    densities.sort()
    density = densities[-1]

    time_allocated = 0
    if density > 5:
        time_allocated = 20 + 2 * (density - 5)
        if time_allocated < 20:
            time_allocated = 20
    elif density < 5:
        time_allocated = 10
    print("Allocated time based on highest density:", time_allocated)

    # if density == densities[-1]:
    #     print("Deleting image with high density:", img_path)
    #     os.remove(img_path)

for i in range(0, len(images_folder), 4):
    batch_images = images_folder[i:i+4]
    batch_densities = []
    for img_path in batch_images:
        vehicles_folder_count = 0
        print("Img path", img_path)
        img = cv2.imread(img_path)
        vehicle_boxes = vd.detect_vehicles(img)
        vehicle_count = len(vehicle_boxes)

        vehicles_folder_count += vehicle_count

        density = vehicles_folder_count
        batch_densities.append(density)

        for box in vehicle_boxes:
            x, y, w, h = box

            cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

            cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)
        print("Vehicles count in image: ", vehicle_count)

        cv2.imshow("Cars", img)
        cv2.waitKey(1)

        print("Total current count", vehicles_folder_count)
    densities.extend(batch_densities)
    for img_path, density in zip(batch_images, batch_densities):
        counting(density, densities, img_path)
        delete(densities)

    print(densities)

# import cv2
# import os
# import glob
# from vehicle_detector import VehicleDetector


# vd = VehicleDetector()
# time_allocated = 0


# images_folder = sorted(glob.glob("images/*.jpg"))
# count = []
# densities = []
# density=0

# def counting(density, densities):
#     densities = sorted(densities)
#     density = densities[-1:][0]

#     time_allocated = 0
#     if density > 5:
#         time_allocated = 20 + 2 * (density - 5)
#         if time_allocated < 20:
#             time_allocated = 20
#     elif density < 5:
#         time_allocated = 10
#     print("Allocated time based on highest density:", time_allocated)
   
# for i in range(0, len(images_folder), 4):
#     batch_images = images_folder[i:i+4]
#     batch_vehicle_counts = []
#     for img_path in batch_images:
#         vehicles_folder_count = 0
#         print("Img path", img_path)
#         img = cv2.imread(img_path)
#         vehicle_boxes = vd.detect_vehicles(img)
#         vehicle_count = len(vehicle_boxes)

#         vehicles_folder_count += vehicle_count
#         batch_vehicle_counts.append(vehicle_count)

#         density = vehicles_folder_count
#         densities.append(density)

#         for box in vehicle_boxes:
#             x, y, w, h = box

#             cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

#             cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)
#         print("Vehicles count in image: ", vehicle_count)

#         cv2.imshow("Cars", img)
#         cv2.waitKey(1)

#     batch_density = sum(batch_vehicle_counts) / len(batch_vehicle_counts)
#     densities.append(batch_density)

#     if batch_density > 5:
#         for img_path in batch_images:
#             if os.path.exists(img_path):
#                 os.remove(img_path)
#                 print("Deleted image with high vehicle density:", img_path)
    
#     print("Total current count", vehicles_folder_count)

# counting(density, densities)
# print(densities)












# import cv2
# import os
# import glob
# from vehicle_detector import VehicleDetector


# vd = VehicleDetector()
# time_allocated = 0


# images_folder = sorted(glob.glob("images/*.jpg"))
# count = []
# densities = []
# density = 0


# def counting(density, densities):
#     if len(densities) == 0:
#         print("No densities found")
#         return

#     densities = sorted(densities)
#     density = densities[-1]

#     time_allocated = 0
#     if density > 5:
#         time_allocated = 20 + 2 * (density - 5)
#         if time_allocated < 20:
#             time_allocated = 20
#     elif density < 5:
#         time_allocated = 10
#     print("Allocated time based on highest density:", time_allocated)


# for img_path in images_folder:
#     vehicles_folder_count = 0
#     print("Img path", img_path)
#     img = cv2.imread(img_path)
#     vehicle_boxes = vd.detect_vehicles(img)
#     vehicle_count = len(vehicle_boxes)

#     vehicles_folder_count += vehicle_count

#     density = vehicle_count
#     densities.append(density)

#     for box in vehicle_boxes:
#         x, y, w, h = box

#         cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

#         cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

#     print("Vehicles count in image: ", vehicle_count)

#     cv2.imshow("Cars", img)
#     cv2.waitKey(1)

#     densities = sorted(densities)

#     if len(densities) > 0 and density == densities[-1]:
#         if os.path.exists(img_path):
#             os.remove(img_path)

#     print("Total current count", vehicles_folder_count)

# counting(density, densities)
# print(densities)
































# import cv2
# import os
# import glob
# from vehicle_detector import VehicleDetector

# # Load Veichle Detector
# vd = VehicleDetector()
# time_allocated = 0

# # Load the first four images from the folder
# images_folder = sorted(glob.glob("images/*.jpg"))
# count = []
# densities = []
# density=0

# def counting(density, densities):
#     densities = sorted(densities)
#     density = densities[-1:][0]

#     # Allocate time based on density
#     time_allocated = 0
#     if density > 5:
#         time_allocated = 20 + 2 * (density - 5)
#         if time_allocated < 20:
#             time_allocated = 20
#     elif density < 5:
#         time_allocated = 10
#     print("Allocated time based on highest density:", time_allocated)
#     # if len(densities) > 0 and density == densities[-1:][0]:
#     #     if os.path.exists(img_path):
#     #         os.remove(img_path)

# for img_path in images_folder:
#     vehicles_folder_count=0
#     print("Img path", img_path)
#     img = cv2.imread(img_path)
#     vehicle_boxes = vd.detect_vehicles(img)
#     vehicle_count = len(vehicle_boxes)

#     # Update total count
#     vehicles_folder_count += vehicle_count

#     # density = vehicle_count
#     density=vehicle_count
#     densities.append(density)
#     # counting(density, densities)
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
#     if len(densities) > 0 and density == densities[-1:][0]:
#         if os.path.exists(img_path):
#             os.remove(img_path)

#     print("Total current count", vehicles_folder_count)
# counting(density, densities)
# print(densities)
# # densities.pop(0)

