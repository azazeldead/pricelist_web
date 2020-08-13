function myFunction() {
  var input, filter, table, tr, td, i,alltables;
    alltables = document.querySelectorAll("table[data-name=mytable]");
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  alltables.forEach(function(table){
      tr = table.getElementsByTagName("tr");
      for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
          if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
          } else {
            tr[i].style.display = "none";
          }
        }       
      }
  });
  filterTable_activities(filter);
}

function filterTable_activities(filter) {
  
      var rows = document.querySelector("#activities tbody").rows;
      var type = document.querySelectorAll("input[name=optradio]:checked")[0].value.toUpperCase();
          for (var i = 0; i < rows.length; i++) {
              try{
              var thirtCol = rows[i].cells[4].textContent.toUpperCase();
              var td = rows[i].cells[0].textContent.toUpperCase();
              if (thirtCol.indexOf(type) > -1 && td.indexOf(filter) > -1) {
                if (rows[i].style.display === "none"){
                  rows[i].style.display = "";
                }
              }else {
                rows[i].style.display = "none";
                console.log(type);
            }
          }catch{
              
          }
          }
      
      
} 
