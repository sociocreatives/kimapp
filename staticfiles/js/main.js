
    // Check if geolocation is supported
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(function(position) {
        var latitude = position.coords.latitude;
        var longitude = position.coords.longitude;

        // Create a Geocoder instance
        var geocoder = new google.maps.Geocoder();

        // Define the location based on latitude and longitude
        var latlng = new google.maps.LatLng(latitude, longitude);

        // Perform reverse geocoding
        geocoder.geocode({ 'location': latlng }, function(results, status) {
          if (status === google.maps.GeocoderStatus.OK) {
            if (results[0]) {
              // Display the formatted address
              document.getElementById("location").innerText = "Address: " + results[0].formatted_address;
            } else {
              document.getElementById("location").innerText = "No results found";
            }
          } else {
            document.getElementById("location").innerText = "Geocoder failed due to: " + status;
          }
        });
      });
    } else {
      // Geolocation is not supported
      document.getElementById("location").innerText = "Geolocation is not supported by your browser";
    }