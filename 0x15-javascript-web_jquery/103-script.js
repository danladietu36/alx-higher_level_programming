$(document).ready(function () {
  $("INPUT#btn_translate").click(translate);
  $("INUT#language_code").keyup(function (event) {
    if (even.keyCode == 13) {
      fetch();
    }
  });

  function translate() {
    const language_code = $("INPUT#language_code").val();
    $.getJSON(
	    "https://www.fourtonfish.com/hellosalut/hello/?lang=${language_code}",
	    function (data) {
	      $("#hello").text(data.hello);
	    }
    );
  }
});
