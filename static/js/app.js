let swiper = new Swiper(".mySwiper", {
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});

const modal = document.querySelector('.modal')
const modalTrigger = document.querySelector('[data-modal]')

modalTrigger.addEventListener('click' , openModal)
modal.addEventListener('click' , closeModal)

function openModal () {
    modal.classList.add('show')
    modal.classList.remove('hide')
    console.log(23)
}
function closeModal(){
    modal.classList.add('hide')
    modal.classList.remove('show')
}
