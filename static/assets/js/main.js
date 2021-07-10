const spin = document.querySelector('.spin');

// remove loader 
window.addEventListener('load', () =>{
    setTimeout(() => {
        spin.classList.remove('loader')
    }, 500);
})

const form_fields = document.querySelectorAll('input')
const navbar = document.querySelector('.navbar-area ')
const toogler = document.querySelector('.toogler')
const collapse = document.querySelector('.collapse')

toogler.addEventListener('click',()=>{
    toogler.classList.toggle('active')
    navbar.classList.toggle('height')
    collapse.classList.toggle('show')
})

if (form_fields.length > 0){
    form_fields[1].setAttribute('placeholder', 'John Doe')
    form_fields[2].setAttribute('placeholder', '********')

    if (form_fields.length > 3){
        form_fields[3].setAttribute('placeholder', '********')
    }
}
