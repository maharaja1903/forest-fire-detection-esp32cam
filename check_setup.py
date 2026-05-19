import platform
import sys

print("=" * 50)
print("SYSTEM INFO")
print("=" * 50)

print(f"OS              : {platform.system()} {platform.release()}")
print(f"Python Version  : {sys.version}")

print("\n" + "=" * 50)
print("PYTORCH")
print("=" * 50)

try:
    import torch

    print(f"PyTorch Version : {torch.__version__}")
    print(f"CUDA Available  : {torch.cuda.is_available()}")

    if torch.cuda.is_available():
        print(f"CUDA Version    : {torch.version.cuda}")
        print(f"GPU Name        : {torch.cuda.get_device_name(0)}")
        print(f"GPU Count       : {torch.cuda.device_count()}")

        cudnn_version = torch.backends.cudnn.version()
        print(f"cuDNN Version   : {cudnn_version}")

except Exception as e:
    print("PyTorch Error:", e)

print("\n" + "=" * 50)
print("TENSORRT")
print("=" * 50)

try:
    import tensorrt as trt

    print(f"TensorRT Version: {trt.__version__}")

except Exception as e:
    print("TensorRT Error:", e)

print("\n" + "=" * 50)
print("OPENCV")
print("=" * 50)

try:
    import cv2

    print(f"OpenCV Version  : {cv2.__version__}")

except Exception as e:
    print("OpenCV Error:", e)

print("\n" + "=" * 50)
print("ULTRALYTICS")
print("=" * 50)

try:
    import ultralytics

    print(f"Ultralytics Ver : {ultralytics.__version__}")

except Exception as e:
    print("Ultralytics Error:", e)

print("\n" + "=" * 50)
print("ONNX")
print("=" * 50)

try:
    import onnx

    print(f"ONNX Version    : {onnx.__version__}")

except Exception as e:
    print("ONNX Error:", e)

print("\n" + "=" * 50)
print("DONE")
print("=" * 50)

