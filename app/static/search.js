$(function() {
    $( "#in_search" ).autocomplete({
        source: function( request, response ) {
            $.ajax({
                    url: "/tags",
                    data: {search_item: request.term},
                    dataType: "json",
                    success: function( data ) {
                         response( $.map( data, function(item, key) {
                                return {label: item, value: key}
                }));
            }
          });
        },
        select: function( event, ui ) {
          window.location.replace(ui.item.value);
          return false;
        },
        focus: function( event, ui ) {
          $(this).val(ui.item.label);
          return false;
        }
      });
    });