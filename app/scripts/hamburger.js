const menuButton = document.querySelector("#header-hamburger");
const mobileMenu = document.querySelector("#header-nav-mobile");
let menuOpen = false;


menuButton.addEventListener("click", () => {
    if (!menuOpen) {
        menuButton.classList.add("open-hamburger");
        mobileMenu.style.maxHeight = mobileMenu.scrollHeight + "px";
        menuOpen = true;
    }
    else {
        menuButton.classList.remove("open-hamburger");
        mobileMenu.style.maxHeight = "0px";
        menuOpen = false;
    }
})


window.addEventListener("resize", () => {
    const windowWidth = window.innerWidth;
    const maxWidth = 900;

    if (windowWidth >= maxWidth && menuOpen) {
        menuButton.classList.remove("open-hamburger");
        mobileMenu.style.maxHeight = "0px";
        menuOpen = false;
    }
})