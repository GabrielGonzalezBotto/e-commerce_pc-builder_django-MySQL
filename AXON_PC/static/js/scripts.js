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
document.querySelectorAll('.btn-favorito').forEach(icon => {
    icon.addEventListener('click', function(e) {
        e.preventDefault(); // Evita que la página salte
        if (this.classList.contains('fa-regular')) {
            this.classList.remove('fa-regular');
            this.classList.add('fa-solid');
            this.style.color = '#e74c3c'; // Se pinta de rojo Axon
        } else {
            this.classList.remove('fa-solid');
            this.classList.add('fa-regular');
            this.style.color = ''; // Vuelve al color base
        }
    });
});