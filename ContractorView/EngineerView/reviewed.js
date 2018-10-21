$(document).ready(function(){
        $('select').change(function(){
            var value = $('#inputState').val();
            switch(value) {
            	case "0":
            		$('.tableRow').addClass('d-flex');
            		break;
            	case "1":
            		$('.tableRow').removeClass('d-flex');
            		$('.tableRow').hide();
            		$('.Rejected').addClass('d-flex');
            		break;
            	case "2":
            		$('.tableRow').removeClass('d-flex');
            		$('.tableRow').hide();
            		$('.Approved').addClass('d-flex');
            		break;
            }
        });

        $('input[type="file"]').change(function(e){
            var fileName = e.target.files[0].name;
        
            $('.custom-file-label').text(fileName);
        });

        $('#dialogSubmit').click(function(){
        	$(this).attr("data-toggle", "modal").attr("data-target", "#resultDialog");
        });
    });