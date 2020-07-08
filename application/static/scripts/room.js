let socket = io()

socket.on('connect', function () {
    socket.emit('message', {data: 'test'})
});
