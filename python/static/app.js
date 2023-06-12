var mediaItems = [];

fetch('/get_images', {method: 'GET'})
    .then(response => response.json())
    .then(data => {mediaItems = data;})
    .then(data => {console.log(data)})

let currentIndex = 0;

const mediaContainer = document.getElementById("mediaContainer")
const previousButton = document.getElementById("previousButton");
const nextButton = document.getElementById("nextButton");

previousButton.addEventListener('click', showPreviousMedia);
nextButton.addEventListener('click', showNextMedia);

const hammer = new Hammer(document.body);
hammer.get('swipe').set({direction: Hammer.DIRECTION_HORIZONTAL});
hammer.on('swipeleft', showNextMedia);
hammer.on('swiperight', showPreviousMedia);

function showNextMedia() {
    currentIndex = (currentIndex + 1) % mediaItems.length;
    updateMedia();
}

function showPreviousMedia() {
    currentIndex = (currentIndex - 1 + mediaItems.length) % mediaItems.length;
    updateMedia();
}

function updateMedia() {
    const mediaItem = mediaItems[currentIndex];
    mediaContainer.innerHTML = '';

    const imageExtensions = ['jpg', 'jpeg', 'png'];
    const videoExtensions = ['mp4', 'webm', 'ogg'];
    const fileExt = getFileExt(mediaItem);

    if (imageExtensions.includes(fileExt)) {
        const img = document.createElement('img');
        img.src = `${mediaItem}`
        mediaContainer.appendChild(img);
    }
    else if (videoExtensions.includes(fileExt)) {
        const video = document.createElement('video');
        video.src = `${mediaItem}`;
        video.controls = true;
        mediaContainer.appendChild(video);
    }
}

function getFileExt(filename) {
    return filename.split('.').pop().toLowerCase();
}

updateMedia();