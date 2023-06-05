$(document).ready(function () {
  const url = "https://www.fourtonfish.com/hellosalut/?";
  $("INPUT#btn_translate").click(function () {
    $.get(url + $.param({language: $("INPUT#language_code").val() }), function (data) {
      $("DIV#hello").html(data.hello);
    });
  });
});
