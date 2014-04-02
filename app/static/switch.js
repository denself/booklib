function act1() {
  $(".switcher2").parent().removeClass("active");
  $(".switcher1").parent().addClass("active");
  $(".f1").removeClass("hid");
  $(".f2").addClass("hid");

}
function act2() {
  $(".switcher1").parent().removeClass("active");
  $(".switcher2").parent().addClass("active");
  $(".f2").removeClass("hid");
  $(".f1").addClass("hid");
}
$( "body" ).on( "click",".switcher1", act1 );
$( "body" ).on( "click",".switcher2", act2 );