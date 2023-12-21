function loadTitle() {
    const title = document.querySelector("#header-main > h1");
    title.style.opacity = "1";
}


function loadSubTitle() {
    const subTitle = document.querySelector("#header-main > p");
    subTitle.style.opacity = "1";
    subTitle.style.color = "var(--color-blue-bright)";
}

window.addEventListener("load", loadTitle);
window.addEventListener("load", loadSubTitle);