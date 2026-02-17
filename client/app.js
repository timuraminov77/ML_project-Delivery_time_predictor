function getCourierExp() {
  var CEY = document.getElementsByName("CEY");
  for (var i = 0; i < CEY.length; i++) {
    if (CEY[i].checked) {
      return parseInt(CEY[i].value);
    }
  }
  return -1;
}


function onClickedEstimateTime() {
  console.log("Estimate Time button clicked");

  var distance = parseFloat($('#distanceKM').val());
  var traffic = $('#Traffic').val();
  var weather = $('#Weather').val();
  var courierExp = getCourierExp();

  var estTime = $('#EstimatedTime');
  $('#EstimatedTime').show();

  function isFloat(value) {
    const num = parseFloat(value);
    return !isNaN(num) && num.toString() === value.toString();
  }
  if (!isFloat(distance)){
    estTime.html("<h2>Please fill correct distance</h2>");
    return;
  }
  if (!traffic || !weather || courierExp === -1 || isNaN(distance)) {
    estTime.html("<h2>Please fill all fields</h2>");
    return;
  }
  $.ajax({
    url: "/api/predict_delivery_time",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({
      weather: weather,
      distance: distance,
      traffic_level: traffic,                 
      courier_experience_yrs: courierExp     
    }),
    success: function (data) {
      estTime.html(
        "<h2>Estimated time: " + data.estimated_time_min + " min</h2>"
      );
    },
    error: function (err) {
      console.error(err);
      estTime.html("<h2>Error predicting time</h2>");
    }
  });
}


function onPageLoad() {
  console.log( "document loaded" );
  var url = "/api/get_weather";
  $.get(url,function(data, status) {
      console.log("got response for get_weather request");
      if(data) {
          var weather = data.weather;
          var Weather = document.getElementById("Weather");
          $('#Weather').empty();
          for(var i in weather) {
              var opt = new Option(weather[i]);
              $('#Weather').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;
