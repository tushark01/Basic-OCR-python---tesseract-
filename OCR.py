import pytesseract
import cv2

args = {
	"image": "sample3.jpg",
}
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(image)
print(text)
