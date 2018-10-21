$(document).ready(function(){
        $('input[type="file"]').change(function(e){
            var fileName = e.target.files[0].name;
            $('.custom-file-label').text(fileName);
        });

        $('#dialogSubmit').click(function(){
        	$.getJSON('https://pld4lkh5ta.execute-api.us-east-1.amazonaws.com/prod/pdfSimilarity?file1%3Dhttps://www.peerlesspump.com/tech_manuals/Tab%2520Section%25201500%2520Horizontal%2520Split%2520Case,%2520End%2520Suction,%2520Inline%2520Fire%2520Pumps/Section%25201520%2520Data.pdf%26file2%3Dhttp://www.georgedill.net/bw2018/fire_protection.pdf&sa=D&source=hangouts&ust=1540218703428000&usg=AFQjCNGygNlmELWBm6jasbwqmsmnncsCOw', function(data) {
    			console.log(data);//data is the JSON string
			});
        	$(this).attr("data-toggle", "modal").attr("data-target", "#resultDialog");
        });
    });