document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#copy-url').addEventListener('click', () => {
        const short_url = document.querySelector('#your-url');
        short_url.select();
        document.execCommand('Copy');
        document.querySelector('.alert').classList.remove('d-none');
        setTimeout(() => {
            document.querySelector('.alert').classList.add('d-none');
        }, 3000);
    });

    document.querySelector('#open-url').addEventListener('click', () => {
        const short_url = document.querySelector('#your-url');
        const url = short_url.value.trim();
        window.open(url, '_blank');
    });
});
