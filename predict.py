from scipy.special import softmax
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import cv2
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt

classes={'Crack Not Found': 0, 'Crack Found': 1}


model = load_model('model.h5')
video_path = "tomato2.mp4"
cap = cv2.VideoCapture("http://192.168.29.235:8080/video")  # 0 is typically the default webcam

fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:  # fallback if fps is not available
    fps = 30  # or any reasonable default based on your camera
frame_interval = int(fps * 3)  # Save every 3 seconds

frame_count = 0
saved_images_count = 0
heat_map_list=[]
crop_size=(128,128)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    if frame_count % frame_interval == 0:
        saved_images_count += 1
#         img_filename = f"saved_frame_{saved_images_count}.jpg"
#         cv2.imwrite(img_filename, frame)
#         print(f"Saved {img_filename}")
    
#     h,w,_=frame.shape
#     x_centre=w//2- crop_size[0]//2
#     y_centre = h//2 - crop_size[1]//2

#     leaf_image= frame[y_centre:y_centre+crop_size[1], x_centre:x_centre+crop_size[0]]


        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        img=cv2.resize(frame, (128,128))

        img_array= image.img_to_array(img)
        img_array= np.expand_dims(img_array, axis=0)
        img_array=img_array/255.0

        pred = model.predict(img_array)
        prob = softmax(pred, axis=1) * 100
        pecentage=np.max(prob, axis=1)

        out=np.argmax(pred,axis=1)[0]
        heat_map_list.append(out)
        for i in classes.items():
            if i[1]==out:
                out = i[0]
        cv2.putText(frame, f"prediction: {out} percentage{pecentage}", (10,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
        cv2.imshow("Video Pred", frame)
    frame_count += 1
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

a=np.array(heat_map_list)
a=a.reshape(5,5)
colormap = sns.color_palette("Greens") 
sns.heatmap(a, cmap=colormap)
plt.show()
cap.release()
cv2.destroyAllWindows()