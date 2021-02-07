import os 
import cv2
from console_logging.console import Console
console = Console()

def resize_image(img_path):
    console.log(" RESIZE IMAGE : "+img_path)
    h = 420
    w = 420
    dim = (w, h)
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(img_path, img) 
    console.success("DONE ! ")

def main():
    [resize_image("Data/{}".format(img)) for img in os.listdir("Data")]
    
if __name__ == "__main__":
    main()    