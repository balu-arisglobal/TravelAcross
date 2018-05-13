
$(document).ready(function(){
   $('#saveTravelDetailsBtn').click(function(){

        var $fileUpload = $("input[type='file']");
            if (parseInt($fileUpload.get(0).files.length)>5){
             alert("You can only upload a maximum of 5 files");
            }


             $.ajax({
                url: '/travelDetails/save',
                data: $('#travelDetailsForm').serialize(),
                type: 'POST',
                success: function(response){
                    $('#travelDetailsForm').trigger("reset");
                    document.write(response);

                },
                error: function(error){
                    alert(error);
                }
            });

	})
});


function checkNull(value){
isValid = true;
if(value == '' || value == 'null' || value == ' '){
 isValid = false;
}

return isValid;
}