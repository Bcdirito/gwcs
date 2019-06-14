// Step 2: Ask students what kinds of information they need to start with:
//  -- Since this is a "Map API" - we probably need a map.
//  -- We also need to specify where to center the map!
//     Have the students go to Google and find out the
//     longitude and latitude of the SIP location.
//  -- In order to "see" the map and interact with it, we need
//     a view. A view is like a computer screen. The computer
//     can do processes without it, but we won't be able to see.

// Briefly explain event listeners and what this one means
window.addEventListener("DOMContentLoaded", function(){
    // Our actual current location
    // Make sure coordinates are Longitute, Latitude
    let currentLocation = ol.proj.fromLonLat([-74.028106, 40.738729])
    
    // Follow example from docs
    let view = new ol.View({
      center: currentLocation,
      zoom: 8 // Can be set to whatever, this was just a preference
    })

    let map = new ol.Map({
      target: 'map', // The name of the div where we will be placing the map
      layers: [
        new ol.layer.Tile({
          source: new ol.source.OSM() // Listed as required in docs
        })
      ],
      loadTilesWhileAnimating: true, // UX/UI decision
      view: view // Referencing Global Variable view
    })
})
  