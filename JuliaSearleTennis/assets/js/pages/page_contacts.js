var ContactPage = function () {

    return {
        
    	//Basic Map
        initMap: function () {
			var map;
			$(document).ready(function(){
			  map = new GMaps({
				div: '#map',
				scrollwheel: false,				
				lat: 51.43187,
				lng: -0.13321
			  });
			  
			  var marker = map.addMarker({
				lat: 51.43187,
				lng: -0.13321,
	            title: 'Wigmore Tennis Club'
		       });
			});
        },

        //Panorama Map
        initPanorama: function () {
		    var panorama;
		    $(document).ready(function(){
		      panorama = GMaps.createPanorama({
		        el: '#panorama',
		        lat: 51.43187,
		        lng: -0.13321
		      });
		    });
		}        

    };
}();