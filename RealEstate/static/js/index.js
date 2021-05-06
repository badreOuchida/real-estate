let navbar = document.querySelector("#navbar .nav_container .nav_links");
let openIcon = document.getElementById("nav_open");
let closeIcon = document.getElementById("close_nav");
openIcon.addEventListener("click", (e) =>{
    openIcon.classList.add("clicked");
    navbar.classList.add("open");
})
closeIcon.addEventListener("click", (e) =>{
    openIcon.classList.remove("clicked");
    navbar.classList.remove("open");
    console.log("work2");
})
console.log("work");