var map, infoWindow, userPosition;
    function initMap() {
        map = new google.maps.Map(document.getElementById('map-container-google-1'), {
            center: {lat: -34.397, lng: 150.644},
            zoom: 15
        });

        infoWindow = new google.maps.InfoWindow;

        // get information from csrf_token
        const csrftoken = $.cookie('csrftoken');

        function csrfSafeMethod(method) {
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        // setup csrf_token submission before main AJAX request
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
          
        // Geolocation coordinates with Google Maps API to get User location
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
        
            // Ajax request to send user location to back end, receive a list of restaurants in your area
            // display markers in google maps and display list of restaurants and deals
            $.ajax({
                type: 'GET',
                contentType: 'application/json;charset-utf-08',
                dataType:'json',
                url:'http://127.0.0.1:8000/deals/',
                data: {
                    lat: pos.lat,
                    long: pos.lng,
                    csrfmiddlewaretoken: window.CSRF_TOKEN
                },
                success: function(data) {
                    console.log(data)
                    data = JSON.parse(data)
                    data.forEach(function(res) {
                        let latlng = {}
                        latlng.lat = res.lat
                        latlng.lng = res.lng
                        console.log(latlng)
                        const marker = new google.maps.Marker({
                            position: latlng,
                            map: map,
                            label:{
                                fontSize: '8pt',
                                text: res.name
                            }
                        });
                        console.log(`${res.res_id}`)
                        let block = `<div class="card text-center">` +
                                        `<div class="card-header">${res.deal_name}</div>` +
                                        `<div class="card-body">` +
                                            `<h5 class="card-title">${res.name}</h5>` +
                                            `<p class="card-text">${res.deal_description}</p>` +
                                            '<a href="" class="btn"><span class="fas fa-star fa-fw mr-3"></span>Favorites</a>' +
                                            '<a href="#" class="btn">See more deals</a>' +
                                        '</div>' +
                                     '</div>';
                        document.getElementById('restaurant_list').innerHTML += block;
                        block = '';
                    });
                }
            });


            infoWindow.setPosition(pos);
            infoWindow.setContent('Your Location');
            infoWindow.open(map);
            map.setCenter(pos);
            map.zoom = 13;
            }, function() {
            handleLocationError(true, infoWindow, map.getCenter());
            });
        }   else {
            // Browser doesn't support Geolocation
            handleLocationError(false, infoWindow, map.getCenter());
            }
    }

    function handleLocationError(browserHasGeolocation, infoWindow, pos) {
        infoWindow.setPosition(pos);
        infoWindow.setContent(browserHasGeolocation ?
                              'Error: The Geolocation service failed.' :
                              'Error: Your browser doesn\'t support geolocation.');
        infoWindow.open(map);
    }