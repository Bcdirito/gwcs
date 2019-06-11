window.addEventListener("DOMContentLoaded", function(){
  let currentLocation = ol.proj.fromLonLat([-74.028106, 40.738729])
  const homeLocation = ol.proj.fromLonLat([-74.028106, 40.738729])

  let view = new ol.View({
    center: currentLocation,
    zoom: 8
  })

  let map = new ol.Map({
    target: 'map',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    loadTilesWhileAnimating: true,
    view: view
  })

  const buttons = document.getElementsByClassName('buttons')[0]

  buttons.addEventListener("click", function(e) {
    if (e.target.name === "panHomeButton"){
      animateToLocation(homeLocation)
    } else {
      panToNewLocation()
    }
  })

  function panToNewLocation(){
    let country = document.getElementById("countryName").value.toLowerCase()
    const requestURL = `https://restcountries.eu/rest/v2/name/${country}`;
    fetch(requestURL)
    .then(res => res.json())
    .then(json => {
      let results = json[0]
      currentLocation = ol.proj.fromLonLat([results["latlng"][1], results["latlng"][0]])
      animateToLocation(currentLocation)
    })
  }

  function animateToLocation(loc){
    view.animate({
      center: loc,
      duration: 2000
    })
  }
  // console.log("Map: ", map)
  // console.log("View: ", view)
})
