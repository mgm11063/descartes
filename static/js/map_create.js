
var mapContainer = document.getElementById("map"),
    mapOption = {
        center: new kakao.maps.LatLng(36.01606, 129.40045),
        level: 5, // 지도의 확대 레벨
    };
var map = new kakao.maps.Map(mapContainer, mapOption);