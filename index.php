<!DOCTYPE html>
<html>
<head>
    <title>Rover Dashboard</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

<h1>Autonomous Rover Dashboard</h1>

<div class="controls">
    <button onclick="sendCommand('forward')">Forward</button>
    <button onclick="sendCommand('left')">Left</button>
    <button onclick="sendCommand('stop')">Stop</button>
    <button onclick="sendCommand('right')">Right</button>
    <button onclick="sendCommand('backward')">Backward</button>
</div>

<h2>Live Camera</h2>
<img src="http://RASPBERRY_PI_IP:5000/video" width="640">

<script src="script.js"></script>

</body>
</html>
