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
        console.log('catch');
        $(this).toggleClass('btn-default');
        $(this).toggleClass('btn-success');
      });
    });
    table.fillTableData();
});
