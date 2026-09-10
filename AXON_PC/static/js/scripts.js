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