const CAM_IMAGES = [
    ["/assets/breast-cancer-detection/cam_10638_L.svg", "10638_L"],
    ["/assets/breast-cancer-detection/cam_11249_L.svg", "11249_L"],
    ["/assets/breast-cancer-detection/cam_12463_R.svg", "12463_R"],
    ["/assets/breast-cancer-detection/cam_16346_R.svg", "16346_R"],
    ["/assets/breast-cancer-detection/cam_1775_L.svg", "1775_L"],
    ["/assets/breast-cancer-detection/cam_40614_L.svg", "40614_L"],
    ["/assets/breast-cancer-detection/cam_43561_L.svg", "43561_L"],
    ["/assets/breast-cancer-detection/cam_49442_R.svg", "49442_R"],
    ["/assets/breast-cancer-detection/cam_50877_R.svg", "50877_R"],
    ["/assets/breast-cancer-detection/cam_36748_L.svg", "36748_L"]
]

let IMAGE_INDEX = 0;


function showImage(index) {
    const galleryImage = document.getElementById("gallery-image");
    const galleryID = document.getElementById("gallery-id");
    
    [cam_image, patient_id] = CAM_IMAGES[index]
    galleryImage.src = cam_image;
    galleryID.innerText = patient_id;
}

function showPreviousImage() {
    IMAGE_INDEX -= 1;
    if (IMAGE_INDEX < 0) {
        IMAGE_INDEX = CAM_IMAGES.length - 1
    }

    showImage(IMAGE_INDEX);
}

function showNextImage() {
    IMAGE_INDEX += 1;
    if (IMAGE_INDEX >= CAM_IMAGES.length) {
        IMAGE_INDEX = 0;
    }

    showImage(IMAGE_INDEX);
}