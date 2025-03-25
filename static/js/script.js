function toggleMenu() {
    var menu = document.getElementById("mobile-menu");
    var overlay = document.querySelector(".menu-overlay");

    // اگر منو باز باشد، ببند
    if (menu.classList.contains("show-menu")) {
        menu.classList.remove("show-menu");
        overlay.remove();
    } else {
        // منو را باز کن
        menu.classList.add("show-menu");

        // اضافه کردن یک لایه روی صفحه برای بستن منو
        var overlayDiv = document.createElement("div");
        overlayDiv.classList.add("menu-overlay");
        overlayDiv.onclick = toggleMenu;
        document.body.appendChild(overlayDiv);
    }
}
document.addEventListener("DOMContentLoaded", function () {
    let menuIcon = document.querySelector(".menu-icon");  // دکمه همبرگر
    let mobileMenu = document.getElementById("mobile-menu");  // منوی موبایل

   
    // بستن منو هنگام کلیک روی هرجای صفحه
    document.addEventListener("click", function (event) {
        if (!mobileMenu.contains(event.target) && !menuIcon.contains(event.target)) {
            mobileMenu.classList.remove("show-menu");
        }
    });
});
