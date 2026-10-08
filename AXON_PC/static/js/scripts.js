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