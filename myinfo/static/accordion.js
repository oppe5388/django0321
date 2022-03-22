document.addEventListener('DOMContentLoaded', e => {
    for (const button of document.getElementsByClassName('accordion-button')) {
        button.addEventListener('click', e => {
            button.parentNode.classList.toggle('open');
        });
    }
});