$(document).ready(function() {
    // Función para abrir el menú lateral
    function openSidebar() {
        // Usa la clase .open que define tu CSS
        $('.sidebar').addClass('open'); 
        $('.sidebar-overlay').addClass('open');
        
        // Esta clase (opcional en tu CSS) desplaza el contenido
        $('body').addClass('menu-open'); 
    }

    // Función para cerrar el menú lateral
    function closeSidebar() {
        // Remueve las mismas clases para ocultarlo
        $('.sidebar').removeClass('open');
        $('.sidebar-overlay').removeClass('open');
        $('body').removeClass('menu-open');
    }

    // --- MANEJADORES DE EVENTOS ---

    // Al hacer clic en el ícono de hamburguesa
    $('#menuToggle, .menu-toggle').on('click', function(e) {
        e.preventDefault();
        openSidebar();
    });

    // Al hacer clic en el botón de cerrar (X)
    $('.close-sidebar').on('click', function() {
        closeSidebar();
    });

    // Al hacer clic en el fondo oscuro (overlay)
    $('.sidebar-overlay').on('click', function() {
        closeSidebar();
    });

    // --- Lógica del Modal (sin cambios, ya debería funcionar) ---
    $('#ingresoBtn').on('click', function(e) {
        e.preventDefault();
        $('.modal').fadeIn('fast');
    });

    $('.modal .close').on('click', function() {
        $('.modal').fadeOut('fast');
    });

    $(window).on('click', function(event) {
        if ($(event.target).is('.modal')) {
            $('.modal').fadeOut('fast');
        }
    });

    $('.role-option').on('click', function() {
        $('.role-option').removeClass('selected');
        $(this).addClass('selected');
        $(this).find('input[type="radio"]').prop('checked', true);
    });
});