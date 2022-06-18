const modal = document.querySelectorAll('#modal')
const openModal = document.querySelectorAll('.open-modal')
const closeModal = document.querySelectorAll('.modal-botao')
openModal.forEach(button => {
    button.addEventListener('click', () => {
        console.log('ola');
        modal.forEach(nome => {
            nome.showModal();
        })
    })
})

closeModal.addEventListener('click', () => {
    modal.close();
})

