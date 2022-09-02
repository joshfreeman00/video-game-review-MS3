/* jshint esversion: 11 */

document.addEventListener("DOMContentLoaded", function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);
    // modal initialization
    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);
    // form select initialization
    let select = document.querySelectorAll('select');
    M.FormSelect.init(select);
});
