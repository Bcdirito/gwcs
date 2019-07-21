window.addEventListener("DOMContentLoaded", function(){
    let currentLocation = ol.proj.fromLonLat([-74.028106, 40.738729])
    let homeLocation = ol.proj.fromLonLat([-74.028106, 40.738729])
    let buttons = document.getElementsByClassName('buttons')[0]

    
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
  
    buttons.addEventListener("click", function(e) {
      if (e.target.name === "panHomeButton") animateToLocation(homeLocation)
      else if (e.target.name === "panToNewLocationButton") panToNewLocation()
    })
  
    function panToNewLocation(){
        // Discuss how we got this
        // Discuss why id vs class or name
        // Discuss why you have made it lowercase
        let country = document.getElementById("countryName").value.toLowerCase()

        // Discuss why you made a variable vs. just putting it in a fetch request
        let requestURL = `https://restcountries.eu/rest/v2/name/${country}`

        // Discuss the process of a fetch request
        // Discuss why fetch vs. XML
        // Discuss asynch JS with .then()
        fetch(requestURL)
        .then(res => res.json())
        .then(json => {
            if (json.length) getLongLat(json[0])
            else alert("Sorry, I couldn't find that!")
        })
    }
    
    // Discuss why we broke this down into function
    function getLongLat(results){
        // Dicuss how we figured this out
        // Discuss why bracket vs dot notation
        currentLocation = ol.proj.fromLonLat([results["latlng"][1], results["latlng"][0]])
        animateToLocation(currentLocation)
    }
  
    function animateToLocation(loc){
      view.animate({
        center: loc,
        duration: 2000
      })
    }
  })
  