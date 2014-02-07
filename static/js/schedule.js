require([
  "underscore",
  "jquery",
  "lib/table"
  ], function(_, $, Table) {
    var table = new Table();
    console.log(table);
    table.findTable();
    $(function(){
      $('.btn-default, .btn-success').click(function(event){
        $(this).toggleClass('btn-success');
      });
    });
    table.fillTableData();
    $('#yes123').click(function() {
      table.postTableData();
    })
    $('#clearTable').click(function() {
      table.clearTable();
    })
});
