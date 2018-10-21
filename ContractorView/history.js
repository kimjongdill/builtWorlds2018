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
            		$('.submitted').addClass('d-flex');
            		break;
            	case "2":
            		$('.tableRow').removeClass('d-flex');
            		$('.tableRow').hide();
            		$('.rejected').addClass('d-flex');
            		break;
            	case "3":
            		$('.tableRow').removeClass('d-flex');
            		$('.tableRow').hide();
            		$('.approved').addClass('d-flex');
            		break;
                case "4":
                    $('.tableRow').removeClass('d-flex');
                    $('.tableRow').hide();
                    $('.ordered').addClass('d-flex');
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