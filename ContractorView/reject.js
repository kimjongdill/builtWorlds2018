$(document).ready(function(){
        $('input[type="file"]').change(function(e){
            var fileName = e.target.files[0].name;
            $('.custom-file-label').text(fileName);
        });

        $('#dialogSubmit').click(function(){
        	$(this).attr("data-toggle", "modal").attr("data-target", "#resultDialog");
        });
    });