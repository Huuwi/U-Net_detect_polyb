

const image1 = document.querySelector("#image1")
const image2 = document.querySelector("#image2")

let input_image

const set_image = (element, file) => {
    const reader = new FileReader();
    reader.onload = function (e) {
        const imgElement = document.createElement('img');
        imgElement.src = e.target.result;
        imgElement.style.width = '100%';
        imgElement.style.height = '100%';
        element.innerHTML = '';
        element.appendChild(imgElement);
    }
    reader.readAsDataURL(file);
}


async function handleImageUpload(file) {
    const formData = new FormData();
    formData.append('file', file);
    try {
        const response = await fetch("http://127.0.0.1:5000/handler_image", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const blob = await response.blob();

        let imageUrl = URL.createObjectURL(blob);
        input_image = imageUrl
        return imageUrl;
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}


const choose_file_btn = document.querySelector("#choose_file").addEventListener("change", async (event) => {
    const file = event.target.files[0];
    if (file) {
        set_image(image1, file)
        let handled_image = await handleImageUpload(file)
        console.log(handled_image);
    } else {
        alert("tải ảnh không thành công")
    }
})

const btn = document.querySelector("#display_btn").addEventListener("click", () => {
    console.log(input_image);
    const divElement = document.getElementById('image2');
    divElement.style.backgroundImage = `url(${input_image})`;
    divElement.style.backgroundSize = 'cover'; // Tùy chọn: Đảm bảo ảnh bao phủ toàn bộ div
    divElement.style.backgroundPosition = 'center'; // Tùy chọn: Canh giữa ảnh
})