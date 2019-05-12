$(document).ready(function() {
	$("#button").click(upload);
});

function upload() {
	$.ajax({
		url : '/VASP/readexcel/addasd',
		type : 'post',
		cache : false,
		data : new FormData($("#uploadForm")[0]),
		dateType : 'json',
		processData : false,
		contentType : false,
		success : function(result) {
			if (result.state != 0) {
				alert(result.message);
			} else {
				alert(result.data);
			}
		},
		error : function() {
			alert('ERROR');
		}
	});

}
