Ultralytics 8.4.14 🚀 Python-3.12.12 torch-2.10.0+cpu CPU (Intel Xeon CPU @ 2.20GHz)
💡 ProTip: Export to OpenVINO format for best performance on Intel hardware. Learn more at https://docs.ultralytics.com/integrations/openvino/
YOLOv8n-cls summary (fused): 30 layers, 1,437,442 parameters, 0 gradients, 3.3 GFLOPs

PyTorch: starting from 'runs/classify/train/weights/best.pt' with input shape (1, 3, 224, 224) BCHW and output shape(s) (1, 2) (2.8 MB)
requirements: Ultralytics requirements ['onnx>=1.12.0,<2.0.0', 'onnxslim>=0.1.71', 'onnxruntime'] not found, attempting AutoUpdate...
Using Python 3.12.12 environment at: /usr
Resolved 12 packages in 394ms
Prepared 4 packages in 6.31s
Installed 4 packages in 1.43s
 + colorama==0.4.6
 + onnx==1.20.1
 + onnxruntime==1.24.2
 + onnxslim==0.1.85

requirements: AutoUpdate success ✅ 9.3s
WARNING ⚠️ requirements: Restart runtime or rerun command for updates to take effect


ONNX: starting export with onnx 1.20.1 opset 22...
/usr/local/lib/python3.12/dist-packages/torch/onnx/_internal/torchscript_exporter/utils.py:552: OnnxExporterWarning: Exporting to ONNX opset version 22 is not supported. by 'torch.onnx.export()'. The highest opset version supported is 20. To use a newer opset version, consider 'torch.onnx.export(..., dynamo=True)'. 
  _export(
ONNX: slimming with onnxslim 0.1.85...
ONNX: export success ✅ 11.4s, saved as 'runs/classify/train/weights/best.onnx' (5.5 MB)

Export complete (11.5s)
Results saved to /content/runs/classify/train/weights
Predict:         yolo predict task=classify model=runs/classify/train/weights/best.onnx imgsz=224 
Validate:        yolo val task=classify model=runs/classify/train/weights/best.onnx imgsz=224 data=/content/drive/MyDrive/pothole_yolo  
Visualize:       https://netron.app
✅ ONNX model saved successfully