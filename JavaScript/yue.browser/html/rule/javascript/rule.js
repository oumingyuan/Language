/**
 * 
 */

function load() {


    //http://localhost:8080/VASP/html/rule/ruleSetting.html
	$.ajax({
		url : 'http://localhost:8080/VASP/refresh/id',
		type : 'post',
		cache : false,
		data : new FormData($("#uploadForm")[0]),
		dateType : 'json',
		processData : false,
		contentType : false,
		success : function(returndata) {
			console.log('111');
			if (returndata) {
				document.getElementById("id1").value = returndata;
				document.getElementById("id2").value = returndata;
			} else {
				alert('ERROR');
			}
		},
		error : function(returndata) {
			alert('服务端返回错误: ' + returndata);
		}
	});

}



//
$(document).ready(function() {
	console.log('111');
	$("#save").click(save);
});

function save() {

    nullcheck()

    $.ajax({

        url : '/VASP/refresh/insertrule',
        type : 'post',
        cache : false,
        data : new FormData($("#ruleInfo")[0]),
        dateType : 'json',
        processData : false,
        contentType : false,
        success : function(returndata) {

            if (returndata) {

                alert(returndata)

                window.location.href="http://localhost:8081/VASP/html/rule/queryAndModify.html";
                

            } else {

                alert('没有返回数据');

            }
        },
        error : function(returndata) {
            alert('服务端返回错误: ' + returndata);
        }


    })


	



}

function nullcheck() {

    $("form input").each(function () {

        if($(this).val()===''){

            alert("this cannot be null")

            $(this).focus()

            throw "null value"

        }

    })

}



//send test json to the server

$(document).ready(function() {
    console.log('111');
    $("#save1").click(function () {

        alert("lala")

        $("#lala").html("summitting data, do not close windows...")

        $.ajax({
            type:"POST",
            url:"/VASP/refresh/insertrule",
            contentType:"application/json;charset=utf-8",
            data:JSON.stringify(GetJsonData1()),




            dataType:"json",

            success:function (message) {

                if(message>0){
                    alert("submit data success")
                }else{

                }

            },

            error:function (message) {

                $("#lala").html("summit data fail")

            }
        })



    });
});

function GetJsonData() {

    var json={

        "id":2,
        "name":"dog"
        
    }

    alert(JSON.stringify(json))

    return json

}


function GetJsonData1() {
	
	alert("method begin")


	var params=$("#ruleInfo").serializeArray();
	var json={}
	for(var item in params){
		
		alert(item)
	    j[params[item].name]=params[item].value;
    }

    alert(JSON.stringify(json))

    return json

}



