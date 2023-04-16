<h1>Face Detection using YOLOv5 and TensorRT on Jetson Nano</h1>
<p>This repository contains the code for face detection using YOLOv5 and TensorRT on Jetson Nano. The model is based on YOLOv5 and has been optimized using TensorRT for faster inference on Jetson Nano.</p>

<h2>Requirements</h2>
<ul>
<li>Jetson Nano with JetPack 4.4 or later</li>
<li>Python 3.6 or later</li>
<li>PyTorch 1.7.0 or later</li>
<li>OpenCV 4.1.1 or later</li>
</ul>

<h2>Installation</h2>
<p>Clone this repository:</p>
<pre><code>git clone https://github.com/abuod0/Improved-Face-Detection-YOLOv5-Based.git</code></pre>

<p>Install the required packages:</p>
<pre><code>pip3 install -r requirements.txt</code></pre>

<h2>Usage</h2>
<ol>
<li>Download the pre-trained YOLOv5 model for face detection from <a href="https://link/to/download">here</a>.</li>
<li>Copy the downloaded model to the models directory of this repository.</li>
<li>Run the facetrackyolo.py script:<br><code>python3 facetrackyolo.py</code></li>
<li>The script will start the webcam and display the output with bounding boxes around the detected faces.</li>
</ol>

<h2>Credits</h2>
<p>This repository is built using the YOLOv5 repository by Ultralytics: <a href="https://github.com/ultralytics/yolov5">https://github.com/ultralytics/yolov5</a>. The pre-trained model used in this repository has been optimized using TensorRT for faster inference on Jetson Nano.</p>
