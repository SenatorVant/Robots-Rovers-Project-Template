function sendCommand(command) {
    fetch(`control.php?cmd=${command}`)
        .then(response => response.text())
        .then(data => console.log(data));
}
