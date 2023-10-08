function allowDrop(event) {
    event.preventDefault();
}

function drop(event) {
    event.preventDefault();
    const files = event.dataTransfer.files;
    const imageElement = document.getElementById('uploaded-image');

    // Отправка файла на сервер
    const formData = new FormData();
    formData.append('file', files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Файл успешно загружен:', data);

        // Отображение загруженного изображения
        const imageUrl = data.img_url;
        const imageElement = document.getElementById('uploaded-image');
        imageElement.src = imageUrl;;
    })
    .catch(error => {
        console.error('Произошла ошибка при загрузке файла:', error);
    });
}

async function loadImage() {
    const imageElement = document.getElementById("image");
    const response = await fetch("http://127.0.0.1:8000/get_image/image.jpg"); // замените на актуальный URL вашего FastAPI сервера и имя изображения
    const blob = await response.blob();
    const imageUrl = URL.createObjectURL(blob);
    imageElement.src = imageUrl;
}