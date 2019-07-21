window.addEventListener("DOMContentLoaded", function(){
    let currentLocation = ol.proj.fromLonLat([-74.028106, 40.738729])

    let homeLocation = ol.proj.fromLonLat([-74.028106, 40.738729])

    // Explain query selector
    let button = document.getElementsByClassName('button')[0]
    
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

    // Discuss why div event listener vs button event listener
    button.addEventListener("click", function(e) {
        // Discuss e & e.target
        // Discuss non-traditional formatting
        if (e.target.name === "panHomeButton") animateToLocation(homeLocation)
    })

    // Discuss why you made this a dynamic function
    function animateToLocation(loc){
        view.animate({
            center: loc,
            duration: 2000 // Discuss why 2000
        })
    }
})
  