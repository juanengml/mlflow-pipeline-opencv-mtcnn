from mtcnn import MTCNN
import cv2
import os 
from console_logging.console import Console
console = Console()
detector = MTCNN()

def predict(IMG_PATH):
  img = cv2.cvtColor(cv2.imread(IMG_PATH), cv2.COLOR_BGR2RGB)
  console.info("PREDICT IMAGE...")
  return {IMG_PATH:detector.detect_faces(img)}

def main():
    list_valus = [predict("Data/{}".format(img)) for img in os.listdir("Data")]
    console.success(list_valus)

if __name__=="__main__":
    console.log("STARINT INFERENCE MODULE")
    main()
    console.log("DONE INFERENCE MODULE")
