window.addEventListener("DOMContentLoaded", function() {

  const image = document.getElementById('portfolioPhoto')
  const body = document.getElementsByClassName('bodyContent')[0]
  const name = document.getElementsByTagName('h1')[0]
  const originalNameText = name.innerHTML
  const buttons = document.getElementsByClassName("underPhotoButtons")
  let counter = 0

  const portfolioPhotos = ["https://bdirito.dev/static/media/about_me_photo.582ed4a6.jpg", "https://scontent-iad3-1.xx.fbcdn.net/v/t1.0-9/28468271_10215307293583932_8001881987859963124_n.jpg?_nc_cat=110&_nc_ht=scontent-iad3-1.xx&oh=9cb96248604e299ba10934372b096425&oe=5D57F4E2", "https://bdirito.dev/static/media/contact_photo.2af853ad.jpeg"]

  image.addEventListener("mouseenter", function(e){
    image.id = "portfolioPhotoHover"
  })

  image.addEventListener("mouseout", function(e){
    image.id = "portfolioPhoto"
  })

  buttons[0].addEventListener("click", function(e){
    if (e.target.innerHTML === "About Me") e.target.innerText = "Hide"
    else e.target.innerHTML = "About Me"

    if (body.className === "bodyContent") body.className = "bodyContentClicked"
    else body.className = "bodyContent"
  })

  buttons[1].addEventListener("click", function(e){
    if (counter < portfolioPhotos.length - 1) counter += 1
    else counter = 0

    image.src = portfolioPhotos[counter]
  })

})
