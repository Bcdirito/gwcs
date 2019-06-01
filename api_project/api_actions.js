const invalidLonLat = -200;

var lastCountry = "";
var countryLon = invalidLonLat;
var countryLat = invalidLonLat;
let countryName = document.getElementById("country-name").value;
let countryData;

function makeFetchRequest(url, func){
  fetch(url)
    .then(res => res.json())
    .then(res => func(res))
}

function updateCountry() {
  countryName = document.getElementById("country-name").value
}

function makeCountryRequest() {
  let url = "https://restcountries.eu/rest/v2/name/"
  let urlTag = "?fullText=true"

	if(countryName === "") alert("You didn't enter a country name!");
  else {
    const requestURL = `${url}${countryName}${urlTag}`
    makeFetchRequest(requestURL, processCountryResponse)
  }
}

function processCountryResponse(response) {
  countryData = response[0]
	countryLon = countryData.latlng[1];
	countryLat = countryData.latlng[0];
	const countryElts = document.getElementsByClassName("selected-country");

	for (let i = 0; i < countryElts.length; i++) {
		countryElts[i].innerHTML = "Selected Country: " + countryData.name;
	}

	lastCountry = countryData.name;
}

function makeSunriseSunsetRequest() {
	if(!countryData || (countryData.latlng[0] <= invalidLonLat || countryData.latlng[1] <= invalidLonLat)) {
	 	alert("You didn't get country data!");
	} else {
    const requestURL = "https://api.sunrise-sunset.org/json?lat="+countryLat+"&lng="+countryLon+"&date=today";
    makeFetchRequest(requestURL, processSunriseSunsetRequest)
  }
}

function processSunriseSunsetRequest(resp) {
  document.getElementById("sunset-time").innerHTML = "Sunrise: " + resp.results.sunrise + " UTC and Sunset: " + resp.results.sunset + " UTC";
}

function makeISSRequest() {
  if(!countryData.latlng || countryData.latlng[0] <= invalidLonLat || countryData.latlng[1] <= invalidLonLat) alert("You didn't get country data!");
  else {
    const url = `http://api.open-notify.org/iss-pass.json?lat=${countryLat}&alt=20&lon=${countryLon}&callback=?`

    $.getJSON(url, null, processISSRequest)

    // fetch(url, {
    //   method: "GET"
    // })
    //   .catch(error => console.log(error))
    //   .then(res => res.json())
    //   .then(res => {
    //     console.log(res)
    //   })


  }
}

function processISSRequest(issInformation) {
	let date = new Date(issInformation.response[1]['risetime']*1000);

  document.getElementById("iss-time").innerHTML = date.toString();
}

function makeSWRequest() {
	let character = document.getElementById("sw-character").innerHTML;

	if(character === "") alert("You didn't write a character!")
  else {
    const requestURL = "https://swapi.co/api/people/?search="+character;
    makeFetchRequest(requestURL, processSWRequest)
  }
}

function processSWRequest(swInformation) {
  const info = swInformation.results
	document.getElementById("sw-info").innerHTML = info[0].name + ", born: "+ info[0].birth_year;
}

function makeArtistRequest() {
	let artist = document.getElementById("music-artist").innerHTML;
	let genre = document.getElementById("music-genre").innerHTML;

	//console.log(artist);

	if(artist === "") alert("You didn't write a name for the artist!")
	else {
    const requestURL = "http://musicbrainz.org/ws/2/artist/?query=artist:"+artist+"%20AND%20tag:"+genre+"&fmt=json";

    makeFetchRequest(requestURL, processArtistRequest)
  }
}

function processArtistRequest(artistInformation) {
  const info = artistInformation.artists[0]
	document.getElementById("arist-info").innerHTML = info.name + " started in " + info["life-span"].begin;
}

function makeBerryRequest() {
	let berry = document.getElementById("berry-name").innerHTML;

	if(berry === "") alert("You didn't write a name for the berry!")
  else {
    const requestURL = "https://pokeapi.co/api/v2/berry/"+berry+"/";
    makeFetchRequest(requestURL, processBerryRequest)
  }
}

function processBerryRequest(berryInformation) {
	document.getElementById("berry-info").innerHTML = "Natural Gift: " + berryInformation.natural_gift_type.name + " at Power: " + berryInformation.natural_gift_power;
}
