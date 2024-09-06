import os
import gdown

if not os.path.exists("model/"):
    print("[INFO] making directory ./model")
    os.mkdir("model")

print("[INFO] downloading model/gender_detection.model")
gdown.download(
    "https://drive.google.com/file/d/1bv1hl5J0Zyxwd0g6Y3fCu5BUtdROhOjH/view?usp=sharing",
    output="model/gender_detection.model",
)
