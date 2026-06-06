from ultralytics import YOLO

def main():
    model = YOLO("yolo26n-seg.yaml")
    results = model.train(data="coco8.yaml", epochs=3)

    results = model.val()
    model.

    results = model("https://ultralytics.com/images/bus.jpg")

if __name__ == "__main__":
    main()
