import requests
from uuid import uuid4
from console_logging.console import Console
console = Console()


file_haard = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
image = "https://thispersondoesnotexist.com/image"

def download_model():
        url = file_haard
        console.log("DOWNLOADING MODEL ")
        r = requests.get(url, allow_redirects=True)
        console.log("SAVE MODEL")
        open('Model/haarcascade_frontalface_default.xml', 'wb').write(r.content)
        console.success("DONE !")

def download_fotos():
        url = image
        console.log("DOWNLOADING IMAGE ")
        r = requests.get(url, allow_redirects=True)
        console.log("SAVE image")
        path = 'Data/{}.jpg'.format(str(uuid4()))
        console.info(path)
        open(path, 'wb').write(r.content)
        console.success("DONE !")

def main():
    [download_fotos() for p in range(10)]
    #download_model()

if __name__ == "__main__":
    main()