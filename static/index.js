// A $( document ).ready() block.
$( document ).ready(function() {

    $("#frm-login-form").submit(function(e){
        e.preventDefault();
        var formData = JSON.stringify($("#frm-login-form").serializeArray());

        $.ajax({
            type: "POST",
            url: "/login",
            data: formData,
            success: function(data){
                if (data.success) {
                    window.location.href = "/profile";
                } else {
                    var alert = '<div class="alert alert-primary" role="alert"> Invalid credentials </div>';
                    $('#div-msg').html(alert);
                }
            },
            dataType: "json",
            contentType : "application/json"
          });
      })

      $("#frm-search").submit(function(e){
        e.preventDefault();
        var formData = JSON.stringify($("#frm-search").serializeArray());
        $.ajax({
            type: "POST",
            url: "/search",
            data: formData,
            success: function(data){
                if (data.length > 0) {
                    $("#tbl-users tbody").remove();
                    $('#tbl-users').append('<tbody>');
                    var i;
                    for (i = 0; i < data.length; i++) {
                    var html = `<tr>
                                <td>
                                    <div class="form-check-inline">
                                    <label class="form-check-label">
                                        <input type="checkbox" class="form-check-input" value="">
                                    </label>
                                </div>
                                </td>  
                                <td><a href="#"><small>`+ data[i].username +`</small></a></td>
                                <td><small>`+ data[i].email + `</small></td>
                                <td><small>`+ data[i].isActive + `</small></td>
                                <td><small>`+ data[i].managed_by + `</small></td>
                                <td><a href="#"><small>5</small></a></td>
                                <td>
                                    <a href="#"><i class="fa fa-pencil-square-o"></i></a>
                                    <a href="#"><i class="fa fa-eye"></i></a>
                                    <a href="#"><i class="fa fa-trash"></i></a>
                                </td>
                            </tr>`
                    $('#tbl-users').append(html);
                    }
                    $('#tbl-users').append('</tbody>');
                } else {
                    $("#tbl-users tbody").remove();
                }
            },
            dataType: "json",
            contentType : "application/json"
          });
      })
      
});