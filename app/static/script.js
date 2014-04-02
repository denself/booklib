function addAuthorShow(){
    $(".addbtn").addClass("hid");
    $(".addAuthor").removeClass("hid");
}
function delAuthorAjax(){
    $.ajax({
            url: "/AjaxAuthorDelete",
            data: {id: $(this).parent().attr("id")},
            method: "POST",
            dataType: "json",
          })
     .done(function(id) {
            $("#"+id.id).remove();
     });
}
function addAuthorAjax(){
    if ($("#newAuthorName").val()){
   $.ajax({
            url: "/AjaxAuthorCreate",
            data: {name: $("#newAuthorName").val()},
            method: "POST",
            dataType: "json",
          })
     .done(function(author) {
        if (author.name){
            large = '<div class="book" id="'+author.id+'"><a href="/author/'+author.id+'/'+author.name+'">'+author.name+'</a>'
            if (author.is_admin){
                large = large+'<button class="btnDelAuth"><img width="20px" src="/static/delete.png"/></button>'+
                              '<button class="btnEditAuth"><img width="20px" src="/static/edit.png"/></button>'
            }
            large = large+'</div>'
            $(".addAuthor" ).after( large );
            $(".addbtn").removeClass("hid");
            $(".addAuthor").addClass("hid");
            $("#newAuthorName").val("");
        }
       });
       } else{
       $(".addbtn").removeClass("hid");
            $(".addAuthor").addClass("hid");
       }
}
function editAuthorShow(){
    id = $(this).parent().attr("id");
    name = $(this).parent().children("a").text();
    large = '<div class="addAuthor addbook" id="editd'+id+'"><input type="text" id="edit'+id+'" value="'+name+'">'+
                '<button type="submit" class="editAuthorButton_button"><img src="/static/ok.png" /></button></div>'
    $(this).parent().after( large );
    $(this).parent().addClass("hid");
};
function editAuthorAjax(){
    if ($(this).parent().children("input").val()){
   $.ajax({
            url: "/AjaxAuthorEdit",
            data: {id:$(this).parent().children("input").attr("id"),name: $(this).parent().children("input").val()},
            method: "POST",
            dataType: "json",
          })
    .done(function(name) {
            $("#editd"+name.id).remove();
            $("#"+name.id).removeClass("hid");
            $("#"+name.id).children("a").text(name.name);
       });

};
}
function delBookAjax(){
    $.ajax({
            url: "/AjaxBookDelete",
            data: {id: $(this).parent().attr("id")},
            method: "POST",
            dataType: "json",
          })
     .done(function(id) {
            $("#"+id.id).remove();
     });
}

$("body").on( "click","#addauth", addAuthorShow );
$("body").on( "click","#addAuthorButton_button", addAuthorAjax );
$("body").on( "click",".btnDelAuth", delAuthorAjax );
$("body").on( "click",".btnEditAuth", editAuthorShow );
$("body").on( "click",".editAuthorButton_button", editAuthorAjax );

$("body").on( "click",".btnDelBook", delBookAjax );
