import os
import cv2
import csv

def TakeImage(employee_id, name, haarcasecade_path, trainimage_path, csv_file_path):
    if employee_id != "" and name != "":
        try:
            cam = cv2.VideoCapture(0)
            detector = cv2.CascadeClassifier(haarcasecade_path)
            sampleNum = 0
            directory = employee_id + "_" + name
            path = os.path.join(trainimage_path, directory)
            os.mkdir(path)
            
            # Open the CSV file to store image paths and details
            with open("\empdetails\empdetails.csv", mode='a', newline='') as file:
                writer = csv.writer(file)
                
                while True:
                    ret, img = cam.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = detector.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        sampleNum += 1
                        image_path = f"{path}/{name}_{employee_id}_{sampleNum}.jpg"
                        
                        # Save the grayscale image
                        cv2.imwrite(image_path, gray[y:y+h, x:x+w])
                        cv2.imshow("Frame", img)
                        
                        # Store the details in the CSV file
                        writer.writerow([employee_id, name, image_path])
                    
                    if cv2.waitKey(1) & 0xFF == ord("q") or sampleNum >= 50:
                        break
                
                cam.release()
                cv2.destroyAllWindows()

        except FileExistsError:
            pass  # If directory already exists, do nothing
