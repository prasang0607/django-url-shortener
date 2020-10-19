document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#file_upload').addEventListener('change', () => {
        const inputElement = document.querySelector('#file_upload');
        const labelElement = document.querySelector('.custom-file label');
        labelElement.textContent = inputElement.value;
    });
});