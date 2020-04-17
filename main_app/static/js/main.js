// Hide submenus
$('#body-row .collapse').collapse('hide');

// Collapse/Expand icon
$('#collapse-icon').addClass('fa-angle-double-left');

// Collapse click
$('[data-toggle=sidebar-colapse]').click(function () {
    SidebarCollapse();
});

function SidebarCollapse() {
    mainContent = document.getElementById('main-content')
    $('.menu-collapsed').toggleClass('d-none');
    $('.sidebar-submenu').toggleClass('d-none');
    $('.submenu-icon').toggleClass('d-none');
    $('#sidebar-container').toggleClass('sidebar-expanded sidebar-collapsed');

    // Treating d-flex/d-none on separators with title
    var SeparatorTitle = $('.sidebar-separator-title');
    if (SeparatorTitle.hasClass('d-flex')) {
        SeparatorTitle.removeClass('d-flex');
    } else {
        SeparatorTitle.addClass('d-flex');
    }
    var expanded = $('#sidebar-container');
    var collapsed = $('#sidebar-container');
    if (expanded.hasClass('sidebar-expanded')) {
        $('#main-content').css("margin-left", "230px");
    } else if (collapsed.hasClass('sidebar-collapsed')) {
        $('#main-content').css("margin-left", "60px");
    } else {
        $('#main-content').css("margin-left", "230px");
    }


    // Collapse/Expand icon
    $('#collapse-icon').toggleClass('fa-angle-double-left fa-angle-double-right');
}




document.getElementById('share-btn').addEventListener("click", shareFn);
function shareFn(){
    windowHref = window.location.href;
    alert(windowHref);
}