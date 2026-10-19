//Botón Claro / Oscuro//
document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("toggle-theme");
    const html = document.documentElement;

    //Recupera el tema guardado en localStorage
    const savedTheme = localStorage.getItem("theme");
    if(savedTheme) {
        html.setAttribute("data-bs-theme", savedTheme);
    }

    btn.addEventListener("click", function() {
        const current = html.getAttribute("data-bs-theme");
        const next = current === "dark" ? "light" : "dark";
        html.setAttribute("data-bs-theme", next);

        //Guarda el tema elegido en localStorage
        localStorage.setItem("theme", next)
    });
});

//Mostrar y Ocultar contrasenia
function togglePassword(inputId) {
    var input = document.getElementById(inputId);
    var icon = document.getElementById('icon-' + inputId);
    if (input.type === "password") {
        input.type = "text";
        icon.classList.remove('fa-eye');
        icon.classList.add('fa-eye-slash');
    } else {
        input.type = "password";
        icon.classList.remove('fa-eye-slash');
        icon.classList.add('fa-eye');
    }
}

//Marcar producto como favorito
document.addEventListener('DOMContentLoaded', function() {

    document.querySelectorAll('.btn-favorito-ajax').forEach(boton => {
        boton.addEventListener('click', function() {
            const urlFavorito = this.getAttribute('data-url');
            const icono = this.querySelector('i');

            fetch(urlFavorito, {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => {
                if (response.ok) {
                    if (icono.classList.contains('fa-regular')) {
                        icono.classList.remove('fa-regular');
                        icono.classList.add('fa-solid');
                        icono.style.color = '#E67E22';
                    } else {
                        icono.classList.remove('fa-solid');
                        icono.classList.add('fa-regular');
                        icono.style.color = '#E67E22';
                    }
                }
            })
            .catch(error => console.error('Error en favoritos:', error));
        });
    });

})