var x=document.getElementById("osmmap");
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
    alert("adfs.");
  } else {
    alert("Geolocation is not supported by this browser.");
  }
}

function showPosition(position) {
  x.src = "https://www.openstreetmap.org/export/embed.html?bbox=" + position.coords.longitude + "%2C" + position.coord.latitude + "%2C" + position.coords.longitude + "%2C" + position.coord.latitude + "&amp;layer=mapnik&amp;marker=" + position.coord.latitude + "%2C" + position.coords.longitude + "" + position.coords.latitude +
  "<br>Longitude: " + position.coords.longitude;
}


