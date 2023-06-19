var gallery;
var mediaItems;
var currentIndex;

const galleryButton = document.getElementById('galleryButton')
galleryButton.addEventListener('click', showGallery)

document.body.addEventListener('click', function(event) {
    if (event.target.id == 'galleryViewport') {
        removeGallery();
    };
});

async function showGallery() {
    currentIndex = 0;

    const gallery = document.createElement('div');
    gallery.classList.add('gallery');
    gallery.setAttribute('id', 'gallery');
    document.body.appendChild(gallery);

    const galleryViewport = document.createElement('div');
    galleryViewport.classList.add('galleryViewport');
    galleryViewport.setAttribute('id', 'galleryViewport');
    gallery.appendChild(galleryViewport);

    const galleryNavigation = document.createElement('div');
    galleryNavigation.classList.add('galleryNavigation');
    galleryNavigation.setAttribute('id', 'galleryNavigation');
    gallery.appendChild(galleryNavigation)

    const previousButton = document.createElement('button');
    previousButton.classList.add('previousButton');
    previousButton.setAttribute('id', 'previousButton');
    previousButton.innerText = "Previous";
    galleryNavigation.appendChild(previousButton);

    const nextButton = document.createElement('button');
    nextButton.classList.add('nextButton');
    nextButton.setAttribute('id', 'nextButton');
    nextButton.innerText = "Next";
    galleryNavigation.appendChild(nextButton);

    const image = document.createElement('img');
    image.src = "";
    image.classList.add('galleryImage');
    image.setAttribute('id', 'galleryImage');
    galleryViewport.appendChild(image);

    previousButton.addEventListener('click', showPreviousMedia);
    nextButton.addEventListener('click', showNextMedia);

    startFetch()
}

function removeGallery() {
    gallery = document.getElementById('gallery');
    gallery.remove();
}

async function startFetch() {
    const response = await fetch(`/ls?ls=${window.location.pathname.slice(2)}`, {method: 'GET'});
    mediaItems = await response.json();
    console.log(mediaItems)
    updateMedia();
}

function updateMedia() {
    const mediaItem = mediaItems[currentIndex];
    galleryViewport.innerHTML = '';

    const imageExtensions = ['jpg', 'jpeg', 'png', 'gif'];
    const videoExtensions = ['mp4', 'webm', 'ogg'];
    const fileExt = getFileExt(mediaItem);

    if (imageExtensions.includes(fileExt)) {
        const img = document.createElement('img');
        img.src = `/f${mediaItem}`
        galleryViewport.appendChild(img);
    }
    else if (videoExtensions.includes(fileExt)) {
        const video = document.createElement('video');
        video.src = `/f${mediaItem}`;
        video.controls = true;
        galleryViewport.appendChild(video);
    }
}

function getFileExt(filename) {
    return filename.split('.').pop().toLowerCase();
}

function showNextMedia() {
    currentIndex = (currentIndex + 1) % mediaItems.length;
    updateMedia();
}

function showPreviousMedia() {
    currentIndex = (currentIndex - 1 + mediaItems.length) % mediaItems.length;
    updateMedia();
}